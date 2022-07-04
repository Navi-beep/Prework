def show_messages(messages):
    """make a list of messages and then print each message"""
    for message in messages:
        print(message.title())


messages = ['how are you?', 'what time is it?', 'what do you want for lunch?']
show_messages(messages)
