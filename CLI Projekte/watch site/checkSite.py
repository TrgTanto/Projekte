import http.client, ssl, time

def checkSite(name: str):
    try:
        start = time.perf_counter()

        conn = http.client.HTTPSConnection(name)
        conn.request("GET", "/")
        data = conn.getresponse()

        end = time.perf_counter()
        responseTime = end - start

        if data.status == 200:
            status = "ONLINE"

        if data.status >= 300:
            print(f"{data.status} Error - Die Seite existiert, aber unter einer neuen Adresse")
            print(f'Neue URL: {data.getheader("Location")}')
            return
        
        print(f"Website: {name}")
        print(f"Status: {status}")
        print(f"Antwortzeit: {responseTime:.3f} Sekunden")
        print(f"HTTP-Code: {data.status}")

    except ssl.SSLCertVerificationError:
        print("Error - Zertifikatsvalidierung ist fehlgeschlagen.\nVergewissere dich, ob die URL korrekt war.\n")

    except (http.client.HTTPException, http.client.UnknownTransferEncoding) as e:
        print(f"Technischer Fehler: {e}")

    except http.client.NotConnected:
        print("Es konnte keine Verbindung aufgebaut werden.\nVersuche es noch einmal\n")

    except http.client.InvalidURL:
        print("Deine URL ist nicht gültig.")