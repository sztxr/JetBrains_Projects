class CoffeeMachine:
    money = 550
    water = 400
    milk = 540
    beans = 120
    cups = 9

    def __init__(self):
        while True:
            action = input('Write action (buy, fill, take, remaining, exit):')
            if action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                self.print_state()
            elif action == 'exit':
                break

    def print_state(self):
        print('The coffee machine has:')
        print(f'{self.water} ml of water')
        print(f'{self.milk} ml of milk')
        print(f'{self.beans} g of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')

    def check_resources(self, water_needed, milk_needed, beans_needed):
        if self.water < water_needed:
            print('Sorry, not enough water!')
        elif self.milk < milk_needed:
            print('Sorry, not enough milk!')
        elif self.beans < beans_needed:
            print('Sorry, not enough beans!')
        elif self.cups < 1:
            print('Sorry, not enough cups!')
        else:
            print('I have enough resources, making you a coffee!')
            return True

    def buy(self):
        selected = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:, back - to main menu:')
        if selected == '1':  # espresso
            if self.check_resources(250, 0, 16):
                self.money += 4
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
        elif selected == '2':  # latte
            if self.check_resources(350, 75, 20):
                self.money += 7
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
        elif selected == '3':  # cappuccino
            if self.check_resources(200, 100, 12):
                self.money += 6
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add:'))
        self.milk += int(input('Write how many ml of milk do you want to add:'))
        self.beans += int(input('Write how many grams of beans do you want to add:'))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add:'))

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0


CoffeeMachine()

# def count(water_, milk_, beans_, cups_):
#     possible = min(water_ // 200, milk_ // 50, beans_ // 15)
#
#     if possible == cups_:
#         print('Yes, I can make that amount of coffee')
#     elif possible > cups_:
#         print(f'Yes, I can make that amount of coffee (and even {possible - cups_} more than that)')
#     else:
#         print(f'No, I can make only {possible} cups of coffee')
#
#
# water = int(input('Write how many ml of water the coffee machine has:'))
# milk = int(input('Write how many ml of milk the coffee machine has:'))
# beans = int(input('Write how many ml of coffee beans the coffee machine has:'))
# cups = int(input('Write how many cups of coffee you will need:'))
# count(water, milk, beans, cups)
