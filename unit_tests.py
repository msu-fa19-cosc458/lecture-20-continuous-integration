import unittest
import functions

class ChatBotResponseTest(unittest.TestCase):
    def test_not_command(self):
        # response = functions.get_chatbot_response("Purple")
        # self.assertEquals(response, "")
        response = functions.get_chatbot_response("!! add 6 4")
        print(response)
        self.assertEquals(response, 10)

if __name__ == '__main__':
    unittest.main()
