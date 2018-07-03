Eine emotionale Datenreise durch die SMS vom 11. September 2001
###############################################################
:date: 2014-03-25 14:19
:author: marco.bakera
:category: Datenbank
:slug: eine-emotionale-datenreise-durch-die-sms-vom-9-september-2001
:status: published

Wikileaks hat vor einigen Jahren die SMS
`veröffentlicht <https://911.wikileaks.org/>`__, die während des
Anschlages auf das World Trace Center am 11. September 2001 verschickt
wurden. Ich habe mir die Daten etwas genauer angeschaut.

Zunächst habe ich mir die Rohdaten heruntergeladen. Es gibt eine
`Datei <http://file.wikileaks.org/file/9-11_all_messages.7z>`__, die
alle Nachrichten in einer überschaubar großen Textdatei enthält. Nach
dem Auspacken landet eine Datei mit dem nüchternen Namen
"messages\_all.txt" auf meinem Rechner. Ein Blick in die Datei verrät
schnell ihren Aufbau. Die einzelnen Felder wie Datum und Uhrzeit sind
durch Leerzeichen voneinander getrennt. Es gibt seltsame Codes und den
eigentlichen Text der Nachricht.

Zunächst müssen die Daten etwas aufbereitet werden, um eine saubere
CSV-Datei zu erhalten, die ich in eine Datenbank importieren kann.
Zuerst habe ich die Datei nach einem Zeichen durchsucht,  das überhaupt
nicht in der Datei enthalten ist. Dieses Zeichen kann ich dann als
Feldtrenner verwenden. Bei '§' wurde ich fündig. Dies soll mein
Feldtrenner werden. Mit einem kleinen Script, das ich an sed verfüttere,
sollte eine CSV-Datei entstehen, die ich in
`sqlite <http://www.sqlite.org>`__ einlesen kann.

::

    s/  */§/ # Leerzeichen im vorderen Bereich entfernen
    s/  */§/
    s/  */§/ 
    s/  */§/
    s/  */§/
    s/  */§/
    s/\[// # Eckige Klammern entfernen
    s/\]// # 
    s/"//g # " wird beim Import in sqlite falsch interpretiert

Anschließend kann ich sqlite öffnen. Ich erstelle zuerst eine Tabelle
für meine Daten.

::

    CREATE TABLE msgs (
      datum date, 
      zeit time, 
      anbieter varchar, 
      id varchar, 
      kennung varchar, 
      kennung2 varchar, 
      text varchar);

Die Daten können nun in diese neue Tabelle importiert werden. Dazu öffne
ich sqlite und führe die beiden folgenden Befehle aus.

::

    .separator "§"
    .import messages.csv msgs

Eine erste Anfrage zeigt mir, wie viele Nachrichten verschickt wurden.
Diese Zahl stimmt mit der Anzahl der Zeilen aus der Textdatei überein,
die ich mit "wc -l messages\_all.txt" erhalte - es scheint also geklappt
zu haben.

::

    SELECT COUNT(*) FROM msgs;
    count(*)  
    ----------
    448358

448358 Nachrichten. 448358 Geschichten. 448358 Schicksale. Ein Blick
durch die Textdatei verrät, dass sich dort sowohl ganz persönliche
Schicksale wiederfinden als auch Computer, die in regelmäßigen Abständen
Fehlerberichte an ihre Administratoren verschicken. Auch die
Einsatzkräfte vor Ort kommunizieren auf diesem Wege.

Ich erstelle mir ein kleines Bash-Skript, mit dessen Hilfe ich meine
Anfragen schnell mittels `gnuplot <http://www.gnuplot.info/>`__
visualisieren kann.

::

    #!/bin/bash

    SQL=$1
    CSVFILE=/tmp/gnuplot.csv

    # Mit tail -n +3 wird die Ausgabe erst ab der dritten Zeile in die Datei umgeleitet
    # sqlite beginnt mit einer leeren Zeile und gibt dann die header aus
    sqlite3 -csv messages_all.sqlite "${SQL}" |tail -n +3 > $CSVFILE

    gnuplot -p -e "set datafile separator \",\";plot [] [0:] \"$CSVFILE\""

Ich kann dem Skript einen SQL-Befehl übergeben. Die Ausgabe wird als
CSV-Datei abgespeichert und von gnuplot anschließend visualisiert.

Ich möchte mir zunächst einen Überblick über die Verteilung der Anzahl
der SMS über den Tag verschaffen, setze den folgenden SQL-Befehl ab und
erhalte das folgende Bild.

::

    -- Abfragen über den zeitlichen Verlauf mit Dezimalzeiten
    select strftime('%H',zeit)+strftime('%M',zeit)/60.0 zeit2, count(*) anzahl 
    from msgs 
    group by datum, zeit2

|Anzahl SMS nach Uhrzeit|

Ab kurz vor 9 gibt es einen starken Anstieg als das erste Flugzeug in
den ersten Turm fliegt. Die Anzahl der verschickten SMS vervierfacht
sich plötzlich. Ich versuche, die Anfrage abzuwandeln und bin nun nur
noch an Nachrichten interessiert, deren Text das Wort "plane" enthält.
Ich erhalte das folgende Ergebnis.

::

    select 
      strftime('%H',zeit)+strftime('%M',zeit)/60.0 zeit2, 
      count(*) anzahl 
    from msgs 
    where text like '%plane%' 
    group by datum, zeit2

|SMS mit Text plane|

Das Bild zeigt auch hier einen erkennbaren Anstieg der Anzahl der SMS.
Ich probiere weitere Einschränkungen aus - emotionale Schlüsselwörter
wie 'love', 'war' und 'terror' - und werde den Eindruck nicht los, hier
doch ganz private Schicksale zu durchleuchten.

Ich bekomme ein mulmiges Gefühl und beende meine Recherche vorerst. Ich
schließe alle Fenster und lasse die SMS zunächst ruhen. Man könnte noch
tiefer recherchieren, eine Begriffswolke auf den SMS erzeugen und auf
einem Zeitstrahl abbilden. Auch andere Analysen sind denkbar: Wie lässt
sich der Absturz der Computerrechner darstellen? Wie kann die
Kommunikation der Rettungskräfte visualisiert werden?

Eines habe ich bei meinem Projekt gelernt: Die Daten erzählen ihre ganz
eigene Geschichte - vielleicht hat sie sogar etwas mit der Realität zu
tun. Vielleicht aber auch nicht. Und: Daten haben etwas mit Menschen zu
tun. Daher müssen wir sie schützen, auf sie aufpassen und sorgsam mit
ihnen umgehen.

.. |Anzahl SMS nach Uhrzeit| image:: http://bakera.de/wp/wp-content/uploads/2014/03/Anzahl-SMS-nach-Uhrzeit.png
   :class: alignnone size-full wp-image-869
   :width: 640px
   :height: 480px
   :target: http://bakera.de/wp/wp-content/uploads/2014/03/Anzahl-SMS-nach-Uhrzeit.png
.. |SMS mit Text plane| image:: http://bakera.de/wp/wp-content/uploads/2014/03/SMS-mit-Text-plane.png
   :class: alignnone size-full wp-image-871
   :width: 640px
   :height: 480px
   :target: http://bakera.de/wp/wp-content/uploads/2014/03/SMS-mit-Text-plane.png
