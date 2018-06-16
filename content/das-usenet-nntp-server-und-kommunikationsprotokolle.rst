Das Usenet, NNTP-Server und Kommunikationsprotokolle
####################################################
:date: 2015-10-16 10:58
:author: marco.bakera
:category: Informatik, Linux
:tags: INN, Newsgroup, NNTP, Server, Usenet
:slug: das-usenet-nntp-server-und-kommunikationsprotokolle
:status: published

**Das Usenet ist eine alte doch immer noch interessante und lebendige
Institution des Internet - aus technischer, kultureller und auch
historischer Sicht. Ich möchte mit euch eintauchen in diese Welt und sie
als Nutzer und technisch Interessierter erkunden.**

|ic_chat_black_48dp|\ Meine `digitale
Emanzipation <https://www.bakera.de/wp/2013/05/digitale-emanzipation/>`__
schreitet voran: Nachdem ich `meinen
Server <http://www.bakera.de/wp/2014/10/my-home-is-my-server/>`__ in die
heimischen vier Wände geholt und einen eigenen `Jabber-Server
aufgesetzt <http://www.bakera.de/wp/2015/05/ein-eigener-jabber-server/>`__
habe, soll nun ein Newsserver als neues Projekt das heimische Netzwerk
erweitern. Doch zunächst ein paar erklärende Worte.

Usenet: Was es ist und wie man es bedient
-----------------------------------------

Das `Usenet <https://de.wikipedia.org/wiki/Usenet>`__ ist die große alte
Dame des Internet. Sie - also es - wurde 1979 geboren und ist damit
älter als das World Wide Web - also die bunte Welt, die man durch das
Browserfenster betrachtet. Da das Usenet älter als das WWW ist, benötigt
man ein eigenes Programm um darauf zugreifen zu können: einen
Newsreader. Damals wie heute wird das Usenet mit seinen zahlreichen
Diskussionsgruppen für den Wissensaustausch genutzt und für den
Dateiaustausch missbraucht. Es ist der `Geburtsort der Merkbefreiung und
Wirkenskreis von Hürbine von
Pleuselspink <http://www.heise.de/tp/artikel/13/13155/1.html>`__.

Die Nutzerzahl ist seit dem Aufkommen sozialer Netzwerke wie Facebook
und Webforen `rückläufig <http://usenet.dex.de/de.ALL.html>`__. Aber das
muss nichts über die Qualität der Inhalte aussagen. Vielfach findet man
dort technisch versierte und inhaltlich kompetente Nutzer, die
ausführlich und mit viel Erfahrung antworten. Außerdem kann es mit
vielen unterschiedlichen Clients benutzt werden, was die Möglichkeiten
von Filterung, Darstellung und Bedienung deutlich erweitert. Ein
Beispiel für die Qualität ist die intensive Diskussion um das Rätsel
`"Prinzessin im
See" <https://groups.google.com/d/msg/de.rec.denksport/4uWJU6xvwH8/Snup8Kd9BwAJ>`__
in der Gruppe \ *de.rec.denksport*. Ich habe in den letzten Tagen ca.
100 Beiträge pro Tag in den von mir abonnierten Gruppen erhalten und
denke, dass dies ausreichend für eine lebendige Gruppenstruktur ist. Das
Usenet ist also nicht tot, es hat sich nach einem Hype am Ende der 90er
Jahre in einem stabilen Nutzungsverhalten eingependelt.

Ein detaillierte Darstellung des Usenet gibt das schon ältere, dafür
kostenlos erhältliche Buch `Newsgroups - weltweit
diskutieren <http://www.detebe.org/usenet-buch/>`__, das viele
verschiedene Aspekte beschreibt: die Technik, Kommunikationsmodelle
sowie gesellschaftliche und historische Dimensionen. Das Archiv der
Beiträge seit Beginn der 80er Jahre kann z.B. mit der Suchmaschine `The
Usenet Archive <http://www.theusenetarchive.com/>`__ oder `Google
Groups <https://groups.google.com>`__ durchsucht werden.

Der deutsche Teil des Usenet organisiert sich in den de.\*-Gruppen.
Gruppen in dieser Hierarchie werden von der
`dana <http://www.dana.de/>`__ (de.admin.news.announce) koordiniert:
also angelegt, gelöscht, zusammengefasst oder aufgesplittet.

Neugierig geworden? Es ist erstaunlich einfach, einen Account bei einem
Newsserver zu bekommen, der Usenet-Nachrichten verteilt. Das `Open News
Network <http://open-news-network.org/>`__ hat sich vorgenommen, freie
Zugänge für Text-Gruppen bereit zu stellen. Ich habe mir einen
kostenlosen Account beim schweizerischen Anbieter
`albsani.net <http://albasani.net/>`__ erstellt. Daneben gibt es noch
`individual.de <http://news.individual.de>`__. Dies ist ein Anbieter der
Freien Universität Berlin. Er möchte 10 € pro Jahr für seine Dienste
haben und gilt als Urgestein der Usenetszene.

