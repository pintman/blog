WLampe
=======
:date: 2021-10-20 12:20
:author: marco.bakera
:tags: esp8266, hacking, hardware
:status: published
:slug: wlampe

.. image:: {static}images/2021/Lampe.png
   :alt: Lampe beleuchtet
   :width: 600

Man nehme: Eine Ikea-Lampe
`Vickleby <https://www.ikea.com/de/de/p/vickleby-standleuchte-weiss-handarbeit-50430390/>`_,
einen ESP8266, einen Streifen WS2812b LEDs, etwas Kabelbinder und das Projekt 
`WLED <https://kno.wled.ge/>`_ für die Ansteuerung. Fertig ist eine schicke Lampe, die 
sich mit einer App oder über verschiedene Protokolle (MQTT, UDP, DMX, ...) ansteuern lässt.

Das fertige Ergebnis kann man sich in einem Video bei
`YouTube <https://youtu.be/RV2hnFb_tM8>`_ oder
`Peertube <https://tube.tchncs.de/w/iDkTK4NdmmXKMpPRDCbg8K>`_
ansehen.

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/RV2hnFb_tM8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Die LEDs wurden stümperhaft mit etwas Kabelbinder an dem mittleren Metallstab
befestigt:

.. image:: {static}images/2021/Lampe_1183.png
   :alt: Blick in die Lampe
   :width: 400

.. image:: {static}images/2021/Lampe_1184.png
   :alt: LEDs befestigt
   :width: 400

Im unteren Bereich befinden sich eigentlich eine Fassung und ein Netzstecker, die 
ich entfernen musste, da die Fassung Teil der Befestigung der unteren Konstruktion ist.

.. image:: {static}images/2021/Lampe_1185.png
   :alt: Netzstecker entfernt
   :width: 600

Die Kabel der LEDs wurden über eine Lüsterklemme mit ein paar Steckbrücken verbunden,
die wiederum in einem ESP8266 stecken. Zwischen Masse und 5V steckt ein kleiner 
Kondensator. Die LEDs können beim Einschalten recht viel Strom ziehen und geben dem
ESP dann ggf. nicht die Möglichkeit, zu starten.

.. image:: {static}images/2021/Lampe_1186.png
   :alt: Lüsterklemme
   :width: 600

Die folgenden Bilder zeigen die recht simple Verdrahtung mit dem ESP8266. Wichtig ist 
hier nur Pin D4, der als Datenleitung die LEDs ansteuert. Eigentlich mögen die LEDs 
5V und man könnte daher zusätzlich einen Level-Shifter einbauen (die Projektseite von 
WLED stellt unterschiedliche Bauteile vor), bei mir klappte es jedoch auch so.

Wenn der ESP über die USB-Buchse betrieben wird, liegen an Vin 5V an, die für die LEDs 
genutzt werden können.

.. image:: {static}images/2021/Lampe_1187.png
   :alt: ESP Unterseite
   :width: 400

.. image:: {static}images/2021/Lampe_1188.png
   :alt: ESP Oberseite
   :width: 400

Der LED-Streifen verläuft einmal von unten nach oben und dann wieder nach unten. Um die 
beiden Stränge in der gleichen Richtung zu betreiben, werden sie in der Mitte geteilt und 
in WLED in zwei Segmente eingeteilt, wobei das zweite Segment in umgekehrter Reihenfolge
konfiguriert wird.

.. image:: {static}images/2021/wlampe_settings.png
   :alt: ein Bild

Die Einstellungen werden in dem Preset 16 gespeichert - nur dieses Preset speichert auch
die Konfiguration der Segmente ab.

Als JSON-Export sieht die Konfiguration aus wie folgt:


::

    {
    "on": true,
    "bri": 128,
    "transition": 7,
    "mainseg": 0,
    "seg": [
        {
        "id": 0,
        "start": 0,
        "stop": 19,
        "grp": 1,
        "spc": 0,
        "on": true,
        "bri": 255,
        "col": [
            [255, 0, 0 ],
            [0, 0, 255],
            [8, 255, 0]
        ],
        "fx": 66,
        "sx": 121,
        "ix": 125,
        "pal": 0,
        "sel": true,
        "rev": false,
        "mi": false
        },
        {
        "id": 1,
        "start": 19,
        "stop": 38,
        "grp": 1,
        "spc": 0,
        "on": true,
        "bri": 255,
        "col": [
            [255, 0, 0],
            [0, 0, 255],
            [8, 255, 0 ]
        ],
        "fx": 66,
        "sx": 121,
        "ix": 125,
        "pal": 0,
        "sel": true,
        "rev": true,
        "mi": false
        },
        { "stop": 0 },
        { "stop": 0 },
        { "stop": 0 },
        { "stop": 0 },
        { "stop": 0 },
        { "stop": 0 },
        { "stop": 0 },
        { "stop": 0 },
        { "stop": 0 },
        { "stop": 0 }
    ]
    }


Die Lampe kann mit verschiedenen Protokollen angesprochen werden.
Das folgende Beispiel zeigt ein Python-Programm, welches eine sehr 
direkte Steuerung der einzelnen LEDs über ein eigenes UDP basiertes
`Protokoll <https://kno.wled.ge/interfaces/udp-realtime/#udp-realtime>`_ 
erlaubt.

.. code-block:: python

   import socket

   API_ENDPOINT = ('192.168.179.15', 21324)
   NUM_LEDS = 50

   # Byte 0 of the UDP packet tells the server which realtime protocol to use.
   PROTO_WARLS = 1  # WARLS
   PROTO_DRGB = 2   # DRGB
   PROTO_DRGBW = 4  # DRGBW
   PROTO_DNRGB = 3  # DNRGB
   PROTO_WLED_NOTIFIER = 0
   PROTO_WAIT_TIME = 50 # seconds

   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   pos = 0

   while True:
      data = [PROTO_WARLS, PROTO_WAIT_TIME]
      for i in range(NUM_LEDS):
         data.append(i)

         data.append(2*i) # red
         data.append(255-2*i) # green
         data.append(255 if i==pos else 0) # blue

      sock.sendto(bytes(data), API_ENDPOINT)
      pos = (pos  + 1) % NUM_LEDS

**Update** Das Projekt wurde auch im `Labor-Wiki <https://wiki.das-labor.org/w/Projekt/WLampe>`_ 
hinterlegt. Weitere Aktualisierungen werden also vermutlich eher dort zu finden sein.
