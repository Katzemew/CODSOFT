import random
import re

class SupportBot:
    negative_res = ("no", "nope", "nah", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "see you later")

    def __init__(self):
        self.support_responses = {
            'ask_abt_product': r'.*\s*product.*',
            'tech_sup': r'.*tech.*sup.*',
            'abt_returns': r'.*\s*returnpolicy.*',
            'general_query': r'.*how.*help.*'
        }

    def greet(self):
        self.name = input("Hello! Welcome to our customer support. What's your name?\n")
        help_input = input(f"Hi {self.name}, how can I assist you today?\n")
        if help_input.lower() in self.negative_res:
            print("Alright, have a great day!")
            return
        self.chat()

    def exit(self, reply):
        for command in self.exit_commands:
            if command in reply:
                print("Thanks for reaching out. Have a great day!")
                return True
        return False

    def chat(self):
        reply = input("Please tell me your query:\n").lower()
        while not self.exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for intent, regex_pattern in self.support_responses.items():
            if re.search(regex_pattern, reply):
                if intent == 'ask_abt_product':
                    return self.ask_abt_product()
                elif intent == 'tech_sup':
                    return self.tech_sup()
                elif intent == 'abt_returns':
                    return self.abt_returns()
                elif intent == 'general_query':
                    return self.general_query()
        return self.no_match_intent()

    def ask_abt_product(self):
        responses = (
            "Our product is top-notch and has excellent reviews!\n",
            "You can find all product details on our website.\n"
        )
        return random.choice(responses)

    def tech_sup(self):
        responses = (
            "Please visit our technical support page for detailed assistance.\n",
            "You can also call our tech support helpline for immediate help.\n"
        )
        return random.choice(responses)

    def abt_returns(self):
        responses = (
            "We have a 30-day return policy.\n",
            "Please ensure the product is in its original condition when returning.\n"
        )
        return random.choice(responses)

    def general_query(self):
        responses = (
            "How can I assist you further?\n",
            "Is there anything else you'd like to know?"
        )
        return random.choice(responses)

    def no_match_intent(self):
        responses = (
            "I'm sorry, I didn't quite understand that. Can you please rephrase?\n",
            "My apologies, can you provide more details?\n"
        )
        return random.choice(responses)

# Run the bot
bot = SupportBot()
bot.greet()
