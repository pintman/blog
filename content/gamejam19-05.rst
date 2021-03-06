Kleine Spiele, großer Spaß
==========================
:date: 2019-05-13 14:19
:author: marco.bakera
:tags: Programmierung, Spaß, Spiele, gamejam
:status: published
:slug: gamejam19-05

.. figure:: {static}images/2019/ffhunt1.png
   :alt: Das Spiel im Einsatz

   "firefly hunt" im Einsatz.

Bei einem Game Jam werden in kurzer Zeit kleine Spiele mit 
interessanten Themen und witzigen Ideen entwickelt. Und genau
ein solcher `Game Jam <https://game-jam-do.de/>`_ fand am 11.05. in 
Dortmund im Künstlerhaus statt.

Dies war nicht der erste Game Jam: es gab bereits eine Reihe
von Veranstaltungen dieser Art, 
die alle paar Monate in Dortmund stattfinden. Diesmal habe
auch ich mit einem Kollegen wieder mit einem kleinen Projekt unter dem 
Arbeitstitel `firefly hunt 
<https://github.com/elektroschule/firefly_hunt>`_ daran teilgenommen. 

In unserem Projekt haben wir
versucht, eine LED so umzufunktionieren, dass sie statt Licht zu
emittieren, eben dieses Licht in seiner Intensität messen kann. Nach 
einer groben Ideenfindung, war die LED
flux auf ein Steckbrett gesteckt und mit einem Arduino verbunden.
Ziel des Spiels ist,
mit einem Laserpointer auf die LED zu zielen und versuchen, sie 
zu treffen. Mit wachsender Entfernung und zittrigen Fingern steigt die
Schwierigkeit dieser Aufgabe schnell an.

.. figure:: {static}images/2019/ffhunt3.png
   :alt: Nahaufnahme des Spiels

   Eine LED als Sensor umfunktioniert und von einem Arduino angesteuert.

Eine Hauptschwierigkeit war die Kalibrierung dieses Sensors gegenüber
des Umgebungslichtes. Nach verschiedenen Experimenten mit Änderungen im
Programm und dem Verbauen von Kondensatoren, war die einfachste und 
effektivste Lösung die Verwendung einer Papprolle, die das Umgebungslicht
abschirmt. So einfach kann es manchmal sein.

Als Ausgabe-Konzept haben wir uns (etwas ungewöhnlich) für LaTeX und ein
daraus erzeugtes
PDF entschieden. Über ein Template wird eine LaTeX-Datei erzeugt, die 
wiederum genutzt wird, um ein PDF zu erzeugen. Das PDF wird mit einem 
Betrachter im Vollbild angezeigt und bei Änderungen automatisch aktualisiert.

.. figure:: {static}images/2019/ffhunt2.png
   :alt: LaTeX-Ausgabe des Spieles

   Eine Ausgabe über ein LaTeX-Dokument

Das Konzept für die Ausgabe wurde in der letzten Stunde schnell mit der 
heißen Nadel gestrickt, ist es aber wert, noch einmal genauer untersucht
zu werden.


Viele Projekte
--------------

Unser Projekt war nur eines von vielen interessanten, kreativen und
ganz unterschiedlichen Projekten. Ein Textadventure wurde entwickelt, bei
dem man den Ablauf der Geschichte selbst wählen konnte.

Es wurde ein
Editor vorgestellt, mit dessen Hilfe man Musikübergänge innerhalb eines
Spieles realisieren kann. Und zwar so, dass die Musik nicht
zusammengesetzt oder gar abgehackt, sondern geschmeidig ineinander
laufend wirkt. 

Bei einem weiteren Spiel musste der Spieler aus einem
Altenheim entkommen. Der Clou dabei war, dass das Spiel und
der Controller voneinander physisch getrennt waren und über das Netzwerk
miteinander kommunizierten.

Das `15-Puzzle <https://de.wikipedia.org/wiki/15-Puzzle>`_ (ein Schiebepuzzle
mit dem Ziel, die Zahlen von 1 bis 15 in die richtige Reihenfolge zu
bringen) diente als Ideengeber für ein weiteres Spiel. 
Von oben floss Harz durch Kanäle
in einem Holzblock und die Aufgabe des Spielers war es, den Fluss des
Harzes von der Quelle zum Ziel durch das Verschieben von Teilen zu
beeinflussen.

Ein anderes Projekt zeigte, wie man aus echten Holzwürfeln, die in einem 8 mal
8 Raster eines Tapeziertisches angeordnet waren, einen Sprite gestalten konnte. 
Ein zweiter
Sprite konnte direkt daneben konstruiert werden: ebenfalls mit Würfeln.
Eine Kamera, die an einen Raspberry Pi angeschlossen war, hat beide
Bilder aufgenommen und daraus eine Mini-Animation aus zwei Bildern
erstellt - z.B. für Spiele-Engines wie
`Bitsy <https://ledoux.itch.io/bitsy>`_. Es war damit
möglich, einen Sprite mit seinen eigenen Händen physisch zu gestalten.

Ich habe bestimmt noch ein oder mehrere interessante Projekt vergessen. 
Es waren einfach zu viele.

Gute Atmosphäre und interessante Entdeckungen
---------------------------------------------

Die Atmosphäre während der Entwicklung war locker und ungezwungen.
Zwischendurch gab es Pizza (bestellt), Kaffee und Kuchen (jeweils selbstgemacht)
sowie Club-Mate. Auch internationales Publikum war diesmal anwesend, sodass
das ein oder andere Gespräch und auch die Abschlusspräsentationen in
Englisch gehalten wurden.

Eine Führung durch das `Künstlerhaus 
<https://de.wikipedia.org/wiki/K%C3%BCnstlerhaus_Dortmund>`_ hat in die 
Details der Geschichte und
Tiefen der Katakomben des Gebäudes selbst geführt und
interessante geschichtsträchtige Einblicke gewährt.

Der nächste Game Jam findet in ein paar Monaten statt und wird
hoffentlich wieder viele unterschiedliche kreative Ansätze hervorbringen
und genauso viel Spaß bringen.

.. figure:: {static}images/miniggamejamdo.png
   :alt: Gamejam-Logo

