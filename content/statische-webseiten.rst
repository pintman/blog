Statische Webseiten
###################
:date: 2018-06-20 12:20
:author: marco.bakera
:tags: Web
:status: draft

Webseiten gibt es derer viele. Das Internet ist voll davon. Daher auch
der Name. Doch, wie kann man einfach und schnell eine eigene Webseite 
aufsetzen und betreiben? Verschiedene Hoster bieten Pakete an, doch in
manchen Situationen benötigt man sie gar nicht. 

Bei gitlab und github gibt es unter dem Stichwort "gitub pages" bzw. 
"gitlab pages" eine Möglichkeit, schnell und einfach  eine statische 
Webseite zu hosten. Für Webseiten mit rein informatorischem
Anspruch ist das vollkommen ausreichend.

Einrichten
----------

Gitlab pages lassen sich in den Projekteinstellungen konfigurieren. Hierfür
wird ein Script benötigt, das automatisch bei jedem Push auf den Server
ausgeführt wird und die Webseite erzeugt. Dadurch ist das System recht flexibel
und es gibt eine Reihe von statischen Webseiten-Generatoren, die unterstützt 
werden. Das folgende Skript zeigt ein Beispiel für den Generator ``pelican``.

.. code:: yaml

  image: python:3-alpine

  pages:
    script:
    - pip install pelican markdown typogrify
    - pelican -o public -s publishconf.py
  
    artifacts:
      paths:
      - public/


Bei github muss die generierte Seite im Repo liegen - entweder in einem
speziellen Verzeichnis oder einem gesonderten Branch. In den Repo-Einstellungen
kann zwischen verschiedenen Varianten gewählt werden.

Sowohl bei github als auch bei gitlab muss man sich nach den Einstellungen 
einige Minuten gedulden bis das Ergebnis online auftaucht.

Eigene Domain
-------------

Die Webseiten stehen bei gitlab und github unter einer eigenen Domain zur
Verfügung. Eine eigene Domain kann bei beiden Anbietern jedoch einfach
und kostenlos hinzugefügt
werden. Hierfür wird im eigenen DNS ein CNAME Eintrag hinzugefügt, der auf
``benutzername.github.io`` bzw. ``benutzername.gitlab.io`` zeigt. 
Für Gruppen bzw. Projekte müssen diese URLs entsprechend angepasst werden.

HTTPS
-----

Als erheblicher Nachteil stellte sich für mich nach ersten Versuchen die 
Tatsache heraus, dass die Unterstützung für TLS/HTTPS bei gitlab nicht 
sonderlich gut ausgebaut ist. 
Ich muss das Zertifikat selbst erstellen und auf der 
Projektseite in den Einstellungen in ein Textfeld kopieren. Da die 
Zertifikate von Lets  Encrypt nur wenige Monate halten, muss dieses 
Prozeder regelmäßig wiederholt werden. Bei kostenpflichtigen Zertifikaten,
die ein Jahr gültig sind, mag diese noch zumutbar sein. Bei kürzeren
Laufzeiten ist es jedoch ein zusätzlicher Aufwand, der nicht sein muss.
Es gibt Bestrebungen dies zu ändern und ich hoffe, dass auch gitlab bald
automatische Zertifikate von Lets' Encrypt anbietet.

Github hat hier eine bessere Unterstützung. TLS-Zertifikate werden regelmäßig
automatisch erneuert und man muss sich nach der Einrichtung nicht mehr
darum kümmern.

Fazit
-----

Statische Webseiten, die nur Informationen anzeigen und keine Interaktion
mit dem Besucher der Seite erfordern lassen sich TSL-gesichert derzeit
nur auf github praktikabel umsetzen. Sobald gitlab automatische Zertifikate
anbietet liegt der Anbieter vorn, da der Mechanismus, die Webseite über 
CI-Skripte zu generieren einen ganz eigenen Reiz besitzt.

