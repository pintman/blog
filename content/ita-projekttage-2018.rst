Wenn ITAs Projekte machen
=========================
:date: 2018-07-11 12:20
:author: marco.bakera
:tags: ITA, Bildung
:slug: ita-projekttage-2018
:status: draft

In der letzten Woche vor den Ferien passiert in Schulen meiste recht wenig
im Unterricht. Was nicht heißen soll, dass es nicht noch genug zu tun
gibt: Zeugnisse erstellen, Räume einrichten etc.

Wir haben diese letzte Woche genutzt und zwei Tage mit den ITAs
(Informationstechnische Assistentinnen und Assistenten) gemeinsam an 
verschiedenen Projekten verbracht. Hier konnten die Schüler wählen,
ob sie an einem Mini-Game-Jam teilnehmen und ein kleines Spiel programmieren
oder, ob sie ein eigenes Hardware- oder Softwareprojekt umsetzen wollen.

.. image:: {filename}/images/2018/07/game-jam-themen.jpg
   :width: 100%
   :alt: Themen für den Mini-Gam-Jam

Tag 1
-----

Zu Beginn haben sich die Schüler in einem kleinen Spiel gegenseitig erklärt,
was sie  machen wollen. So konnten erste Ideen ausgetauscht werden und
unschlüssige Schüler haben noch Anregungen erhalten.

Die Schüler haben sich dann in kleinen Gruppen organisiert: 9 Gruppen haben
sich für den Mini-Game-Jam, 5 Gruppen für eigene Projekte entschieden. In
den Gruppen haben sie kurz wesentliche Aspekte des Projektes festgehalten:

- Projekttitel
- Kurzbeschreibung
- Das Team

Das hat einerseits den Schülern geholfen, sich festzulegen und die
Themenfindung nicht zu lange hinzuziehen. Andererseite hat es uns bei der
Organisation der Vorstellungen geholfen, einen Überblick über die Projekte zu
bekommen und die Präsentationen in eine Reihenfolge bringen zu können.

Wir haben als Lehrerteam auch ein Projekt umgesetzt: ein lineares 1D-Pong auf
einem Steckbrett. Mehr dazu später.

Dann konnten die Projekte umgesetzt werden. Zwischendurch haben wir Pizza
bestellt und gemeinsam gegessen.

.. image:: {filename}/images/2018/07/anime-quiz.jpg
   :target: {filename}/images/2018/07/anime-quiz.jpg
   :width: 100%
   :alt: Anime Quiz

.. image:: {filename}/images/2018/07/roboarm.jpg
   :width: 100%
   :alt: Roboarm

.. image:: {filename}/images/2018/07/game-maker.jpg
   :width: 100%
   :alt: Game Makera

.. image:: {filename}/images/2018/07/rgb-led.jpg
   :width: 100%
   :alt: RGB LED


Tag 2
-----

Am zweiten Tag konnten die Schüler ihre Projekte vorstellen und mussten sie
schließĺich im Rahmen einer Präsentation kurz vorstellen. Es zeigten  sich
viele interessante und unterschiedliche Projekte. Von rudimentär und einfach
bis zu über-ambitioniert. Von witzung und erstaunlich bis schräg und seltsam.
Es war eine gesunde Mischung und ich hatte den Eindruck, dass die Schüler ein
Menge Spaß an den beiden Tagen gehabt haben.

1D-Pong
-------

.. image:: {filename}/images/2018/07/1d-pong.jpg
   :width: 100%
   :alt: 1D-Pong auf einem Steckbrett


Ein Lichtpunkt wandert über LEDs hinweg hin und her. Durch Druck auf den
Taster im eigenen Feld mit den drei roten LED kann er an den Gegner
zurückgeschlagen werden. Wer zu spät drückt, hat verloren.

Falls jemand das 1D-Pong nachbauen möchte, so findet er hier den Quelltext für
unser Projekt. Wir haben die LEDs auf drei Steckbrettern mit Vorwiderständen
aufgebaut. An den Enden wurde jeweils ein Taster positioniert. Die LEDs hätte
man direkt über den Pi ansteuern können. Wir haben uns jedoch für den "Umweg"
entschieden, einen Port-Expander zu verwenden. So hat unser Team auch noch
etwas Neues hinzulernen können.

.. code:: python

  import hwpong
  import time

