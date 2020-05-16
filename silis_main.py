import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time
import core
from GUI.gui_baseDatos import Ui_root_gestor
import gestor_datos
import DATABASE.data_base as data_base
import threading


baseEjemplo = data_base.getID()
datosUsuario = data_base.displayInfo()
recibo = ""
hora1 = ""
data = ""
deposito_total = 0


def corroborarBooleanos(dato, dato1):
    if dato == '1': #Trabajador[14] y 13, contienen los booleanos almacenados en la base de datos, las variables son temporales
         resultado = True
    else:
         resultado = False

    if dato1 == '1':
         resultado2 = True
    else:
         resultado2 = False

    return resultado, resultado2 #Esto retorna una tupla

#Declaramos la clase Hilo1 donde se efectuara la liquidacion de la base de datos en segundo plano
class Hilo1(QThread):

    countChanged = pyqtSignal(int)
    
    def run(self):

        global baseEjemplo
        i = 0
        while True:
            if i >= len(baseEjemplo):
                #print("Base de datos Liquidada")
                break
            i+=1
            time.sleep(1)
            self.countChanged.emit(i)

class MainGUI(QMainWindow):

    
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi("GUI/gui_raw.ui", self)

        #Seteamos valor iniciales de grafica
        self.txt_valorHora.setPlaceholderText("MENSUAL colocar Nominal")
        self.txt_hs_simples.setPlaceholderText("MENSUAL colocar 0")
        self.progressBar.setProperty("value", 0)
        self.lbl_liquido.setText("")
        self.lbl_depositoTrabajadores.setText("")
        self.actionAbrir_Base_de_Datos.triggered.connect(self.mostrarGestor)
        self.btn_liquidarIndividual.clicked.connect(self.liquidar_individual)
        self.btn_mostrarTrabajadores.clicked.connect(self.mostrarListado)
        self.btn_liquidarBaseDatos.clicked.connect(self.liquidar_base_datos)


        #Creamos el timer del reloj
        timer = QTimer(self)
        timer.timeout.connect(self.tick)
        timer.start(1000)               #1000 = 1 > 1 min = 60 ->
        #Final timer reloj

    def tick(self):
        global hora1
        global hora2
        global minutosReloj
        global segundosReloj
        global horasReloj
        # Hora actual de la pc
        hora2 = time.strftime('%H:%M:%S')

        # actualizamos el texto cuando cambia
        if hora2 != hora1:
            hora1 = hora2
            minutosReloj = time.strftime("%M")
            segundosReloj = time.strftime("%S")
            horasReloj = time.strftime("%H")
            #print(hora2)
        return hora2

    def mostrarGestor(self):
        self.ventana = QMainWindow()
        self.ui = Ui_root_gestor()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def liquidar_individual(self):
        if self.chbox_conyuge.isChecked():
            conyuge = True
        else:
            conyuge = False

        if self.checkBox.isChecked():
            conyuge_disc = True
        else:
            conyuge_disc = False

        obj = core.Trabajador(
            identificador = self.txt_trabajadorID.text(),
            fecha_ingreso = self.txt_fechaIngreso.text(),
            tipo          = self.txt_tipoTrabajador.text(),
            sueldo        = self.txt_valorHora.text(),
            hs_simples    = self.txt_hs_simples.text(),
            hs_ext        = self.txt_hs_Ext.text(),
            hs_ext_esp    = self.txt_hs_ext_esp.text(),
            hs_noct       = self.txt_horas_noc.text(),
            jornada_esp   = self.txt_jornadaEsp.text(),
            hijos         = self.txt_hijos.text(),
            hijos_disca   = self.txt_discapacitados.text(),
            conyuge       = conyuge,
            conyugeDisca  = conyuge_disc)


        self.lbl_liquido.setText("$ " + str( round(obj.liquidar()[0]) ) )
        self.txt_bps.setText( str( round(obj.liquidar()[1]) ) )
        self.txt_fonasa.setText( str( round(obj.liquidar()[2]) ) )
        self.txt_frl.setText( str( round(obj.liquidar()[3]) ) )

        obj.reciboSueldo(
                data                 = data,
                jornales             = str( round(obj.liquidar()[4]) ),
                totalextras          = str( round(obj.liquidar()[5]) ),
                totalEspeciales      = str( round(obj.liquidar()[5]) ),
                totalNocturnas       = str( round(obj.liquidar()[6]) ),
                totalJornadaEspecial = str( round(obj.liquidar()[7]) ),
                nominalDescuento     = str( round(obj.liquidar()[10]) ),
                irpf                 = str( round(obj.liquidar()[11]) ),
                liquidoreal          = str( round(obj.liquidar()[12]) ),
                descBPS              = str( round(obj.liquidar()[1]) ),
                descFonasa           = str( round(obj.liquidar()[2]) ),
                descFRL              = str( round(obj.liquidar()[3]) ),
                descGral             = str( round(obj.liquidar()[14]) ),
                liquido1             = str( round(obj.liquidar()[13]) ),
                hora2                = self.tick,
                nombre               = data[3],
                apellido             = data[4],
                tipo                 = data[2],
                iD                   = data[0]
                )

        obj.liquidar()
        
    def mostrarListado(self):
        global baseEjemplo
        global datosUsuario

        #Creamos la tabla para mostrar los trabajadores
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(16)
        for row_number, row_data in enumerate(datosUsuario):
            #print("Estos seria row_numer ", row_number)
            #print("Esto seria row_data ", row_data)
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                #print("Esto seria column_number ", column_number)
                #print("Esto seria data ", data)
                self.tableWidget.setItem(row_number,column_number, QTableWidgetItem(str(data)))

        #==== Optimizamos la tabla para mejor funcionamiento ====

        #Desactivamos el drag&drop
        self.tableWidget.setDragDropOverwriteMode(False)
        #Habilidamos la posibilidad de seleccionar toda la fila para posteriormente matar el proceso
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        #Evitamos la multiseleccion de lineas
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        #Mostrar puntos suspensivos cuando el texto es mas grande que la celda
        self.tableWidget.setTextElideMode(Qt.ElideRight)
        self.tableWidget.setWordWrap(False)
        #Centramos el texto del encabezado
        #Deshabilitamos el ajuste del texto a la celda
        self.tableWidget.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
        #Deshabilitamos el resaltado del header
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        #Hacemos que la seccion visible ocupe todo el espacio disponible
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        #Ocultamos los encabezados verticales
        self.tableWidget.verticalHeader().setVisible(False)
        #Damos nombres a los headers
        nombre_encabezado = ('ID','Fecha Ingreso','Tipo Trabajador','Nombre','Apellido','Cedula','Valor Hora', 'Horas Simples', 'Horas Extras', 'Hs Ext. Especiales', 'Horas Nocturnas', 'Jornada Especial', 'Hijos a Cargo', 'Hijos Discapacitados', 'Conyuge a Cargo', 'Conyuge a Cargo Discapacitado',)
        self.tableWidget.setHorizontalHeaderLabels(nombre_encabezado)

        #Añadimos funcionalidad de seleccionar del listado
        self.tableWidget.itemClicked.connect(self.__seleccion)

    """ Funcion Privada """
    def __seleccion(self, celda):
        trabajador = []
        items_de_fila = self.tableWidget.selectedItems()

        for items in items_de_fila:
            trabajador.append(items.text())


        self.txt_trabajadorID.setText(trabajador[0])
        self.txt_fechaIngreso.setText(trabajador[1])
        self.txt_tipoTrabajador.setText(trabajador[2])
        self.txt_valorHora.setText(trabajador[6])
        self.txt_hs_simples.setText(trabajador[7])
        self.txt_hs_Ext.setText(trabajador[8])
        self.txt_hs_ext_esp.setText(trabajador[9])
        self.txt_horas_noc.setText(trabajador[10])
        self.txt_jornadaEsp.setText(trabajador[11])
        self.txt_hijos.setText(trabajador[12])
        self.txt_discapacitados.setText(trabajador[13])
        self.chbox_conyuge.setChecked( corroborarBooleanos(dato=trabajador[14], dato1=trabajador[15])[0] )
        self.checkBox.setChecked( corroborarBooleanos(dato=trabajador[14], dato1=trabajador[15])[1] )

    def liquidar_base_datos(self):
        self.calc = Hilo1()
        self.calc.countChanged.connect( self.__barra_progreso)
        self.calc.start()
    
    def __barra_progreso(self, value):

        global baseEjemplo
        global datosUsuario
        global data
        self.progressBar.setMaximum(len(baseEjemplo))

        if self.chbox_conyuge.isChecked():
            conyuge = True
        else:
            conyuge = False
        if self.checkBox.isChecked():
            conyuge_disc = True
        else:
            conyuge_disc = False

        for data in data_base.selectUnique(value):
                self.txt_trabajadorID.setText( str(data[0]))
                self.txt_fechaIngreso.setText( str(data[1]))
                self.txt_tipoTrabajador.setText( str(data[2]))
                self.txt_valorHora.setText( str(data[6]))
                self.txt_hs_simples.setText( str(data[7]))
                self.txt_hs_Ext.setText( str(data[8]))
                self.txt_hs_ext_esp.setText( str(data[9]))
                self.txt_horas_noc.setText( str(data[10]))
                self.txt_jornadaEsp.setText( str(data[11]))
                self.txt_hijos.setText( str(data[12]))
                self.txt_discapacitados.setText( str(data[13]))
                self.chbox_conyuge.setChecked( corroborarBooleanos(dato= data[14], dato1= data[15])[0] )
                self.checkBox.setChecked( corroborarBooleanos(dato= data[14], dato1= data[15])[1] )
                #print(data)

        self.progressBar.setValue(value)

        obj = core.Trabajador(
                identificador       = self.txt_trabajadorID.text(), 
                fecha_ingreso       = self.txt_fechaIngreso.text(), 
                tipo                = self.txt_tipoTrabajador.text(), 
                sueldo              = self.txt_valorHora.text(), 
                hs_simples          = self.txt_hs_simples.text(), 
                hs_ext              = self.txt_hs_Ext.text(), 
                hs_ext_esp          = self.txt_hs_ext_esp.text(), 
                hs_noct             = self.txt_horas_noc.text(), 
                jornada_esp         = self.txt_jornadaEsp.text(), 
                hijos               = self.txt_hijos.text(), 
                hijos_disca         = self.txt_discapacitados.text(),
                conyuge             = conyuge, 
                conyugeDisca        = conyuge_disc)
            
        
        self.lbl_liquido.setText("$ " + str( round(obj.liquidar()[0]) ) )
        self.txt_bps.setText( str( round(obj.liquidar()[1]) ) )
        self.txt_fonasa.setText( str( round(obj.liquidar()[2]) ) )
        self.txt_frl.setText( str( round(obj.liquidar()[3]) ) )



        obj.reciboSueldo(
            data                 = data,
            jornales             = str( round(obj.liquidar()[3]) ),
            totalextras          = str( round(obj.liquidar()[4]) ),
            totalEspeciales      = str( round(obj.liquidar()[5]) ),
            totalNocturnas       = str( round(obj.liquidar()[6]) ),
            totalJornadaEspecial = str( round(obj.liquidar()[7]) ),
            nominalDescuento     = str( round(obj.liquidar()[9]) ),
            irpf                 = str( round(obj.liquidar()[10]) ),
            liquidoreal          = str( round(obj.liquidar()[11]) ),
            descBPS              = str( round(obj.liquidar()[0]) ),
            descFonasa           = str( round(obj.liquidar()[1]) ),
            descFRL              = str( round(obj.liquidar()[2]) ),
            descGral             = str( round(obj.liquidar()[13]) ),
            liquido1             = str( round(obj.liquidar()[12]) ),
            hora2                = self.tick,
            nombre               = data[3],
            apellido             = data[4],
            tipo                 = data[2],
            iD                   = data[0]
            )
        
        obj.liquidar()
        self.calculo_deposito( round(obj.liquidar()[0]) )

    def calculo_deposito(self, sueldo):
        global deposito_total
        deposito_total += sueldo
        self.lbl_depositoTrabajadores.setText("$ " + str( deposito_total ) ) 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MainGUI()
    gui.show()
    sys.exit(app.exec_())
