import json
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    print(data)
#dumps -- will take a string and use it is JSON
#loads -- will do similar to loading
