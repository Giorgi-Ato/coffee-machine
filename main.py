import functions

while True:

    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "report":
        print(functions.report())
        print(functions.CASH_BANK)
    elif order == "off":
        break
    elif order in ['espresso', 'latte', 'cappuccino']:
        if ing := functions.check_resources(order):
            print(f"Sorry there is not enough {', '.join([i for i in ing])}.")
        else:
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))

            paid = functions.coin_counter(quarters=quarters, dimes=dimes, nickles=nickles, pennies=pennies)

            if not functions.check_coins(paid, order):
                print("Sorry that's not enough money. Money refunded.")
            else:
                functions.make_coffee(order)
                change = paid - functions.MENU[order]['cost']
                functions.cash_bank(functions.MENU[order]['cost'])
                text = f"Here is your {order}. Enjoy!"

                if change == 0:
                    print(text)
                else:
                    print(f"Here is ${change} in change.")
                    print(text)
