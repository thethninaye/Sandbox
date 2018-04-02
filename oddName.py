'''Thet Hnin Aye'''

def main():

name = (input("Enter your name here "))

#This is a comment


while len(name) <= 1:
    print("Error")
    name = (input("Enter your name here "))

print(name[::2])

main()