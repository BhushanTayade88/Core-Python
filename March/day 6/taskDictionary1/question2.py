'''
Que 2)Follow the steps:

First, make a list called groceries with the values "banana","orange", and "apple".
Define this two dictionaries:
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
1.Define a function compute_bill that takes one argument food as input. In the function, create a variable total with an initial value of zero.For each item in the food list, add the price of that item to total. Finally, return the total. Ignore whether or not the item you're billing for is in stock.Note that your function should work for any food list.
2.Make the following changes to your compute_bill function:
While you loop through each item of food, only add the price of the item to total if the item's stock count is greater than zero.
If the item is in stock and after you add the price to the total, subtract one from the item's stock count.

output at last for food list ['banana','orange','apple']:
5.5
'''
groceries = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def compute_bill(food):
    total=0
    for rs in food:
        price= prices[rs]
        if stock[rs]>0:
           total=total +price

          
    print (total)

compute_bill(groceries)
