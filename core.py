import pdfkit

""" 
        Valores del data
        data[0]     = ID del trabajador
        data[1]     = fecha de ingreso del trabajador
        data[2]     = Tipo de trabajador
        data[3]     = Nombre del trabajador
        data[4]     = Apellido del trabajador
        data[5]     = cedula del trabajador
        data[6]     = valor de la hora
        data[7]     = Horas Simples
        data[8]     = Horas Extras
        data[9]     = Extras especiales
        data[10]    = Jornadas especiales
        data[11]    = Hijos a cargo
        data[12]    = Hijos Discapacitados
        data[13]    = Conyuge Cargo
        data[14]    = Conyuge cargo discapacitado
"""

class Trabajador:
    def __init__(self, identificador, fecha_ingreso, tipo, sueldo, hs_simples, hs_ext, hs_ext_esp, hs_noct, jornada_esp, hijos, hijos_disca, conyuge, conyugeDisca):
        self.identificador  = identificador
        self.fecha_ingreso  = fecha_ingreso
        self.tipo           = tipo.lower()
        self.sueldo         = sueldo
        self.hs_simples     = hs_simples
        self.hs_ext         = hs_ext
        self.hs_ext_esp     = hs_ext_esp
        self.hs_noct        = hs_noct
        self.jornada_esp    = jornada_esp
        self.hijos          = hijos
        self.hijos_disca    = hijos_disca
        self.conyuge        = conyuge
        self.conyugeDisca   = conyugeDisca

    def debugg(self):
        return """
        ID:                 {0}
        Fecha:              {1}
        Tipo:               {2}
        Sueldo:             {3}
        Horas Simp:         {4}
        Horas Ext:          {5}
        Horas Ext Esp:      {6}
        Horas Noct:         {7}
        Jornada Especial:   {8}
        Hijos:              {9}
        Hijos Disca:        {10}
        Conyuge:            {11}
        Conyuge Disca:      {12}
        """.format(
            self.identificador, 
            self.fecha_ingreso, 
            self.tipo, 
            self.sueldo, 
            self.hs_simples, 
            self.hs_ext, 
            self.hs_ext_esp, 
            self.hs_noct, 
            self.jornada_esp, 
            self.hijos, 
            self.hijos_disca, 
            self.conyuge, 
            self.conyugeDisca)

    def mensual(self):
        sueldo_nominal = self.sueldo
        return sueldo_nominal

    def jornalero(self):
        valor_hora = self.hs_simples * self.sueldo
        return valor_hora

    def calculo_hora(self):
        if self.tipo == 'mensual':
            precio_hora = (int(self.sueldo) / 30) / 8
            return round(int(precio_hora))

        elif self.tipo == 'jornalero':
            precio_hora = self.sueldo
            return round(int(precio_hora))

    def liquidar(self):
        # ================ Calculo nominal ========================
        hora = float( self.calculo_hora() ) 
        base = float( self.hs_simples )
        extra = float( self.hs_ext )
        especiales = float( self.hs_ext_esp )
        nocturnas =  float( self.hs_noct )
        jornadaEspecial = float( self.jornada_esp )


        if base == 0.0 or base == 0:
            jornales = float(self.sueldo)

        else:
            jornales = hora * base


        totalextras = (hora * extra) * 2
        totalEspeciales = (hora * especiales)*2.5
        totalNocturnas = (hora + (hora * 0.20)) * nocturnas
        totalJornadaEspecial = ((8 * hora)) * jornadaEspecial

        nominalBruto = jornales + totalextras + totalEspeciales
        nominalDescuento = jornales + totalextras + totalEspeciales

        
        print("================================")
        print("Tipo de trabajador: ",self.tipo)
        print("$xHora: ",hora)
        print("Jornales: ", jornales)
        print("Total Extras: ", totalextras)
        print("Total Especiales: ", totalEspeciales)
        print("Total Nocturnas: ", totalNocturnas)
        print("Nominal Bruto: ", nominalBruto)
        print("Nominal Descuento ", nominalDescuento)
        print("================================")
        

        if nocturnas != 0:
            nominalBruto = jornales + totalextras + totalEspeciales + totalNocturnas
            nominalDescuento = jornales + totalextras + totalEspeciales + totalNocturnas

        if jornadaEspecial != 0:
            nominalBruto = jornales + totalextras + totalEspeciales + totalJornadaEspecial
            nominalDescuento = jornales + totalextras + totalEspeciales + totalJornadaEspecial

        if nocturnas != 0 and jornadaEspecial != 0:
            nominalBruto = jornales + totalextras + totalEspeciales + totalNocturnas + totalJornadaEspecial
            nominalDescuento = jornales + totalextras + totalEspeciales + totalNocturnas + totalJornadaEspecial

        BPC = 4154 * 10 # todos los datos actualizado 17 de Marzo 2019
        rango8 = ""
        rango7 = round((477710-311550)*0.31)
        rango6 = round((311550-207700)*0.27)
        rango5 = round((207700-124620)*0.25)
        rango4 = round((124620-62310)*0.24)
        rango3 = round((62310-41540)*0.15)
        rango2 = round((41540-29078)*0.10)
        rango1 = ""

        if nominalBruto > BPC:
            nominalBruto = nominalBruto * 1.06

        if nominalBruto > 477710:
            tabla1 = rango2 + rango3 + rango4 + rango5 + rango6 + rango7 + ((nominalBruto - 477710)*0.36)
            #print("Rango 8",tabla1)
        if nominalBruto > 311550:
            tabla1 = rango2 + rango3 + rango4 + rango5 + rango6 + ((nominalBruto - 311550)*0.31)
            #print("Rango 7",tabla1)
        if nominalBruto > 207700:
            tabla1 = rango2 + rango3 + rango4 + rango5 + ((nominalBruto - 207700)*0.27)
            #print("Rango 6",tabla1)
        if nominalBruto > 124620:
            tabla1 = rango2 + rango3 + rango4 + ((nominalBruto - 124620)*0.25)
            #print("Rango 5",tabla1)
        if nominalBruto > 62310:
            tabla1 = rango2 + rango3 + ((nominalBruto - 62310)*0.24)
            #print("Rango 4",tabla1)
        if nominalBruto > 41540:
            tabla1 = rango2 + ((nominalBruto - 41540)*0.15)
            #print("Rango 3",tabla1)
        if nominalBruto > 29078:
            tabla1 = ((nominalBruto - 29078)*0.10)
            #print("Rango 2",tabla1)
        if nominalBruto <= 29078:
            tabla1 = nominalBruto - 29078
            #print("Rango 1",tabla1)
        if tabla1 < 0:
            tabla1 = 0


        # Comienzo de los descuentos TABLA 2
        # todos los datos actualizado 17 de Marzo 2019
        precioHijos = 4500
        precioDiscapacitado = 9000
        valorBPS = 0.15
        valorFRL = 0.00125
        valorFonasa = 0.045
        descBPS = nominalDescuento * valorBPS
        descFonasa = nominalDescuento * valorFonasa
        descFRL = nominalDescuento * valorFRL
        descGral = descBPS + descFonasa + descFRL
        totalDiscap = float( self.hijos_disca )
        tabla2 = 0
        discaDescuentos = 0
        conyugeDisca = 0

        totalhijos = float( self.hijos )

        if totalhijos <= 5:
            hijosDescuento = totalhijos * precioHijos

        else:
            hijosDescuento = 5 * precioHijos

        
        if self.conyugeDisca == 1 or self.conyugeDisca == True:
            conyugeDisca = precioDiscapacitado
            totalDescuentoMasDisca = descGral + conyugeDisca + hijosDescuento

            if totalDescuentoMasDisca > 62310:
                tabla2 = totalDescuentoMasDisca * 0.08

            else:
                tabla2 = totalDescuentoMasDisca * 0.10


        elif self.conyugeDisca == 0 or self.conyugeDisca == False:

            totalDescuentoMasDisca = descGral + conyugeDisca + hijosDescuento

            if totalDescuentoMasDisca > 62310:
                tabla2 = totalDescuentoMasDisca * 0.08

            else:
                tabla2 = totalDescuentoMasDisca * 0.10

            conyugeDisca = 0



        irpf = tabla1 - tabla2

        if irpf < 0:
            irpf = 0
            liquido1 = descGral + irpf
            liquidoreal = nominalDescuento - liquido1

        else:
            liquido1 = descGral + irpf
            liquidoreal = nominalDescuento - liquido1


            #   0           1           2           3       4       5               6               7                       8                   9           10           11    12          13                                    
        return descBPS, descFonasa, descFRL, jornales, totalextras, totalEspeciales, totalNocturnas, totalJornadaEspecial, nominalBruto, nominalDescuento, irpf, liquidoreal, liquido1, descGral

    def reciboSueldo(self, data, jornales, totalextras, totalEspeciales, totalNocturnas, totalJornadaEspecial, nominalDescuento, irpf, liquidoreal, descBPS, descFonasa, descFRL, descGral, liquido1, hora2, nombre, apellido, tipo, iD):
        
        recibo = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Template</title>
        <style>
            .contenedor{{
                border: 1px solid black;
                width: 80%;
            }}
            .table-header{{
                text-align: center;
            }}

            #datos-empresa{{
                border: 1px solid black;
            }}

            
        </style>
        </head>
        <body>

        <div class="contenedor">

            <div id="datos-empresa">
                <table border="0" width="100%" align="center">
                    <h3 class="table-header">DATOS DE LA EMPRESA</h3>
        
                    <tr> <td>Empresa: AMMNI Software</td> <td>RUT: 210326540017</td> <td>BPS: 1234567890</td> <td>MTSS: 98765432</td></tr>
                    <span> Direccion: Zonamerica, Perimetral y Ruta 8, Montevideo </span>
                    
                </table>
            </div>

            <div id="datos-trabajador">
                <table border="0" width="100%" align="center">
                    <h3 class="table-header">DATOS TRABAJADOR</h3>
                    <tr> <td>Nombre: {nombre} {apellido} </td> <td>Documento: {documento} </td> <td>Fecha de ingreso: {fecha_ingreso} </td></tr>
                    <tr> <td>Cargo: Programador Jr</td> <td>Nro Funcionario: {numero_funcionario}</td> <td>Fecha Liqudacion: {fecha_liquidacion} </td></tr>
                    <tr> <td>Tipo: {tipo_trabajador} </td> <td>Oficina: Zonamerica</td> </tr>
                </table>
            </div>


            <table border="0" width="100%" align="center">
                <h5>Nominal</h5>
                    <tr> <td> <hr> </td> <td> <hr> </td> <td> <hr> </td> <td> <hr> </td></tr>
                    <tr> <td>Concepto </td> <td>Cantidad</td> <td>Unitario</td> <td>Total</td></tr>

                    <tr> <td>Horas Simples: </td> <td> {a} </td> <td> {b} </td> <td> {c} </td></tr>
                    <tr> <td>Horas Extras: </td> <td> {d} </td> <td> {e} </td> <td> {f} </td></tr>
                    <tr> <td>Horas Extras Especiales: </td> <td> {g} </td> <td> {h} </td> <td> {i} </td></tr>
                    <tr> <td>Horas Nocturnas: </td> <td> {j} </td> <td> {k} </td> <td> {l} </td></tr>
                    <tr> <td>Feriados Pago: </td> <td> {m} </td> <td> {n} </td> <td> {o} </td></tr>
                    <tr> <td> <hr> </td> <td> <hr> </td> <td> <hr> </td> <td> <hr> </td></tr>
                    <tr> <td>TOTAL NOMINAL: </td> <td> </td> <td> </td> <td> {total_nominal} </td></tr>
                    <tr> <td> <hr> </td> <td> <hr> </td> <td> <hr> </td> <td> <hr> </td></tr>

            </table>


            <table border="0" width="100%" align="center">
                <h5 >Descuentos</h5>
            
                    <tr> <td>Concepto </td> <td>Cantidad</td> <td>Total</td></tr>

                    <tr> <td>BPS: </td> <td> {p} </td> <td> {q} </td> </tr>
                    <tr> <td>FONASA: </td> <td> {r} </td> <td> {s} </td> </tr>
                    <tr> <td>FRL: </td> <td> {t} </td> <td>{u}</td> </tr>
                    <tr> <td>IRPF: </td> <td> </td> <td>{v} </td>  </tr>
                    <tr> <td> <hr> </td> <td> <hr> </td> <td> <hr> </td> <td> <hr> </td></tr>
                    <tr> <td>TOTAL DESCUENTOS: </td> <td> </td> <td> </td> <td> {total_descuento} </td></tr>
                    <tr> <td> <hr> </td> <td> <hr> </td> <td> <hr> </td> <td> <hr> </td></tr>
                    <tr> <td>LIQUIDO A COBRAR: </td> <td> </td> <td> </td> <td> {liquido} </td></tr>
                    <tr> <td> <hr> </td> <td> <hr> </td> <td> <hr> </td> <td> <hr> </td></tr>

            </table>

            <p>
                <table>
                    <p class="table-header">--- Via 1 ---</p>
                    <p class="table-header">
                    La empresa declara haber efectuado los aportes de seguridad social correspondientes
                    a los haberes liquidados del mes anterior
                    </p>
                </table>
            </p>

            <table align="center" width="50%">
                <h3 class="table-header">Firma de conformidad del trabajador</h3>
                <p class="table-header">Recibi el importe mencionado y las copias correspondientes a la liquidacion</p>
                <tr> <td>Fecha de Liquidacion: </td> <td> {fecha_liquidacion} </td></tr>
                <tr> <td>Hora de Liquidacion: </td> <td> {hora_liquidacion} </td></tr>
                <tr> <td>FIRMA: </td> <td>firma</td></tr>
            </table>

        </div>

        </body>
        </html> """.format(
                nombre              = data[3],
                apellido            = data[4],
                documento           = data[5],
                fecha_ingreso       = data[1], 
                numero_funcionario  = data[0],
                fecha_liquidacion   = 'fecha de hoy',
                tipo_trabajador     = data[2],
                a                   = self.hs_simples, 
                b                   = self.calculo_hora(),  
                c                   = jornales, 
                d                   = self.hs_ext, 
                e                   = self.calculo_hora(),  
                f                   = totalextras, 
                g                   = self.hs_ext_esp, 
                h                   = self.calculo_hora(),  
                i                   = totalEspeciales, 
                j                   = self.hs_noct, 
                k                   = self.calculo_hora(),  
                l                   = totalNocturnas, 
                m                   = self.jornada_esp,  
                n                   = totalJornadaEspecial,  
                o                   = totalJornadaEspecial, 
                total_nominal       = nominalDescuento, 
                p                   = "15%",  
                q                   = descBPS, 
                r                   = "4.5%",  
                s                   = descFonasa, 
                t                   = "0.125%",  
                u                   = descFRL,  
                v                   = irpf,  
                total_descuento     = liquido1, 
                liquido             = liquidoreal,  
                hora_liquidacion    = hora2,) 
                                    
        print(totalEspeciales)

        pdfkit.from_string(recibo, 'Recibos/{3}, recibo sueldo {0} {1}, Tipo: {2}, trabajador: {3}.pdf'.format(nombre, apellido, tipo, iD) )

        exit()

        


