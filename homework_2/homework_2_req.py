import requests


def without_params():
    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type")
    return response.text


print(without_params())


def not_include_method():
    response = requests.options("https://playground.learnqa.ru/ajax/api/compare_query_type")
    return response.text


print(not_include_method())


def right_req_with_method():
    payload = {"method": "GET"}
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
    return response.text


print(right_req_with_method())


def check_diff_method_by_get():
    methods = ["GET", "POST", "PUT", "DELETE"]
    len_methods = len(methods)
    for met in range(0,len_methods):
        payload = {"method": methods[met]}
        response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
        print(response.text)
    return


print(check_diff_method_by_get())

def check_diff_method_by_POST():
    methods = ["GET", "POST", "PUT", "DELETE"]
    len_methods = len(methods)
    for met in range(0,len_methods):
        payload = {"method": methods[met]}
        response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
        print(response.text)
    return


print(check_diff_method_by_POST())

def check_diff_method_by_PUT():
    methods = ["GET", "POST", "PUT", "DELETE"]
    len_methods = len(methods)
    for met in range(0,len_methods):
        payload = {"method": methods[met]}
        response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
        print(response.text)
    return


print(check_diff_method_by_PUT())


def check_diff_method_by_DELETE():
    methods = ["GET", "POST", "PUT", "DELETE"]
    len_methods = len(methods)
    for met in range(0,len_methods):
        payload = {"method": methods[met]}
        response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
        print(response.text)
    return


print(check_diff_method_by_DELETE())

