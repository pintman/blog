LTSP über Etherboot booten
##########################
:date: 2013-12-23 10:39
:author: marco.bakera
:category: Informatik, Linux, Tools
:slug: ltsp-ueber-etherboot-booten
:status: published

In einem `vorherigen
Beitrag <http://bakera.de/wp/2013/12/linux-terminal-server-projekt-ltsp-schwache-rechner-haengen-an-einem-starken-server/>`__
habe ich beschrieben, wie man einen LTSP-Server aufsetzt, der an
PXE-fähige Clients ein Boot-Image ausliefert und dann startet.

Wenn die eingesetzte Netzwerkkarte nicht PXE-fähig ist, kann man auf das
Projekt `Etherboot/gPXE <http://etherboot.org>`__ zurückgreifen. Es
stellt bootfähige Images für CDs und Disketten zur Verfügung. Mit diesen
Images kann der Prozess maßgeschneidert angepasst werden. So kann man
z.B. auch über eine WLAN-Karte booten.

`Im Wiki
weiterlesen... <http://bakera.de/dokuwiki/doku.php/schule/ltsp>`__
