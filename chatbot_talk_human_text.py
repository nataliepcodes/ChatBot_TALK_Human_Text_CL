from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from mysay import print_say

# Create a new instance of a chat bot
bot = ChatBot('Cleo', storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3')

trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
    "chatterbot.corpus.english"
)

# Define entrance text
print("\n===============================================")
print_say(f"\nHi, my name is 🤖{bot.name}. How can I help you?\n")

# Define exit conditions
exit_conditions = ("bye", "goodbye", "stop", "quit")

# Define conversation structure
while True:
    try:
        query = input("Human: ")
        if query in exit_conditions:
            print(f"🤖{bot.name}: ", end='')
            print_say("Goodbye! Have a nice day!")
            print("\n===============================================\n")
            break
        else:
            print(f"🤖{bot.name}: ", end='')
            print_say(f"{bot.get_response(query)}")
    except (SystemError, EOFError, KeyboardInterrupt):
        break

# NOTES FOR READ.me FILE

""" ONLY TEXT CHAT """
# pip install chatterbot 
# If the above command doesnt work, try installing the actual version or a version below (according to stackoverflow)
# e.g pip install chatterbot==1.0.4


""" TEXT TO VOICE CHAT """
# Python has two text to speech modules: pyttsx3 for Windows and gTTS for Mac and Linux
# Windows: conda activate chatting, then: pip install pyttsx3
# Mac and Linux: conda activate chatting
# Mac installing mpg123 player: brew install mpg123
# Linux installing mpg123 player: sudo apt-get update, then: sudo apt-get update install mpg123
# Mac and Linux test in the Terminal: gtts-cli --nocheck "hello, how are you?" | mpg123 -q -