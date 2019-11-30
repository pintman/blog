Kleinster Anzunehmender Emulator: CHIP-8
========================================
:date: 2019-11-30 20:30
:author: marco.bakera
:tags: programmierung, hardware, game-engine, 
:status: published
:slug: chip8

.. image:: {static}images/2019/PONG_CHIP8.png
   :alt: Pong auf dem CHIP-8

In den 70er Jahren suchte man eine möglichst einfache 
Spezifikation für die Bescheibung von Videospielen. 
Herausgekommen ist der 
`CHIP-8 <https://en.wikipedia.org/wiki/CHIP-8>`_: 2 Farben, eine 
Auflösung von 64x32 Bildpunkten, 16 Register für die Speicherung
von Variablen, 4kB Speicher, eine Tastatureingabe mit 16 Tasten
und eine Audioausgabe, die genau einen Ton erzeugen kann. Programmiert
wird der CHIP-8 mit 35 Opcodes, die jeweils zwei Byte lang sind.

Ausgedacht hat sich das Joseph Weisbecker bereits in
den 70er  Jahren und den Artikel
`An Easy Programming System <https://archive.org/details/byte-magazine-1978-12/page/n109>`_
in der Zeitschrift »Byte« in der Dezember-Ausgabe von 1978
veröffentlicht - zusammen mit einer Beispiel-Implementierung
eines Spiels.

Seitdem sind einige kleinere Spiele für diese virtuelle
Maschine entstanden und das Projekt hat sich zu einer
Hallo-Welt-Fingerübung der Emulatoren-Programmierung gewandelt.
Daher gibt es für nahezu jede Plattform oder Programmiersprache
einen Emulator, der die Spiele-Roms ausführen kann.

Ich bin durch den Vortrag 
`State of Retro Gaming in Emacs <https://media.ccc.de/v/c4.openchaos.2019.11.retro-gaming-emacs>`_
darauf gestoßen. In diesem stellt *wasamasa* eine eigene 
Emulator-Implementierung vor, die er für den Emacs erstellt hat.
