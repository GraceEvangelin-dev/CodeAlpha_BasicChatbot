# CodeAlpha Internship - Task 4
# Basic Chatbot

def chatbot():
    print("=" * 40)
    print(" BASIC CHATBOT")
    print("=" * 40)
    print("Hello! I am a simple chatbot.")
    print("You can say: hello, how are you, or bye.")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Bot: Hi!")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


chatbot()
