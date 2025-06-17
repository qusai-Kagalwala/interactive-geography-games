# 🐿️ Day 25 - Working with CSV Data and the Pandas Library
# Angela Yu's 100 Days of Code - Python Bootcamp
# Central Park Squirrel Census Data Analysis

# ============================================================================
# 📚 LEARNING OBJECTIVES:
# - Working with CSV files using pandas
# - Data filtering and analysis
# - Creating DataFrames from dictionaries
# - Exporting processed data to CSV
# ============================================================================

# 💡 COMMENTED OUT CODE - Previous exercises with different CSV reading methods:

# # Method 1: Reading CSV with built-in open() function
# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)

# # Method 2: Reading CSV with csv module
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)

# # Method 3: Basic pandas operations (weather data examples)
# # data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])

# # Converting DataFrame to dictionary
# # data_dict = data.to_dict()
# # print(data_dict)

# # Converting column to list and basic statistics
# # temp_list = data["temp"].to_list()
# # print(len(temp_list))
# # print(data["temp"].mean())
# # print(data["temp"].max())

# # Different ways to access columns
# # print(data["condition"])
# # print(data.condition)

# # Filtering data based on conditions
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])

# # Temperature conversion example (Celsius to Fahrenheit)
# # monday = data[data.day == "Monday"]
# # monday_temp = monday.temp[0]
# # monday_temp_F = monday_temp * 9/5 + 32
# # print(monday_temp_F)

# # Creating DataFrame from dictionary and exporting to CSV
# # data_dict = {
# #     "students": ["Amy", "James", "Angela"],
# #     "scores": [76, 56, 65]
# # }
# # data = pandas.DataFrame(data_dict)
# # data.to_csv("new_data.csv")

# ============================================================================
# 🐿️ MAIN PROJECT: Central Park Squirrel Census Analysis
# ============================================================================

# Import pandas library for data manipulation and analysis
import pandas

# 📖 Step 1: Read the squirrel census data from CSV file
# This dataset contains information about squirrels observed in Central Park in 2018
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# 🔍 Step 2: Filter and count squirrels by fur colour
# Using pandas boolean indexing to filter rows where "Primary Fur Color" matches specific colours

# Count grey squirrels
# data[data["Primary Fur Color"] == "Gray"] creates a filtered DataFrame
# len() counts the number of rows in the filtered DataFrame
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])

# Count cinnamon/red squirrels
# Note: The dataset uses "Cinnamon" to represent reddish-brown squirrels
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

# Count black squirrels
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# 📊 Step 3: Display the results
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

# 📈 Step 4: Create a summary DataFrame
# Organising our analysis results into a structured format
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],           # Categories
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]  # Corresponding counts
}

# 💾 Step 5: Convert dictionary to DataFrame and export to CSV
# Create DataFrame from our summary dictionary
df = pandas.DataFrame(data_dict)

# Export the summary to a new CSV file for future reference
# This creates a clean, organised summary of our analysis
df.to_csv("squirrel_count.csv")

# ============================================================================
# 🎯 KEY CONCEPTS LEARNED:
# - pandas.read_csv() for reading CSV files
# - Boolean indexing: data[condition] for filtering
# - len() function to count filtered rows
# - Creating DataFrames from dictionaries
# - Exporting DataFrames to CSV with to_csv()
# ============================================================================

# 📝 CHALLENGE COMPLETED: Successfully analysed Central Park squirrel data
# and created a summary CSV showing the count of squirrels by fur colour!