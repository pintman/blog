Remote Desktops
###############
:date: 2017-11-02 13:28
:author: marco.bakera
:tags: Linux, Windows
:slug: remote-desktops
:status: published

|image0|

Der Charme von Remote Desktops hat mich schon lange fasziniert. Ich
sitze an einem Terminal, das die Tastatur, Maus und vielleicht noch
einen USB-Stick über einen kleinen geräuschlosen und günstigen
ThinClient an einen mächtigen Server weiterleitet. Schon während meines
Studiums habe ich mit VNC und entsprechenden Implementierungen
(hauptsächlich tightvnc und einer einfachen X-Weiterleitung) meine
ersten Versuche gestartet.

**Rechnerpool einrichten**

Nun bin ich in die Verlegenheit gekommen, einen Rechnerraum mit
bescheidenen 6 Clients einrichten zu (müssten) dürfen und das
Thema ereilte mich erneut. Ich kann natürlich jeden Rechner einzeln
einrichten. Ebenso kann ich einen Referenzrechner einrichten, von diesem
ein Image erzeugen und dieses auf die anderen Rechner verteilen - z.B.
mit `Clonezilla <http://clonezilla.org/>`__. Besonders schön wäre es
jedoch, wenn ich nur einen Server pflegen müsste, auf den sich alle
Clients anschließend verbinden würden.

**Remote Desktop as a Service mit x2go und virmach**

Für virtuelle Desktops gibt es sogar Dienstleiter, wie
`virmach <https://virmach.com>`__. Es geht natürlich auch mit jedem
anderen Server, der genügend Ressourcen und Netzwerkbandbreite zur
Verfügung stellt.

Gesagt getan. In einem ersten Test habe ich den für schmale Verbindungen
optimierten Client und Server `x2go <http://x2go.org/>`__ auf dem Server
und meinem Client - Windows und Linux - installiert und konnte mich
direkt verbinden. Das klappt für günstige 4€/Monat schon recht gut.
Eigentlich müsste ich auch lokale Laufwerke/Verzeichnisse auf den fernen
Rechner transferieren können. Das klappte jedoch nicht sofort, da der
gemietete Server lediglich in einer virtuellen Maschine läuft und
notwendige Kernelmodule fehlten. Nach einem erfreulichen IRC-Chat mit
einem Entwickler von x2go war der Schuldige (ein fehlendes FUSE-Modul)
gefunden und zwei Iterationen beim Support von virmach später war dieses
Modul im Kernel meines Servers nachinstalliert.

Das neue Setup läuft soweit schon ganz gut. LibreOffice, eine Konsole
oder Fritzing lassen sich mittelgut bedienen. Lediglich der Firefox
kommt etwas träger über die Leitung.

**Raspberry Pi und andere Thin Clients**

Jetzt wäre es doch toll, wenn mein Rechner-Pool auch eine Verbindung zu
einem Server im Schul-LAN aufbauen könnte. Da wir noch einige Raspberry
Pis haben, wäre doch dieser kleine Rechner als ThinClient ideal. Es gibt
mit `rpitc <https://rpitc.blogspot.de/>`__ sogar eine Distribution, die
genau dies leisten möchte. Erste Tests verliefen gut, wenngleich die
Webseite insgesamt unprofessionell wirkt. Zudem ist unklar, wie lange
die SD-Karte in den Pi halten und wie sich die Geräte ausschalten lassen
sollen. Für das Problem des Ausschaltens gibt es mit dem `Pi Desktop
Gehäuse <https://shop.heise.de/katalog/pi-desktop-gehause-kit>`__ zwar
eine Lösung - diese ist mit ca. 50 € jedoch auch nicht günstig.

Vielleicht gibt es außer dem Raspberry Pi noch andere Möglichkeiten für
Clients. Eine `Suche bei
Ebay <https://www.ebay.de/sch/i.html?_from=R40&_sacat=0&_sop=2&_nkw=thin+client&rt=nc&LH_BIN=1>`__
nach günstigen ThinClients lieferte brauchbare Geräte ab 9 € zu Tage.
Das ist deutlich günstiger als ein Pi. Auf der Seite
`ParkyTowers <http://www.parkytowers.me.uk/thin/index.shtml>`__ stellt
David Parkinson verschiedene dieser Geräte vor. Eigentlich müssen sie
nicht viel können: netzwerkbootfähig über PXE sollten sie sein, ein
gering dimensionierter RAM ab 64 MB kann schon ausreichen.

**Thinstation: das ThinClient OS**

Doch welches Betriebssystem biete sich an, um einen ThinClient über das
Netzwerk in ein System zu booten, das nur einen Remote Desktop Client
starten muss? Man könnte eine einfache Linux Distribution wie
`slitaz <http://slitaz.org/>`__ nehmen. Sie ist genügsam, klein und
lässt sich auch über das Netz booten.

Daneben gibt es mit
`thinstation <https://thinstation.github.io/thinstation/>`__ eine
lebendige Distribution, bei der das Boot-Image genauer angepasst werden
kann, als es eine fertige Distribution leisten könnte.

**PXE**

Essentiell für den Netzwerkboot ist das Protokoll PXE, das im
Zusammenspiel mit DHCP und TFTP ein Boot-Image über das Netz ausliefern
kann. Der Client fragt über DHCP nach einer IP-Adresse, einem Gateway
und kann auch nach einem Boot-Image fragen. Das `Wiki von
ubuntuusers <https://wiki.ubuntuusers.de/PXE-Boot/>`__ erklärt diesen
Prozess und beschreibt, wie man `dnsmasq
einrichten <https://wiki.ubuntuusers.de/PXE-Installation/>`__ muss,
damit der Dienst mit einem bestehenden DHCP-Server zusammenarbeiten
kann: dnsmasq kümmert sich um den Netzwerkboot, der vermutlich schon
vorhandene DHCP-Server übernimmt die Netzwerkkonfiguration des Client.
Bei der Einrichtung müssen ein Bootloader (pxelinux.0), ein Kernel
(vmlinuz) und ein initiales Dateisystem, das im RAM läuft (initrd oder
rootfs) bereitgestellt werden.

**Und Windows?**

Windows kann auch seinen Desktop an Clients weitergeben. Dazu müssen auf
einem Windows Server sogenannte Windows *Remote Desktop Services
(Terminaldienste)* aktiviert werden. Nach der Aktivierung können alle
lokalen Benutzer auf dem Server über einen RDP-Client auf den Server
zugreifen. Windows hat hierfür *Remote Desktopverbindung*, Linux bietet
rdesktop oder das neuere xfreerdp an.

.. |image0| image:: images/2017/11/preferences-desktop-remote-desktop-300px.png
   :class: alignnone size-full wp-image-2107
   :width: 300px
   :height: 300px
