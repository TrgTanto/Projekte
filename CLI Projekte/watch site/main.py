from checkSite import checkSite

def formateSite(name):
    if len(name) == 0:
        print("Du musst eine URL eingeben.")
        return

    if name[0:8] == "https://":
        name = name[8:]

    if name[0:7] == "http://":
        name = name[7:]

    if name[-1] == '/':
        name = name[:-1]

    checkSite(name)

if __name__ == "__main__":
    website = input("URL eingeben: ").strip().lower()
    formateSite(website)