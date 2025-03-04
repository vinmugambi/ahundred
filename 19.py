# for loop
for day in range(7):
    print("Day", day)


# interest calculator
def calculateLoan(principle: float, rate: float, months: int):
    amount = principle
    percentage = 100 + rate
    for i in range(months):
        amount = amount * percentage / 100
    return amount


principle = 1000
rate = 9
months = 5

loan = calculateLoan(principle, rate, months)

print(
    "If you borrow",
    principle,
    "at a rate of",
    rate,
    "%. You will pay",
    loan,
    "in",
    months,
    "months",
)
