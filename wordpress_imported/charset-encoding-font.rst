Charset - Encoding - Font
#########################
:date: 2017-12-09 10:46
:author: marco.bakera
:category: Informatik, Video
:slug: charset-encoding-font
:status: published

Immer wieder komme ich mit den Begrifflichkeiten Zeichensatz
(Characterset), Zeichkodierung (Encoding) und Schriftart (Font)
durcheinander. Damit scheine ich nicht alleine zu sein. Das Chaosseminar
Ulm hat daher einen
`Vortrag <https://ulm.ccc.de/ChaosSeminar/2016/10_charset-encoding-font>`__
mit dem gleichen Titel veröffentlicht, der die Begrifft erklärt.

-  *Font*: Schriftzeichen, die auf einem Bildschirm oder Papier
   ausgegeben werden - "das, was man sieht". Es werden Bitmap- und
   Proportionalfonts unterschieden. Erstere beschreiben die Zeichen in
   einem Pixelformat, letztere in Kurven.
-  *Characterset*: Alle Zeichen, die relevant zu sein scheinen: nur
   US-amerikanische, Chinesische, Griechische etc. Nicht alle
   Schritftarten unterstützen alle Zeichen und sind in ihrem Umfang
   unterschiedlich groß. Der umfangreichste Zeichensatz ist derzeit
   Unicode. Die Zeichen werden durchnummeriert abgelegt.
-  *Encoding*: Die Beschreibung, wie Zeichen eines Zeichensatzes im
   Rechner in Form von Bitmustern abgelegt werden. Solange maximal ein
   Byte benutzt wird, entspricht die Kodierung genau der Interpretation
   als Ganzzahl in der Zeichentabelle. ASCII (7 Bit) und latin1 (8 Bit)
   machen dies so. Bei mehr als einem Byte pro Zeichen, können die
   Zeichen mit fester oder variabler Anzahl von Bytes kodiert werden.
   Bei fester Anzahl werden für reine ASCII-Buchstaben viele Bytes
   häufig nur mit Nullen befüllt und damit schlecht ausgenutzt. Eine
   variable Breite, wie etwa bei UTF8 genutzt, ermöglicht, ein Zeichen
   auf mehrere Bytes zu verteilen. Beginnt ein UTF8-Zeichen mit
   110xxxxx, so folgen ein oder mehrere Bytes, die mit 10yyyyyy
   beginnen. Die freien Plätze xxxxxyyyyyy zusammen ergeben damit den
   Eintrag in der Zeichentabelle.
