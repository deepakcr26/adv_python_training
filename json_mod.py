import json
Family = {
    "firstName": "Shah Rukh",
    "lastName": "Khan",
    "hobbies": ["Acting", "Hockey", "Football"],
    "age": 50,
    "children": [
        {
            "firstName": "Suhana",
            "age": 12
        },
        {
            "firstName": "Aryan",
            "age": 8
        },

        {
            "firstName": "AbRam",
            "age": 2
        }
    ]
}

with open("data_file.json", "w") as write_file:
    json.dump(Family, write_file)

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
print("data: ", data)
