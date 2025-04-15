# Multiplication table

multiplier = int(input("What number do you want to multiply by? "))
score = 0
maxScore = 10

for i in range(1, maxScore + 1):
    response = int(input(f"{i} x {multiplier} = "))
    answer = i * multiplier
    if response == answer:
        print("Great")
        score = score + 1
    else: 
        print("Nope, the answer was", answer)

print(f"You scored {score} out of {maxScore}!")