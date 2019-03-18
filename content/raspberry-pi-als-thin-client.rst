Raspberry Pi als Thin Client
############################
:date: 2017-10-27 16:05
:author: marco.bakera
:tags: Hardware, Informatik, Linux
:slug: raspberry-pi-als-thin-client
:status: published

Ich überlege derzeit, RaspberryPis als ThinClient für die Einrichtung
eines Rechnerraumes zu nutzen. Diese sollen sich dann auf einen
Linux-Server verbinden und Standard-Anwendungen wie Browser, Office,
Python-Umgebung etc. ausführen.

Als Lösung habe ich an `x2go <http://x2go.org/>`__ für Client und Server
gedacht, welches auch mit geringen Bandbreiten auskommt und evt. sogar
eine Nutzung von zu Hause möglich machen könnte.

Die Raspi-Distribution `RPiTC <https://rpitc.blogspot.de/>`__ (für
Raspberry Pi Thin Client) sieht vielversprechend aus und funktioniert in
ersten Tests solide.

Habt ihr schon Erfahrungen mit einem solchen Setup gemacht oder könnt
Quellen angeben, die mir bei den ersten Schritten helfen? Dann schreibt
es bitte in den Kommentar oder antwortet mir `bei
Twitter <https://twitter.com/pintman/status/923913857197801472>`__.

Kommentare
----------

    Zum Booten wird wohl immer noch eine SD-Karte nötig sein.
    Bei uns an der Schule läuft die Linuxmusterlösung ziemlich unkompliziert.

    Schöne Grüße
    Sebastian

`Sebastian <http://www.informaticana.de/>`_ 27.10.2017


    Das ist richtig, obwohl der Pi auch schon netzbootfähig ist. Ich vermute, dass
    die Linuxmusterlösung einen FatClient voraussetzt. Die Lösung wollte ich mir
    aber auch einmal anschauen.

`Marco Bakera <https://www.bakera.de>`_ 29.10.2017
 
