Wenn ITAs Projekte machen
=========================
:date: 2018-07-11 20:09
:author: marco.bakera
:tags: Bildung
:slug: ita-projekttage-2018
:status: published

.. figure:: {filename}images/2018/07/an_electrical_machine.jpg
   :alt: Zwei Personen hinter Maschine
   :width: 75%

   (Quelle: CC-BY 
   `Wellcome Collection <https://wellcomecollection.org/works/dazvcmnt>`_)


In der letzten Woche vor den Ferien passiert in Schulen meiste recht wenig
im Unterricht. Was nicht heißen soll, dass es nicht noch genug zu tun
gibt: Zeugnisse erstellen, Räume einrichten etc.

Wir haben diese letzte Woche genutzt und zwei Tage mit den ITAs
(Informationstechnische Assistentinnen und Assistenten) gemeinsam an 
verschiedenen Projekten gearbeitet. Die Schüler konnten wählen,
ob sie an einem Mini-Game-Jam teilnehmen und ein kleines Spiel programmieren
oder, ob sie ein eigenes Hardware- oder Softwareprojekt umsetzen wollen.

.. image:: {filename}/images/2018/07/small_game-jam-themen.jpg
   :target: {filename}/images/2018/07/game-jam-themen.jpg
   :alt: Themen für den Mini-Gam-Jam

Tag 1
-----

Zu Beginn haben sich die Schüler in einem kleinen Spiel gegenseitig erklärt,
was sie  machen wollen. So konnten erste Ideen ausgetauscht werden und
Unschlüssige haben noch Anregungen erhalten.

Die Schüler haben sich dann in kleinen Gruppen organisiert: 9 Gruppen haben
sich für den Mini-Game-Jam, 5 Gruppen für eigene Projekte entschieden. In
den Gruppen haben sie kurz wesentliche Aspekte des Projektes festgehalten:

- Projekttitel
- Kurzbeschreibung
- Das Team

Das hat einerseits geholfen, sich festzulegen und die Themenfindung nicht
zu lange hinzuziehen. Andererseite hat es uns bei der Organisation der
Vorstellungen für den zweiten Tag derart geholfen, dass wir einen Überblick
über die Projekte bekommen haben und so die Präsentationen in eine Reihenfolge
bringen konnten. 
Dann ging es an die Arbeit und die Projekte konnten umgesetzt werden. 
Zwischendurch haben wir ganz nerdig Pizza bestellt und gemeinsam gegessen.

Als Lehrerteam haben wir auch ein Projekt umgesetzt: ein lineares 1D-Pong auf
einem Steckbrett. Dazu später jedoch mehr.

Ohne Anspruch auf Vollständigkeit greife ich ein paar Projekte heraus, von denen
ich Bilder machen konnte. Diese Auswahl umfasste z.B. ein Anime-Quiz.

.. image:: {filename}/images/2018/07/small_anime-quiz.jpg
   :target: {filename}/images/2018/07/anime-quiz.jpg
   :alt: Anime Quiz

Es wurde ein Roboterarm aus einem 3D-Drucker gedruckt, der über Servo-Motoren
angesteuert wurde.

.. image:: {filename}/images/2018/07/small_roboarm.jpg
   :target: {filename}/images/2018/07/roboarm.jpg
   :alt: Roboarm

Ein Spiel wurde mit dem Game-Maker-Studio erstellt.

.. image:: {filename}/images/2018/07/small_game-maker.jpg
   :target: {filename}/images/2018/07/game-maker.jpg
   :alt: Game Maker

Eine RGB-LED leuchtete in verschiedenen Farben.

.. image:: {filename}/images/2018/07/small_rgb-led.jpg
   :target: {filename}/images/2018/07/rgb-led.jpg
   :alt: RGB LED

Und vieles andere mehr.

Tag 2
-----

Am zweiten Tag konnten die Schüler ihre Projekte im Rahmen einer Präsentation
kurz vorstellen. Es waren viele interessante und unterschiedliche Projekte
dabei. Von rudimentär und einfach bis zu über-ambitioniert. Von witzig und
erstaunlich bis schräg und seltsam. Es war eine gesunde Mischung und ich hatte
den Eindruck, dass die Schüler ein Menge Spaß an den beiden Tagen gehabt
haben.

Breadboardpong
--------------

.. image:: {filename}/images/2018/07/small_1d-pong.jpg
   :target: {filename}/images/2018/07/1d-pong.jpg
   :alt: 1D-Pong auf einem Steckbrett

Das "Lehrerteam" hat auch ein Projekt umgesetzt: *Breadboardpong*. Hierbei wandert
ein Lichtpunkt über LEDs hinweg hin und her. Durch Druck auf den
Taster im eigenen Feld mit den drei roten LED kann er an den Gegner
zurückgeschlagen werden. Wer zu spät drückt, hat verloren.

Falls jemand das 1D-Pong nachbauen möchte, so findet er oder sie in dem Archiv
`breadboardpong.zip <{filename}media/breadboardpong.zip>`_ den Quelltext für
unser Projekt. Wir haben die LEDs auf drei Steckbrettern mit Vorwiderständen
aufgebaut. An den Enden wurde jeweils ein Taster positioniert. Die LEDs hätte
man direkt über den Pi ansteuern können. Wir haben uns jedoch für den "Umweg"
entschieden, einen Port-Expander zu verwenden. So hat unser Team auch noch
etwas Neues hinzulernen können.
