Ein eigener PyPI-Server
#######################
:date: 2017-11-20 20:23
:author: marco.bakera
:category: Informatik, Programmierung, Python
:slug: ein-eigener-pypi-server
:status: published

Der Python Package Index - kurz PyPI - ist die zentrale Anlaufstelle für
die Installation von Pythonpaketen. Wenn das Internet mal streikt, der
Dienst nicht verfügbar oder nur schlecht erreichbar ist, lohnt sich der
Blick auf das Paket
`pypiserver <https://pypi.python.org/pypi/pypiserver>`__. Der Server
wird mit ``pip install pypiserver`` installiert und kann anschließend
mit ``pypi-server`` gestartet werden

Die Pakete erwartet es im Verzeichnis ``~/packages`` oder in einem
Ordner, der als Parameter im Aufruf übergeben wird. Damit pip im
Anschluss den neuen Server bei seiner Arbeit respektiert, muss er als
Parameter übergeben werden:
``pip install --extra-index-url http://mein-server/ bottle`` oder bei
einer Suche ``pip search --index http://mein-server bottle``. Die
Anleitung beschreibt zwei Möglichkeiten, die URL nicht immer übergeben
zu müssen: via Konfiguration in einer Umgebungsvariable oder über eine
Konfigurationsdatei.

Einmal installierte Pakete können mit ``pypi-server -U`` auf ihre
Aktualität hin überprüft und ggf. mit einer neuen Version aus der
offiziellen PyPI-Quelle aktualisiert werden.
