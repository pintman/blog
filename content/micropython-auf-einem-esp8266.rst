Micropython auf einem ESP8266
#############################
:date: 2016-08-25 15:44
:author: marco.bakera
:tags: Hardware, Informatik, Programmierung, Python
:tags: ESP8266, Python
:slug: micropython-auf-einem-esp8266
:status: published

|esp8266|

Hinter `Micropython <https://micropython.org>`__ verbirgt sich eine
Variante von Python, die auf Mikrocontroller zugeschnitten ist. Der
`ESP8266 <http://www.mikrocontroller.net/articles/ESP8266>`__ ist ein
recht günstiger (~4$) Baustein mit WLAN-Funktionen, für den jetzt eine
Micropython-Firmware erschienen ist. Über das Development-Kit, das auf
dem Bild zu sehen ist, verfügt der Baustein über einen USB-Anschluss,
über den man mit dem Chip kommunizieren kann. Die PINs sind
herausgeführt und lassen sich in Schaltungen verwenden.

Nun soll die Firmware für Micropython installiert werden. Diese lässt
sich von der Webseite
`herunterladen <https://micropython.org/download/#esp8266>`__. Für die
Installation gibt es das Tool esptool.py, das sich ebenso einfach
installieren lässt.

::

    $ sudo pip2 install esptool

Leider funktioniert esptool derzeit nur mit Python2.

Anschließend kann die vorhandene Firmware auf den ESP8266 zunächst
gelöscht und mit dem zweiten Befehl die neue Firmware übertragen werden.

::

    $ esptool.py --port /dev/ttyUSB0 erase_flash
    $ esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash --flash_size=8m 0 esp8266-20160825-v1.8.3-49-ga589fa3.bin

Bei mir kam es bei Geschwindigkeiten über 115200 Baud zu Probleme,
weshalb ich die Geschwindigkeit reduziert habe. Die Befehle habe ich der
`Anleitung <http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html#deploying-the-firmware>`__
von mircopython entnommen.

Nun kann mit einem Terminalprogramm auf den Microcontroller zugegriffen
werden. Das geht mit Putty, minicom oder auch miniterm.py.

::

    $ miniterm.py /dev/ttyUSB0 115200

Sollte miniterm.py noch nicht installiert sein, so kann es mit "pip
install pyserial" nachinstalliert werden.

Im Anschluss erhält man eine Python-Konsole, die man für eigene Projekte
verwenden kann. Beim Start steht der ESP als Access Point zur Verfügung,
auf den sich Clients mit dem Standardpasswort 'micropythoN' verbinden
können. Für den Dateitransfer kann dann das Kommandozeilentool
`webrepl\_cli.py <https://github.com/micropython/webrepl>`__ verwendet
werden.

Anlagen
'''''''

-  Firmware:
   `esp8266-20160825-v1.8.3-49-ga589fa3.bin <media/esp8266-20160825-v1.8.3-49-ga589fa3.bin_.zip>`__
-  Vortrag der Froscon 2016: `Python für das Internet der Dinge -
   Einführung in MicroPython für ESP8266 und Cortex-M4
   Mikroprozessorboards <https://media.ccc.de/v/froscon2016-1791-python_fur_das_internet_der_dinge>`__
-  `mpfshell <https://github.com/wendlers/mpfshell>`__ ist eine
   shell-basierter Datei-Explorer, um den ESP zu erkunden.
-  `rshell <https://github.com/dhylands/rshell>`__ ist eine remote shell
   für den ESP8266
-  `ampy <https://github.com/adafruit/ampy>`__ ist ein von adafruit
   entwickelt kleines Skript-Tool für den Dateitransfer und die
   Ausführung von Skripten.
-  Unter Windows werden eventuell Treiber für den USB-UART-Konverter
   benötigt. Ein populärer Treiber ist unter
   `MSXFAQ <http://www.msxfaq.de/sonst/bastelbude/nodemcu.htm>`__
   verlinkt.

.. |esp8266| image:: https://www.bakera.de/wp/wp-content/uploads/2016/08/esp8266.jpeg
   :class: alignnone size-full wp-image-1986
   :width: 1280px
   :height: 719px
