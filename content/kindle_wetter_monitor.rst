Wetter Monitor mit einem Kindle
===============================
:date: 2018-07-03 12:20
:author: marco.bakera
:tags: Hacking, Hardware
:slug: kindle_wetter_monitor
:status: draft

E-Book-Reader haben meist ein E-Ink-Display, ein schönes Gehäuse und sind 
meist recht günstig. Genau diese Kombination machen sie so reizvoll, um
daraus ein Türschild zu bauen oder sie als Wetteranzeige zu verwenden. Die
Displays stellen die Informationen sehr scharf dar, verbrauchen nur wenig
Strom und stellen die Inhalt scharf dar.

Setup des Kindle
----------------

In einem kleinen Projekt wollte ich mich eines 
`Kindle-Keyboard <https://de.wikipedia.org/wiki/Amazon_Kindle#Kindle_Keyboard_(3._Generation)>`_ 
annehmen. Diese bekommt man für ca. 30-40 € gebraucht bei Ebay und sie 
lassen sich gut mit einem JailBreak öffnen und für eigene Projekte
umfunktionieren. Das Mobileread-Forum bietet hierfür eine schöne
`Anleitung für JailBreak <https://wiki.mobileread.com/wiki/Kindle_Hacks_Information#Jail_break_JB>`_

In Kurzform: Kindle an den USB-Port stöpseln, die richtige Firmware ins
Wurzelverzeichnis des USB-Laufwerkes ablegen, im Menü die
Firmware-Aktualisierung auswählen. Das funktioniert erstaunlich gut und
ohne größere Probleme.

SSH-Server einrichten
~~~~~~~~~~~~~~~~~~~~~

Neben dem Jailbreak sollte man das *USB-Network* installieren. Das hat nicht
ausschließlich etwas mit USB zu tun, sondern richtet auch den SSH-Server ein.
Nach einem Neustart sollte man den eigenen SSH-Key an der richtigen
Stelle ablegen. Die ausführliche Anleitung im Jailbreak hilft weiter.

Nach einem Neustart kann der Kindle in den Debug-Modus versetzt werden. Dazu
gibt man auf der Home-Seite ``;debugOn``ein. Um das USB Network zu starten
gibt man ``~usbNetwork``ein und kann sich anschließend per SSH mit dem Kindle
verbinden.

Prinzipiell kann das Geräte nun alles Anzeigen, was in Form eines
PNG auf einem Server findet. Hierfür richtet man einen Cronjob ein,
der das Bild von einem Server herunterlädt und im Vollbild auf dem
Kindle anzeigt. 

Cronjob einrichten
~~~~~~~~~~~~~~~~~~

Das Einrichten des Cronjobs stellte sich komplizierter heraus als zunächst
angenommen.
Auf dem gewohnten Wege mit ``crontab -e`` klappt es nicht. Auch ein
direktes Ändern des cronfiles in ``/etc/crontabs/root`` führte zu 
keinem Ergebnis, da die Datei nicht editierbar. Der Grund: das Dateisystem
wir read-only (nur lesend) eingebunden.
Man muss es mit ``mntroot rw`` als beschreibbares Dateisystem mounten; 
dann kann das Cronfile editiert werden.


Setup des Servers
-----------------



Die Schultern der Giganten
--------------------------

Mein Projekt fußt auf dem *Kindle Weather Display*-
`Projekt von Matthew Petroff <https://mpetroff.net/2012/09/kindle-weather-display/>`_
und der 
`Anleitung von Jennifer <http://www.shatteredhaven.com/2012/11/1347365-kindle-weather-display.html>`_

`github repo <https://github.com/pintman/wettermonitor>`_

`eips <https://wiki.mobileread.com/wiki/Eips>`_ 
