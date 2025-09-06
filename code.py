def get-user-guess():
    while True:
        try:
            guess=int(input("enter ur guess(1-100)"))
            if 1<=guess<=100:
                return guess
            else:
                print("please enter number between them")
            except ValuEurror:
                print("invalid error")
list=[]
import random
respones=[
    "yes",
    "no",
    "ask again",
    "certain",
    "doubtful",
    "outloke is good",
    "better not to tell",
    "c aand ask agauin",
]
def get_random_response():
    return random.choice(respones)