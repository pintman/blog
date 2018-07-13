Wetter-Monitor mit einem Kindle
===============================
:date: 2018-07-03 12:20
:author: marco.bakera
:tags: Hacking, Hardware
:slug: kindle_wetter_monitor
:status: draft

.. image:: {filename}images/2018/07/kindle_weather_display.jpg
   :alt: Kindle mit Wetteranzeige
   :width: 100%


E-Book-Reader haben meist ein E-Ink-Display, ein schönes Gehäuse und ältere
Modelle bekommt man für wenig Geld.
Genau diese Kombination machen sie so reizvoll, um
daraus ein Türschild zu bauen oder, um sie als Wetteranzeige zu verwenden. Die
Displays stellen die Informationen sehr scharf dar und verbrauchen nur wenig
Strom.

Setup des Kindle
----------------

In einem kleinen Projekt wollte ich mich eines 
`Kindle-Keyboard <https://de.wikipedia.org/wiki/Amazon_Kindle#Kindle_Keyboard_(3._Generation)>`_ 
annehmen, um das Gerät für eigene Anzeigewecke zu ge- bzw. misbrauchen. 
Diese Geräte bekommt man für ca. 30-40 € gebraucht bei Ebay und sie 
lassen sich gut mit einem JailBreak öffnen und für eigene Projekte
umfunktionieren. Das Mobileread-Forum bietet hierfür eine schöne
`Anleitung für JailBreak <https://wiki.mobileread.com/wiki/Kindle_Hacks_Information#Jail_break_JB>`_
an.

Die Kurzform lautet in etwa wie folgt: 

1. Kindle an den USB-Port stöpseln, 
2. die richtige Firmware im Wurzelverzeichnis des USB-Laufwerkes ablegen und
3. im Menü *HOME > MENU > Settings > MENU > Update your Kindle* die Firmware-Aktualisierung 
   auswählen. 

Das Prozedere funktioniert erstaunlich einfach und ohne größere Probleme.

SSH-Server einrichten
~~~~~~~~~~~~~~~~~~~~~

Neben dem Jailbreak sollte man das *USB-Network* installieren. Der Name ist 
etwas irreführend, hat es doch nicht
ausschließlich etwas mit USB zu tun, sondern richtet auch einen SSH-Server ein.
Auf diesen kann man sich dann über USB oder Wifi verbinden - sofern der gewählte
Kindle über Wifi verfügt.
Nach einem Neustart sollte man den eigenen SSH-Key an der richtigen
Stelle unter ablegen. Die ausführliche Anleitung im Jailbreak hilft weiter.

Nach einem Neustart kann der Kindle in den Debug-Modus versetzt werden. Dazu
gibt man auf der Home-Seite ``;debugOn`` ein. Das USB Network startet man mit 
``~usbNetwork`` . Anschließend kann man sich per SSH mit dem Kindle verbinden.

Prinzipiell kann das Geräte nun alles Anzeigen, was sich in Form eines
PNG-Bildes auf einem Server befindet. Hierfür richtet man einen Cronjob ein,
der das Bild vom Server herunterlädt und im Vollbild auf dem Kindle anzeigt. 

Cronjob einrichten
~~~~~~~~~~~~~~~~~~

Das Einrichten des Cronjobs stellte sich komplizierter heraus als zunächst
angenommen. Auf dem gewohnten Wege mit ``crontab -e`` klappte es zunächst
nicht. Auch ein direktes Ändern des Cronfiles ``/etc/crontab/root`` führte zu
keinem Ergebnis, da die Datei nicht editierbar ist. Der Grund: das Dateisystem
wird read-only (nur lesend) eingebunden. Man kann es mit ``mntroot rw`` als
beschreibbares Dateisystem mounten und anschließend das Cronfile editieren.

Bilder auf dem Kindle darstellen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Für die Darstellung von Bildern und Text auf dem Kindle ist das 
Kommandozeilentool
`eips <https://wiki.mobileread.com/wiki/Eips>`_ zuständig - vermutlich
steht die Abkürzung für *e ink postscript*. Damit
kann man den Bildschirm löschen, Text und auch Bilder anzeigen.


Setup des Servers
-----------------

Beim Einrichten des Servers ist mir aufgefallen, wir schwer es ist, an deutsche
Wetterdaten zu kommen:  als Web-Service, den ich ohne Anmeldung einfach
aufrufen kann. Ich habe mich dann für einen etwas umständlichen Weg entschieden:
über den norwegischen Wetterdienst `YR <https://www.yr.no>`_. Diese haben
schöne und `übersichtliche Darstellungen - hier z.B. 
für Bochum <https://www.yr.no/place/Germany/North_Rhine-Westphalia/Bochum/hour_by_hour.html>`_.
Aus einem PDF habe ich mit inkscape ein SVG erzeugt, dieses etwas 
zurechgeschnitten und in ein PNG konvertiert. Hierbei wird das Bild
gedreht. Zum Schluss wird das PNG in ein Graustufenbild gewandelt und etwas 
komprimiert. Dieser Prozess wird durch einen Cronjob regelmäßig durchgeführt
und das Ergebnisbild auf einem lokalen Webserver abgelegt.

.. code:: bash
  
  #!/bin/bash
  
  PDFURL=https://www.yr.no/place/Germany/North_Rhine-Westphalia/Bochum/forecast.pdf
  OUTPDF=forecast.pdf
  OUTPNG=forecast.png
  OUTSVG=forecast.svg
  
  # Download pdf with forecast
  wget -O $OUTPDF $PDFURL
  
  # convert to svg
  inkscape --without-gui --file=$OUTPDF --export-plain-svg=$OUTSVG
  
  # change viewbox size in SVG file
  sed -i -e '10s/height=.*/height="600.0"/' \
    -e '11s/width=.*/width="800.0"/'\
    -e '9s/viewBox=.*/viewBox="30 90 700 600"   preserveAspectRatio="slice"/'\
    $OUTSVG
  
  rsvg-convert --background-color=white -o $OUTPNG $OUTSVG
  # rotate landscape image
  convert $OUTPNG -rotate "90" $OUTPNG
  pngcrush -c 0 -ow $OUTPNG
  


Diese Bemühungen sind in einem 
`github repo <https://github.com/pintman/wettermonitor>`_ beschrieben.

Die Schultern der Giganten
--------------------------

Mein Projekt fußt auf dem Projekt `Kindle Weather 
Display <https://mpetroff.net/2012/09/kindle-weather-display/>`_ von Matthew Petroff
und der `Anleitung "Kindle Weather Display" von 
Jennifer <http://www.shatteredhaven.com/2012/11/1347365-kindle-weather-display.html>`_

