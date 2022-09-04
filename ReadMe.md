# Installation

---

## Inhalt
- [Installation Python](#python)
- [Installation Flask](#neues-projekt-aufsetzen)
  - [Powershell Variante](#powershell-variante)
  - [Pycharm Variante](#pycharm-variante)
- [Flask einrichten](#flask-einrichten)
- [Dependency Injection](#dependency-injection)

---

## Python
Um mit der Entwicklung von Python starten zu können, wird der Python Interpreter benötigt. Mit dem nachfolgenden Command lässt sich überprüfen, ob Python bereits auf dem Computer installiert ist.
> python

Ist noch eine 2.X Version installiert, empfiehlt es sich, auf die 3.X Version zu updaten.  
</br>
Sollte dies nicht der Fall sein, muss man die neuste Version des Interpreters von der [Downloadseite](https://www.python.org/downloads/) herunterladen.
Hier ist pip (Paketverwaltungsprogramm) bereits dabei.
</br>
Beim Ausführen des Installers darauf achten die Checkbox mit dem PATH mit anzukreuzen. Ich würde auch noch mal in der Customize Installation checken, ob pip wirklich angekreuzt ist.
</br>
Nach der Installation nochmals mit den Nachfolgenden Commands checken, ob die wichtigen Module installiert worden sind.
> python

> pip

Sollte dies der Fall sein, kann mit der Installation von Flask fortgesetzt werden.

---

## Neues Projekt aufsetzen

Hier gibt es nun 2 Möglichkeiten, ich würde die Variante mit der Installation in der Powershell verwenden. Möchte man Flask im Zusammenhang mit reactive nutzen sowieso. 
Ich habe noch keine Möglichkeit gesehen, dass hier über Pycharm mit zu installieren.

### Powershell Variante

Erst muss ein Ordner erstellt und diesem ein venv, also eine virtuelle Umgebung angelegt werden.

> mkdir myproject

> cd myproject

> py -3 -m venv venv

Durch den nachfolgenden Command wird diese virtuelle Umgebung aktiviert

> venv\Scripts\activate

Möchte man nun Flask mit reactive nutzen, kommt der Command zum Einsatz.

> pip install flask[async]

Dadurch lassen sich async und await aufrufe realisieren. Möchte man Flask ohne reactive Funktionalität nutzen, reicht der Command ohne das angehängte [async]

### Pycharm Variante

In dieser Variante reicht es aus, über File bzw. bei der Projektübersicht auf "new Project" zu klicken. 
Hier sollte eine neue virtuelle Umgebung erzeugt werden lassen. So wie es Best Practice ist für Python.
Damit wird automatisch eine venv und Flask mit erzeugt.  
Hier sollte man auch noch mal darauf achten, dass der Path zu Python richtig eingetragen ist.

---

## Flask einrichten

Damit das Projekt sauber funktioniert und auch zum Beispiel Logging aktiviert ist, muss am Interpreter noch etwas konfiguriert werden.  
Dazu oben auf den Interpreter, dieser hat meistens den Namen des Projekts.

>Interpreter > Edit Configurations

Folgende Environment variables zu setzen:

> FLASK_APP=flaskr;FLASK_DEBUG=true

Unter Umständen muss noch bei FLASK_DEBUG die Checkbox gesetzt werden.  
Bei FLASK_APP muss man vorsichtig sein. Hier muss der Name des Ordners eingetragen sein, indem die Flask Code Instanz zu finden ist,
also die __init__.py. Sollte die installation via Pycharm passiert sein, muss hier die app.py in __init__.py umbenannt werden.

---

## Dependency Injection

### Installation

Um den Dependency Injector hinzuzufügen, muss er in der requirements.txt hinzugefügt werden. Dieses lässt sich als package.json verstehen.  
Hierzu fügen wir dort die beiden Zeilen:

> Flask==2.2.2

> dependency-injector==4.40.0

ein. Je nachdem mit welcher Version.  
In der Powershell müssen wir diese nun mit folgendem Command installieren:

> pip install -r requirements.txt

Nun sollte der Dependency-Injector installiert sein.

### Verwendung

Dazu erstellen wir ein container.py Datei.  
Hier erstellen wir eine Klasse mit dem Namen Container, welcher **containers.DeclarativeContainer** vererbt bekommt.
</br>
Hier instanziieren wir 2 Variablen:

>wiring_config = containers.WiringConfiguration(packages=["rest"])
> 
>config = providers.Configuration()

Wobei wir bei Packages den Namen der Packages angeben, in denen die Dependency Injection verwendet wird.

> WICHTIG: IN DIESEM PACKAGE MUSS ES EINE __init__.py GEBEN!

Im nächsten Schritt werden Variablen der Klassen angelegt, welche bei der Dependency Injection verwendet werden.

> kunde_read_service = providers.Factory(
>
>KundeReadService,
>
>)

Innerhalb der Argumente für Factory werden die Parameter der jeweiligen Klasse benötigt,
da wird immer nur 'self' haben, brauchen wir hier nur ein Verweis auf die KundeReadService Klasse selbst.  
</br>
Im nächsten Schritt verwenden wir die Dependency Injection.  
Dazu müssen wir die Funktion, welche zum Beispiel den ReadService nutzt, mit 

> @inject

annotieren.
In der Parameterliste instanziieren wir nun die Variable mit dem Verweis auf die Variable im Container

> read_service: KundeReadService = Provide[Container.kunde_read_service]

Nun lässt sich die Dependency Injection verwenden.