USB-Sticks und SD-Karten validieren
###################################
:date: 2018-01-05 10:45
:author: marco.bakera
:tags: Hardware, Linux, Tipp, Tools
:slug: usb-sticks-und-sd-karten-validieren
:status: published

|image0|

Nicht immer funktionieren USB-Sticks und SD-Karten so wie sie sollen.
Bei meiner letzten Bestellung aus China hatte ich den Verdacht, dass
einige SD-Karten defekt waren - sie funktionierten für einen kurzen
Zeitraum und gaben dann den Geist auf. Aus der c't kannte ich das
Programm `H2testw <http://www.heise.de/download/h2testw.html>`__, mit
dem Flashspeicher geprüft werden kann. Dazu wird das Speichermedium mit
Testdaten vollständig beschrieben und die Daten anschließend wieder
gelesen. Wenn alles korrekt läuft, stimmen die gelesenen Daten mit den
ursprünglich geschriebenen Daten überein. Das kann je nach Größe des
Speichermediums durchaus eine Weile dauern.

Für Linux gibt es hierfür das Paket f3, das mit den Programmen f3write
und f3read das gleiche tut. Für einen korrekten USB-Stick läuft das
Programm wie folgt ab:

::

    $ f3write /media/STICK/
    Free space: 196.84 MB
    Creating file 1.h2w ... OK! 
    Free space: 0.00 Byte
    Average writing speed: 6.76 MB/s

Anschließend werden die geschriebenen Daten wieder gelesen.

::

    $ f3read /media/STICK/
                      SECTORS     ok/corrupted/changed/overwritten
    Validating file 1.h2w ... 403128/        0/      0/      0

      Data OK: 196.84 MB (403128 sectors)
    Data LOST: 0.00 Byte (0 sectors)
              Corrupted: 0.00 Byte (0 sectors)
       Slightly changed: 0.00 Byte (0 sectors)
            Overwritten: 0.00 Byte (0 sectors)
    Average reading speed: 7.75 MB/s

 

.. |image0| image:: {filename}images/2018/01/webmichl-sd-card-800px.png
   :class: alignnone size-full wp-image-2191
   :width: 800px
   :height: 510px
   :target: {filename}images/2018/01/webmichl-sd-card-800px.png
