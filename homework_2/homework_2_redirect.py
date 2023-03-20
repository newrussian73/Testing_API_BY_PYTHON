import requests


response = requests.get("https://playground.learnqa.ru/api/long_redirect",allow_redirects=True)
first_url = response.history[0].url
second_url = response.history[1].url
third_url = response.url
print(first_url)
print(second_url)
print(f"конечный урл {third_url}")
