.bashrc
#######
:date: 2007-02-18 08:48
:author: admin
:tags: Informatik
:slug: bashrc
:status: published

Die Option HISTCONTROL steuert in der ``.bashrc`` die
Einstellungen für die history. Mit ``export HISTCONTROL=ignoredups``
kann diese etwas kleiner halten werden,
wenn man die Duplikate (wie etwa ``ls`` oder ``cd``)
entfernt. Dies ist z.B. dann sinnvoll, wenn man mit ``Strg-S``
vorwärtssuchend oder ``Strg-R`` rückwärts suchend diese History
durchsucht und den heißgeliebten alten Aufruf nicht mehr findet, nur
weil die history mit jeder Menge Verzeichniswechseln zugekleistert
ist.

Natürlich sollte sich das Ganze auf die Performance auswirken, da im
Falle der Aktualisierung der History nicht mehr nur einfach angehängt,
sondern eben auch nachgeschaut
werden muss, ob der entsprechende Eintrag bereits vorhanden ist.
Bisher konnte ich jedoch noch keine Probleme feststellen.
