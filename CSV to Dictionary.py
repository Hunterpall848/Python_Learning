import csv

with open('CSV File', newline='') as food_cost:
    food = csv.DictReader(food_cost)
    for row in food:
        print(row)

#dictionary to csv
AG_food = {
    'Food': ['AG Burger' , 'Fish and Chips' , 'Pizza'],
    'Price':[ 15, 16, 12 ],
    'Location': ['Middle', 'Fryer' , 'Saute']
}

with open('CSV File2', 'w', newline='') as dict2csv:
    w = csv.DictWriter(dict2csv, fieldnames = AG_food.keys())
    w.writeheader()
    for row in zip(*AG_food.values()):
        w.writerow(dict(zip(AG_food, row)))


#Git test
#Git test 2





