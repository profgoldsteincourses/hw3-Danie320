# Daniel Millman
# Name Game
# Bonus assignment
# HW 3B

# get user name
name = input("What's your name: ").capitalize()

#check for blending consonants
if name[0:2] == 'Sh':
    name_end = name[2:]
elif name[0:2] == 'Th':
    name_end = name[2:]
elif name[0:2] == 'Ch':
    name_end = name[2:]
else:
    name_end = name[1:]

vowel = False
#check if name starts with a vowel
for i in "AEIOU":
    if name[0] == i:
        vowel = True

# main printing function
def main():
    if name[0] == 'B':
        print(f"{name}, {name}, bo-{name_end}\nBanana-fana fo-f{name_end}\nFee-fi-mo--m{name_end}\n{name}!")
    elif name[0] == 'F':
        print(f"{name}, {name}, bo-b{name_end}\nBanana-fana fo-{name_end}\nFee-fi-mo--m{name_end}\n{name}!")
    elif name[0] == 'M':
        print(f"{name}, {name}, bo-b{name_end}\nBanana-fana fo-f{name_end}\nFee-fi-mo--{name_end}\n{name}!")
    elif vowel == True:
        print(f"{name}, {name}, bo-b{name.lower()}\nBanana-fana fo-f{name.lower()}\nFee-fi-mo--m{name.lower()}\n{name}!")
    else:
        print(f"{name}, {name}, bo-b{name_end}\nBanana-fana fo-f{name_end}\nFee-fi-mo--m{name_end}\n{name}!")

# Call the function
main()
