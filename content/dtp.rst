Dektop Publishing im Jahr 2019
==============================
:date: 2019-04-25 19:30
:author: marco.bakera
:tags: dtp, pdf, software
:status: published
:slug: dtp2019

.. figure:: {static}images/2019/groff_latex.png
   :alt: Bücher

   Zwei Standardwerke zu LaTeX und groff

Eigentlich wollte ich nur einen schönen Text erstellen, oder genauer: gestalten. Ein Skript mit 
Abbildungen und Grafiken zu einem Thema. So, dass man den Text ausdrucken und in Form eines kleines 
Buches verteilen kann. Doch womit macht man das heutzutage eigentlich - also 
mit welcher Software? Mit InDesign bzw. QuarkXPress (kommerziell), 
LaTeX (kompliziert), Scribus (mir noch ungekannt), groff (vielleicht zu unflexibel), 
LibreOffice/Word (fühlt sich falsch an)? Ich habe mir die verschiedenen
Programme mal angeschaut und resümiere hier etwas.

InDesign und QuarkXPress
------------------------
Das Programm InDesign scheint so eine Art Goldstandard in der Magazinwelt zu 
sein. Das will man haben, wenn man professionell Magazine erstellt. Viele Ausgaben der 
`Datenschleuder <http://ds.ccc.de/>`_ des CCC wurden sogar damit erstellt. Leider steht aber auch ein
hohes Preisschild an der Software, welches ich nicht zahlen wollte. Selbst steinalte 
Versionen kosten bei Ebay gebraucht immer noch mehrere Hundert Euro. Bei neuen Versionen ist 
ein Abo in der CreativeCloud von Adobe nötig. Zudem werden leider nur 
Nischen-Betriebssysteme wie Windows oder MacOS unterstützt.

Eine ähnliche Verbreitung hat QuarkXPress in der professionellen Welt. Wer Adobe nicht nutzt
oder andere Gründe vorweisen kann, wird QuarkXPress für seine Dienste nutzen. Ich habe keine 
Erfahrungen damit und weiß nur, dass es seit 1987(!) regelmäßig neue Versionen gibt und diese 
zu fürstlichen Preisen um 800 € (bei Aktionen für 400 €) verkauft werden. 
Sympathisch wird die Software durch die Slogans "cloud-frei" oder 
"Lebenslange Lizenz - Kein Abonnement", die eindeutig gegen InDesign sticheln.

Scribus
-------
Hinter `Scribus <https://www.scribus.net/>`_ verbirgt sich der ambitionierte 
und begrüßenswerte Versuch, eine 
OpenSource-Variante von InDesign zu erstellen. Das Programm kann eine ganze Menge 
und fühlt sich genügend kompliziert an, als dass es viele Möglichkeiten bietet, die ich 
bei meinen ersten Gehversuchen vielleicht noch nicht kennengelernt habe.

Alles scheint irgendwie möglich zu sein - wenn auch manchmal 
auf umständlichen Wegen. Dynamische Inhalte wie Inhaltsverzeichnisse oder Kopfzeilen, die 
sich an aktuellen Abschnitten orientieren, lassen sich nur umständlich oder gar nicht realisieren.
Die Software ist jedoch gut abgehangen und wird von einer aktiven Community getragen. Die 
produzierten PDFs haben die richtigen Farbprofile, die eine Druckerei so haben möchte. Insgesamt
also ein schönes Stück Software, das mehr Unterstützung gebrauchen könnte.

groff
-----
So viel möchte ich über dieses steinalte Tool (und damit ist eine durchaus positive Wertung 
verbunden) hier gar nicht schreiben. Ich habe einen  ausführlichen Artikel darüber geschrieben, 
der demnächst an andere Stelle erscheinen wird. Für diesen Artikel sei aber schon so viel verraten: für 
technische Berichte ist das Tool mehr als gut geeignet - immerhin ist es auch für die 
Generierung von man pages unter Linux verantwortlich. Textsatz, der Umgang mit Abbildungen 
oder ein variabler Textfluss um Abbildungen herum sind definitiv nicht seine Stärken.

LaTeX
-----
Ach ja, das gute alte LaTeX. Viele Textmakros, eine kryptische Syntax, die sich auf deutschen
Tastaturlayouts vehement weigert, ins motorische Gedächtnis gebrannt zu werden und irgendwie
ist selbst Einfaches viel zu kompliziert. Aber dafür habe 
ich reinen Text, eine gute Unterstützung für die Arbeit mit mehreren Leuten und viele Pakete, die
versprechen, jeden Wunsch zu erfüllen. Ja, es gibt viele Pakete. Und auch viele Dateien. 
Und irgendwie ist alles viel und groß.

