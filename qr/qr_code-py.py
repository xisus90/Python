import pandas as pd
import qrcode
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class QR:

    def __init__(self, file_path="exported_data.csv"):
            """Inicializa el DataLoader y carga los datos desde un archivo CSV/Excel."""
            self._file_path = file_path
            self._df = self.load_data()

    def load_data(self):
        """Carga los datos del archivo en un DataFrame de Pandas."""

        try:
            df = pd.read_csv(self._file_path, delimiter='\t', encoding='utf-8')
            print(f"✅ Archivo {self._file_path} cargado correctamente.")
            return df
        except FileNotFoundError:
            print(f"❌ Error: El archivo {self._file_path} no se encontró.")
            return None
        except Exception as e:
            print(f"❌ Error al leer el archivo: {e}")
            return None


    def Sendmail(self, mails, file_name):
        """Envía un correo a los usuarios suscritos cuando el precio de un juego baja."""
        
        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = 587
        EMAIL_SENDER = "krukasd90@gmail.com"  
        EMAIL_PASSWORD = "swvh utym onkh gzxp"

        if isinstance(mails, str):  
            mails = [mails]  

        subject = "Código QR para comida de la falla"
        body = f"""        Hola, aquí tienes el código QR para la falla.       """

        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = ", ".join(mails)
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain")) 


        file_path = os.path.abspath(os.path.join("QR_with_mail", file_name))

        with open(file_path, "rb") as attachment:  # ✅ Usa la ruta completa
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={file_name}")

        msg.attach(part)

        try:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls() 
            server.login(EMAIL_SENDER, EMAIL_PASSWORD) 

            server.sendmail(EMAIL_SENDER, mails, msg.as_string())

            print(f"✅ Correo enviado correctamente. {mails}")

        except Exception as e:
            print(f"❌ Error al enviar el correo: {e}")

        finally:
            server.quit() 


    def QR_generate(self):
        
        directory_script = os.path.dirname(os.path.abspath(__file__))
        os.chdir(directory_script)

        destiny_Carpet_mail = "QR_with_mail"
        destiny_Carpet_no_mail = "QR_Without_mail"
        os.makedirs(destiny_Carpet_mail, exist_ok=True)
        os.makedirs(destiny_Carpet_no_mail, exist_ok=True)

        #print(f"Columnas detectadas antes de limpieza: {self._df.columns.tolist()}")
        self._df.columns = self._df.columns.str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

        colum_needed = ["nombre", "telefono", "mail"]
        for col in colum_needed:
            if col not in self._df.columns:
                print(f"Error: Falta la columna '{col}' en el archivo CSV.")
                exit()

        count_mails = 0
        count_no_mails = 0

        for line in range(len(self._df)):
            name = str(self._df["nombre"].iloc[line]).strip()
            mail = str(self._df["mail"].iloc[line]).strip()

            data = f"Nombre: {name}"

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill="black", back_color="white")

            if mail == "nan":
                img.save(os.path.join(destiny_Carpet_no_mail, f"codigo_qr_{name}.png"))
                count_no_mails += 1
            if mail != "nan":
                count_mails += 1
                img.save(os.path.join(destiny_Carpet_mail, f"codigo_qr_{name}.png"))
                file_name = f"codigo_qr_{name}.png"
                self.Sendmail(mail, file_name)

        total_count = count_no_mails + count_mails
        print (f"se han guardado un total de {count_mails} QR con mails y {count_no_mails} QR sin mails, total {total_count}")

            

if __name__ == "__main__":
    QR().QR_generate()

