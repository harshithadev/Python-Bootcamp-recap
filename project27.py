# Project 27 : Calculate price 

items = {
   1 : { "item" : "Computer", "price" : 50.0, "stock" : 0}, 
  2:  { "item" : "Computer2", "price" : 500.0, "stock" : 3},
   3: { "item" : "Computer3", "price" : 520.0, "stock" : 6},
   4: { "item" : "Computer4", "price" : 570.0, "stock" : 1},
    5: { "item" : "Computer5", "price" : 150.0, "stock" : 9},
    6:{ "item" : "Computer6", "price" : 950.0, "stock" : 3},
   7: { "item" : "Computer7", "price" : 650.0, "stock" : 7},
   8: { "item" : "Computer8", "price" : 250.0, "stock" : 0},
  9:  { "item" : "Computer9", "price" : 510.0, "stock" : 4},
  10:  { "item" : "Computer10", "price" : 450.0, "stock" : 0},
    11: { "item" : "Computer11", "price" : 950.0, "stock" : 1},
   12:  { "item" : "Computer12", "price" : 150.0, "stock" : 3}
}

print("Please add options from the list : ")
for id, item in items.items() :
    print(f"{id} : {item['item']}")
print("0 : to finish adding to cart!")
input_id = -1
total = 0
while(True):
    option = int(input(" > "))
    if option == 0 :
        break
    if option not in items.keys():
        print("Invalid option!")
        continue
    if items[option]["stock"] <= 0 : 
        print(f'{items[option]["item"]} is out of stock!')
    else : 
        print(f'Adding {items[option]["item"]}!')
        items[option]["stock"] -= 1
        total += items[option]["price"]
print(f'The total price is : {total}')
    