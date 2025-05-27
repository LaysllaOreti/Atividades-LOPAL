import json

with open("dados.json", "w") as f:
    json.dump({"nome":"Layslla", "idade": 19}, f)

with open("dados.json", "r") as f:
    data = json.load(f)
    print(data)

