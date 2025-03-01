pip install nltk
import nltk
from nltk.chat.util import Chat, reflections
# Download NLTK data (only required once)
nltk.download("punkt")

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! How can I help you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot. You can call me CodeBot.", "My name is CodeBot. How can I help you?"]
    ],
    [
        r"how are you?",
        ["I'm just a bot, so I don't have feelings, but thanks for asking!", "I'm doing great! How about you?"]
    ],
    [
        r"what can you do?",
        ["I can answer your questions, provide information, and assist with basic tasks.", "I'm here to help you with your queries!"]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!"]
    ],
    [
        r"quit|bye|exit",
        ["Goodbye! Have a great day!", "Bye! Feel free to come back anytime."]
    ],
    [
        r"what is NLP?",
        ["NLP stands for Natural Language Processing. It is a field of AI that focuses on the interaction between computers and humans using natural language."]
    ],
    [
        r"what is AI?",
        ["AI stands for Artificial Intelligence. It is the simulation of human intelligence in machines that are programmed to think and learn."]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem! Happy to help."]
    ],
    [
        r"default",
        ["I'm sorry, I didn't understand that. Can you please rephrase?", "I'm not sure I understand. Could you clarify?"]
    ]
]

# Create a chatbot
chatbot = Chat(pairs, reflections)

# Function to interact with the chatbot
def chat():
    print("Hello! I'm CodeBot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit"]:
            print("CodeBot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"CodeBot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chat()
