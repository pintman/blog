Analyse einer seriellen Kommunikation
#####################################
:date: 2015-01-21 18:58
:author: marco.bakera
:category: Hardware, Informatik
:tags: Bus Pirate, Logic Analyzer, Logic Sniffer, Trinket Pro
:slug: analyse-einer-seriellen-kommunikation
:status: published

|SerielleKommunikation_Aufbau|

Diesmal habe ich mir die Kommunikation über eine serielle Schnittstelle
angeschaut. Und zwar auf der untersten Ebene, da, wo die digitalen
Signale über die Leitung gehen und man die Bits noch rauschen hört. Dazu
habe ich auf der einen Seite einen Mikrocontroller verwendet, der auf
die serielle Schnittstelle schreibt und auf der anderen Seite einen
`Logikanalysator <https://de.wikipedia.org/wiki/Logikanalysator>`__, mit
dem ich die geschriebenen Daten auswerten kann.

Oben seht ihr den einfachen Aufbau bestehend aus einem `Bus
Pirate <http://dangerousprototypes.com/docs/Bus_Pirate>`__, den ich als
Logikanalysator betreiben werde, und einem `Trinket
Pro <https://learn.adafruit.com/introducing-pro-trinket?view=all>`__ mit
einem Mikrocontroller - so eine Art kleiner Arduino. Die serielle
Ausgabe TX des Trinket Pro ist über ein Kabel mit dem Eingang MISO
(Master In Slave Out - so eine Art generischer Eingang) des Bus Pirate
verbunden. Der Bus Pirate versorgt den Trinket zusätzlich über 5V mit
Strom.

Der Quelltext, der auf dem Trinket läuft, ist einfach gehalten und unten
abgebildet. Zunächst folgt die Setup-Routine, die beim Start des Trinket
ausgeführt wird.

::

    void setup() {
      pinMode(13, OUTPUT);
      Serial.begin(300);
    }

Hier wird Pin 13 - eine on-Board LED - als Ausgabe konfiguriert. Sie
soll später nur blinken und dadurch signalisieren, dass das Programm
läuft. Sie hat keine weitere Funktion für dieses Projekt.

Die Geschwindigkeit der seriellen Schnittstelle wird für mickrige 300
Baud konfiguriert. Da ich die Ausgabe später anschauen möchte, habe ich
die Geschwindigkeit bewusst sehr langsam eingestellt.

::

    void loop() {
      digitalWrite(13, HIGH);
      Serial.write(0b01010101);
      delay(100);            
      digitalWrite(13, LOW); 
      Serial.write(0b10000001);
      delay(100);            
    }

Die Hauptschleife befindet sich in der Methode loop. Sie wird immer
wieder ausgeführt und schaltet abwechselnd die LED an (HIGH) und wieder
aus (LOW). Das hat eigentlich keine Funktion, sondern dient nur der
Funktionskontrolle des Controllers.

Zusätzlich sende ich auf die serielle Schnittstelle das Bitmuster
01010101, warte ein paar Millisekunden und sende anschließend das
Bitmuster 10000001. Das voran gestellte "0b" signalisiert, dass die
folgende Zahl keine Dezimalzahl, sondern eine binäre Zahl bestehend aus
0en und 1en darstellt. Ich habe die Hoffnung, dass ich die beiden
Bitmuster im Logic-Sniffer gut wiedererkennen kann.

Nun wird der BusPirate entsprechend der obigen Verkabelung an die
serielle Schnittstelle angeschlossen. Mit dem Programm `OLS
Client <http://www.lxtreme.nl/ols/>`__ kann ich die Kommunikation
mitschneiden. OLS steht hierbei für Open Bench Logic Sniffer. Die
folgende Abbildung zeigt einen Mitschnitt, den ich um die
korrespondierenden Quelltextzeilen ergänzt habe.

|LogicSniffer|

Und tatsächlich kann man im LogicSniffer die Impulse als Bitmuster und
die Pause von 100ms zwischen den beiden Sendungen wiedererkennen. Das
Programm kann sogar versuchen, den Bitstrom zu rekonstruieren, wenn wir
wissen, dass es sich um eine Kommunikation über die serielle
Schnittstelle handelt. Das ist nicht selbstverständlich. So könnte der
Logikanlysator auch die Kommunikation eines anderen Buses mitgehört
haben.

|OLS-Analyse|

Links oben können wir die einzelnen Pins den aufgezeichneten Kanälen
zuordnen. Links in der Mitte stellen wir 300 Baud als
Übertragungsgeschwindigkeit ein. Und tatsächlich taucht das versendete
Bitmuster in der Analyse wieder auf (rot markiert). Die zugehörigen
Hexwerte 0x55 und 0x81 hatte der Sniffer bereits im obigen Logikdiagramm
erkannt und eingetragen.

Mich hat erstaunt, dass es wenig Rauschen um die eigentlichen Nutzdaten
der beiden Bitmuster gibt. Im Wesentlichen werden die Bitmuster genau in
den Signalen abgebildet.

.. |SerielleKommunikation_Aufbau| image:: https://www.bakera.de/wp/wp-content/uploads/2014/12/SerielleKommunikation_Aufbau-1021x1024.jpg
   :class: alignnone size-large wp-image-1563
   :width: 625px
   :height: 626px
   :target: http://www.bakera.de/wp/wp-content/uploads/2014/12/SerielleKommunikation_Aufbau.jpg
.. |LogicSniffer| image:: https://www.bakera.de/wp/wp-content/uploads/2014/12/LogicSniffer-1024x120.png
   :class: alignnone size-large wp-image-1567
   :width: 625px
   :height: 73px
   :target: http://www.bakera.de/wp/wp-content/uploads/2014/12/LogicSniffer.png
.. |OLS-Analyse| image:: https://www.bakera.de/wp/wp-content/uploads/2014/12/OLS-Analyse.png
   :class: alignnone size-full wp-image-1561
   :width: 935px
   :height: 468px
   :target: http://www.bakera.de/wp/wp-content/uploads/2014/12/OLS-Analyse.png
