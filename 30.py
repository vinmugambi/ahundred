name = "Jesus"

print(f"""
{name} wept
""")

print('\n\033[32m {} wept  again\n'.format(name))

print('\n\033[35m {name} wept  again and again\n'.format(name = name))


for i in range(9, 14):
    print(f'Day {i: <2} of 100') # left align the number in a space of 3 characters


for i in range(1,6):
    print('\033[0m')
    comment = input(f'How do you the think about day {i} of code? ')
    print('\033[31m')
    print(f'''You  think day {i} was 
    {comment: ^10}
    ''')
