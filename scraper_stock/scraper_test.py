import unittest
from unittest.mock import Mock

# Importa la clase que quieres probar
from data_code import ActionAlertWhenPriceIsCheaper

class TestPriceAlert(unittest.TestCase):


    
    def test_send_email_for_cyberpunk(self):

        mock_database = Mock()
        mock_mail_client = Mock()

        mock_database.getAllSubscribers.return_value = ["pepe@gmail.com"]

        action = ActionAlertWhenPriceIsCheaper(mock_database, mock_mail_client)
        action.Execute("Cyberpunk 2077", 50)

        mock_mail_client.send_mail.assert_called_with(
            "pepe@gmail.com", "El juego Cyberpunk 2077 ha bajado de precio a 50€"
        )

        self.assertEqual(mock_mail_client.send_mail.call_count, 1)


    def test_send_email_for_elden_ring(self):

        mock_database = Mock()
        mock_mail_client = Mock()

        mock_database.getAllSubscribers.return_value = ["secon@gmail.com"]

        action = ActionAlertWhenPriceIsCheaper(mock_database, mock_mail_client)
        action.Execute("Elden Ring", 30)

        mock_mail_client.send_mail.assert_called_with(
            "secon@gmail.com", "El juego Elden Ring ha bajado de precio a 30€"
        )

        self.assertEqual(mock_mail_client.send_mail.call_count, 1)


if __name__ == "__main__":
    unittest.main()