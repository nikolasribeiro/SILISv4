

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
        """.format(self.identificador, self.fecha_ingreso, self.tipo, self.sueldo, self.hs_simples, self.hs_ext, self.hs_ext_esp, self.hs_noct, self.jornada_esp, self.hijos, self.hijos_disca, self.conyuge, self.conyugeDisca)

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
        hora = float( self.calculo_hora() ) #El .text() te devuelve el valor que se encuentra dentro del entry
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
            tabla1 = rango2 + rango3 + rango4 + rango5 + \
                rango6 + rango7 + ((nominalBruto - 477710)*0.36)
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

        try:
            if totalDiscap > totalhijos:
                pass
            else:
                pass
        except:
            pass



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



        return liquidoreal, descBPS, descFonasa, descFRL, jornales, totalextras, totalEspeciales, totalNocturnas, totalJornadaEspecial, nominalBruto, nominalDescuento, irpf, liquidoreal, liquido1, descGral

    def reciboSueldo(self, data, jornales, totalextras, totalEspeciales, totalNocturnas, totalJornadaEspecial, nominalDescuento, irpf, liquidoreal, descBPS, descFonasa, descFRL, descGral, liquido1, hora2, nombre, apellido, tipo, iD):

        recibo = open("Recibos/{3} ,recibo sueldo {0} {1}, tipo: {2}, trabajador: {3}.txt".format(nombre, apellido, tipo, iD) , "w", encoding="utf-8")
        recibo.write(
    """
    ╔══════════════════════════════════ DATOS EMPRESA ══════════════════════════════════════════╗
    ║                                                                                           ║
    ║   Empresa: AMMNI Software  RUT:  210326540017     Nro BPS: 1234567890  Nro MTSS: 98765432 ║
    ║   Zonamerica, Perimetral y Ruta 8, MONTEVIDEO                                             ║
    ║                                                                                           ║
    ╠══════════════════════════════════ DATOS TRABAJADOR ═══════════════════════════════════════╣
    ║                                                                                           ║
    ║    Nombre: {0} {1}                   Documento: {32}      Ingreso: {2}                    ║
    ║    Cargo: Programador Jr           Oficina: Zonamerica         Nro Funcionario: {3}       ║
    ║    Fecha liquidacion: {4}           Tipo: JORNALERO                                       ║
    ║                                                                                           ║
    ╠═══════════════════════════════════════════════════════════════════════════════════════════╣
    ║    CONCEPTO                Cant                  Unid                     TOTAL           ║
    ║                                                                                           ║
    ║    Horas simples            {5}                   {6}                     {7}             ║
    ║    Horas extras             {8}                   {9}                     {10}            ║
    ║    Horas extras especiales  {11}                  {12}                    {13}            ║
    ║    Horas Nocturnas          {14}                  {15}                    {16}            ║
    ║    Feriado pago             {17}                  {18}                    {19}            ║
    ║                                                                                           ║
    ╠══════╦═══════════════════════════════════════════════════════════════════════════╦════════╣
    ║      ║    TOTAL NOMINAL:                                                   {20}  ║        ║
    ║      ╚═══════════════════════════════════════════════════════════════════════════╝        ║
    ║                                                                                           ║
    ║    BPS:                     {21}                                           {22}           ║
    ║    Fonasa:                  {23}                                           {24}           ║
    ║    FRL:                     {25}                                           {26}           ║
    ║    IRPF:                                                                   {27}           ║
    ╚══════╦═══════════════════════════════════════════════════════════════════════════╦════════╝
           ║    TOTAL DESCUENTOS:                                                {28}  ║
           ╠═══════════════════════════════════════════════════════════════════════════╣
           ║    LIQUIDO A COBRAR:                                                {29}  ║
           ╚═══════════════════════════════════════════════════════════════════════════╝

    ╔═══════════════════════════════════════════════════════════════════════════════════════════╗
    ║                                       --- Via 1 ---                                       ║
    ║    La empresa declara haber efectuado los aportes de seguridad social correspondientes a  ║
    ║                        los haberes liquidados el mes anterior                             ║
    ╠═══════════════════════════════════════════════════════════════════════════════════════════╣
    ║                                                                                           ║
    ╠════════════════════════════ Firma de conformidad del trabajador ══════════════════════════╣
    ║                                                                                           ║
    ║    Recibi el importe mencionado y las copias correspondientes a la liquidacion            ║
    ║    Fecha liquidacion: {30}                                                                ║
    ║    Hora liquidacion:  {31}                                                                ║
    ║                                                                                           ║
    ║    Firma: ______________________________________________________                          ║
    ╚═══════════════════════════════════════════════════════════════════════════════════════════╝
        """.format(data[1],data[2],data[6],data[0], 'fecha de hoy', self.hs_simples, self.calculo_hora(),  jornales, self.hs_ext, self.calculo_hora(),  totalextras, self.hs_ext_esp, self.calculo_hora(),  totalEspeciales, self.hs_noct, self.calculo_hora(),  totalNocturnas, self.jornada_esp,  totalJornadaEspecial,  totalJornadaEspecial, nominalDescuento, "15%",  descBPS, "4.5%",  descFonasa, "0.125%",  descFRL,  irpf,  liquido1,  liquidoreal,   'Fecha de hoy', hora2, data[3])
        )
        #print(data[1])
        recibo.close()

        #self.lbl_LIQUIDO.setText(str(round(liquidoreal)))
