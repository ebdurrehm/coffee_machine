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
    
