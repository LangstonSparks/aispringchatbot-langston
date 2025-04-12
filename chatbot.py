import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["hello %1, how can I help you today?",]
    ],
    [
        r"hello|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"Hello fine shyt",
        ["Hola!", "Hola como estas?",]
    ],
    [
        r"Hello studious young fella",
        ["Howdy!", "How are you doing young fella?",]
    ],
    [
        r"Greetings black youth",
        ["Blessings!", "Stay off those streets young buck",]
    ],
    [
        r"Salutations gorgeous shyt",
        ["Hello!", "Tips fedora hat with rizz",]
    ],
    [
        r"Sup brudda",
        ["Ni hao", "How is your day going?",]
    ],
    [
        r"Quit",
        ["Goodbye! have a good day!",]
    ],
    [
        r"sigma",
        ["Holy rizz",]
    ],
]

chatbot = Chat(pairs, reflections)

#Function to intereact with the chatbot
def chat():
    print("Hello, I am your chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Goodbye! Have a nice day!")
            break
        else:
            response = chatbot.respond(user_input)
            if response:
                print("Chatbot: ", response)
            else: 
                print("Chatbot: I'm not sure how to respond to that.")
chat()