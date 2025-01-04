Mediawiki unter docker
######################
:date: 2015-08-12 15:31
:author: marco.bakera
:tags: Informatik, Linux, Video
:slug: mediawiki-unter-docker
:status: published

Mit docker lassen sich schnell und einfach virtuelle Maschine betreiben,
die Serverdienste wie ein Wiki bereitstellen. An einer
Beispielinstallation eines Mediawikis zeige ich, wie das funktionieren
kann.

Hier sind die im Video eingesetzten Befehle:

docker run --name=mw -i -t -p 8080:80 32bit/debian:jessie bash

| apt-get update
| apt-get install mediawiki
| a2enconf mediawiki
| cd etc/mediawiki
| vi apache.conf
| service apache2 reload

.. image:: {filename}images/2018/06/2kn0Y2nriWw.jpg
   :alt: Youtube-Video
   :target: https://www.youtube-nocookie.com/embed/2kn0Y2nriWw?rel=0
