from datetime import datetime

def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hey there! I'm your quirky AI buddy!"
    elif "your name" in user_input:
        return "I'm ChatDaBot — powered by sarcasm and Python."
    elif "time" in user_input:
        return "It's currently " + datetime.now().strftime("%I:%M %p")
    elif "how are you" in user_input:
        return "I'm functioning at 100%... until someone pulls my power plug."
    elif "joke" in user_input or "fun" in user_input:
        return "Why don't robots ever panic? Because they have nerves of steel!"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Stay weird!"
    else:
        return "I'm not sure what that means, but it sounds interesting!"

