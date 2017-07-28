class Animal:

    def __init__ (self, name):
        self.name = name
        self.spots = 0
        self.hungry = True

    def num_spots(self, spots):
        self.spots = spots

    def eat_food(self):
        print("To feed " +self.name+ " type 'feed' in the bar")
        input_var= input()
        if input_var ==  "feed":
            self.hungry = False
            print("Good job! You fed " +self.name + "!")


    # Define the fields and methods for your object here.
#class Network:
    # Define the fields and methods for your object here.

def main():
    # Define the program flow for your user interface here.
    print("Welcome to The Animal House! Charlie is an 8 year old panda and Allie Goss is a baby unicorn. Help take care of them!")
    panda = Animal("Charlie")
    if panda.hungry:
        print(panda.name +" is hungry!")
    panda.eat_food()
    if panda.hungry:
        print("Is" +panda.name+"still hungry?")
    unicorn = Animal("Allie Goss")
    if unicorn.hungry:
        print(unicorn.name + " is hungry")
        unicorn.eat_food()



# Runs your program.
if __name__ == '__main__':
    main()
