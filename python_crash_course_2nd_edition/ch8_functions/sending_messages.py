# 8-10 sending messages
def show_messages(messages: list):
    """Print messages in list"""
    for m in messages:
        print(f"{m}")

def send_messages(messages, sent_messages):
    """"""
    while messages:
        m = messages.pop()
        print(f"sending message: {m}")
        sent_messages.append(m)


messages = ['this is text one', 'this is text 2']
sent_messages = []
show_messages(messages)
send_messages(messages, sent_messages)

print(f"messages: {messages}")
print(f"sent messages: {sent_messages}")
