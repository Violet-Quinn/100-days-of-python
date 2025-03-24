# with open("weather_data.csv") as file:
#     data=file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as file:
#     data=csv.reader(file)
#     temperatures=[]
#     next(data)
#     for row in data:
#         temp=int(row[1])
#         temperatures.append(temp)
#     print(temperatures)

import pandas
data=pandas.read_csv("weather_data.csv")
print(data["temp"])

