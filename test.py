import requests

city = input("Enter the name of the city\n")

# Use an f-string to correctly format the URL with the city name
url = f"https://api.weatherapi.com/v1/current.json?key=b1669ea07cf444988fe182830242005&q={city}"
r = requests.get(url)

# Print the response text
print(r.text)