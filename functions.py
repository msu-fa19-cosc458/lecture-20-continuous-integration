def get_chatbot_response(message):
    if message[:2] != "!!":
        return ''

    points, command, args = message.split(' ', 2)
    if command == "hey":
        return "What's Up!"
    elif command == "add":
        num1, num2 = args.split()
        return int(num1) + int(num2)
    elif command == "divide":
        num1, num2 = args.split()
        return num1 / num2
    elif command == "say":
        return args
    else:
        return "Oops! I didn't recognize your command :("

