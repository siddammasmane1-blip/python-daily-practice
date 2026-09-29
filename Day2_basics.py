while True:
    name = input("Enter the name of the customer:")
    total = 0
    discount = 0

    while True:
        print("Enter the amount and Quantity")
        amount = float(input("enter the amount:"))
        quantity = float(input("Enter the Quantity of the item:"))
        discount = float(input("Enter the discount percentage:"))
        total += amount*quantity
        discount = total * discount / 100
        total -= discount

        repeat = input("Do you want to repeat the item(yes/no):")
        if repeat == "no" or "No":
            break
    print("---------------------------")
    print("Name:",name)
    print("Discount applied:", discount)
    print("total amount paid:",total)
    print("-----------------------------")
    repeat = input("do you want to continue(yes/no):")
    if repeat == "no" or repeat == "No":
        break    