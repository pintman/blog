Dektop Publishing 2019
======================
:date: 2019-04-17 12:20
:author: marco.bakera
:tags: 
:status: draft
:slug: dtp2019

.. image:: {static}images/2019/groff_latex.png
   :alt: Bücher

Eigentlich wollte ich nur einen schönen Text erstellen - genauer: gestalten. Ein Skript mit 
Abbildungen und Grafiken zu einem Thema. So, dass den Text ausdrucken und in Form eines kleines 
Buches verteilen kann. Doch womit - also mit welcher Software - macht man das heutzutage 
eigentlich? Mit InDesign (kommerziell), 
LaTeX (kompliziert), Scribus (mir noch ungekannt), groff (vielleicht zu unflexibel), 
LibreOffice/Word (fühlt sich falsch an)? Ich habe mir die verschiedenen
Programme mal angeschaut und resümiere hier etwas.

InDesign
--------
Das Programm scheint so eine Art Goldstandard in der Magazinwelt zu sein. Das will man haben, 
wenn man 
professionell Magazine erstellt. Bis zur vorletzten Ausgabe #97 wurde auch die `Datenschleuder 
<http://ds.ccc.de/>`_ des CCC 
damit erstellt. Leider steht aber auch ein hohes Preisschild an der Software, welches ich nicht 
zahlen wollte. Selbst steinalte Versionen kosten bei Ebay immer noch um die 100 €.

Scribus
-------
Hinter `Scribus <https://www.scribus.net/>`_ verbirgt sich der ambitionierte Versuch, eine 
OpenSource-Variante von InDesign zur Verfügung zu stellen. Das Programm kann eine ganze Menge 
und fühlt sich genügend kompliziert an, als dass es viele Möglichkeiten bietet, die ich 
vielleicht noch gar nicht kenne. Alles scheint irgendwie möglich zu sein - wenn auch manchmal 
auf umständlichen Wegen. Dynamische Inhalte wie Inhaltsverzeichnisse oder Kopfzeilen, die 
sich an aktuellen Abschnitten orientieren, klappen nur umständlich oder gar nicht.
Die Software ist aber gut abgehangen und hat eine aktive Community. Die 
produzierten PDFs haben die richtigen Farbprofile, die eine Druckerei so haben möchte. Ein 
schönes Stück Software, das mehr Unterstützung gebrauchen könnte.

groff
-----
So viel möchte ich über dieses steinalte (und damit ist eine durchaus positive Wertung verbunden)
Tool hier gar nicht schreiben. Ich habe einen 
ausführlichen Artikel darüber geschrieben, der demnächst in der XXX erscheinen wird. Für 
technische Berichte ist das Tool gut geeignet: immerhin ist es auch für die Generierung von man
pages unter Linux verantwortlich; Textsatz und der Umgang mit Abbildungen ist aber definitiv
nicht seine Stärke. 

LaTeX
-----
Achja, das gute alte LaTeX. Viele Textmacros, eine kryptische Syntax, die auf deutschen
Tastaturlayouts nicht so richtig ins motorische Gedächtnis wechseln will und irgendwie
ist selbst einfaches kompliziert. Aber dafür habe 
ich reinen Text, eine gute Unterstützung für die Arbeit mit mehreren Leuten und viele Pakete, die
versprechen, jeden Wunsch zu erfüllen. Ja, es gibt viele Pakete. Und auch viele Dateien. 
Und irgendwie ist alles viel und groß.
Die Installation verschlingt gigantische 4 GB. Ganz schön viel für ein Programm, das
hauptsächlich Text produzieren möchte. Und jedes Paket hat seine eigene Dokumentation. Mit 
``texdoc PAKETNAME`` findet man die Dokumentation zu einem Paket - wenn man Glück hat. Alternativ
hilft ein Blick auf `CTAN <https://www.ctan.org/>`_ (Comprehensive TeX Archive Network). Dort 
findet man eigentlich immer die 
richtigen Dokumente. Und Dokumentation gibt es eine Menge: KOMAScript ist eine Art Ersatz
für die gewohnte Klassen für article, book, etc. Alleine diese Dokumentation umfasst über 500 
Seiten, die gelesen werden soll.
So richtig schick sehen die Dokumente damit am Ende aber nicht aus. Das Schriftbild ist 
toll und vieles sieht zunächst gut aus. Man merkt aber schnell, dass LaTeX für die 
Konzeption von längeren Fließtexten und rechteckige Layouts erstellt wurde. Gerade das 
Umfließen von Text um Bilder ist nicht seine Stärke und nur mit Klimmzügen möglich.

LibreOffice und Word
--------------------
Ein einfacher Wordprocessor wie LibreOffice-Writer oder Word (welches aber direkt ausscheidet,
da ich Plattformunabhängigkeit mag) kann doch sicher auch schon eine 
ganze Menge. Und ja, das stimmt schon. 
Mit Writer sieht ein solches Dokument durchaus schick aus. Man kann viel machen und 
einfache Layouts gehen leicht von der Hand. Bei der Positionierung von Abbildungen merkt man 
dann aber doch, dass sich Writer an Zeilen, Zeichen oder Absätzen orientieren mag und nicht so 
gut mit der freien Platzieung von Grafiken harmoniert.

Fazit
-----
Mein Fazit: Viele Wege führen nach Rom und alle sind leider steinig. Eine richtig überzeugende 
Lösung konnte ich leider nicht finden. Scribus ist ein würdiges Werkzeug für schönes und
unkonventionelles Layout und ist sicher einen Blick wert. LaTeX ist auf der anderen Seite das 
zuverlässige Pferd im Stall, das häufig muckt, am Ende aber doch zuverlässig abliefert.

