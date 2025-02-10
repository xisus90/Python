import unittest
from unittest.mock import Mock

# Importa la clase que quieres probar
from data_code import ActionAlertWhenPriceIsCheaper

class TestPriceAlert(unittest.TestCase):


    
    def test_send_email_for_cyberpunk(self):
        # 1️⃣ Simulamos la base de datos y el cliente de correo
        mock_database = Mock()
        mock_mail_client = Mock()

        # 2️⃣ Simulamos un suscriptor para "Cyberpunk 2077"
        mock_database.getAllSubscribers.return_value = ["pepe@gmail.com"]

        # 3️⃣ Ejecutamos la función solo para Cyberpunk
        action = ActionAlertWhenPriceIsCheaper(mock_database, mock_mail_client)
        action.Execute("Cyberpunk 2077", 50)

        # 4️⃣ Verificamos que se envió el correo correctamente
        mock_mail_client.send_mail.assert_called_with(
            "pepe@gmail.com", "El juego Cyberpunk 2077 ha bajado de precio a 50€"
        )

        # 5️⃣ Aseguramos que solo se haya enviado un correo
        self.assertEqual(mock_mail_client.send_mail.call_count, 1)

    def test_send_email_for_elden_ring(self):
        # 1️⃣ Simulamos la base de datos y el cliente de correo
        mock_database = Mock()
        mock_mail_client = Mock()

        # 2️⃣ Simulamos un suscriptor para "Elden Ring"
        mock_database.getAllSubscribers.return_value = ["secon@gmail.com"]

        # 3️⃣ Ejecutamos la función solo para Elden Ring
        action = ActionAlertWhenPriceIsCheaper(mock_database, mock_mail_client)
        action.Execute("Elden Ring", 30)

        # 4️⃣ Verificamos que se envió el correo correctamente
        mock_mail_client.send_mail.assert_called_with(
            "secon@gmail.com", "El juego Elden Ring ha bajado de precio a 30€"
        )

        # 5️⃣ Aseguramos que solo se haya enviado un correo
        self.assertEqual(mock_mail_client.send_mail.call_count, 1)


if __name__ == "__main__":
    unittest.main()