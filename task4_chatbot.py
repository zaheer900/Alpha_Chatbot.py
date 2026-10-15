def get_reply(message):
    message = message.lower().strip()

    if message in ("hello", "hi", "hey"):
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "what is your name":
        return "I'm a simple Python chatbot."
    elif message == "help":
        return "Try: hello, how are you, what is your name, bye"
    elif message in ("bye", "goodbye", "exit"):
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I know."


def main():
    print("=== SIMPLE CHATBOT ===")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print("Bot:", reply)

        if reply == "Goodbye!":
            break


if __name__ == "__main__":
    main()
