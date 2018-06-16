Blinken-Rocket
##############
:date: 2018-01-01 21:26
:author: marco.bakera
:tags: Hardware, Programmierung
:tags: 34c3
:slug: blinken-rocket
:status: published

|image0|

Auf dem 34C3 habe ich mir einen Bausatz (12 €) einer `blinken
rocket <http://blinkenrocket.de/>`__ gekauft: eine Platine in
Raketenform mit einer 8x8-LED-Matrix und zwei Buttons. Eine Anleitung
erklärt, wie ich die Bauteile korrekt anlöten kann und ein Editor hilft
bei den ersten Schritten, eine Schrift oder einfache Animationen über
das Display laufen zu lassen. Das Programm wird über ein
Audioschnittstelle übertragen und so kann man mit seinem Handy direkt
ein kleines Programm erstellen und loslegen. Betrieben wird die
Schaltung mit einer CR2023 Knopfzelle. Die Quellen für das
Hardware-Design und auch die Firmware für den auf der Platine verbauten
ATiny88 sind bei `github
verfügbar <https://github.com/blinkenrocket>`__.

Nach meinen ersten Lötversuchen mit SMD-Bauteilen, konnte ich die Rakete
innerhalb kurzer Zeit in Betrieb nehmen. Leider lassen sich die Buttons
nicht über das Interface programmieren - sie dienen lediglich zum
Durchschalten verschiedener Programme und als Ausschalter. Da die
Firmware aber offen ist, kann sie vielleicht einfach erweitert werden,
so dass auch komplexe Programme ablaufen können. Mangels internen
Zustands ist z.B. auch kein Game of Life möglich.

**Update** Ich habe gesehen, dass die Rakete bei einem
`Shop <https://hackerspaceshop.com/products/blinkenrocket>`__ aus dem
Dunstkreis des Metalab in Wien vertrieben wird - dort allerdings für gut
investierte 25€.

.. |image0| image:: https://www.bakera.de/wp/wp-content/uploads/2018/01/Screenshot-2018-1-1-blinkenrocket.png
   :class: alignnone size-full wp-image-2153
   :width: 314px
   :height: 371px
