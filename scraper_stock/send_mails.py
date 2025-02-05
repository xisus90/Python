import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from data_code import Database


class AutoMails:
  
    def __init__(self):
        pass

    def Sendmail(self, mails, current_title, current_price, db_price):
    # 📌 Configurar credenciales del correo
        SMTP_SERVER = "smtp.gmail.com"  # Servidor SMTP de Gmail
        SMTP_PORT = 587  # Puerto de salida (587 es estándar para TLS)
        EMAIL_SENDER = "krukasd90@gmail.com"  # Cambia esto por tu correo
        EMAIL_PASSWORD = "!123456@"  # Cambia esto por tu contraseña o contraseña de aplicación


        while len(AutoMails):
            # 📌 Asunto y cuerpo del correo
            subject = "¡Saludos desde Python!"
            body = f"""
            Hola, El juego {current_title} al que estás suscrito ha bajado su precio ha {current_price}€ el su 
            anterior precio era de {db_price}€
            Saludos
            """

            # 📌 Lista de destinatarios
            EMAIL_RECEIVERS = mails

            # 📌 Construir el mensaje
            msg = MIMEMultipart()
            msg["From"] = EMAIL_SENDER
            msg["To"] = ", ".join(EMAIL_RECEIVERS)  # Convertir la lista en una cadena separada por comas
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))  # "plain" = texto sin formato (también puedes usar "html")

            try:
                # 📌 Conectar al servidor SMTP
                server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
                server.starttls()  # Habilitar TLS
                server.login(EMAIL_SENDER, EMAIL_PASSWORD)  # Autenticación

                # 📌 Enviar el correo a todos los destinatarios
                server.sendmail(EMAIL_SENDER, EMAIL_RECEIVERS, msg.as_string())

                print("✅ Correo enviado correctamente a todos los destinatarios.")

                # 📌 Cerrar la conexión
                server.quit()

            except Exception as e:
                print(f"❌ Error al enviar el correo: {e}")

