def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm fine, thanks for asking!"

    elif "your name" in user_input:
        return "I'm a simple Python chatbot."

    elif "bye" in user_input:
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I didn't understand that."

def chatbot():
    print("🤖 Simple Python Chatbot")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ")

        response = get_response(user)
        print("Bot:", response)

        if "bye" in user.lower():
            break

    print("Chatbot ended.")

# Run the chatbot
chatbot()
