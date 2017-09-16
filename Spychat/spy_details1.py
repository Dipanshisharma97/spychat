from datetime import datetime

# Spy class
class Spy:
    def __init__(self, name, salutation, age, rating):
        # initializing the values
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

        # counting the number of words
        self.count = 0

# a class for chat messages
class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

# details of default user.
spy = Spy('dipanshi', 'Ms.', 20, 8.8)

# details of some existing friends
one1 = Spy('akshita ', 'Ms.', 19, 7.8)
two2 = Spy('priya, ', 'Ms.', 21, 8.2)
three3 = Spy('khushi, ', 'Ms.',22, 8.1)

# lists of existing friends
friends = [one1, two2, three3]