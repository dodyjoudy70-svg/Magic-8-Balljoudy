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
