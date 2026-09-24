# ASCII Gallery Level 2 - 2026 (Exercise level 2)

Öffentliches Übungsrepository für den Kurs **Software Engineering für Data Science**.

Dieses Repository trainiert den typischen **Fork-Workflow eines Open-Source-Projekts**. Studierende haben absichtlich **keine Schreibrechte** auf dieses Repository. Beiträge kommen aus einem eigenen Fork über einen Pull Request.

## Lernziele

Nach der Übung kannst du:

- ein fremdes Repository forken,
- deinen Fork lokal klonen,
- verstehen, was `origin` und `upstream` bedeuten,
- in einem Feature-Branch arbeiten,
- einen Pull Request aus deinem Fork in das Ursprungsrepository erstellen,
- Review-Feedback in deinem Fork einarbeiten,
- deinen Fork später mit dem Upstream synchronisieren.

## Deine Aufgabe

Füge **ein eigenes ASCII-Art-Werk** zur Galerie hinzu. Die fertige Galerie findest du hier: https://zddduesseldorf.github.io/ascii-gallery-zdd-2026/

Anders als im Kursrepository `ASCII Gallery Level 1` bearbeiten wir hier **nicht gemeinsam dieselbe HTML-Datei**!
Stattdessen legt **jede Person eine eigene Datei** an. Die Webseite wird daraus automatisch gebaut.

Das ist Absicht: Gute Projektstruktur kann Merge-Konflikte stark reduzieren.

## 1. Repository forken

Klicke auf GitHub oben rechts auf **Fork** und erstelle einen Fork in deinem eigenen Account.

## 2. Deinen Fork klonen

```bash
git clone https://github.com/<DEIN-USERNAME>/ascii-gallery-zdd-2026.git
cd ascii-gallery-zdd-2026
```

Prüfe den Remote:

```bash
git remote -v
```

`origin` zeigt jetzt auf **deinen Fork**.

## 3. Upstream hinzufügen

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

Sowohl dieses Repository als auch die daraus erstellte Webseite sind aus dem Netz frei erreichbar. Für alle.
Darum bitte:

- maximal ca. 20 Zeilen,
- keine beleidigenden oder diskriminierenden Inhalte,
- keine sensiblen, personenbezogenen Daten

## 6. Webseite lokal bauen

Der Build nutzt nur die Python-Standardbibliothek:

```bash
python scripts/build_gallery.py
```

Danach liegt die fertige Seite unter:

```text
_site/index.html
```

Und das Ergebnis kann dann lokal im Browser angesehen werden.

## 7. Commit + Push zu deinem Fork

```bash
git status
git diff
git add art/<github-username>.txt
git commit -m "Add ASCII art by <github-username>"
git push -u origin ascii/<github-username>
```

## 8. Pull Request zum Upstream

Öffne auf GitHub einen Pull Request:

```text
<dein Fork>:ascii/<username>  ->  ZDDduesseldorf/ascii-gallery-zdd-2026:main
```

Nutze die PR-Vorlage und fordere ein Review an, falls dies im Praktikum so vereinbart wurde.

## 9. Review-Feedback einarbeiten

Ändere bei Bedarf deine Datei, committe und pushe erneut zu **demselben Branch**. Der offene Pull Request aktualisiert sich automatisch.

## 10. Später: Fork aktualisieren

Wenn der Upstream inzwischen neue Commits hat:

```bash
git switch main
git fetch upstream
git merge upstream/main
git push origin main
```

## Wie entsteht die Webseite?

Der GitHub-Pages-Workflow führt nach jedem Merge nach `main` Folgendes aus:

1. Repository auschecken.
2. `python scripts/build_gallery.py` ausführen.
3. Alle `art/*.txt`-Dateien HTML-sicher in Karten umwandeln.
4. Die erzeugte `_site/index.html` als GitHub Pages deployen.

Du musst für deinen Beitrag also weder HTML noch die Build-Pipeline verändern.
