from menu import MENU, resources

COIN_VALUE_DICT = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

CASH_BANK = 0


def report() -> str:
    """
    :return: string with an information about left resources
    """

    return '\n'.join([f"{key}: {value}" for key, value in resources.items()])


def check_resources(coffee: str) -> list:
    """
        This function check if there is an enough resources for ordered coffee

    :param coffee: type of coffee
    :return: if there is enough resources for coffee function return empty list, else list with ingredients
    """

    check_ingredients = [i for i in MENU[coffee]['ingredients']]
    not_sufficient_ingredients = [i for i in check_ingredients if MENU[coffee]['ingredients'][i] > resources[i]]

    return not_sufficient_ingredients


def check_coins(payed, coffee) -> bool:
    """
        This function check is paid money enough or not
    :param payed: Amount of money that is paid by user
    :param coffee: Type of coffee
    :return: if paid money is enough return True, else False
    """

    if payed < MENU[coffee]['cost']:
        return False
    return True


def coin_counter(quarters: int, dimes: int, nickles: int, pennies: int) -> float:
    """
        Function count how meny money is paid by user, according coins amount
    :param quarters: amount of quarters
    :param dimes: amount of dimes
    :param nickles: amount of nickles
    :param pennies: amount of pennies
    :return: Amount of money that is paid by user
    """

    lst = zip([quarters, dimes, nickles, pennies], COIN_VALUE_DICT.keys())
    client_paied = 0
    for pair in lst:
        client_paied += COIN_VALUE_DICT[pair[1]] * pair[0]

    return client_paied


def make_coffee(coffee):
    """
    :param coffee: ordered coffee
    :return: None
    """

    ingredients = MENU[coffee]['ingredients']
    for i in ingredients:
        resources[i] -= ingredients[i]


def cash_bank(paid_money):
    global CASH_BANK
    CASH_BANK += paid_money
