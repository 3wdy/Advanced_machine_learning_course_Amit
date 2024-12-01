import random
import os

class Chatbot:
    _responses = {
        "hello": ["Hello!", "Hi there!", "Greetings!"],
        "how are you": ["I'm doing well, thank you!", "I'm fine, how about you?"],
        "goodbye": ["Goodbye!", "See you later!", "Farewell!"],
        "exit": ["Goodbye! It was nice chatting with you.", "See you next time!"],
        "default": ["I'm sorry, I didn't understand.", "Could you please rephrase that?"]
    }

    def _get_response(self, user_input):
        user_input = user_input.lower().strip()  
        
        for key in self._responses:
            if key in user_input:
                return random.choice(self._responses[key])
        return random.choice(self._responses["default"])

    def chatbot_generate(self):
        print("Chatbot: Hi! How can I assist you today?")
        
        while True:
            try:
                user_input = input("User: ").strip()  
                
                if not user_input:  
                    print("Chatbot: Please say something.")
                    continue

                if user_input.lower() in ["goodbye", "exit", "bye"]:  
                    print("Chatbot: " + random.choice(self._responses["exit"]))
                    break 

                response = self._get_response(user_input)
                print("Chatbot:", response)

            except Exception as e:  
                print(f"Error: {e}. Something went wrong, please try again.")
                continue


if __name__ == "__main__":
    chatbot_instance = Chatbot()
    chatbot_instance.chatbot_generate()
