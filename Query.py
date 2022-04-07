#writing a program to scearch the requird jokes in python from the website
import requests
url = "https://icanhazdadjoke.com/search"#from this website we are getting search results of "dog" 

response =requests.get(url, 
                    headers= {"Accept":"application/json"}, #coverts the webpage to json
                    params= {"term":"dog", "limit": 2, } # we mentions sceach word and limit of scearchs
                    )
data = response.json()
print(data["results"])#there would be lots of keyvalue pairs, we have specified to get that specific results
