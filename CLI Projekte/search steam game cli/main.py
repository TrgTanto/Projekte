import requests, os

def getGameInfos(gameName):
    request = requests.get(f"https://store.steampowered.com/api/storesearch/?term={gameName}&l=english&cc=DE")
    data = request.json()

    checkGame = data["items"]
    if len(checkGame) == 0:
        print(f"\nDas Spiel '{gameName}' konnte nicht gefunden werden.\n")
        return
    
    else:
        name = data["items"][0]["name"]
        appID = data["items"][0]["id"]
        windows = data["items"][0]["platforms"]["windows"]
        mac = data["items"][0]["platforms"]["mac"]
        linux = data["items"][0]["platforms"]["linux"]
        gameURL = data["items"][0]["tiny_image"]

        operationSystems = []
        if windows:
            operationSystems += ["Windows"]
        if mac:
            operationSystems += ["Mac"]
        if linux:
            operationSystems += ["Linux"]
        operationSystems = ", ".join(operationSystems)

        if data["items"][0]:
            if "price" in data["items"][0]:
                price = data["items"][0]["price"]["initial"]
                priceSale = data["items"][0]["price"]["final"]

                price = round(price/100, 2)
                priceSale = round(priceSale/100, 2)

                price = str(price) + '€'
                priceSale = str(priceSale) + '€'
            else:
                price, priceSale = "Kostenlos", "Kostenlos"

        print(f"\nInformationen über - {name}")
        print(f"App ID: {appID}")
        print(f"Preis: {price}")
        if price != priceSale:
            print(f"!!! Spiel ist im Angebot für: {priceSale} !!!")
        print(f"Unterstützte Betriebssysteme: {operationSystems}")
        print(f"Spiel Icon-URL: {gameURL}\n")

if __name__ == "__main__":
    os.system("cls")
    while True:
        try:
            game = input("[X] Abbruch\nSteam Spiele-Name eingeben: ").lower().strip()
            if game == 'x':
                quit()
            getGameInfos(game)
        except KeyboardInterrupt:
            quit()