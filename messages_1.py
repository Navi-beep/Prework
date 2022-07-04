def send_messages(unsent_messages, sent_messages):
    """make a list of messages and then prints each message and moves it to a new list"""

    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f"sending message: {current_message}")
        sent_messages.append(current_message)

def show_sent_messages(sent_messages):
    """show messages being sent"""
    print(f"The following message has been sent: ")
    for sent_message in sent_messages:
        print(sent_message)

unsent_messages = ['How are you?', 'where is the cat?', 'What do you want for lunch?']
sent_messages = []

send_messages(unsent_messages, sent_messages)
show_sent_messages(sent_messages)

print(unsent_messages)
print(sent_messages)