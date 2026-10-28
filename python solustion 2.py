def basic_chatbot():
    print("--- WELCOME TO BASIC CHATBOT ---")
    print("Chatbot: Hello! I am a simple rule-based chatbot. Type 'bye' to exit.")
    
    while True:
        # User kitta irunthu input vaanguthu
        user_input = input("You: ").strip().lower()
        
        # 1. Exit condition check panrathu
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day! 👋")
            break
            
        # 2. "hello" nu sonna reply
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi! How can I help you today?")
            
        # 3. "how are you" nu ketta reply
        elif "how are you" in user_input:
            print("Chatbot: I'm doing great, thank you! How about you?")
            
        # 4. Matha general text-ku reply
        elif "thank you" in user_input or "thanks" in user_input:
            print("Chatbot: You're welcome! Happy to help.")
            
        # 5. Puriyatha kelviku default reply
        else:
            print("Chatbot: I am a basic chatbot. I can understand 'hello', 'how are you', and 'bye'.")

# Chatbot-ah run panrathu
if __name__ == "__main__":
    basic_chatbot()
