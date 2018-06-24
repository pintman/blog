Auf den RaspberryPi mit der seriellen Schnittstelle verbinden
#############################################################
:date: 2015-06-27 17:10
:author: marco.bakera
:tags: Hardware, Informatik, Arduino, GPIO, RaspberryPi, rs232, serielle Schnittstelle
:slug: auf-raspberrypi-mit-serieller-schnittstelle-verbinden
:status: published

Man kann sich über die serielle Schnittstelle mit dem Raspberry Pi
verbinden. Dazu nutzt man bestimmte Pins der GPIO-Schnittstelle, einen
Konverter USB-nach-RS232 und drei Kabel.

Die Details erkläre ich in dem 
`Video <https://www.youtube-nocookie.com/embed/ghDI3usCk-4?rel=0>`_.

**Nachtrag:** Ein Arduino lässt sich auch als Wandler zwischen USB und
serieller Schnittstelle verwenden. Dazu müssen GND und RST (bzw. Reset)
miteinander verbunden werden. Dies deaktiviert den Chip auf dem Arduino.
Nun werden TX und RX direkt an USB weitergegeben und können ebenso
genutzt werden.
