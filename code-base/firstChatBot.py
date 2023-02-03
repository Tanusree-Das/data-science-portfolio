from nltk.chat.util import Chat,reflections

pairs=[
    [
        r"Hi I am (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey There!!"]
    ],
    [
        r"I am good! How are you?",
        ["Hey I am fine, thanks for asking", "Wow good to know, have a great day"]
    ],
    [
        r".*",
        ["How can I help you today?"]
    ]
]

chatbot=Chat(pairs,reflections)
chatbot.converse()