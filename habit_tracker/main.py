import requests
from datetime import datetime


USERNAME="ada3432m"
TOKEN="jnfesbfidnvjkzngiudada1sz"
GRAPH_ID="graph1"
pixela_endpoint="https://pixe.la/v1/users"
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# responseuser=requests.post(url=pixela_endpoint,json=user_params)
# print(responseuser.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

today=datetime.now()

graph_config={
    "id":GRAPH_ID,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ichou",
}

headers={
    "X-USER-TOKEN":TOKEN,
}
# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_config={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How much did you run today?"),
}

responsePixel=requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)
print(responsePixel.text)

update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_config={
    "quantity":"55",
}

# responseUpdated=requests.put(url=update_endpoint,json=new_pixel_config,headers=headers)
# print(responseUpdated)

delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# responseDelete=requests.delete(url=delete_endpoint,headers=headers)
# print(responseDelete.text)