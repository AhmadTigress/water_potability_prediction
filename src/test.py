import json
import requests

url = "https://water-potability-api-1.onrender.com/predict"

x_new = {
  "ph": 5.24,
  "Hardness": 309.40,
  "Solids": 44903.56,
  "Chloramines": 7.99,
  "Sulfate": 183.92,
  "Conductivity": 270.23,
  "Organic_carbon": 3.72,
  "Trihalomethanes": 107.50,
  "Turbidity": 4.61
}

#x_new_json = json.dumps(x_new)

response = requests.post(url, json=x_new)

print("Response Text:", response.text)
print("Status Code:", response.status_code)