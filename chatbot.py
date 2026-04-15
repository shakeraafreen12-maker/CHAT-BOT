import json
import random

# Load JSON data
with open("intents.json", "r") as file:
    data = json.load(file)

def get_response(user_input):
    user_input = user_input.lower()

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if pattern in user_input:
                return random.choice(intent["responses"])

    return "Sorry, I didn't understand that."

print("🤖 Chatbot is running! Type 'bye' to exit.")

while True:
    user = input("You: ")
    response = get_response(user)
    print("🤖 Chatbot:", response)

    if user.lower() in ["bye", "goodbye"]:
        break
