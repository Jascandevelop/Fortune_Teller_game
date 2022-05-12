import random

fortunes = [
    "I see a dark and mysterious path.", 
    "only when the smoke clears will you see the true light.",
    "without a doubt you will find your way.", 
    "I cannot get a read on this right now, focus and ask again.",
    "the powers beyond me are saying no, but you should ask again.",
    "I sense a strong energy you carry, without a doubt you shall prevail.",
    "after all your hardships, your tenacity has pulled you through. It is likely.",
    "only you can answer this for yourself.",
    "it is certain.",
    "there's not a shadow of a doubt."
]

print("Hello and welcome kind soul, you have arrived to the right place...\n", 
    "...I am ~*The Great Mystic*~ here to provide you with wisdom...\n")

def fortune_teller():
    chose_fortune = random.choice(fortunes)
    print("~* ...As I call on the spirits that guide me... ", chose_fortune, "\n")
    print("...I hope this reading satisfies you...*~\n")

while fortunes:
    choose_one = input("Would you like to ask me a question?\n")
    if choose_one == "no":
        print("I bid you well my friend, til next time.\n")
        break 
    if choose_one == "yes":
        input("Ask me the truth you seek - when you have a 'yes' or 'no' question, press Enter.\n")
        fortune_teller()
    else:
        print("Try typing yes or no.")
