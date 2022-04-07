import requests
from random import choice
from termcolor import colored
import pyfiglet

header=pyfiglet.figlet_format("BAD JOKES")
header2=colored(header,color="blue")
print(header2)

user_input = input("What joke would you like to see...")
url ="https://icanhazdadjoke.com/search"
res = requests.get(url,
                   headers={"Accept":"application/json"},
                   params={"term":user_input }
                   ).json()

num = res["total_jokes"]
result = res["results"]
if num >1:
    print(f"Found {num} jokes of {user_input}, here is one those for you")
    print(choice(result)["joke"])
elif num ==1:
    print(f"Found a joke of {user_input}, here it is..")
    print(result [0]["joke"])
else:
    print(f"Sorry not able to find {user_input} jokes, try someother jokes")
             
