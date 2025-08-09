"""
Task 3 - AI Chatbot with NLP
Internship: CODTECH
Author: Saurav Tiwari
Date: 2025-08-05

Description:
A simple AI chatbot using spaCy for NLP. 
It can answer predefined questions and can be expanded easily.
"""

import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

# Predefined question-answer pairs
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a program, but I'm doing great! How about you?",
    "what is your name": "I'm your friendly internship chatbot!",
    "bye": "Goodbye! Have a great day.",
    "weather": "I can't fetch live weather yet, but you can check sites like weather.com."
}

def chatbot_response(user_input):
    # Process input
    doc = nlp(user_input.lower())

    # Extract main keywords
    keywords = [token.lemma_ for token in doc if not token.is_stop]

    # Match keywords with known responses
    for key in responses.keys():
        if key in " ".join(keywords):
            return responses[key]
    
    return "Sorry, I don't understand that yet."

# Chat loop
print("🤖 Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("🤖 Chatbot:", responses["bye"])
        break
    print("🤖 Chatbot:", chatbot_response(user_input))
