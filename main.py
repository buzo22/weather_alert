import requests
import twilio.rest import client


OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "6b95bdcb980bf8eb6a5f256438d41e18e"
account_sid = "Acstdhsbdsy53436dh87e728e78t"
auth_token = "1262763825er87e72582yhdy8573"


weather_params = {
    "lat": 8.524367,
    "lon": 3.376546,
    "appid": api_key,
    "exclude": "current,minute,daily"
}
response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0][id]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = client(account_sid, auth_token)
    message = client.message \
        .create(
        body="It will rain today, get your umbrella and brace up",
        from="+123456789",
        to="your verified phone number"
    )
    print(message.status)