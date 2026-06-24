import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=28.6139&longitude=77.2090&current=temperature_2m,relative_humidity_2m"

try:
    response = requests.get(url)
    data = response.json()

    temperature = data["current"]["temperature_2m"]
    humidity = data["current"]["relative_humidity_2m"]

    print("===== Weather Report =====")
    print("City: Delhi")
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")

except Exception as e:
    print("Error:", e)