import json

read_file = "../data/data.json"
write_file = "../data/data_bak.json"


def load_data():
    with open(read_file, 'r') as load_f:
        return json.load(load_f)


def write_data(data_dict):
    with open(write_file, "w") as write_f:
        json.dump(data_dict, write_f)


data_dict = load_data()
print(data_dict)

