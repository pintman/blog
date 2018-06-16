piCore: Zwischen Einplatinencomputer und Microcontroller
########################################################
:date: 2018-03-31 12:24
:author: marco.bakera
:category: Hardware, Linux
:tags: RaspberryPi
:slug: picore-zwischen-einplatinencomputer-und-microcontroller
:status: published

Der RaspberryPi ist ein Einplatinencomputer, der über GPIO Pins mit
angeschlossener Elektronik kommunizieren kann. Mikrocontroller (µC)
können das auch. Dafür hat der Pi ein ausgewachsenes Betriebssystem
(meist Raspbian), ein Dateisystem, ein Netzwerk etc. Andererseits
benötigt der µC wenig Strom und man kann ihn ohne Bedenken ausschalten.
Der Pi mag das Ausschalten nicht so gerne: er möchte sauber
heruntergefahren werden. Und auch sonst muss man sich mehr um ihn
"kümmern" - Software aktuell halten, ggf. das Betriebssystem
aktualisieren.

Besonders der Punkt des Herunterfahrens störte mich bei vielen
Pi-Projekten, die irgendwann in den Dauerbetrieb gehen sollen. Wenn ich
eine LED-Wand damit ansteuere, möchte ich sie ausschalten können, ohne
mich zuvor per SSH anmelden zu müssen.

Diese Lücke zwischen ausgewachsenem OS und µC-Firmware adressiert die
Distribution
`piCore <http://tinycorelinux.net/9.x/armv6/releases/RPi/README>`__ -
ein auf `TinyCoreLinux <http://tinycorelinux.net/>`__ aufbauendes Linux,
das komplett im RAM läuft. Mittlerweile gibt es schon Version 9 und ein
aktives
`Forum <http://forum.tinycorelinux.net/index.php/board,57.0.html>`__ mit
Nutzern und Entwicklern. Das Basisimage von PiCore ist weniger als 40 MB
groß und lässt sich daher schnell installieren. Eine Testinstallation
bootete flott in weniger als zehn Sekunden. Weil alle Programme direkt
im RAM laufen und es keine langsamen Zugriffe auf die SD-Karte gibt,
verhält sich das System äußerst responsiv und flott. Da das OS von
SD-Karte bootet und diese anschließend nicht mehr benötigt, kann der Pi
ohne schlechtes Gewissen ausgeschaltet werden - alle Daten liegen ja im
RAM. Sollen Daten das Ausschalten überleben und auch beim nächsten
Bootvorgang erhalten bleiben, gibt es hierfür das Programm
``filetool.sh``, das die Userdaten auf die SD-Karte schreibt.

**Fazit:** Die Grenzen von piCore liegen klar bei Anwendungen, die viele
Daten schreiben - insbesondere, wenn diese Daten nicht mehr in der RAM
passen und auch beim nächsten Bootvorgang erhalten bleiben sollen. Wer
jedoch die umfangreiche Hardwareausstattung des Pi nutzen möchte und
keine Sorgen mit dem Blinden Trennen von der Stromversorgung haben
möchte, sollten einen Blick auf piCore werfen.
