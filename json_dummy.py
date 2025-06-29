import json

data = {
    "name" : "Ghazi",
    "Roll No" : 123
}

#json.dumps() converts a Python object into a JSON string.
json_string = json.dumps(data, indent=2)

with open("data.json", "w") as json_file:
    json_file.write(json_string)



# print(json_string)