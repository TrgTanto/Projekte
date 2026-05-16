# System Monitor (Python)

Ein moderner System Monitor mit grafischer Benutzeroberfläche, entwickelt mit Python und CustomTkinter.

Das Projekt wurde erstellt, um praktische Erfahrung mit GUI-Programmierung, Systemanalyse und Python-Anwendungsentwicklung zu sammeln.

## Vorschau

Der System Monitor bietet:

- CPU-Auslastung in Echtzeit
- RAM-Auslastung in Prozent
- Anzeige des Betriebssystems inkl. Version, Edition und Architektur
- Hostname des Systems
- Internetstatus (Online / Offline)
- Benutzername des aktuellen Users
- Systemlaufzeit (Uptime)
- Aktuelle Uhrzeit und Datum
- modernes Dark-Mode Design
- automatische Live-Updates der Systemdaten

## Funktionen

- Echtzeit-Überwachung von CPU und RAM
- Erkennung des Betriebssystems (Windows Version, Edition, 32/64-bit)
- Anzeige des Hostnames
- Prüfung der Internetverbindung über Socket (Google DNS)
- Anzeige des aktuellen Benutzers
- Berechnung der Systemlaufzeit seit Boot
- Live-Uhrzeit mit 1-Sekunden-Update
- modulare GUI-Struktur mit CustomTkinter Frames
- automatische UI-Aktualisierung über after()-Loops

## Verwendete Technologien

- Python 3
- CustomTkinter
- Tkinter
- psutil
- platform
- socket
- PIL (Pillow)
- os
- sys
- datetime
- getpass