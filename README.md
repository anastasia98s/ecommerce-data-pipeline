# E-Commerce Data Engineering Pipeline

Ein durchgängiges Data-Engineering-Projekt, das Produktdaten über eine API abruft, transformiert und validiert, in PostgreSQL speichert und mit Power BI visualisiert.

## Projektübersicht

Dieses Projekt zeigt den Aufbau einer vollständigen ETL-Pipeline (Extract, Transform, Load) anhand eines E-Commerce-Produktdatensatzes.

## Verwendete Technologien

- **Python** – Datenextraktion, Transformation und Validierung
- **Apache Airflow** – Orchestrierung und zeitliche Planung der Pipeline
- **PostgreSQL** – relationale Datenbank zur Speicherung der Produktdaten
- **Power BI** – Dashboard und Datenvisualisierung
- **Docker** – Ausführung der Airflow-Umgebung in Containern
- **Git und GitHub** – Versionsverwaltung und Veröffentlichung des Projekts

## Aufbau der Pipeline

1. **Extract (Extraktion):** Produktdaten werden über die Fake Store API abgerufen.
2. **Transform (Transformation):** Produktbeschreibungen und Kategorien werden ins Deutsche übersetzt.
3. **Validate (Validierung):** Pflichtfelder, doppelte IDs, negative Preise und ungültige Bewertungen werden überprüft.
4. **Load (Laden):** Die Daten werden in PostgreSQL eingefügt oder vorhandene Datensätze aktualisiert.
5. **Visualisierung:** Die Produktdaten werden in Power BI ausgewertet und dargestellt.

## Datenquelle

[Fake Store API](https://fakestoreapi.com/products)

## Datenbank

Die Pipeline speichert die Produktdaten in einer PostgreSQL-Tabelle namens `products`.

## Power-BI-Dashboard

Das Dashboard enthält folgende Kennzahlen und Diagramme:

- Gesamtzahl der Produkte
- Anzahl der Produktkategorien
- Produktverteilung nach Kategorie
- Durchschnittlicher Preis je Kategorie
- Produktbewertungen

## Projektstatus

Die ETL-Pipeline wird mit Apache Airflow ausgeführt. Die geladenen Produktdaten wurden in PostgreSQL überprüft.

## Autor

Erstellt als praktisches Data-Engineering-Projekt für ein Portfolio.
