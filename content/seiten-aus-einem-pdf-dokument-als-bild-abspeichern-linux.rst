Seiten aus einem PDF-Dokument als Bild abspeichern
##################################################
:date: 2014-03-16 20:35
:author: marco.bakera
:tags: Linux
:slug: seiten-aus-einem-pdf-dokument-als-bild-abspeichern-linux
:status: published

Mit dem folgenden einfachen Befehl lassen sich die einzelnen Seiten aus
einem PDF-Dokument extrahieren und z.B. in PNG-Bilddateien abspeichern.

::

    pdftoppm -png dokument.pdf dokument

Die Seiten des PDF-Dokumentes werden als *dokument-SEITENZAHL.png*
abgespeichert.
