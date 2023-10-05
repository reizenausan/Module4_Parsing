import json

#example json
x = '{"Name": "Reizen", "Age": "23", "City": "Taytay"}'

#parse json
y = json.loads(x)

print("The Output of the JSON file is: ", y)
print("Name:", y["Name"])
print("Age:", y["Age"])
print("City:", y["City"])