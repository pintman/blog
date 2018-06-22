My Home Is My Server
####################
:date: 2014-10-16 09:30
:author: marco.bakera
:tags: Informatik, Linux
:tags: Cubietruck
:slug: my-home-is-my-server
:status: published

|server20|

Die (`meine <{filename}digitale-emanzipation.rst>`__)
digitale Emanzipation schreitet weiter voran. Nachdem ich mich in den
letzten Monaten und Jahren zunehmend von den Diensten großer Unternehmen
wie Google unabhängig gemacht habe, betrete ich nun einen weiteren
Bereich der Unabhängigkeit: ein eigener Server.

Die Hardware
------------

Der erste Server, mit dem ich es probiert habe, war ein RaspberryPI.
Dieser hat seinen Dienst auch schon ganz gut geleistet - für einfach
Aufgaben ist ein Pi ausreichend. Beim Betrieb eines Webservers mit
PHP-Unterstützung und einer MySQL-Datenbank kommt er jedoch schnell an
seine Grenzen und wird verdammt langsam.

Es musste eine schnellere CPU her. Bei der zweiten Generation fiel die
Wahl auf den `Cubietruck <http://cubieboard.org/>`__ (Cubieboard 3) -
eine gute Kombination aus Rechenpower und Stromverbrauch. Dieser findet
seinen Platz in einem schönen
`Gehäuse <http://cubieboard.org/2014/02/27/ewell-has-come-minipc-not-be-far-behind/>`__
unter dem Schreibtisch. Mit der Erweiterung um eine 128 GB große SDD
werkelt er nun flott und lautlos. In dieser Konfiguration fluppt die
Kiste zügig und ist in der Lage, meine Webseite, dieses Blog, ein
MediaWiki und eine Owncloud auszuliefern.

Als Betriebssystem kommt eine Server-Variante von Lubuntu für
ARM-Prozessoren zum Einsatz. Die
`Installation <http://docs.cubieboard.org/tutorials/cubietruck/start#installation>`__
ist ausführlich im Wiki des Cubietruck beschrieben.

Die Vernetzung
--------------

Doch wie landet der Surfer auf der Kiste? Wenn ihr die Adresse
www.bakera.de in den Browser eingebt, wandelt sie ein DNS-Server in die
IP-Adresse meines Internetanschlusses um. Da hängt dann ein Router (z.B.
in Form einer FritzBox), der alle Anfragen abschmettert - normalerweise.
Mit einer
`Portweiterleitung <https://de.wikipedia.org/wiki/Portweiterleitung>`__
habe ich Anfragen für HTTP und HTTPS nun auf den Cubietruck umgeleitet.
Wie das mit eurem Router funktioniert, steht im Handbuch eures Routers.

Woher weiß nun der DNS-Server, wie die IP-Adresse meines Rechners
lautet? Da die Adresse von meinem Internet-Provider (der Telekom)
zugewiesen wird und sich ändern kann, muss ich diese Änderung regelmäßig
prüfen. Das klappt über einen Dienst für dynamische DNS-Einträge. Früher
war DynDNS in diesem Segment Namensgeber und Marktführer. Wegen eines
uninteressantes Preismodells habe ich mich aber für den Dienst
`afraid.org <http://www.afraid.org>`__\ entschieden. Er bietet kostenlos
viele Domainnamen und eine einfache Konfiguration an. Dort habe ich mir
die Adresse bakera.homenet.org gesichert. Die IP-Adresse wird dann über
den Aufruf einer Webseite regelmäßig aktualisiert. Dazu läuft im
Cubietruck ein Cronjob, der stündlich seine aktuelle IP-Adresse an
afraid,org schickt.

::

    curl -k https://freedns.afraid.org/dynamic/update.php?dkgmdn53kdmgn64l3nd

Die kryptische Zeichenkette am Ende ist ein geheimer Schlüssel, der
dafür sorgt, dass nur ich den Eintrag aktualisieren kann. Natürlich habe
ich ihn in diesem Artikel geändert.

