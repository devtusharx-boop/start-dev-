items = {
    "rice": 50,
    "milk": 30,
    "oil": 120,
    "sugar": 45,
    "tea": 80
}

cart = []
total = 0

print("grocery store")

while True:
    print("\nitems")
    for name, price in items.items():
        print(name, "-", price)

    item = input("\nenter item: ").lower()

    if item == "exit":
        break

    if item in items:
        qty = int(input("enter quantity: "))
        cost = items[item] * qty
        cart.append((item, qty, cost))
        total += cost
        print("added")
    else:
        print("item not found")

print("\nbill")
for item, qty, cost in cart:
    print(item, qty, cost)

print("total =", total)
print("thank you")