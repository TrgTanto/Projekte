# WatchSite – Website Status Checker (Python)

Ein kleines Python-Konsolenprogramm zum Überprüfen der Erreichbarkeit von Websites inklusive HTTP-Statuscode, Antwortzeit und Weiterleitungen.

Das Projekt wurde erstellt, um meine Python-Kenntnisse zu verbessern und praktische Erfahrung mit HTTP-Requests, Fehlerbehandlung und URL-Verarbeitung zu sammeln.

## Funktionen

- Prüfung der Erreichbarkeit von Websites
- Anzeige des HTTP-Statuscodes
- Messung der Antwortzeit der Anfrage
- Erkennung von Weiterleitungen (301, 302, 308)
- Ausgabe der neuen URL bei Redirects
- Fehlerbehandlung für:
  - ungültige URLs
  - SSL-Zertifikatsfehler
  - Verbindungsprobleme
  - HTTP-Fehler

## Funktionsweise

Das Programm sendet eine HTTPS-Anfrage an eine angegebene Domain und wertet die Serverantwort aus.

## Verwendete Technologien

- Python 3
- http.client
- ssl
- time