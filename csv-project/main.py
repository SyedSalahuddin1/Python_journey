# with open("weather_data.csv") as data:
#     data = data.readlines()
#
#     print(data)

import csv

import pandas

with open("weather_data.csv") as data_file:
    # data1 = csv.reader(data_file)
    # temperature = []
    # for row in data1:
    #     print(row)
    # print("\n")
    # data_file.seek(0)
    # for num in data1:
    #     if num[1] != "temp":
    #         temperature.append(int(num[1]))
    # print(temperature)
    # data_file.seek(0)
    # print("\n")

    import pandas
data = pandas.read_csv("weather_data.csv")
print(data["temp"])
print(type(data))
print(type(data["temp"]))
data_dict = data.to_dict()
print(data_dict)


temp_list = data["temp"].to_list()
print(temp_list)
#
avg_temp = sum(temp_list) / len(temp_list)
print(round(avg_temp))

print(data["temp"].max())
print(data["temp"].mean())

print(data["condition"])
print(data.condition)

print(data[data.day == "Friday"])
print(data[data.temp == data.temp.max()])

# Get  Data in row
monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# creating a dataframe from scratch
data_dict = {
    "students": ["Salah", "Azeem", "Zubair"],
    "scores": [76, 56, 65]
}

data1 = pandas.DataFrame(data_dict)
print(data1)
data1.to_csv("new_data_csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count_csv")
