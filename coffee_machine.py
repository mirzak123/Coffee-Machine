# initial ingredients in the machine
money = 550
water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9


# prints the ingredients currently in the machine
def print_status():
    print()
    print("The coffee machine has:")
    print(f"{water} ml of water")
    print(f"{milk} ml of milk")
    print(f"{coffee_beans} g of coffee beans")
    print(f"{disposable_cups} disposable cups")
    print(f"${money} of money")
    print()
    main()


# makes a cup of coffee if there are enough ingredients
def buy():
    print()
    global water
    global money
    global milk
    global coffee_beans
    global disposable_cups

    # finalizing the sale
    def sell_a_cup(_water, _milk, _coffee_beans, _money):
        global water
        global money
        global milk
        global coffee_beans
        global disposable_cups

        water -= _water
        milk -= _milk
        coffee_beans -= _coffee_beans
        money += _money
        disposable_cups -= 1

    # returns the ingredient missing for the particular coffee
    def whats_missing(_water, _milk, _coffee_beans):
        global water
        global money
        global milk
        global coffee_beans
        global disposable_cups

        if water < _water:
            return 'water'
        elif milk < _milk:
            return 'milk'
        elif coffee_beans < _coffee_beans:
            return 'coffee beans'
        else:
            return 'disposable_cups'

    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    option = input()
    if option == '1':
        if water < 250 or coffee_beans < 16 or disposable_cups < 1:
            print(f"Sorry, not enough {whats_missing(250, 0, 16)}!")
        else:
            sell_a_cup(250, 0, 16, 4)
            print('I have enough resources, making you a coffee!')
        print()
        main()

    elif option == '2':
        if water < 350 or milk < 75 or coffee_beans < 20 or disposable_cups < 1:
            print(f"Sorry, not enough {whats_missing(350, 75, 20)}!")
        else:
            sell_a_cup(350, 75, 20, 7)
            print('I have enough resources, making you a coffee!')
        print()
        main()

    elif option == '3':
        if water < 200 or milk < 100 or coffee_beans < 12 or disposable_cups < 1:
            print(f"Sorry, not enough {whats_missing(200, 100, 12)}!")
        else:
            sell_a_cup(200, 100, 12, 6)
            print('I have enough resources, making you a coffee!')
        print()
        main()

    elif option == 'back':
        print()
        main()

    else:
        buy()


# allows you to refill the machine
def fill():
    print()
    global water
    global money
    global milk
    global coffee_beans
    global disposable_cups

    print("Write how many ml of water you want to add:")
    water += int(input())
    print("Write how many ml of milk you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans you want to add:")
    coffee_beans += int(input())
    print("Write how many disposable cups of coffee you want to add:")
    disposable_cups += int(input())
    print()
    main()


# takes out all the money inside the machine
def take():
    print()
    global money

    print(f"I gave you ${money}")
    money = 0
    print()
    main()


def main():
    print("Write action (buy, fill, take, remaining, exit):")
    option = input()
    if option == 'buy':
        buy()
    elif option == 'fill':
        fill()
    elif option == 'take':
        take()
    elif option == 'remaining':
        print_status()
    elif option == 'exit':
        quit()
    else:
        main()


if __name__ == "__main__":
    main()
