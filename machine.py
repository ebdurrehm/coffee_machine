def cump_num(water,milk,coffe):
    count_water=water//200
    count_milk=milk//50
    count_coffee=coffe//15
    cup_count=min(count_water,count_milk,count_coffee)
    return cup_count
    
water=int(input("Write how many ml of water the coffee machine has:\n"))
milk=int(input("Write how many ml of milk the coffee machine has:\n"))
coffe=int(input("Write how many grams of coffee beans the coffee machine has:\n"))
cup=int(input("Write how many cups of coffee you will need:\n"))
cup_count=cump_num(water,milk,coffe)
if cup_count==cup:
    print("Yes, I can make that amount of coffee")
if cup_count>cup:
    
    cup_countn=cup_count-cup
    print("Yes, I can make that amount of coffee (and even {} more than that)".format(cup_countn))
   
else:
        print("No, I can make only {} cup(s) of coffee".format(cup_count))
    
   

class Coffee:
    def __init__(self,water,milk,bean,cost,cup):
        self.water=water
        self.milk=milk
        self.bean=bean
        self.cost=cost
        self.cup=cup
        
class Action(Coffee):
    def __init__(self,water,milk,bean,cost,cup):
        Coffee.__init__(self,water,milk,bean,cost,cup)
    def buy(self):
        chose=input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")

        if chose=='1':
            self.water=self.water-250
            self.bean=self.bean-16
            self.cost=self.cost+4
            self.cup-=1
        if chose=='2':
            self.water=self.water-350
            self.milk=self.milk-75
            self.bean=self.bean-20
            self.cost=self.cost+7
            self.cup -= 1
        if chose=='3':
            self.water=self.water-200
            self.milk=self.milk-100
            self.bean=self.bean-12
            self.cost=self.cost+6
            self.cup -= 1

    def fill(self):
        self.water=self.water+int(input("Write how many ml of water do you want to add:\n"))
        self.milk=self.milk+int(input("Write how many ml of milk do you want to add:\n"))
        self.bean=self.bean+int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.cup=self.cup+int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def  take(self):
        print("I gave you {}".format(self.cost))
        self.cost=0

    def state(self):
        print("The coffee machine has:\n {0} of water\n "
              "{1} of milk\n {2} of coffee beans\n "
              "{3} of disposable cups\n {4} of money".format(self.water,self.milk,self.bean,self.cup,self.cost))


def action(machine):
    action = input("Write action (buy, fill, take):\n")
    if action == 'buy':
        machine.buy()
    if action == 'fill':
        machine.fill()
    if action == 'take':
        machine.take()

def main():
    machine=Action(400 , 540, 120 , 550 , 9)
    print(machine.state())
    action(machine)
    print(machine.state())





if __name__ == '__main__':
    main()

