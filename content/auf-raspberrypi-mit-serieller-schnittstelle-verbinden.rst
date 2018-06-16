Auf den RaspberryPi mit der seriellen Schnittstelle verbinden
#############################################################
:date: 2015-06-27 17:10
:author: marco.bakera
:category: Hardware, Informatik
:tags: Arduino, GPIO, RasbperryPi, rs232, serielle Schnittstelle
:slug: auf-raspberrypi-mit-serieller-schnittstelle-verbinden
:status: published

Man kann sich über die serielle Schnittstelle mit dem Raspberry Pi
verbinden. Dazu nutzt man bestimmte Pins der GPIO-Schnittstelle, einen
Konverter USB-nach-RS232 und drei Kabel.

Die Details erkläre ich in dem Video.

**Nachtrag:** Ein Arduino lässt sich auch als Wandler zwischen USB und
serieller Schnittstelle verwenden. Dazu müssen GND und RST (bzw. Reset)
miteinander verbunden werden. Dies deaktiviert den Chip auf dem Arduino.
Nun werden TX und RX direkt an USB weitergegeben und können ebenso
genutzt werden.