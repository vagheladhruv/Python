'''
5.	Create two dictionaries – one containing grocery items and their prices and 
another containing grocery items and quantity purchased. 
By using the values from these two dictionaries compute the total bill.
'''
prices = {
    "apple": 2.5,
    "banana": 1.2,
    "orange": 3.0,
    "milk": 1.5,
    "bread": 2.0
}


quantities = {
    "apple": 4,
    "banana": 6,
    "orange": 3,
    "milk": 2,
    "bread": 1
}
def billtotal(prices, quantities):
    total = 0
    for item in quantities:
        if item in prices:
            total += prices[item] * quantities[item]
    return total

total_bill = billtotal(prices, quantities)

print(f"The total bill is: ${total_bill:.2f}")
