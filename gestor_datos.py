
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, Qt
import time
import core
import data_base

baseEjemplo = data_base.getID()
datosUsuario = data_base.displayInfo()


class GestorGUI(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi("gui_gestor_base.ui", self)
        self.setFixedSize(1331, 700)
        self.btn_limpiar.clicked.connect(self.limpiar)
        self.btn_anadir.clicked.connect(self.anadir)
        self.btn_mostrar.clicked.connect(self.mostrar)

        #Refrescado automatico de registros
        timer = QTimer(self)
        timer.timeout.connect(self.mostrar)
        timer.start(1000)


    def limpiar(self):
        self.txt_id.setText('')
        self.txt_fecha_ingreso.setText('')
        self.txt_tipo.setText('')
        self.txt_nombre.setText('')
        self.txt_apellido.setText('')
        self.txt_cedula.setText('')
        self.txt_valorHora.setText('')
        self.txt_hsSimples.setText('')
        self.txt_horasExtras.setText('')
        self.txt_hs_ext_esp.setText('')
        self.txt_hsNocturnas.setText('')
        self.txt_jornadaEsp.setText('')
        self.txt_hijosCargo.setText('')
        self.lineEdit.setText('') #Hijos discapacitados
        self.rb_conyuge.setChecked(False)
        self.rb_conyugeDisca.setChecked(False)

    def anadir(self):
        self.txt_id.setText("1")
        if self.rb_conyuge.isChecked():
            conyuge = True
        else:
            conyuge = False

        if self.rb_conyugeDisca.isChecked():
            conyugeDisca = True
        else:
            conyugeDisca = False

        #print("Este mensaje deberia de aparecer desde la ventana PRINCIPAL")
        if(len( self.txt_id.text() )!=0):
            print(self.txt_fecha_ingreso.text())
            data_base.addInfo(self.txt_fecha_ingreso.text(), self.txt_tipo.text(), self.txt_nombre.text(), self.txt_apellido.text(), self.txt_cedula.text(), self.txt_valorHora.text(), self.txt_hsSimples.text(), self.txt_horasExtras.text(), self.txt_hs_ext_esp.text(), self.txt_hsNocturnas.text(), self.txt_jornadaEsp.text(), self.txt_hijosCargo.text(), self.lineEdit.text(), conyuge, conyugeDisca)

    def mostrar(self):
        global baseEjemplo
        global datosUsuario

        #Creamos la tabla para mostrar los trabajadores
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(15)
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
        #Dibujamos el fondo con colores alternados
        self.tableWidget.setAlternatingRowColors(True)
        #Damos nombres a los headers
        nombre_encabezado = ('ID','Fecha Ingreso','Tipo Trabajador','Nombre','Apellido','Cedula','Valor Hora', 'Horas Simples', 'Horas Extras', 'Hs Ext. Especiales', 'Horas Nocturnas', 'Jornada Especial', 'Hijos a Cargo', 'Hijos Discapacitados', 'Conyuge a Cargo', 'Conyuge a Cargo Discapacitado',)
        self.tableWidget.setHorizontalHeaderLabels(nombre_encabezado)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GestorGUI()
    gui.show()
    sys.exit(app.exec_())
