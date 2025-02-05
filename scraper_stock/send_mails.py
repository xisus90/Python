import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class AutoMails:
  
    def __init__(self):
        pass

    def Sendmail(mails, current_title, current_price, db_price):
        """Envía un correo a los usuarios suscritos cuando el precio de un juego baja."""

        # Configurar credenciales del correo
        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = 587
        EMAIL_SENDER = "krukasd90@gmail.com"  # Cambia esto por tu correo
        EMAIL_PASSWORD = "swvh utym onkh gzxp"  # Usa una contraseña de aplicación

        # 🔹 Asegurar que `mails` es una lista válida de correos
        if isinstance(mails, str):  
            mails = [mails]  # Convertir en lista si es un solo correo

        if not mails:
            print("⚠️ No hay destinatarios para enviar el correo.")
            return

        print("📧 Enviando correo a:", ", ".join(mails))

        # Asunto y cuerpo del correo
        subject = "¡El precio de tu juego ha bajado!"
        body = f"""
        Hola,

        El juego '{current_title}', al que estás suscrito, ha bajado de precio.

        🔻 Nuevo precio: {current_price}€
        📌 Precio anterior: {db_price}€

        ¡Aprovecha la oferta!

        Saludos,
        El equipo de notificaciones de precios
        """

        # Construir el mensaje
        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = ", ".join(mails)  # Convertir la lista en una cadena separada por comas
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))  # "plain" = texto sin formato

        try:
            # Conectar al servidor SMTP
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()  # Habilitar TLS para conexión segura
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)  # Autenticación

            # Enviar el correo a todos los destinatarios
            server.sendmail(EMAIL_SENDER, mails, msg.as_string())

            print("✅ Correo enviado correctamente.")

        except Exception as e:
            print(f"❌ Error al enviar el correo: {e}")

        finally:
            server.quit()  # Cerrar conexión SMTP siempre, sin importar si hubo error o no