Liebend gern hätte ich diesen Dienst auch direkt bei meiner Adresse
www.bakera.de. Leider bietet mein Registrar HostEurope einen solchen
Dienst nicht an. Da steht demnächst also auch noch ein Wechsel ins Haus
- `InterNetworX <http://www.inwx.com/>`__ scheint einen guten und
günstigen Dienst hierfür anzubieten. Daher gehe ich im Moment einen
kleinen Umweg und habe für www.bakera.de bei HostEurope einen
`CNAME-Eintrag <https://de.wikipedia.org/wiki/CNAME_Resource_Record>`__
(eine Weiterleitung direkt im Nameserver) hinterlegt, der auf die
Adresse bei afraid.org zeigt.

Eine weitere spannende Alternative ist das
`OpenNIC-Projekt <http://www.opennicproject.org/>`__. Es betreibt eigene
Nameserver und vergibt kostenlos eigene Adresse für Top Level Domains
wie z.B. .free .geek .null. Da die Adressen parallel zu den von der
`ICANN <https://de.wikipedia.org/wiki/Internet_Corporation_for_Assigned_Names_and_Numbers>`__
vergebenen Adressen laufen, kann man deren Nameserver auch für das
"normale" Internet verwenden. Die Adressen bakera.free und bakera.geek
habe ich dort sicherheitshalber schon registriert.

Die Sicherheit
--------------

Nun ist der Server erreichbar und ich kann die Inhalte abrufen. Jetzt
wird es Zeit für ein wenig Sicherheit. Die Verbindung soll durch ein
Zertifikat und eine SSL (TLS) Verbindung über HTTPS abgesichert werden.
Mann kann ein selbst-signiertes Zertifikat erstellen und für den eigenen
Webserver verwenden. Gängige Browser meckern dann jedoch, weil sie es
für keine gute Idee halten, wenn das Zertifikat nicht von einer Stelle
ausgestellt wurde, die dafür gewöhnlich Geld nimmt. Gott sei Dank gibt
es eine rühmliche Ausnahme bei den Zertifizierungstellen: `Start
SSL <https://www.startssl.com/>`__ stellt kostenlose Zertifikate aus und
wird von aktuellen Browsern als vertrauenswürdig eingestuft. Eine gute
`Anleitung bei
heise <http://www.heise.de/security/artikel/SSL-fuer-lau-880221.html>`__
erklärt, wie es geht.

Damit die Daten auch nach einem Defekt oder Ausfall der Hardware
wiederherstellbar sind, muss ein Backup her. Da der Server über SSH
erreichbar ist, kann ich ein einfaches Skript schreiben, das die Daten
vom Server holt und lokal sichert. Ich hatte ein solches Skript bereits
`vorgestellt <{filename}backup-ueber-ssh-und-eine-pipe.rst>`__.
Die Backupskripte werden auf dem Backuperechner ausgeführt und sehen
etwa wie folgt aus:

::

    ssh user@server "mysqldump -u wiki --password=wikkipasswort wiki" | gzip -c > wiki.sql.gz
    ssh user@server "php /var/www/wiki/maintenance/dumpBackup.php --full" | gzip -c > wiki-pages.txt.gz
    ssh user@server "tar cf - /var/www /home/user" | gzip -c > files.tar.gz

Für ein aktuelles Backup der Dateien bietet sich auch rsync an, das auf
dem Backuprechner ausgeführt wird. Das läuft für gewöhnlich schneller,
da rsync nur Daten überträgt, die sich seit dem letzten Lauf geändert
haben.

::

    rsync -av user@server:/home/user files
    rsync -av user@server:/var/www file

Zu guter Letzt habe ich mir angewöhnt, alle Dinge, die ich an der
Konfiguration oder Installation ändere, in einer Textdatei auf dem
Server abzuspeichern. So habe ich immer einen Überblick darüber, was
gemacht wurde oder später erneut gemacht werden muss, wenn der Server
einmal neu aufgesetzt wird.

Nun liegen die Daten direkt bei mir unter dem Schreibtisch und ich habe
die vollständige Kontrolle über den Server. Ein gutes Gefühl.

.. |server20| image:: images/2014/10/server20.png
   :class: alignright size-full wp-image-1455
   :width: 128px
   :height: 128px
