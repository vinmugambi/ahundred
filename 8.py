name  = input("who are you? ")
goal = input("what do you want to achieve? ")
mood = input("on a scale of 1-10, how do you feel today")

# use f string to inject variables
print(f"""
Heyyyy  {name}, keep your chin up! Today you're going to
{goal} in the most amazing way, simply by being you
Here is something I never told you
YOU ROCK
""")

# or .format
print("Hello {}, \nDon't give up, You can do it.".format(name))
