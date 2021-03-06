class Coffee:
    def __init__(self, water, milk, bean, cost, cup):
        self.water = water
        self.milk = milk
        self.bean = bean
        self.cost = cost
        self.cup = cup

    def cump_num(self, min_wat, min_milk, min_bean):
        count_water = self.water // min_wat
        count_milk = self.milk // min_milk
        count_coffee = self.bean // min_bean
        cup_count = min(count_water, count_milk, count_coffee)

        if count_water==cup_count:
            return cup_count,'water'
        if count_milk==cup_count:
            return cup_count, 'milk'
        if count_coffee==cup_count:
            return  cup_count, 'bean'

    def check_machine(self, water, milk, bean):
        cup_count,res = self.cump_num(water, milk, bean)
        if cup_count >= 1:
            return True
        else:
            return False


class Action(Coffee):
    def __init__(self, water, milk, bean, cost, cup,):
        Coffee.__init__(self, water, milk, bean, cost, cup,)

    def buy(self):
        chose = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")

        if chose == '1':
            response = self.check_machine(250, 1, 16)
            if response == True:
                print("I have enough resources, making you a coffee!")
                self.water = self.water - 250
                self.bean = self.bean - 16
                self.cost = self.cost + 4
                self.cup -= 1
            else:
                respon,res=self.cump_num(250,1,16)
                print("Sorry, not enough {}!".format(res))

        if chose == '2':
            response = self.check_machine(350, 75, 20)
            if response == True:
                print("I have enough resources, making you a coffee!")
                self.water = self.water - 350
                self.milk = self.milk - 75
                self.bean = self.bean - 20
                self.cost = self.cost + 7
                self.cup -= 1
            else:
                respon , res = self.cump_num(350, 75, 20)
                print("Sorry, not enough {}!".format(res))

        if chose == '3':
            response = self.check_machine(200, 100, 12)
            if response == True:
                print("I have enough resources, making you a coffee!")
                self.water = self.water - 200
                self.milk = self.milk - 100
                self.bean = self.bean - 12
                self.cost = self.cost + 6
                self.cup -= 1
            else:
                respon, res = self.cump_num(200, 100, 12)
                print("Sorry, not enough {}!".format(res))

        if chose == 'back':
            self.action()

    def fill(self):
        self.water = self.water + int(input("Write how many ml of water do you want to add:\n"))
        self.milk = self.milk + int(input("Write how many ml of milk do you want to add:\n"))
        self.bean = self.bean + int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.cup = self.cup + int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def take(self):
        print("I gave you {}".format(self.cost))
        self.cost = 0

    def state(self):
        print("The coffee machine has:\n {0} of water\n "
              "{1} of milk\n {2} of coffee beans\n "
              "{3} of disposable cups\n {4} of money".format(self.water, self.milk, self.bean, self.cup, self.cost))

    def action(self):
        ac=input("Write action (buy, fill, take,remaining, exit):\n")
        if ac=="buy":
            self.buy()
        if ac=="fill":
            self.fill()
        if ac=="take":
            self.take()
        if ac=="remaining":
            self.state()
            return "remaining"
        if ac=="exit":
            return "exit"    
        
    
    



def main():
    loop = True
    machine = Action(400, 540, 120, 550, 9)
    while loop:
        response = machine.action()
        if response == "exit":
            break
        
            
            



if __name__ == '__main__':
    main()
