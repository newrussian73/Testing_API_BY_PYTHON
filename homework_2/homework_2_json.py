import json

json_text = {"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}

json_parsed = json.dumps(json_text)
obj = json.loads(json_parsed)
objt = obj["messages"][1]
key = "message"
if key not in objt:
    print("Ошибка, нет такого значения")
else:
    print(f"В значении {key} хранится такое сообщение '{objt[key]}'")
print(obj["messages"][1]["message"])