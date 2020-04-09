"""
Sistema liquidacion de sueldos - Backend
Copyright 2019 - AMNII Software
"""
import sqlite3

def workerData():
    start = sqlite3.connect("trabajadores.db")
    start.execute("CREATE TABLE IF NOT EXISTS trabajadores(Workerid INTEGER PRIMARY KEY AUTOINCREMENT, fechaIngreso TEXT, tipo TEXT, nombre TEXT, apellido TEXT, cedula TEXT, valorHora TEXT, simples TEXT, extras TEXT, especiales TEXT, nocturnas TEXT, jorEspecial TEXT, hijos TEXT, discapacitados TEXT, conyuge BOOL, conyugeDisca BOOL)")
    start.commit()
    start.close()

def addInfo(fechaIngreso, tipo, nombre, apellido, cedula, valorHora, simples, extras, especiales, nocturnas, jorEspecial, hijos, discapacitados, conyuge, conyugeDisca):
    start = sqlite3.connect("trabajadores.db")
    pointer = start.cursor()
    test = pointer.execute("INSERT INTO trabajadores(Workerid, fechaIngreso, tipo, nombre, apellido, cedula, valorHora, simples, extras, especiales, nocturnas, jorEspecial, hijos, discapacitados, conyuge, conyugeDisca) VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(fechaIngreso, tipo, nombre, apellido, cedula, valorHora, simples, extras, especiales, nocturnas, jorEspecial, hijos, discapacitados, conyuge, conyugeDisca,),)
    print(test)
    start.commit()
    start.close()

def displayInfo():
    start = sqlite3.connect("trabajadores.db")
    pointer = start.cursor()
    pointer.execute("SELECT * FROM trabajadores")
    row = pointer.fetchall() #Te da una tupla con todos los datos
    start.close()
    return row

def displayInfoMainWindow():
    start = sqlite3.connect("trabajadores.db")
    pointer = start.cursor()
    pointer.execute("SELECT Workerid, nombre, apellido FROM trabajadores")
    row = pointer.fetchall() #Te da una tupla con todos los datos
    start.close()
    return row

def selectUnique(Workerid):
    start = sqlite3.connect("trabajadores.db")
    pointer = start.cursor()
    pointer.execute("SELECT * FROM trabajadores WHERE Workerid=?",(Workerid,))
    row = pointer.fetchall()
    start.close()
    return row

def getID():
    start = sqlite3.connect("trabajadores.db")
    pointer = start.cursor()
    pointer.execute("SELECT Workerid FROM trabajadores")
    row = pointer.fetchall()
    start.close()
    return row

def deleteInfo(Workerid):
    start = sqlite3.connect("trabajadores.db")
    pointer = start.cursor()
    pointer.execute("DELETE FROM trabajadores WHERE Workerid=?",(Workerid,))
    pointer.execute("DELETE FROM sqlite_sequence WHERE name = 'trabajadores' ")
    start.commit()
    start.close()

def searchInfo(ingreso="", cedula="", valorHora="", simples="", extras="", especiales="", nocturnas="", jorEspecial=""):
    start = sqlite3.connect("trabajadores.db")
    pointer = start.cursor()
    pointer.execute("SELECT * FROM trabajadores WHERE ingreso =? OR cedula=? OR valorHora =? OR simples =? OR extras =? OR especiales =? OR nocturnas =? OR jorEspecial =?",(ingreso, cedula, valorHora, simples, extras, especiales, nocturnas, jorEspecial))
    row = pointer.fetchall()
    start.close()
    return row

def getSon():
    start = sqlite3.connect("trabajadores.db")
    pointer = start.cursor()
    pointer.execute("SELECT Workerid, hijos FROM trabajadores")
    row = pointer.fetchall()
    start.close()
    return row

def updateInfo(fechaIngreso, tipo, nombre, apellido, cedula, valorHora, simples, extras, especiales, nocturnas, jorEspecial, hijos, discapacitados, conyuge, conyugeDisca, Workerid):
    start = sqlite3.connect('trabajadores.db')
    pointer = start.cursor()
    pointer.execute('UPDATE trabajadores SET fechaIngreso=?, tipo=?, nombre=?, apellido=?, cedula=?, valorHora=?, simples=?, extras=?, especiales=?, nocturnas=?, jorEspecial=?, hijos=?, discapacitados=?, conyuge=?, conyugeDisca=? WHERE Workerid=?', (fechaIngreso, tipo, nombre, apellido, cedula, valorHora, simples, extras, especiales, nocturnas, jorEspecial, hijos, discapacitados, conyuge, conyugeDisca, Workerid,))
    start.commit()
    start.close()

workerData()