Nun benötige ich noch ein Programm, um auf die Gruppen zugreifen zu
können. Gott sei dank werden viele E-Mail-Programme heutzutage schon mit
einer Unterstützung für Newsgroups ab Werk ausgeliefert. So auch
Thunderbird (eine Anleitung ist
`hier <https://support.mozilla.org/de/kb/newsgruppen-konto-einrichten>`__
und
`hier <https://www.thunderbird-mail.de/wiki/Newsgruppen-Konto_einrichten>`__)
und `Windows Mail <https://support.microsoft.com/de-de/kb/956674>`__.
Viele weitere Anleitungen für unterschiedliche Betriebssysteme und
Programme gibt es bei
`individual.de <http://news.individual.de/config.php>`__. Für Android
hat mir das Programm `Usenet Newsreader <http://usenet.sinaapp.com/>`__
gut gefallen.

Nach der Einrichtung kann man eine umfangreiche Gruppenliste (über
25.000 Gruppen!) herunterladen und ein wenig darin stöbern. Mir haben
die Gruppen unter de.\* und ger.\* auf den ersten Blick ganz gut
gefallen. Du musst aber selbst ein wenig suchen und nach deinen eigenen
Interessen schauen.

Eigener Server
--------------

Aber die reine Verwendung eines Newsservers hat mir natürlich nicht
gereicht. Schließlich möchte ich meine Infrastruktur selbst gestalten
und aufbauen. Also musste ein eigener Newsserver her. Hier ist
`INN <http://www.eyrie.org/~eagle/software/inn/>`__ der de-facto
Standard - in Version 2 heißt das Paket auch häufig *inn2* in den
Distributionen. Die Freifunker haben eine schöne
`Anleitung <https://wiki.freifunk.net/Newsserver_einrichten>`__ für die
Einrichtung geschrieben. Dass die Konfiguration so ihre Tücken aufweist
zeigt ein `Beitrag aus dem
FreeBSD-Diary <http://www.freebsddiary.org/inn.php>`__. Er stellt die
üblichen Stolperstellen vor und gibt Hinweise darauf, wie man sie
umgehen kann.

Es geht aber auch einfacher - und zwar mit dem Server
`WendzelNNTPd <https://github.com/cdpxe/WendzelNNTPd/releases>`__. Der
Server lässt sich einfach installieren und hat wenig Ansprüche. Außerdem
reagierte der Autor Steffen Wendzel bei meinen Recherche extrem schnell
auf Anfragen und Probleme. Innerhalb von Stunden war mir geholfen. Eine
Installationsanleitung hat Steffen Wendzel selbst in dem `Kapitel zu
NNTP-Servern <http://openbook.rheinwerk-verlag.de/linux/linux_kap17_004.html#dodtp519616a1-d189-4793-b529-e6527490a15a>`__
des Buches "Linux - das umfassende Handbuch" (Rheinwerk Verlag)
geschrieben.

Das Programm wird nicht als Paket ausgeliefert, sondern muss mit einem
C-Compiler kompiliert werden. Das ist einfacher als es sich anhört, da
vieles automatisch abläuft. Zunächst laden wir den Quelltext aus dem
`git-repo <https://github.com/cdpxe/WendzelNNTPd/releases>`__  herunter
und entpacken das Archiv.

Es werden noch ein paar Bibliotheken benötigt, die wir leicht
installieren können.

::

    $ sudo apt-get install gcc flex bison libsqlite3-dev make

Als Backend für die Daten kommen eine SQLite- oder MySQL-Datenbank in
Frage. Die Nachrichten selbst werden als Textdateien abgespeichert. In
der Datenbank werden nur Zugangsdaten sowie die Verlinkungsstruktur der
Nachrichten untereinander und die Zuordnung zu den Diskussionsgruppen
realisiert. Ich entscheide mich für eine leichtgewichtige Variante mit
SQLite und werfe das Konfigurationsskript an.

::

    $ MYSQL=NO ./configure

Sollten nun immer noch Bibliotheken fehlen, meldet sich das Skript und
sagt genau, was es noch benötigt. Danach kann ich die Software
kompilieren und nach */usr/local* installieren lassen.

::

    $ make
    $ sudo make install

Im Sourcenpaket ist noch ein init-skript, das ich an die richtige Stelle
kopiere.

::

    $ sudo cp ~/src/WendzelNNTPd-2.0.5/WendzelNNTPd-OSE/scripts/startup/init.d_script /etc/init.d/wendzelnntpd

Nun kann ich den Dämon ein erstes mal starten.

::

    $ sudo /etc/init.d/wendzelnntpd start

Damit der Dienst auch nach einem Reboot läuft, starte ich ihn für
runlevel 2. Dazu lege ich einen symbolischen Link auf das Init-Skript
an.

::

    /etc/rc2.d$ ln -s ../init.d/wendzelnntpd S92wendzelnttpd

Damit der Dienst auch bei einem Shutdown (runlevel 0) und einem reboot
(runlevel 6) sorgfältig heruntergefahren wird, sorge ich für Links an
den korrekten Stellen in den rc-Verzeichnissen.

