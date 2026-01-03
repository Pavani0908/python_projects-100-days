# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)
from typing import Any

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# import pandas
# from gradio.themes.utils.colors import gray
#
# data = pandas.read_csv("weather_data.csv")
# print(data)

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #get data in columns


# print(data["condition"])
# print(data.condition)

#get data in row on data frame

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp *9/5 +32
# print(monday_temp_f)

# create a data frame from scratch
# data_dic = {
# #     "student":["Amy", "james", "Angela"],
# #     "Score": [76,56,65]
# #
# # }
# # data = pandas.DataFrame(data_dic)
# # data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251206.csv")

gray_Squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
white_Squirrel_count = len(data[data["Primary Fur Color"] == "White"])
cinnamon_Squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

print(gray_Squirrel_count)
print(white_Squirrel_count)
print(cinnamon_Squirrel_count)

data_dict = {
    "fur colors": ("gray","cinnamon","white"),
     "count": [gray_Squirrel_count, white_Squirrel_count,cinnamon_Squirrel_count]
}
df = pandas.DataFrame[data_dict]
df.to_csv("Squirrel_count.csv")


