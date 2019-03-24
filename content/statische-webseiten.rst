Statische Webseiten bei gitlab und github
=========================================
:date: 2018-07-12 22:21
:author: marco.bakera
:tags: bloggen
:status: published
:slug: statische-webseiten-gitlab-github

.. image:: {filename}images/2018/07/machinepipe.jpg
   :alt: Maschine Pipe (https://openclipart.org/detail/300339/machine-pipe)

Webseiten gibt es viele. Das Internet ist voll davon. 
Doch, wie kann man einfach und schnell eine eigene Webseite 
aufsetzen und betreiben? Verschiedene Hoster bieten Pakete an, doch in
vielen Situationen sind selbst diese meist kleinen Pakete nicht nötig.
	
Bei gitlab und github gibt es unter den Stichwörtern *github pages* bzw. 
*gitlab pages* die Möglichkeit, schnell und einfach eine statische 
Webseite zu hosten. Für Webseiten mit rein informatorischem
Anspruch ist das vollkommen ausreichend.

Einrichten
----------

**Gitlab pages** lassen sich auf der Webseite in den Projekteinstellungen 
konfigurieren. Hierfür
wird ein Script benötigt, das automatisch bei jedem Push auf den Server
ausgeführt wird und die Webseite erzeugt. Dadurch ist das System recht flexibel
und es gibt eine Reihe von statischen Webseiten-Generatoren, die unterstützt 
werden. Das folgende Skript zeigt ein Beispiel für den Generator 
`pelican <https://blog.getpelican.com/>`_.

.. code:: yaml

  image: python:3-alpine

  pages:
    script:
    - pip install pelican markdown typogrify
    - pelican -o public -s publishconf.py
  
    artifacts:
      paths:
      - public/

Weitere Beispiele für andere Generatoren werden in einem 
`eigenen Repository <https://gitlab.com/pages>`_ von gitlab selbst gesammelt.

Bei **github pages** dagegen muss die generierte Seite in Form von 
HTML-Seiten direkt im Repo liegen - entweder in
einem speziellen Verzeichnis oder einem gesonderten Branch. In den Repo-
Einstellungen kann zwischen verschiedenen Varianten gewählt werden.

Sowohl bei github als auch bei gitlab muss man sich nach den Einstellungen 
einige Minuten gedulden bis das Ergebnis online erscheint.

Eigene Domain
-------------

Die Webseiten werden bei gitlab und github als Subdomain unterhalb einer Domain 
von ``github.io`` bzw. ``gitlab.io`` publiziert.
Eine eigene Domain kann bei beiden Anbietern jedoch einfach und
kostenlos hinzugefügt werden. Hierfür muss im eigenen DNS ein CNAME-Eintrag
für eine Subdomain hinzugefügt werden, der auf ``benutzername.github.io`` bzw.
``benutzername.gitlab.io`` zeigt.  Für Gruppen bzw. Projekte müssen diese URLs
entsprechend angepasst werden.

Bei github wird eine Datei ``CNAME`` im Wurzelverzeichnis der Webseite 
angelegt. Die Datei enthält lediglich den Namen der Domain.

HTTPS
-----

Die Unterstützung von TLS/HTTPS bei **Gitlab pages** ist leider nicht so gut
ausgebaut. Ich muss das Zertifikat selbst erstellen und auf der  Projektseite in den
Einstellungen in ein Textfeld kopieren. Da die  Zertifikate von Lets Encrypt nur
wenige Monate halten, muss dieses  Prozedere regelmäßig wiederholt werden. Bei
Zertifikaten, die ein Jahr gültig sind, mag dies noch zumutbar sein. Bei kürzeren
Laufzeiten ist es jedoch ein zusätzlicher Aufwand, der nicht sein muss. Es gibt
Bestrebungen dies zu ändern und ich hoffe, dass auch gitlab bald automatische
Zertifikate von Lets Encrypt anbietet.

**Github pages** hat hier eine bessere Unterstützung. TLS-Zertifikate werden
regelmäßig automatisch erneuert und man muss sich nach der Einrichtung nicht mehr
darum kümmern.

Datenschutz
-----------

Ein Wermutstropfen bleibt bei gitlab wie auch github: Beide Anbieter haben
ihren Sitz nicht in Deutschland und sind damit auch nicht dem deutschen
Datenschutz unterstellt. Ob sich mit der DSGVO diesbzgl. etwas tut, kann ich
zum heutigen Tage noch nicht abschätzen. Als Daten fallen vermutlich nur
die IP-Adresse des Besuchers der Webseite an, da es meist keine weiteren
aktiven Komponenten auf statischen Webseiten gibt.

Wünschenswert wäre jedoch auch ein deutscher Anbieter, der als
datenschutzfreundliche Alternative auftauchen würde.

Neben dem Schutz der Daten der Nutzer, gibt es auch Unterschiede beim Schutz
der Daten in der Webseite selbst. So lässt github in dem kostenlosten Account keine
privaten Repositories zu, gitlab dagegen schon. Für nicht öffentliche Inhalte
im Blog ist gitlab also besser geeignet. Hier können nach Belieben
private Repositories angelegt werden, die nicht öffentlich einsehbar sind,
deren Webseiten jedoch schon.


Fazit
-----

Statische Webseiten, die nur Informationen anzeigen und keine Interaktion
mit dem Besucher der Seite erfordern, lassen sich TSL-gesichert derzeit
nur auf github praktikabel umsetzen. Sobald gitlab automatische Zertifikate
anbietet liegt der Anbieter vorn, da der Mechanismus, die Webseite über 
CI-Skripte zu generieren, einen ganz eigenen Reiz besitzt und das Repository
mit diesem Ansatz insgesamt schlanker bleibt.