::

    /etc/rc0.d$ sudo ln -s ../init.d/wendzelnntpd K20wendzelnntpd
    /etc/rc6.d$ sudo ln -s ../init.d/wendzelnntpd K20wendzelnntpd

Nun können wir die Konfigurationsdatei in
*/usr/local/etc/wendzelnntpd.conf* anpassen. Wir müssen zunächst mit
*listen* dafür sorgen, dass der Newsserver von außen erreichbar ist.
Damit er nicht sofort Ziel von ungebetenen Nutzern wird, aktiviere ich
zudem die Benutzerauthentifikation.

::

    listen 192.168.178.60
    use-authentication

Wir starten den Dämon nach unseren Änderungen neu.

::

    $ sudo /etc/init.d/wendzelnntpd restart

Nun können wir einen ersten Nutzer und eine erste Gruppe anlegen.
Hierbei hilft das Administrationstool *wendzelnntpadm* weiter.

::

    $ sudo wendzelnntpadm adduser marco PASSWORT
    $ sudo wendzelnntpadm addgroup de.bakera.test y

Das 'y' hinter der Gruppe besagt, dass in diese Gruppe geschrieben
werden darf. Da schon zu Beginn ein paar Gruppen vorhanden sind, lösche
ich diese noch.

::

    $ sudo wendzelnntpadm delgroup alt.wendzelnntpd.test

Damit der Server auch hinter meiner Fritz-Box erreichbar ist, habe ich
im DNS noch den Eintrag *news.bakera.de* ergänzt und eine
Portweiterleitung auf Port 119 im Router eingerichtet. Nun kann einer
Nutzung des Servers nichts mehr im Wege stehen.

Die Nachrichten werden im Verzeichnis */var/spool/news/wendzelnntpd*
abgelegt. Für jede Nachricht existiert dort eine Datei mit einer
eindeutigen Message-ID. Weitere Informationen über den Ort der Nachricht
oder deren Headerdaten  werden bei einer sqlite-Installation in der
Datei *usenet.db* abgelegt. Die Tabelle kann man sich mit einem
sqlite-Client leicht anschauen. Man entdeckt folgende Tabellen mit den
entsprechenden Attributen.

::

    newsgroups (id, name, pflag, high)
    ngposts (msgid, ng, postnum)              PRIMARY KEY(msgid, ng)
    postings (msgid, date, author, newsgroups, subject, lines, header)
    users (name, password)
    roles (role)
    users2roles (username, role) PRIMARY KEY(username, role)
    acl_users (username, ng)                 PRIMARY KEY(username, ng)
    acl_roles (role, ng)                     PRIMARY KEY(role, ng)

Kommunikationsprotokoll
-----------------------

Da das Protokoll NTTP, das der Newsserver spricht, sehr einfach
aufgebaut ist, können wir sogar direkt über Telnet mit dem Server
kommunizieren. Unten sehen wir eine Beispielsitzung. Meine eigenen
Eingaben habe ich fett hervorgehoben. Der Rest sind Antworten des
Servers. Eine ausführliche Kommunikation findet ihr auch auf Seite 95
des oben erwähnten
`Usenet-Buches <http://www.detebe.org/usenet-buch/docs/Newsgroups-Buch.pdf>`__.

::

    telnet news.bakera.de 119
    Trying 79.226.231.205...
    Connected to news.bakera.de.
    Escape character is '^]'.
    200 WendzelNNTPd-OSE (Open Source Edition) 2.0.5 'Auckland' - (Sep 26 2015 06:42:09 #2517) ready (posting ok).
    AUTHINFO USER marco
    381 More authentication information required.
    AUTHINFO PASS *****
    281 Authentication accepted.
    HELP
    100 help text follows
    --
     article [number|<message-id>]
     authinfo <user|pass> <username|password>
     body [number|<message-id>]
     date
     group <group>
     head [number|<message-id>]
     help
     list [overview.fmt|newsgroups [wildmat*]]
     listgroup [group]
     mode reader (always returns 200)
     post
     quit
     stat [number|<message-id>]
     xhdr <from|date|newsgroups|subject|lines> <number[-[endnum]]|msgid>
     xover <from[-[to]]>
     xgtitle [wildmat*] (equals LIST NEWSGROUPS but return code differs)
    --
    Send questions and problems to <swendzel [at] ploetner-it [dot] de>
    Website: http://www.wendzel.de/software/wendzelnntpd.html
    Notes:
    * Wildmat format is based on the used regex library and is not 100%
     wildmat format compatible (XGTITLE *x -> XGTITLE .*x)!
    .
    DATE
    111 20150927185030 
    LIST 
    215 list of newsgroups follows 
    de.bakera.test 2 1 y 
    . 
    POST
    340 send article to be posted. End with <CR-LF>.<CR-LF>
    From: marco@bakera.de
    Newsgroups: de.bakera.test
    Subject: Ein Test

    Ein Testartikel.
    .
    240 article posted
     
     

.. |ic_chat_black_48dp| image:: https://www.bakera.de/wp/wp-content/uploads/2015/10/ic_chat_black_48dp.png
   :class: alignright size-full wp-image-1870
   :width: 144px
   :height: 144px
