import requests, os

def showMenu():
    print("[1] Stadt eingeben")
    print("[2] Länge- und Breitengrad eingeben")
    print("[0] Beenden")

def checkWeatherLatLon(lat, lon, apiKey):
    request = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang=de&units=metric&appid={apiKey}")

    if request.status_code == 401:
        print("\nFehler: 401 - Ungültiger API-Schlüssel\n")
        return
    
    elif request.status_code == 429:
        print("\nFehler: 429 - Dein Konto ist vorübergehend gesperrt, da Sie das Anfragelimit Ihres Abonnementtypes überschritten haben.\n")

    elif request.status_code == 200:
        data = request.json()
        country = data["sys"]["country"]
        weatherCondition = data["weather"][0]["description"]
        maxTemp = data["main"]["temp_max"]
        temp = data["main"]["temp"]
        minTemp = data["main"]["temp_min"]
        print(f"\nLand: {country}")
        print(f"Breitengrad: {lat}")
        print(f"Längengrad: {lon}")
        print(f"Wetterzustand: {weatherCondition}")
        print(f"Maximale Temperatur: {maxTemp}°C")
        print(f"Temperatur: {temp}°C")
        print(f"Mindest Temperatur: {minTemp}°C\n")
    
    else:
        print(request)

def checkWeatherCity(city, apiKey):
    request = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={apiKey}')

    if request.status_code == 401:
        print("\nFehler: 401 - Ungültiger API-Schlüssel\n")
        return
    
    elif request.status_code == 429:
        print("\nFehler: 429 - Dein Konto ist vorübergehend gesperrt, da Sie das Anfragelimit Ihres Abonnementtypes überschritten haben.\n")

    elif request.status_code == 200:
        data = request.json()
        lat = data[0]["lat"]
        lon = data[0]["lon"]
        checkWeatherLatLon(lat, lon, apiKey)
    
    else:
        print(request)

def choiceOption(n: int):
    if n == 1:
        city = input("\nStadt eingeben: ")
        apiKey = input("Gib deinen API-Schlüssel ein: ")
        checkWeatherCity(city, apiKey)
    elif n == 2:
        lat = input("Breitengrad eingeben: ")
        lon = input("Längengrad eingeben: ")
        apiKey = input("Gib deinen API-Schlüssel ein: ")
        checkWeatherLatLon(lat, lon, apiKey)
    elif n == 0:
        quit()
    else:
        print("\nÜberprüf deine Zahl\n")

if __name__ == "__main__":
    os.system("cls")
    while True:
        try:
            showMenu()
            option = int(input("> "))
            choiceOption(option)
        except ValueError:
            print("\nDu musst eine Zahl eingeben\n")
        except KeyboardInterrupt:
            quit()