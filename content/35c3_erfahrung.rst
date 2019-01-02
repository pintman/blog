35C3 - ein Erfahrungsbericht
============================
:date: 2019-01-02 12:20
:author: marco.bakera
:tags: 35c3, sdr, ctf, lernen
:status: published

.. image:: {filename}images/2019/35C3Logo.svg
   :alt: Logo des 35C3

Der letzte Kongress des 35C3 stand unter dem Motto *refreshing memories* und 
fand am Ende des Jahres wie gewohnt 
zwischen dem 27.12. und dem 30.12. in Leipzig statt.
Da es Vieles zu entdecken gab, hat jeder Teilnehmer sicher seinen
eigenen Kongress erlebt. Ich versuche einmal, ein paar für mich relevante Highlights
herauszugreifen.

Vor Ort hat ein kleines CTF auf Basis von  *Software Defined Radio (SDR)*
stattgefunden: 
die `SDR-Challenge <https://sdr-challenge.muc.ccc.de>`_. Es war mein erster
intensiverer Kontakt mit SDR überhaupt. Hierbei geht es darum,
Radiosignale zu empfangen und zu dekodieren. Mit alten DVBT-Sticks klappt
das erstaunlich gut und vor allem günstig. Für 10 € konnte ich einen solchen
Empfänger erwerben/leihen und erste Versuche unternehmen. Das Programm
`gqrx <http://gqrx.dk/>`_ visualisiert die Signale und kann auch für das Speichern
genutzt werden. Diese Aufzeichnungen können dann z.B. mit 
`inspectrum <https://github.com/miek/inspectrum>`_ betrachtet und analysiert.
Ich war erstaunt, wie groß diese Dateien werden können - 1GB pro Minute sind keine
Seltenheit. Da jedoch das gesamte empfangene Spektrum aufgezeichnet wird, ist
die Dateigröße wiederum erklärbar. Weitere Programme wie gnuradio habe ich 
leider nicht zum Laufen gebracht und daher auch nicht getestet - unter ArchLinux 
hat eine alte Qt4-Bibliothek gefehlt. Der Vortrag
`Digital Airwaves <https://media.ccc.de/v/35c3-9508-digital_airwaves>`_ hat
theoretische Grundlagen geliefert - mich jedoch auch recht schnell inhaltlich
abgehängt. Ich werde mir die Aufzeichnnung noch einmal in Ruhe anschauen müssen.

Als die Tools schließlich liefen, konnte ich auf einigen Frequenzen Piepsignale, 
Radiosignale oder
einen kurzen Puls auf einem breiten Spektrum entdecken. Leider sind wir mit einer
kleinen Gruppe - darunter sogar ein Amateurfunker - jedoch nicht so weit gekommen, 
wie erhofft. Die Piepsignale konnten
wir zwar als Morsecode dekodieren, sind jedoch auf eine Zufallsfolge ohne Wiederholung
gestoßen. BTW, Morsecode ist verdammt schwierig. Daher hoffe ich auf ein Write-Up
zu den Aufgaben.

Eine weitere interessante Neuigkeit, die ich mitnehme, ist das Programm
`Anki <https://apps.ankiweb.net/>`_ - verfügbar für Windows, Linux, Mac, Android
und iOS. Anki will Lerner_innen beim Lernen unterstützen. 
Es nutzt dafür Karteikarten, die als Lückentext
oder klassisch mit einer Vorder- und Rückseite präsentiert werden. Ich werde das mal
mit Lückenquelltext ausprobieren. Im Selbstversuch fühlte es sich bereits recht
gut an. Leider kam die dafür angesetze Session nicht zum angesagten Zeitpunkt
zustande und musste verschoben werden. Gut hingegen war,
dass sich eine Medizinstudentin, die das Programm schon länger nutzt und sich
weitere Tipps erfhoffte, spontant bereit erklärte, einer kleinen Gruppe Anfänger
die Grundlagen zu erklären.

Auch in diesem Jahr habe ich mich wieder als Engel angemeldet und diesmal die 
`Untertitelung <https://wiki.c3subtitles.de/de:start>`_ genauer angeschaut. 
Es ist eine sehr ruhige und konzentrierte
Engelarbeit. Die Texte der Talks werden automatisch vorbereitet und stehen in 
einem Etherpad zur Verfügung. Meine Aufgabe war es nun, diese Texte zu korrigieren
und gegenzulesen. Ich war erstaunt, wie wenig ich in der Zeit geschafft habe. So 
war ich gerade bei Minute 8:40 eines Talks als meine 1-Stundenschicht zu Ende ging.

Nun werde ich mir noch viele der Talks anschauen, die glücklicherweise aufgezeichnet
wurden und bei `media.ccc.de <https://media.ccc.de/c/35c3>`_ abgerufen werden können.
Ich freue mich jetzt schon auf den nächsten Kongress.
