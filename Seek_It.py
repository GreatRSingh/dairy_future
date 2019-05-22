import CowCalculator

end = ""
cow_increment = 0
money_increment = 0
cow_buy = 0
money_total = 0
cow_total = 0
cow_data = []
age = 0

while (end != "yes") or (end != "YES"):

    age += 1

    cow_increment = 0
    money_increment = 0
    cow_buy = 0
    money_increment = input("do any investment in {}".format(money_total))
    if money_increment == "":
        money_increment = 0
        pass

    money_increment = int(money_increment)

    money_total = money_total + money_increment

    while True:
        cow_buy = input("how many cow you want to buy you have {}".format(money_total))

        if cow_buy is "":
            cow_buy = 0
            pass

        cow_buy = int(cow_buy)

        if cow_buy * 50000 < money_total:
            break
        print("get a begging bowl for yourself")

    cow_increment = input("how many new cows are brought in")
    if cow_increment == "":
        cow_increment = 0
        pass

    cow_increment = int(cow_increment)

    b1 = cow_data
    c1 = cow_increment
    d1 = cow_buy
    e1 = money_total

    a = CowCalculator.CowCalculator(b1, c1, d1, e1).returning_method()
    b1, c1, d1, e1, f1 = a

    print(f1)

    cow_data = b1
    cow_increment = c1
    cow_buy = d1
    money_total = e1
    cow_total = f1

    print("money_total:", money_total)
    print("cow_total:", cow_total)
    for z in cow_data:
        print(z)

    end = input("DONE (YES) or (NO)")
    age = age + 1
    pass
