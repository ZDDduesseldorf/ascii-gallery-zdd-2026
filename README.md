# ASCII Gallery ZDD 2026

Oeffentliches Uebungsrepository fuer den Kurs **Software Engineering fuer Data Science**.

Dieses Repository trainiert den typischen **Fork-Workflow eines Open-Source-Projekts**. Studierende haben absichtlich **keine Schreibrechte** auf dieses Repository. Beitraege kommen aus einem eigenen Fork ueber einen Pull Request.

## Lernziele

Nach der Uebung kannst du:

- ein fremdes Repository forken,
- deinen Fork lokal klonen,
- verstehen, was `origin` und `upstream` bedeuten,
- in einem Feature-Branch arbeiten,
- einen Pull Request aus deinem Fork in das Ursprungsrepository erstellen,
- Review-Feedback in deinem Fork einarbeiten,
- deinen Fork spaeter mit dem Upstream synchronisieren.

## Deine Aufgabe

Fuege **ein eigenes ASCII-Art-Werk** zur Galerie hinzu.

Anders als im internen Kursrepository bearbeiten wir hier **nicht gemeinsam dieselbe HTML-Datei**. Jede Person legt eine eigene Datei an. Die Webseite wird daraus automatisch gebaut.

Das ist Absicht: Gute Projektstruktur kann Merge-Konflikte stark reduzieren.

## 1. Repository forken

Klicke auf GitHub oben rechts auf **Fork** und erstelle einen Fork in deinem eigenen Account.

## 2. Deinen Fork klonen

```bash
git clone https://github.com/<DEIN-USERNAME>/ascii-gallery-zdd-2026.git
cd ascii-gallery-zdd-2026
```

Pruefe den Remote:

```bash
git remote -v
```

`origin` zeigt jetzt auf **deinen Fork**.

## 3. Upstream hinzufuegen

```bash
git remote add upstream https://github.com/ZDDduesseldorf/ascii-gallery-zdd-2026.git
git remote -v
```

Damit gilt:

- `origin` = dein Fork
- `upstream` = das originale Kursrepository

## 4. Feature-Branch erstellen

```bash
git switch -c ascii/<github-username>
```

## 5. Eigene ASCII-Datei anlegen

Lege genau eine Datei an:

```text
art/<github-username>.txt
```

Beispiel:

```text
art/octocat.txt
```

In der Datei steht **nur die ASCII-Art**, kein HTML.

Beispiel:

```text
 /\_/\\
( o.o )
 > ^ <
```

Bitte:

- maximal ca. 20 Zeilen,
- keine beleidigenden oder diskriminierenden Inhalte,
- keine personenbezogenen Daten,
- keine kopierten urheberrechtlich geschuetzten Grafiken.

## 6. Webseite lokal bauen

Der Build nutzt nur die Python-Standardbibliothek:

```bash
python scripts/build_gallery.py
```

Danach liegt die fertige Seite unter:

```text
_site/index.html
```

Lokal ansehen:

```bash
python -m http.server 8000 --directory _site
```

Dann `http://localhost:8000` oeffnen.

## 7. Commit + Push zu deinem Fork

```bash
git status
git diff
git add art/<github-username>.txt
git commit -m "Add ASCII art by <github-username>"
git push -u origin ascii/<github-username>
```

## 8. Pull Request zum Upstream

Oeffne auf GitHub einen Pull Request:

```text
<dein Fork>:ascii/<username>  ->  ZDDduesseldorf/ascii-gallery-zdd-2026:main
```

Nutze die PR-Vorlage und fordere ein Review an, falls dies im Praktikum so vereinbart wurde.

## 9. Review-Feedback einarbeiten

Aendere bei Bedarf deine Datei, committe und pushe erneut zu **demselben Branch**. Der offene Pull Request aktualisiert sich automatisch.

## 10. Spaeter: Fork aktualisieren

Wenn der Upstream inzwischen neue Commits hat:

```bash
git switch main
git fetch upstream
git merge upstream/main
git push origin main
```

## Wie entsteht die Webseite?

Der GitHub-Pages-Workflow fuehrt nach jedem Merge nach `main` folgendes aus:

1. Repository auschecken.
2. `python scripts/build_gallery.py` ausfuehren.
3. Alle `art/*.txt`-Dateien HTML-sicher in Karten umwandeln.
4. Die erzeugte `_site/index.html` als GitHub Pages deployen.

Du musst fuer deinen Beitrag also weder HTML noch die Build-Pipeline veraendern.
