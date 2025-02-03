import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from data_code import Database


class AutoMails:

    def Mails_to_users(title, current_price, db_price):
        
        user = Database().user_to_game(title)

        if not user:
            return None

        users = [item for u in user for item in u.split(", ")]
        cleaned_user = str(users).replace("[", "").replace("]", "").replace("'", "")
        print(f"El usuario {cleaned_user} está suscrito al juego: {title}")
        
        #sender_mail = "xisus90@gmail.com"
        #receiver_mail = ""
