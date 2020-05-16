# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_gestor_base.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer

import src.nombres
import src.apellidos
import random

import DATABASE.data_base as data_base
baseEjemplo = data_base.getID()
datosUsuario = data_base.displayInfo()





class Ui_root_gestor(object):
    def setupUi(self, root_gestor):
        root_gestor.setObjectName("root_gestor")
        root_gestor.resize(1330, 697)
        self.centralwidget = QtWidgets.QWidget(root_gestor)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_head = QtWidgets.QFrame(self.centralwidget)
        self.frame_head.setGeometry(QtCore.QRect(0, 0, 1331, 101))
        self.frame_head.setStyleSheet("background-color: rgb(116, 6, 144);")
        self.frame_head.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_head.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_head.setObjectName("frame_head")
        self.label = QtWidgets.QLabel(self.frame_head)
        self.label.setGeometry(QtCore.QRect(360, 20, 641, 61))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 36pt \"Sans Serif\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_bottom_controller = QtWidgets.QFrame(self.centralwidget)
        self.frame_bottom_controller.setGeometry(QtCore.QRect(0, 600, 1331, 101))
        self.frame_bottom_controller.setStyleSheet("background-color: rgb(116, 6, 144);")
        self.frame_bottom_controller.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bottom_controller.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bottom_controller.setObjectName("frame_bottom_controller")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_bottom_controller)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1311, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_anadir = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_anadir.sizePolicy().hasHeightForWidth())
        self.btn_anadir.setSizePolicy(sizePolicy)
        self.btn_anadir.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_anadir.setObjectName("btn_anadir")
        self.horizontalLayout.addWidget(self.btn_anadir)
        self.btn_mostrar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mostrar.sizePolicy().hasHeightForWidth())
        self.btn_mostrar.setSizePolicy(sizePolicy)
        self.btn_mostrar.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_mostrar.setObjectName("btn_mostrar")
        self.horizontalLayout.addWidget(self.btn_mostrar)
        self.btn_limpiar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_limpiar.sizePolicy().hasHeightForWidth())
        self.btn_limpiar.setSizePolicy(sizePolicy)
        self.btn_limpiar.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_limpiar.setObjectName("btn_limpiar")
        self.horizontalLayout.addWidget(self.btn_limpiar)
        self.btn_borrar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_borrar.sizePolicy().hasHeightForWidth())
        self.btn_borrar.setSizePolicy(sizePolicy)
        self.btn_borrar.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_borrar.setObjectName("btn_borrar")
        self.horizontalLayout.addWidget(self.btn_borrar)
        self.btn_buscar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_buscar.sizePolicy().hasHeightForWidth())
        self.btn_buscar.setSizePolicy(sizePolicy)
        self.btn_buscar.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_buscar.setAutoDefault(False)
        self.btn_buscar.setDefault(False)
        self.btn_buscar.setFlat(False)
        self.btn_buscar.setObjectName("btn_buscar")
        self.horizontalLayout.addWidget(self.btn_buscar)
        self.btn_actualizar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_actualizar.sizePolicy().hasHeightForWidth())
        self.btn_actualizar.setSizePolicy(sizePolicy)
        self.btn_actualizar.setStyleSheet("color: rgb(255, 255, 255);")
        self.btn_actualizar.setObjectName("btn_actualizar")
        self.horizontalLayout.addWidget(self.btn_actualizar)
        self.frame_body = QtWidgets.QFrame(self.centralwidget)
        self.frame_body.setGeometry(QtCore.QRect(0, 100, 1331, 501))
        self.frame_body.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.frame_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_body.setObjectName("frame_body")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame_body)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 411, 504))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lbl_id = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_id.setObjectName("lbl_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_id)
        self.txt_id = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_id.setObjectName("txt_id")
        self.txt_id.setReadOnly(True)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_id)
        self.lbl_fecha_ingreso = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_fecha_ingreso.setObjectName("lbl_fecha_ingreso")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_fecha_ingreso)
        self.txt_fecha_ingreso = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_fecha_ingreso.setObjectName("txt_fecha_ingreso")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_fecha_ingreso)
        self.lbl_tipo = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_tipo.setObjectName("lbl_tipo")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_tipo)
        self.txt_tipo = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_tipo.setObjectName("txt_tipo")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_tipo)
        self.lbl_nombre = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_nombre)
        self.txt_nombre = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_nombre.setObjectName("txt_nombre")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_nombre)
        self.lbl_apellido = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_apellido.setObjectName("lbl_apellido")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_apellido)
        self.txt_apellido = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_apellido.setObjectName("txt_apellido")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txt_apellido)
        self.lbl_cedula = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_cedula.setObjectName("lbl_cedula")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lbl_cedula)
        self.txt_cedula = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_cedula.setObjectName("txt_cedula")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txt_cedula)
        self.lbl_valorHora = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_valorHora.setObjectName("lbl_valorHora")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lbl_valorHora)
        self.txt_valorHora = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_valorHora.setObjectName("txt_valorHora")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.txt_valorHora)
        self.lbl_hsSimples = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_hsSimples.setObjectName("lbl_hsSimples")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.lbl_hsSimples)
        self.txt_hsSimples = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_hsSimples.setObjectName("txt_hsSimples")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.txt_hsSimples)
        self.lbl_horasExtras = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_horasExtras.setObjectName("lbl_horasExtras")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.lbl_horasExtras)
        self.txt_horasExtras = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_horasExtras.setObjectName("txt_horasExtras")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.txt_horasExtras)
        self.lbl_hs_ext_esp = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_hs_ext_esp.setObjectName("lbl_hs_ext_esp")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.lbl_hs_ext_esp)
        self.txt_hs_ext_esp = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_hs_ext_esp.setObjectName("txt_hs_ext_esp")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.txt_hs_ext_esp)
        self.lbl_hsNocturnas = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_hsNocturnas.setObjectName("lbl_hsNocturnas")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.lbl_hsNocturnas)
        self.txt_hsNocturnas = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_hsNocturnas.setObjectName("txt_hsNocturnas")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.txt_hsNocturnas)
        self.lbl_jornadaEsp = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_jornadaEsp.setObjectName("lbl_jornadaEsp")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.lbl_jornadaEsp)
        self.txt_jornadaEsp = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_jornadaEsp.setObjectName("txt_jornadaEsp")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.txt_jornadaEsp)
        self.line = QtWidgets.QFrame(self.formLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.lbl_hijosCargo = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_hijosCargo.setObjectName("lbl_hijosCargo")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.lbl_hijosCargo)
        self.txt_hijosCargo = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_hijosCargo.setObjectName("txt_hijosCargo")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.txt_hijosCargo)
        self.lbl_hijosDisca = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_hijosDisca.setObjectName("lbl_hijosDisca")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.lbl_hijosDisca)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lbl_conyugeCargo = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_conyugeCargo.setObjectName("lbl_conyugeCargo")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.lbl_conyugeCargo)
        self.rb_conyuge = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.rb_conyuge.setObjectName("rb_conyuge")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.rb_conyuge)
        self.radioButton = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.radioButton)
        self.lbl_conyugeDisca = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_conyugeDisca.setObjectName("lbl_conyugeDisca")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.lbl_conyugeDisca)
        self.rb_conyugeDisca = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.rb_conyugeDisca.setObjectName("rb_conyugeDisca")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.rb_conyugeDisca)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_body)
        self.tableWidget.setGeometry(QtCore.QRect(410, 0, 921, 501))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        root_gestor.setCentralWidget(self.centralwidget)
        self.retranslateUi(root_gestor)
        QtCore.QMetaObject.connectSlotsByName(root_gestor)

        #Para desactivar, comenta la linea
        #self.__ingresarUsuarios()

        """ #============== CLASE DEFINIDA EN GESTOR_DATOS ==============# """
        self.btn_limpiar.clicked.connect(self.limpiar)
        self.btn_anadir.clicked.connect(self.anadir)
        self.btn_mostrar.clicked.connect(self.mostrar)
        self.btn_borrar.clicked.connect(self.eliminar)
        self.btn_actualizar.clicked.connect(self.actualizar)


        #Optimizamos tableWidget para poder eliminar registros y tener mejor control
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

        #Añadimos funcionalidad de seleccionar del listado
        self.tableWidget.itemClicked.connect(self.__seleccion)


    def __seleccion(self):
        trabajador = []
        items_de_fila = self.tableWidget.selectedItems()

        for items in items_de_fila:
            trabajador.append(items.text())


        self.txt_id.setText(trabajador[0])
        self.txt_fecha_ingreso.setText(trabajador[1])
        self.txt_tipo.setText(trabajador[2])
        self.txt_nombre.setText(trabajador[3])
        self.txt_apellido.setText(trabajador[4])
        self.txt_cedula.setText(trabajador[5])
        self.txt_valorHora.setText(trabajador[6])
        self.txt_hsSimples.setText(trabajador[7])
        self.txt_horasExtras.setText(trabajador[8])
        self.txt_hs_ext_esp.setText(trabajador[9])
        self.txt_hsNocturnas.setText(trabajador[10])
        self.txt_jornadaEsp.setText(trabajador[11])
        self.txt_hijosCargo.setText(trabajador[12])
        self.lineEdit.setText(trabajador[13]) #Hijos discapacitados

        return trabajador[0]



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
        """ #============== CLASE DEFINIDA EN GESTOR_DATOS ==============# """

    def eliminar(self):
        msg = QMessageBox()
        msg.setWindowTitle("Borrar Registro")
        msg.setText("¿Estas seguro que deseas eliminar el registro? no lo podras recuperar.")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self.__popup)
        msg.exec_()

    def __popup(self, i):

        if i.text() == 'OK' or i.text() == 'Ok' or i.text() == '&Ok' or i.text() == '&OK':
            msg2 = QMessageBox()
            msg2.setWindowTitle("Borrar Registro")
            msg2.setText("Registro Eliminado Satisfactoriamente. Cierra y vuelve a abrir la pantalla para ver los cambios.")
            msg2.setIcon(QMessageBox.Information)
            msg2.setStandardButtons(QMessageBox.Ok)
            msg2.exec_()
            data_base.deleteInfo(Workerid=self.__seleccion())
        else:
            pass



        """ #============== CLASE DEFINIDA EN GESTOR_DATOS ==============# """

    def actualizar(self):
        self.txt_id.setText("1")
        if self.rb_conyuge.isChecked():
            conyuge = True
        else:
            conyuge = False

        if self.rb_conyugeDisca.isChecked():
            conyugeDisca = True
        else:
            conyugeDisca = False


        if(len( self.txt_id.text() )!=0):
            print(self.txt_fecha_ingreso.text())
            data_base.updateInfo(self.txt_fecha_ingreso.text(), self.txt_tipo.text(), self.txt_nombre.text(), self.txt_apellido.text(), self.txt_cedula.text(), self.txt_valorHora.text(), self.txt_hsSimples.text(), self.txt_horasExtras.text(), self.txt_hs_ext_esp.text(), self.txt_hsNocturnas.text(), self.txt_jornadaEsp.text(), self.txt_hijosCargo.text(), self.lineEdit.text(), conyuge, conyugeDisca, self.txt_id.text())


            msg2 = QMessageBox()
            msg2.setWindowTitle("Base de datos actualizada")
            msg2.setText("Registro Actualizado Satisfactoriamente. Cierra y vuelve a abrir la pantalla para ver los cambios.")
            msg2.setIcon(QMessageBox.Information)
            msg2.setStandardButtons(QMessageBox.Ok)
            msg2.exec_()

    def __ingresarUsuarios(self):
        """ Esta Funcion es peligrosa, añade muchisimos Usuarios a la base de datos y llega hasta 1 millon de usuarios """
        global x
        global y
        tipos = 'Jornalero', 'Mensual'
        booleanos = True, False
        _id = 0

        for x in src.nombres.names:
            for y in src.apellidos.apellidos:
                _id+=1
                print("Esto vale id: ",_id)
                self.txt_id.setText( str(_id) )
                self.txt_fecha_ingreso.setText( "{}/{}/{}".format(random.randrange(1, 30, 1), random.randrange(1, 12, 1), random.randrange(2000, 2015, 1)) )
                z = self.txt_tipo.setText( '{}'.format(random.choice(tipos)) )
                self.txt_nombre.setText(x)
                self.txt_apellido.setText(y)
                self.txt_cedula.setText( str(random.randrange(10000000, 99999999)) )

                if self.txt_tipo.text() == 'mensual' or self.txt_tipo.text()== 'Mensual':
                    self.txt_valorHora.setText( str(random.randrange(10000, 80000, 1)) )
                    self.txt_hsSimples.setText('0')

                elif self.txt_tipo.text() == 'jornalero' or self.txt_tipo.text() == 'Jornalero':
                    self.txt_valorHora.setText( str( random.randrange(100, 800, 20)) )
                    self.txt_hsSimples.setText( str(random.randrange(100, 200, 1)) )

                self.txt_horasExtras.setText( str(random.randrange(0,30,1)) )
                self.txt_hs_ext_esp.setText( str(random.randrange(0,10,1)) )
                self.txt_hsNocturnas.setText( str(random.randrange(0,5,1)) )
                self.txt_jornadaEsp.setText( '0' )
                self.txt_hijosCargo.setText( str(random.randrange(0, 5)) )
                self.lineEdit.setText( str(random.randrange(0,5)) ) #Hijos discapacitados
                self.rb_conyuge.setChecked( random.choice(booleanos) )
                self.rb_conyugeDisca.setChecked( random.choice(booleanos) )

                if _id <= 100:
                    self.anadir()





    def retranslateUi(self, root_gestor):
        _translate = QtCore.QCoreApplication.translate
        root_gestor.setWindowTitle(_translate("root_gestor", "Gestor - Base de datos"))
        self.label.setText(_translate("root_gestor", "GESTOR BASE DE DATOS"))
        self.btn_anadir.setText(_translate("root_gestor", "Añadir trabajador"))
        self.btn_mostrar.setText(_translate("root_gestor", "Mostrar base de datos"))
        self.btn_limpiar.setText(_translate("root_gestor", "Limpiar campos"))
        self.btn_borrar.setText(_translate("root_gestor", "Borrar Registro"))
        self.btn_buscar.setText(_translate("root_gestor", "Buscar Trabajador"))
        self.btn_actualizar.setText(_translate("root_gestor", "Actualizar base de datos"))
        self.lbl_id.setText(_translate("root_gestor", "ID:"))
        self.lbl_fecha_ingreso.setText(_translate("root_gestor", "Fecha de Ingreso"))
        self.lbl_tipo.setText(_translate("root_gestor", "Tipo de Trabajador"))
        self.txt_tipo.setPlaceholderText(_translate("root_gestor", "Mensual o Jornalero"))
        self.lbl_nombre.setText(_translate("root_gestor", "Nombre"))
        self.lbl_apellido.setText(_translate("root_gestor", "Apellido"))
        self.lbl_cedula.setText(_translate("root_gestor", "Cedula Nro"))
        self.lbl_valorHora.setText(_translate("root_gestor", "Valor de la hora"))
        self.lbl_hsSimples.setText(_translate("root_gestor", "Horas simples"))
        self.lbl_horasExtras.setText(_translate("root_gestor", "Horas Extras"))
        self.lbl_hs_ext_esp.setText(_translate("root_gestor", "Horas Extras Especiales"))
        self.lbl_hsNocturnas.setText(_translate("root_gestor", "Horas Nocturnas"))
        self.lbl_jornadaEsp.setText(_translate("root_gestor", "Jornada Especial"))
        self.lbl_hijosCargo.setText(_translate("root_gestor", "Hijos a Cargo"))
        self.lbl_hijosDisca.setText(_translate("root_gestor", "Hijos discapacitados"))
        self.lbl_conyugeCargo.setText(_translate("root_gestor", "Conyuge a Cargo"))
        self.rb_conyuge.setText(_translate("root_gestor", "Si"))
        self.radioButton.setText(_translate("root_gestor", "No"))
        self.lbl_conyugeDisca.setText(_translate("root_gestor", "Conyuge Discapacitado"))
        self.rb_conyugeDisca.setText(_translate("root_gestor", "Si"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    root_gestor = QtWidgets.QMainWindow()
    ui = Ui_root_gestor()
    ui.setupUi(root_gestor)
    root_gestor.show()
    sys.exit(app.exec_())
