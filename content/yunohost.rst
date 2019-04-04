YunoHost - das Ubuntu für Server?!
==================================
:date: 2019-01-03 12:20
:author: marco.bakera
:tags: 35c3, cloud, e-mail, wiki, RaspberryPi, server
:status: published
:slug: yunohost


.. figure:: {static}images/2019/dude_yunohost.jpg
   :alt: Meme
   
   Quelle: https://github.com/alexAubin/yunohostWorkshop/tree/master/img


`YunoHost <http://yunohost.org/>`_ soll es jedem ermöglichen, einen eigenen
kleinen Server zu betreiben - z.B. auf einem Raspberry Pi oder auf einer 
virtuellen Serverinstanz. So, wie es Ubuntu ermöglicht hat, jedem ein Linux
auf seinem Rechner zu installieren.

Yunohost wird ausgesprochen als "Why You No Host" - 
also "warum hostet du nicht" und versteht sich als Aufruf an alle, denen
das Hosting eigener Dienste zu kompliziert erscheint.

Ich spiele das prozedere einmal mit einem Cloudserver von Hetzner durch. 
Zuerst wird eine Instanz mit einem aktuellen Debian Image erstellt. 
Die kleinste Version ist hier ausreichend.

.. image:: {static}images/2019/yunohost1.gif
   :alt: Start eines Hetzner-Servers

Nach dem Start kann ich mich per SSH einloggen und die Installation starten.
Die Anleitung empfiehlt hierfür, den folgenden Einzeiler.

::

    curl https://install.yunohost.org | bash

Puristen mögen solche Installationsroutinen überhaupt nicht. Und tatsächlich
muss man dem Projekt an dieser Stelle Vertrauen entgegen bringen, da nun 
"alles Mögliche" in eine root-shell geschickt werden kann. Die 
Installationsanleitung ist sich dessen bewusst und verweist auf den Artikel 
`Is curl|bash insecure? <https://sandstorm.io/news/2015-09-24-is-curl-bash-insecure-pgp-verified-install>`_
der die Problematik erläutert. Ich vertraue dem Projekt an dieser Stelle
und führe den Befehl aus.

Nach dem ersten Zugriff begrüßt mich die Seite mit einer Zertifikatswarnung. 
Da ich noch kein Zertifikat für eine Domäne eingerichtet habe, kann ich diese
Warnung ignorieren und das selbst signierte Zertifikat akzeptieren.

.. image:: {static}images/2019/yunohost2.gif
   :alt: erster Zugriff

Nun erfolgt eine Post-Installationsroutine, in der ein Administrationspasswort und 
eine Domain angelegt werden müssen. Wer noch keine eigene Domäne hat, kann 
eine der von dem Projekt bereitgestellten Domains verwenden. Die Einträge im DNS
werden dann automatisch vorgenommen.

Die Projektleiter haben zusätzlich noch den französischen Dienst 
`NetLibe.re <http://netlib.re/>`_ empfohlen,
über den eigenständig beliebige DNS-Einträge vorgenommen werden können.

.. image:: {static}images/2019/yunohost3.gif
   :alt: Post Installation

Für eine sinnvolle Verwendung, muss nun ein erster Nutzer angelegt werden. Die Nutzer
werden an zentraler Stelle verwaltet und können anschließend auf alle installierten 
Dienste zugreifen.

.. image:: {static}images/2019/yunohost4.gif
   :alt: Benutzer anlegen

Es sind noch keine Dienste installiert. Als einfaches Beispiel installiere ich ein
DokuWiki - eine populäre und einfache Wiki-Software. Die Installation anderer Dienste
erfolgt analog. Selbst ein E-Mail-Server lässt sich leicht einrichten. 

In der Auswahl lässt sich erkennen, dass die Dienste nach ihrer Güte in 
verschiedene Level eingeteilt sind. Erprobte Dienste bekommen ein höheres Level als
experimentelle Dienste.

.. image:: {static}images/2019/yunohost5.gif
   :alt: Applikation installieren

Ich habe noch keine längeren Tests mit dem System durchgeführt, gebe ihm aber 
eine Chance. Die französischen Entwickler durfte ich beim 35C3 kennenlernen. Sie 
haben einen kompetenten und ambitionierten Eindruck gemacht. Daher würde es mich
freuen, wenn mehr Menschen ihre eigene Dienste hosten würden. Vielleicht ist
es gar nicht so schwer.

**Update:** Bei Twitter gibt es eine 
`kurze Diskussion <https://twitter.com/pintman/status/1080794746677854208>`_
zu diesem Post.
