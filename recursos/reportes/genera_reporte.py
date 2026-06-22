import base64

from PySide6.QtCore import QMarginsF, QDateTime
from PySide6.QtGui import QTextDocument
from PySide6.QtPrintSupport import QPrinter, QPrintPreviewDialog

from models.empresa import EmpresaModel


class GeneraReporte:
    def __init__(self, datos, parent):
        self.datos = datos
        inf = EmpresaModel().informacion()
        self.nombre_empresa = "Martin Electronic's"
        self.diremp = ""
        self.t1 = ""
        self.t2 = ""
        self.pw = ""
        self.em = ""
        self.img = None
        self.n1 = ""
        self.n2 = ""
        if inf:
            self.nombre_empresa = inf[1]
            self.diremp = inf[2]
            self.t1 = inf[3]
            self.t2 = inf[4]
            self.pw = inf[5]
            self.em = inf[6]
            self.img = base64.b64encode(inf[7]).decode("utf-8")
            self.n1 = inf[8]
            self.n2 = inf[9]
        self.printer = QPrinter()
        self.printer.setResolution(300)
        self.printer.setFullPage(False)
        self.printer.setPageMargins(QMarginsF(0, 0, 0, 0))
        self.preview = QPrintPreviewDialog(self.printer, parent)

    def reporte_de_entrada(self):
        self.preview.paintRequested.connect(self.render_entrada)
        self.preview.exec()


    def reporte_de_salida(self):
        self.preview.paintRequested.connect(self.render_salida)
        self.preview.exec()

    def render_entrada(self, printer):
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <style>
            *{{
                margin: 0;
                padding: 0;
            }}
            body {{
                font-family: 'Segoe UI', sans-serif;
                color: #333333;
            }}
            .container {{
                width: 100%;
                /* max-width: 750px; Limita el ancho para simular documento */
                margin: 0 27px;
                box-sizing: border-box;
            }}
            .header-table {{
                width: 100%;
            }}
            .line{{
                background-color: #2c3e50;
            }}
            .logo-container {{
                width: 120px; /* Ancho fijo para el logo */
                height: auto;
                text-align: left;
                padding-right: 0;
            }}
            .logo-img {{
                max-width: 80px;
                height: auto;
                max-height: 50px; /* Altura máxima para el logo */
                vertical-align: middle;
            }}
            .company-info {{
                padding: 0 35px 0 35px;
                vertical-align: top;
                text-align: center;
            }}
            .company-info strong {{
                color: #2c3e50;
                margin: 0 0 5px 0;
                font-size: 11pt;
                text-transform: uppercase;
            }}
            .company-info p {{
                margin: 2px 0;
                font-size: 7pt;
                line-height: 0.8;
            }}
            .report-title-section {{
                text-align: right;
                vertical-align: middle;
                white-space: nowrap; /* Evita que se rompa "Reporte de Entrada" */
            }}
            .report-title-section strong {{
                color: #7f8c8d;
                font-size: 8pt;
            }}
            .report-title-section p {{
                margin: 0;
                font-size: 7pt;
            }}
            .report-title-section .red {{
                color: red;
            }}
            .section-title {{
                background-color: #ecf0f1;
                font-weight: bold;
                padding: 6px 10px;
                color: #2c3e50;
                border-left: 5px solid #3498db; /* Un toque de color azul */
                margin-bottom: 5px;
                font-size: 7pt;
                text-transform: uppercase;
            }}
            .content-table {{
                width: 100%;
                font-size: 7pt;
                margin-bottom: 5px;
                border-collapse: collapse; /* Para bordes limpios */
            }}
            .content-table td {{
                padding-left: 0;
                vertical-align: top;
            }}
            
            .label {{
                font-weight: bold;
                color: #555555;
                width: 10%; /* Ajusta el ancho para las etiquetas */
                padding-right: 5px;
            }}
            .value {{
                border-bottom: 1px dotted #cccccc; /* Línea punteada sutil */
                width: 75%;
                padding-bottom: 2px;
                padding-left: 5px;
                min-height: 20px; /* Para asegurar el espacio si está vacío */
                vertical-align: bottom;
            }}
            .value.full-width {{
                width: 100%;
            }}
            .signature-table {{
                width: 100%;
                margin-top: 60px;
                border-collapse: collapse;
            }}
            .signature-table td {{
                width: 50%;
                text-align: center;
                padding-top: 20px; /* Espacio para la línea de firma */
            }}
            .signature-line {{
                padding-top: 5px;
                font-size: 7pt;
                color: #444444;
                text-align: center;
            }}
            .footer-note {{
                margin-top: 30px;
                font-size: 8pt;
                font-style: italic;
                color: #7f8c8d;
                text-align: center;
                border-top: 1px solid #ecf0f1;
                padding-top: 10px;
            }}
        </style>
        </head>
        <body>
            <div class="container">
                <table class="header-table">
                    <tr>
                        <td class="logo-container">
                            <img src="data:image/png;base64, {self.img}" alt="Logo Empresa" class="logo-img">
                        </td>
                        <td width="8%"></td>
                        <td class="company-info" >
                            <strong>{self.nombre_empresa}</strong>
                            <p>{self.diremp}</p>
                            <p>{self.t1} |  {self.t2}</p>
                            <p>{self.pw}</p>
                            <p>{self.em}</p>
                        </td>
                        <td width="8%"></td>
                        <td class="report-title-section">
                            <strong>REPORTE DE ENTRADA</strong>
                            <p><b>Nº Reporte:</b></p><p class="red"> 0{self.datos["equipo"][0]}</p>
                            <p><b>Fecha:</b>  {self.datos["fecha"][0:10]}</p>
                            <p><b>Hora:</b> {self.datos["fecha"][10:]}</p>
                        </td>
                    </tr>
                </table>
                <hr class="line" width="90%">
                <div class="section-title">Información del Cliente</div>
                <table class="content-table">
                    <tr>
                        <td class="label">Nombre del Cliente:</td>
                        <td class="value full-width">{self.datos["cliente"].nombre}</td>
                    </tr>
                    <tr>
                        <td class="label">Teléfono:</td>
                        <td class="value full-width">{self.datos["cliente"].telefono}</td>
                    </tr>
                </table>
        
                <div class="section-title">Información del Equipo</div>
                <table class="content-table">
                    <tr>
                        <td class="label">Equipo:</td>
                        <td class="value" width= 30%>{self.datos["equipo"][3]}</td>
                        <td width="10%"></td>
                        <td class="label">Marca:</td>
                        <td class="value" width= 30%>{self.datos["equipo"][4]}</td>
                    </tr>
                    <tr>
                        <td class="label">Modelo:</td>
                        <td class="value">{self.datos["equipo"][5]}</td>
                        <td></td>
                        <td class="label">Serie:</td>
                        <td class="value">{self.datos["equipo"][6]}</td>
                    </tr>
                    <tr>
                        <td class="label" width="11%">Falla Reportada:</td>
                        <td colspan="1" class="value full-width">{self.datos["equipo"][7]}</td>
                        <td></td>
                        <td class="label" width="11%">Accesorios incluidos:</td>
                        <td colspan="1" class="value full-width">{self.datos["equipo"][8]}</td>
                    </tr>
                </table>
                <table class="content-table">
                    <tr>
                        <td colspan="2" class="label">Información Adicional:</td>
                        <td colspan="3" class="value full-width">{self.datos["equipo"][9]}</td>
                    </tr>
                </table>
        
                <div class="section-title">Detalles del Servicio</div>
                <table class="content-table">
                    <tr>
                        <td class="label">Responsable de Recepción:</td>
                        <td class="value" width="25%">{self.datos["equipo"][12]}</td>
                        <td width="11%"></td>
                        <td width="40%"></td>
                        <td></td>
                    </tr>
                    <tr></tr>
                    <tr>
                        <td colspan="5">
                        <hr class="line" width="30%">
                            <div class="signature-line">Firma del Cliente: {self.datos["cliente"].nombre}</div>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="5">
                            <div class="footer-note">{self.n1}</div>
                        </td>
                    </tr>
                </table>
            </div>
        </body>
        </html>
        """
        doc = QTextDocument()
        doc.setDocumentMargin(0)
        doc.setHtml(html)
        doc.setPageSize(printer.pageRect(QPrinter.Unit.Point).size())
        doc.print_(printer)

    def render_salida(self, printer):
        print(self.datos)
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <style>
            *{{
                margin: 0;
                padding: 0;
            }}
            body {{
                font-family: 'Segoe UI', sans-serif;
                color: #333333;
            }}
            .container {{
                width: 100%;
                /* max-width: 750px; Limita el ancho para simular documento */
                margin: 0 27px;
                box-sizing: border-box;
            }}
            .header-table {{
                width: 100%;
            }}
            .line{{
                background-color: #2c3e50;
            }}
            .logo-container {{
                width: 120px; /* Ancho fijo para el logo */
                height: auto;
                text-align: left;
                padding-right: 0;
            }}
            .logo-img {{
                max-width: 80px;
                height: auto;
                max-height: 50px; /* Altura máxima para el logo */
                vertical-align: middle;
            }}
            .company-info {{
                padding: 0 35px 0 35px;
                vertical-align: top;
                text-align: center;
            }}
            .company-info strong {{
                color: #2c3e50;
                margin: 0 0 5px 0;
                font-size: 11pt;
                text-transform: uppercase;
            }}
            .company-info p {{
                margin: 2px 0;
                font-size: 7pt;
                line-height: 0.8;
            }}
            .report-title-section {{
                text-align: right;
                vertical-align: middle;
                white-space: nowrap; /* Evita que se rompa "Reporte de Entrada" */
            }}
            .report-title-section strong {{
                color: #7f8c8d;
                font-size: 8pt;
            }}
            .report-title-section p {{
                margin: 0;
                font-size: 7pt;
            }}
            .report-title-section .red {{
                color: red;
            }}
            .section-title {{
                background-color: #ecf0f1;
                font-weight: bold;
                padding: 6px 10px;
                color: #2c3e50;
                border-left: 5px solid #3498db; /* Un toque de color azul */
                margin-bottom: 5px;
                font-size: 7pt;
                text-transform: uppercase;
            }}
            .content-table {{
                width: 100%;
                font-size: 7pt;
                margin-bottom: 5px;
                border-collapse: collapse; /* Para bordes limpios */
            }}
            .content-table td {{
                padding-left: 0;
                vertical-align: top;
            }}

            .label {{
                font-weight: bold;
                color: #555555;
                width: 10%; /* Ajusta el ancho para las etiquetas */
                padding-right: 5px;
            }}
            .value {{
                border-bottom: 1px dotted #cccccc; /* Línea punteada sutil */
                width: 75%;
                padding-bottom: 2px;
                padding-left: 5px;
                min-height: 20px; /* Para asegurar el espacio si está vacío */
                vertical-align: bottom;
            }}
            .value.full-width {{
                width: 100%;
            }}
            .total {{
                border-bottom: 1px dotted #cccccc; /* Línea punteada sutil */
                width: 75%;
                padding-bottom: 2px;
                padding-left: 5px;
                min-height: 20px; /* Para asegurar el espacio si está vacío */
                vertical-align: bottom;
                font-size: 11pt;
            }}
            .signature-table {{
                width: 100%;
                margin-top: 60px;
                border-collapse: collapse;
            }}
            .signature-table td {{
                width: 50%;
                text-align: center;
                padding-top: 20px; /* Espacio para la línea de firma */
            }}
            .signature-line {{
                padding-top: 5px;
                font-size: 7pt;
                color: #444444;
                text-align: center;
            }}
            .footer-note {{
                margin-top: 30px;
                font-size: 8pt;
                font-style: italic;
                color: #7f8c8d;
                text-align: center;
                border-top: 1px solid #ecf0f1;
                padding-top: 10px;
            }}
        </style>
        </head>
        <body>
            <div class="container">
                <table class="header-table">
                    <tr>
                        <td class="logo-container">
                            <img src="data:image/png;base64, {self.img}" alt="Logo Empresa" class="logo-img">
                        </td>
                        <td width="8%"></td>
                        <td class="company-info" >
                            <strong>{self.nombre_empresa}</strong>
                            <p>{self.diremp}</p>
                            <p>{self.t1}  |  {self.t2}</p>
                            <p>{self.pw}</p>
                            <p>{self.em}</p>
                        </td>
                        <td width="8%"></td>
                        <td class="report-title-section">
                            <strong>REPORTE DE SALIDA</strong>
                            <p><b>Nº Reporte:</b></p><p class="red"> 0{self.datos["equipo"][0]}</p>
                            {self.datos["equipo"][15]}
                        </td>
                    </tr>
                </table>
                <hr class="line" width="90%">
                <div class="section-title">Información del Cliente</div>
                <table class="content-table">
                    <tr>
                        <td class="label">Nombre del Cliente:</td>
                        <td class="value full-width">{self.datos["cliente"][1]}</td>
                    </tr>
                    <tr>
                        <td class="label">Teléfono:</td>
                        <td class="value full-width">{self.datos["cliente"][2]}</td>
                    </tr>
                </table>

                <div class="section-title">Información del Equipo</div>
                <table class="content-table">
                    <tr>
                        <td class="label">Equipo:</td>
                        <td class="value" width= 30%>{self.datos["equipo"][8]}</td>
                        <td width="10%"></td>
                        <td class="label">Marca:</td>
                        <td class="value" width= 40%>{self.datos["equipo"][9]}</td>
                    </tr>
                    <tr>
                        <td class="label">Modelo:</td>
                        <td class="value">{self.datos["equipo"][10]}</td>
                        <td></td>
                        <td class="label">Serie:</td>
                        <td class="value">{self.datos["equipo"][11]}</td>
                    </tr>
                    <tr>
                        <td class="label" width="11%">Falla Reportada:</td>
                        <td colspan="1" class="value full-width">{self.datos["equipo"][12]}</td>
                        <td></td>
                        <td class="label" width="11%">Accesorios incluidos:</td>
                        <td colspan="1" class="value full-width">{self.datos["equipo"][13]}</td>
                    </tr>
                </table>
                <table class="content-table">
                    <tr>
                        <td colspan="2" class="label">Información Adicional:</td>
                        <td colspan="3" class="value full-width">{self.datos["equipo"][14]}</td>
                    </tr>
                </table>

                <div class="section-title">Detalles del Servicio</div>
                <table class="content-table">
                    <tr>
                        <td class="label">Diagnostico:</td>
                        <td class="value" width= 30%>{self.datos["equipo"][3]}</td>
                        <td width="10%"></td>
                        <td class="label">Fecha de Reparación:</td>
                        <td class="value">{self.datos["equipo"][5]}</td>
                    </tr>
                    <tr>
                        <td class="label">Total:</td>
                        <td class="total"><b>${self.datos["equipo"][2]}</b></td>
                        <td></td>
                        <td class="label">Con garantia hasta:</td>
                        <td class="value">{QDateTime.fromString(self.datos["equipo"][5], 'dd/MM/yyyy hh:mm:ss ap').addDays(int(self.datos["equipo"][6])).toString('dd/MM/yyyy hh:mm:ss ap')}</td>
                    </tr>
                    <tr>
                        <td class="label">Responsable de Entrega:</td>
                        <td class="value">{self.datos["user"][1]}</td>
                        <td width="11%"></td>
                        <td class="label">Tecnico:</td>
                        <td class="value">{self.datos["equipo"][16]}</td>
                    </tr>
                    <tr></tr>
                    <tr>
                        <td colspan="5">
                        <hr class="line" width="30%">
                            <div class="signature-line">Firma del Cliente: {self.datos["cliente"][1]}</div>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="5">
                            <div class="footer-note">{self.n2}</div>
                        </td>
                    </tr>
                </table>
            </div>
        </body>
        </html>
        """
        doc = QTextDocument()
        doc.setDocumentMargin(0)
        doc.setHtml(html)
        doc.setPageSize(printer.pageRect(QPrinter.Unit.Point).size())
        doc.print_(printer)
