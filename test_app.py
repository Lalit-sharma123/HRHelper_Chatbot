import unittest
from app import app

class ChatbotTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_known_question(self):
        res = self.client.post('/chat', json={'message': 'What is the leave policy?'})
        self.assertIn('paid leave', res.get_json()['answer'])

    def test_unknown_question(self):
        res = self.client.post('/chat', json={'message': 'What is the moon color?'})
        self.assertIn("don't know", res.get_json()['answer'])

if __name__ == '__main__':
    unittest.main()