# KCSE grade calculator
minPoints = 7
maxpoints = 84

print("KCSE grade calculator")
points = int(input("kCSE points: "))

if points < minPoints or points > maxpoints:
    print("\033[31m", "Liar! Points must be between 7 and 84 (inclusive)")
else:
    grade = (
        "A"
        if points > 80
        else "A-" if points > 73 else "B+" if points > 66 else "Disqualified"
    )

    print("With", points, "points,", "your grade is", grade)