Die Installation verschlingt gigantische 4 GB. Ganz schön viel für ein 
Programm, das hauptsächlich Text produzieren möchte. Und jedes Paket hat seine
eigene Dokumentation. Mit ``texdoc PAKETNAME`` findet man diese - wenn man 
Glück hat. Wenn nicht, hilft ein Blick auf `CTAN <https://www.ctan.org/>`_ 
(Comprehensive TeX Archive Network). Dort versammelt sich ein Berg von 
umfänglichen Dokumenten. Und davon gibt es wahrlich eine Menge, z.B. zu 
`KOMAScript <https://www.ctan.org/pkg/koma-script>`_. Das ist eine 
Art Ersatz für die gewohnten LaTeX-Klassen ``article, book``, etc. Alleine diese 
Dokumentation umfasst über 500 Seiten, die gelesen werden wollen. Ein weiteres
Beispiel ist das Paket `inputenc <https://www.ctan.org/pkg/inputenc>`_, welches
verspricht, dass man auch UTF8-Zeichen wie deutsche Umlaute eingeben darf. Wieder 
45 Seiten, die dieses eigentlich selbstverständliche Detail erklären.

So richtig schick sehen die Dokumente damit am Ende aber nicht aus. Das Schriftbild ist 
toll und vieles sieht zunächst gut aus. Man merkt aber schnell, dass LaTeX für die 
Konzeption von längeren Fließtexten und rechteckigen Layouts erstellt wurde. Gerade das 
Umfließen von Text um Bilder ist nicht seine Stärke und nur mit `Klimmzügen
<https://www.ctan.org/topic/text-flow>`_ möglich.

LibreOffice und Word
--------------------
Ein einfacher Wordprocessor wie LibreOffice-Writer oder Word (welches aber direkt ausscheidet,
da ich Plattformunabhängigkeit mag) kann doch sicher auch schon eine 
ganze Menge. Und ja, das stimmt schon. 
Mit Writer sieht ein solches Dokument durchaus schick aus. Man kann viel machen und 
einfache Layouts gehen leicht von der Hand. Bei der Positionierung von Abbildungen merkt man 
dann aber doch, dass sich Writer an Zeilen, Zeichen oder Absätzen orientieren mag und nicht so 
gut mit der freien Platzierung von Grafiken harmoniert.

Gefrickel
---------
Als etwas frickelige Lösung bietet sich ein Stückwerk an, in dem ein Dokument aus 
Einzelseiten zusammensetzt wird. Jede Einzelseite wird mit dem Programm der Wahl erstellt
und das Gesamtdokument wird zum Schluss durch Aneinanderhängen der Einzelseiten 
konstruiert. Das Aneinanderhängen kann leicht mit `pdftk 
<https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/>`_ realisiert werden.

Man kann das Dokument noch etwas einheitlicher gestalten, indem zuvor eine Art
Musterdokument erstellt wird, das wie eine Folie über alle Seiten gelegt wird.
Dieses kann z.B. Seitennummern oder ein Logo enthalten Mit der Operation `multistamp
<https://manpages.debian.org/stretch/pdftk/pdftk.1.en.html>`_ von ``pdftk`` kann 
das Musterdokument am Ende auf die Einzelseiten gepresst werden [1]_.

In Kombination mit Scribus und dem Einfügen von PDF-Seiten als "Bild-Objekte" können
auch interessante Gestaltungskonzepte umgesetzt werden, die mehr als zwei Ebenen 
zulassen.

Mein Fazit
----------
Viele Wege führen nach Rom und leider sind alle steinig. Alle Lösungen haben
ihre Berechtigung und damit Vor- und Nachteile. Eine in allem überzeugende 
Lösung konnte ich daher leider nicht finden. Scribus ist ein würdiges Werkzeug für schönes,
unkonventionelles Layout und ist sicher einen Blick wert. LaTeX ist auf der anderen Seite das 
zuverlässige Pferd im Stall, das häufig muckt, am Ende aber doch konsequent abliefert.

----

.. [1] Eine mögliche Anwendung von pdftk: 

   ``pdftk a.pdf b.pdf cat output out.pdf`` 

   Dann kann die Musterseite aufgedruckt werden: 
   
   ``pdftk out.pdf multistamp muster.pdf output final.pdf``.
