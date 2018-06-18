Ein eigener Jabber-Server
#########################
:date: 2015-05-26 07:51
:author: marco.bakera
:tags: Informatik
:tags: Chat, chatsecure, jabber, pidgin, prosody, xmpp
:slug: ein-eigener-jabber-server
:status: published

|XMPP_logo.svg|

Die fehlende Vielfalt und die kritische Datenschutzsituation freier
Messenger wie WhatsApp haben mich bewogen, nach Alternativen Ausschau zu
halten. Früher haben wir den Kampf schon einmal mit ICQ ausfechten
müssen - und mit dem Siegeszug von
`XMPP <https://de.wikipedia.org/wiki/Extensible_Messaging_and_Presence_Protocol>`__
und Jabber gewonnen. Nachdem sich Google und Facebook von diesem
Standard - zumindest in öffentlichen Schnittstellen - verabschiedet
haben oder verabschieden werden, ist es wieder einmal an der  Zeit, das
Breitschwert der digitalen Emanzipation aus dem Rucksack zu holen.

Nun wiederholt sich die Geschichte also im Mobilbereich. Als Jabber-User
der frühen Stunde bin ich auf die Idee gekommen, einen eigenen
Jabber-Server aufzusetzen. Eigentlich ist es ja ein XMPP-Server, aber
das hört sich irgendwie zu technisch an.

|prosody|

Nach einer kurzen Recherche unter verschiedenen Jabber-Servern fiel die
Wahl auf die Software `Prosody <http://prosody.im/>`__, die nun auch auf
`meinem
Server <http://www.bakera.de/wp/2014/10/my-home-is-my-server/>`__ läuft.
Eine `Liste mit öffentlichen Servern <https://xmpp.net/directory.php>`__
verrät, welche Software häufig zum Einsatz kommt und ermöglicht eine
erste Einschätzung. Prosody ist leicht zu konfigurieren und
ressourcenschonend im Betrieb. Wer zudem in die `Programmierung mit
lua <http://prosody.im/doc/developers/modules>`__ einsteigen möchte,
findet mit Prosody ein interessantes Projekt. Andere Server wie
*ejabberd* habe ich nicht getestet und kann sie daher weder empfehlen
noch von ihnen abraten. Ihr könnt mich nun unter der JabberID (JID)
*marco@jabber.bakera.de* erreichen - kontaktiert mich mal, wenn ihr eure
eigene Konfiguration testen wollt.

Kommen wir nun zur Installation und Konfiguration des Servers. Prosody
ist mit *apt-get install prosody* schnell auf einem Debian-System
installiert. Dann kann im Ordner */etc/prosody* die Konfiguration
erfolgen. Eine allgemeine Konfigurationsdatei liegt in \ */etc/prosody*,
die Konfigurationsdateien für einen oder mehrere Hosts liegen in
*/etc/prosody/conf.avail*. Aktive Konfigurationen werden aus
*/etc/prosody/conf.d* verlinkt und können so bequem aktiviert und
deaktiviert werden.

Der Server muss sich mit einem Zertifikat ausweisen, das jedoch leicht
mit *prosodyctl cert generate jabber.bakera.de* generiert werden kann.
Es wird ein selbst signiertes Zertifikat erstellt. Manche Clients
meckern da ein wenig herum, weil es nicht von einer "ordentlichen" CA
unterschrieben wurde. Meist muss man dies jedoch nur beim ersten Kontakt
mit dem Server im Client bestätigen. Da ich der einzige Nutzer auf dem
Jabber-Server bin, vertraue ich mir natürlich.

Damit der Server von Außen erreichbar ist, habe ich eine neue Subdomain
*jabber.bakera.de* im DNS eingetragen und in meiner Fritzbox die Ports
5222 und 5269 auf meinen Server weitergeleitet. Port 5222 vermittelt die
Kommunikation der Clients mit dem Server (c2s - client to server), Port
5269 realisiert die Kommunikation zwischen verschiedenen Jabber-Servern
(s2s - server to server).

Einen ersten Hinweis darauf, ob alles korrekt läuft, liefert ein Test
von `xmpp.net <https://xmpp.net/>`__ - bringt bei eigenen Versuchen
etwas Geduld mit, da der Test einige Minuten dauern kann.

Damit ist die Konfiguration auch schon fertig. Die einzelnen Module von
prosody können jetzt noch separat konfiguriert werden. Die Dokumentation
auf der Seite von prosody hilft hierbei weiter.

|Pidgin-chatsecure|

Nachdem der Server nun steht, geht es an die Clients, die sich mit ihm
verbinden sollen. Dafür habe ich auf dem Desktop
`pidgin <https://pidgin.im/>`__ und auf meinem Handy
`chatsecure <https://chatsecure.org/>`__ installiert. Pidgin kenne ich 
seit vielen Jahren. Es läuft unter Windows, Linux und Mac OS, hat viele
Plugins und ist trotzdem nicht überladen. Auf dem Handy teste ich
chatsecure, das eine einfache Bedienung verspricht und vom
guardianproject unterstützt wird. Wer keinen zusätzlichen Client
installieren möchte und sowieso schon Thunderbird installiert hat, kann
auch `diesen dafür
verwenden <https://support.mozilla.org/de/kb/sofortnachrichten-und-chat>`__.
Leider gibt es derzeit (Stand Mai 2015) keine Unterstützung für eine
Verschlüsselung in Thunderbird Chat, obwohl eine
`Anfrage <https://bugzilla.mozilla.org/show_bug.cgi?id=954310>`__ dafür
seit mehreren Jahren diskutiert wird.

Nun steht (m)einer freien und sicheren Kommunikation nichts mehr im
Wege.

.. |XMPP_logo.svg| image:: images/2015/04/XMPP_logo.svg_.png
   :class: alignnone size-full wp-image-1696
   :width: 233px
   :height: 240px
.. |prosody| image:: images/2015/04/prosody.png
   :class: alignnone size-full wp-image-1694
   :width: 757px
   :height: 170px
.. |Pidgin-chatsecure| image:: images/2015/04/Pidgin-chatsecure.png
   :class: alignnone size-full wp-image-1711
   :width: 276px
   :height: 152px
