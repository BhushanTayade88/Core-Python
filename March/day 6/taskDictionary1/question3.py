'''
3)Create a new dictionary called prices. 
Put these values in your prices dictionary:
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
Loop through each key in prices. For each key, print out the key along with its price and stock information. Print the answer in the following format(use prices and stock of above example):
apple
price: 2
stock: 0

Let's determine how much money you would make if you sold all of your food.
Create a variable called total and set it to zero.
Loop through the prices dictionaries.For each key in prices, multiply the number in prices by the number in stock. Print that value into the console and then add it to total.
Finally, outside your loop, print total.

Expected output:
orange
price: 1.5
stock: 32
pear
price: 3
stock: 15
banana
price: 4
stock: 6
apple
price: 2
stock: 0
48.0
45
24
0
The total money is 117.0
'''
prices={}

prices["banana"]=4
prices["apple"]= 2
prices["orange"]= 1.5
prices["pear"]= 3
stock={}
stock["banana"]= 6
stock["apple"]= 0
stock["orange"] =32
stock["pear"]= 15
for food in prices:
    
    print (food)
    print ("price: ", prices[food])
    print ("stock: :",stock[food])
 
total=0
for rs in prices:
    money= (prices[rs]*stock[rs])
    print (money)
    total=total +money
 
print ("The total money is", total)
