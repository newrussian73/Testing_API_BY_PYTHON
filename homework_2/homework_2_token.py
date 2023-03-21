import time
import requests

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")

print(response.text)

timespend = int(response.json()["seconds"])
token = response.json()["token"]

payload = {"token":token}
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job",params=payload)
print(response2.text)

time.sleep(timespend+1)

response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job",params=payload)

print(response3.text)
