import requests

api_key="85c24789bafc52c9a392539561e4ab1c"



response=requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast?lat=17.385044&lon=78.486671&cnt=4&appid={api_key}")
response.raise_for_status()
data=response.json()
# print(data["list"][0]["weather"][0]["id"])
for hour_data in data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if condition_code<700:
        print("Bring an umbrella.")
    else:
        print("No need for umbrella")
