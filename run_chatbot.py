from chatbot.bot import chatbot_response

if __name__ == "__main__":
    while True:
        user_input = input("Ask me anything (or type 'exit' to quit): ").strip()
        if user_input.lower() in ["exit", "quit"]:
            break
        print(chatbot_response(user_input))
