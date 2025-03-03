## while true loop

tries: int = 0
while True:
    tries = tries + 1
    print("Excuse me? _ _ _ _ _ ? Nah Nah! You can tell me nothing!")
    missing = input("""What's the missing part in this rap bar? """)
    if missing == "Did you say something":
        print("Correct, you got it", tries, "tries")
        break
    elif missing == "exit":
        break
    else:
        print("Nope! Try again.")
