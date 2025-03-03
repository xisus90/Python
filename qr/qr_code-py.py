import pandas as pd
import qrcode
import os


class Falla_QR_Mail():

    def __init__(self):
        pass        

    def send_mail(self, mail):

        print(f"el correo es {mail}")



    def QR(self):
        
        directory_script = os.path.dirname(os.path.abspath(__file__))
        os.chdir(directory_script)

        file = "datos_falla.csv"

        destiny_Carpet_mail = "QR_with_mail"
        destiny_Carpet_no_mail = "QR_Without_mail"
        os.makedirs(destiny_Carpet_mail, exist_ok=True)
        os.makedirs(destiny_Carpet_no_mail, exist_ok=True)

        try:
            df = pd.read_csv(file, delimiter='\t', encoding='utf-8')
        except Exception as e:
            print(f"Error al leer el archivo CSV: {e}")
            exit()

        print(f"Columnas detectadas antes de limpieza: {df.columns.tolist()}")

        df.columns = df.columns.str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)

        print(f"Columnas detectadas después de limpieza: {df.columns.tolist()}")

        colum_needed = ["nombre", "telefono", "mail"]
        for col in colum_needed:
            if col not in df.columns:
                print(f"Error: Falta la columna '{col}' en el archivo CSV.")
                exit()

        count_mails = 0
        count_no_mails = 0

        for fila in range(len(df)):
            name = str(df["nombre"].iloc[fila]).strip()
            phone = str(df["telefono"].iloc[fila]).strip()
            mail = str(df["mail"].iloc[fila]).strip()

            data = f"Nombre: {name}, Teléfono: {phone}, Correo: {mail}"


            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill="black", back_color="white")

            file_name = "".join(c if c.isalnum() or c in " _-" else "_" for c in name)

            if mail == "nan":
                img.save(os.path.join(destiny_Carpet_no_mail, f"codigo_qr_{file_name}.png"))
                count_no_mails += 1
            if mail != "nan":
                count_mails += 1
                mails = self.send_mail(mail)
                img.save(os.path.join(destiny_Carpet_mail, f"codigo_qr_{file_name}.png"))
        
        total_count = count_no_mails + count_mails
        print (f"se han guardado un total de {count_mails} QR con mails y {count_no_mails} QR sin mails, total {total_count}")

            


if __name__ == "__main__":
    Falla_QR_Mail().QR()

