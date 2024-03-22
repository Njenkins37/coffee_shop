from coffee import coffee
from coffee import coffee_machine


def change_calculations(quarters, nickels, dimes, pennies):
    quarter_dols = quarters * 0.25
    nickel_dols = nickels * 0.05
    dime_dols = dimes * 0.10
    penny_dols = pennies * 0.01
    total = quarter_dols + nickel_dols + dime_dols + penny_dols
    return total


def get_money():
    quarters = int(input('Input number of quarters:\n'))
    dimes = int(input('Input number of dimes:\n'))
    nickels = int(input('Input number of nickels:\n'))
    pennies = int(input('Input number of pennies:\n'))
    total = change_calculations(quarters, nickels, dimes, pennies)
    return total


def print_report(coffee_machine):
    for key, value in coffee_machine.items():
        print(key, value)


def resource_check(coffee_type, coffee_machine):
    water_check = coffee_machine['water']
    coffee_check = coffee_machine['coffee']
    milk_check = coffee_machine['milk']

    is_enough = True

    if coffee[coffee_type]['water'] > water_check:
        print('Sorry there is not enough water.')
        is_enough = False
    elif coffee[coffee_type]['coffee'] > coffee_check:
        print('Sorry there is not enough coffee.')
        is_enough = False
    elif coffee[coffee_type]['milk'] > milk_check:
        is_enough = False
        print('Sorry there is not enough milk.')

    return is_enough


def resource_subtract(coffee_type):
    coffee_machine['water'] = coffee_machine['water'] - coffee[coffee_type]['water']
    coffee_machine['coffee'] = coffee_machine['coffee'] - coffee[coffee_type]['coffee']
    coffee_machine['milk'] = coffee_machine['milk'] - coffee[coffee_type]['milk']
    coffee_machine['money'] = coffee_machine['money'] + coffee[coffee_type]['money']


def change_maker(money, cost):
    return_money = money - cost
    print(f"Here's ${return_money} in change.")


want = ''
while want != 'stop':
    want = input('What would you like from the coffee shop?\n')
    if want == 'espresso':
        resources = resource_check('espresso', coffee_machine)
        if resources:
            total = get_money()
            if total == coffee['espresso']['money']:
                resource_subtract('espresso')
                print('Enjoy your Espresso!')
            elif total > coffee['espresso']['money']:
                resource_subtract('espresso')
                change_maker(total, coffee['espresso']['money'])
                print('Enjoy your Espresso!')
            else:
                print(f'That is not enough for this {want}')
    elif want == 'latte':
        resources = resource_check('latte', coffee_machine)
        if resources:
            total = get_money()
            if total == coffee['latte']['money']:
                resource_subtract('latte')
                print('Enjoy your Latte!')
            elif total > coffee['latte']['money']:
                resource_subtract('latte')
                change_maker(total, coffee['latte']['money'])
                print('Enjoy your Latte!')
            else:
                print(f'That is not enough for this {want}')
    elif want == 'cappuccino':
        resources = resource_check('cappuccino', coffee_machine)
        if resources:
            total = get_money()
            if total == coffee['cappuccino']['money'] and resources:
                resource_subtract('cappuccino')
                print('Enjoy your cappuccino!')
            elif total > coffee['cappuccino']['money']:
                resource_subtract('cappuccino')
                change_maker(total, coffee['cappuccino']['money'])
                print('Enjoy your cappuccino!')
            else:
                print(f'That is not enough for this {want}')
    elif want == 'print report':
        print_report(coffee_machine)
