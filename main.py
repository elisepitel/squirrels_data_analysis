import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

cinnamon_squirrels = data[data['Primary Fur Color'] == 'Cinnamon']
cinnamon_squirrels_amount = len(cinnamon_squirrels)
#print(cinnamon_squirrels_amount)

gray_squirrels = data[data['Primary Fur Color'] == 'Gray']
gray_squirrels_amount = len(gray_squirrels)
#print(gray_squirrels_amount)

white_squirrels = data[data['Primary Fur Color'] == 'White']
white_squirrels_amount = len(white_squirrels)
#print(white_squirrels_amount)

black_squirrels = data[data['Primary Fur Color'] == 'Black']
black_squirrels_amount = len(black_squirrels)
#print(black_squirrels_amount)


data_dict = {
    "Fur Color": ["Cinnamon", "Gray", "White", "Black"],
    "Count": [cinnamon_squirrels_amount, gray_squirrels_amount, white_squirrels_amount, black_squirrels_amount]
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("squirrel_color.csv")
