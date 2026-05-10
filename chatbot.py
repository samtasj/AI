print("===== Customer Support Chatbot =====")

while True:

    user = input("\nYou: ").lower()

    if user == "hi" or user == "hello":
        print("Bot: Hello! How can I help you?")

    elif user == "who are you":
        print("Bot: I am a virtual customer assistant.")

    elif user == "where do you operate":
        print("Bot: We operate from Singapore.")

    elif user == "payment methods":
        print("Bot: We accept debit cards and major credit cards.")

    elif user == "customer service":
        print("Bot: Please call +65 3333 3333")
        print("Bot: Available Monday to Friday, 9 AM to 5 PM")

    elif user == "timing":
        print("Bot: Our working hours are 9 AM to 5 PM.")

    elif user == "bye" or user == "ok":
        print("Bot: Thank you! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I did not understand your question.")
