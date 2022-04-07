import requests
url = "https://icanhazdadjoke.com/"
respnse = requests.get(url, headers ={"Accept" :"text/plain"})
respnse2 =requests.get(url, headers ={"Accept" :"application/json"})
respnse3= requests.get(url, headers ={"Accept" :"application/json"})

data =respnse2.json()

print(respnse.text)
print(respnse2.json())
print(respnse3.text)
print(type(respnse2.json()))

print(data["joke"]) #as you see since we coverted the url into json and put it in "data" varaible 
print(data["id"])# we can use it like dictonaries and the manulipate the code


# import requests
# url = "https://www.google.co.in/"
# res = requests.get(url)
# print(f"your request to the {url} came back with the {res.status_code}"