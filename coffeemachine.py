from main import MENU
res = {"milk": 200,
       "water": 300,
       "coffee": 100,
       }


def naming(char):
    """It names the characters as full"""
    if char == "e":
        return "espresso"

    elif char == 'l':
        return "latte"
    elif char == 'c':
        return"cappuccino"


def report(profit):
    for x in res:
        print(f"{x}: {res[x]}g")
    print(f"money: ${profit}")


def check_resources(ordered_drink):
    """Returns True if the resources are sufficient and returns False if they are insufficient"""
    for x in res:
        if res[x] < ordered_drink["ingredients"][x]:
            print(f"Sorry, there isn't enough {x}")
            return False
    return True


def total_money():
    """It returns the total money entered by the user."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def check_money(users_money, chosen_drink):
    """It checks if the money is sufficient."""
    if users_money >= chosen_drink["cost"]:
        change = round(users_money - drink['cost'], 2)
        print(f"Here's ${change} in change. ")

        return True
    print("Sorry,that's not enough money. Money refunded.")


def make_coffee(chosen_drink, name_of_drink):
    print(f"Here's your {name_of_drink}! Enjoy! ☕ ")

    for x in res:
        res[x] -= chosen_drink["ingredients"][x]


money = 0
not_off = True


while not_off:

    ch = input("What would you like? (e for espresso/l for latte/c for cappuccino):").lower()
    if ch == "report":
        report(money)

    elif ch == "off":
        print("Come soon!")
        not_off = False

    else:
        choice = naming(ch)
        drink = MENU[choice]
        if check_resources(drink):
            user_money = total_money()
            print(f"Your money : ${user_money}")
            if check_money(user_money, drink):
                make_coffee(drink, choice)
                money += drink["cost"]