import json

filename = 'your_json_data.json'
entry = {"carl":24}

with open(filename, "r") as file:
    data = json.load(file)
    
data.append(entry)

with open(filename,"w") as file:
    json.dump(data, file)