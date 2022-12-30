import requests

API_KEY = "35d680a6c62b8846fdd3fccc567a1b73"

def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    # 40 Values over 5 days, 8 values per day (3hr intervals)
    filtered_data = data["list"]
    # Filter by forecast days
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    # Filter by kind of data required
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Temperature"))