#  File I/O and working with JSON in Python

import json
import csv

# Writing to a file
with open("D:\\New Job\\Month1\\Stage 1 — Python & Async Foundations\\data file\\example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a file I/O example.\n") 

# Reading from a file
with open("D:\\New Job\\Month1\\Stage 1 — Python & Async Foundations\\data file\\example.txt", "r") as file:
    content = file.read()
    print(content)

# Working with JSON data
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_data = json.dumps(data)
print(json_data)  # Output: {"name": "John", "age": 30, "city": "New York"}
parsed_data = json.loads(json_data)
print(parsed_data["name"])  # Output: "John"

with open("D:\\New Job\\Month1\\Stage 1 — Python & Async Foundations\\data file\\data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["John", 30, "New York"])
    writer.writerow(["Jane", 25, "San Francisco"])
    
with open("D:\\New Job\\Month1\\Stage 1 — Python & Async Foundations\\data file\\data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Output: ['Name', 'Age', 'City'], ['John', '30', 'New York'], ['Jane', '25', 'San Francisco']  

