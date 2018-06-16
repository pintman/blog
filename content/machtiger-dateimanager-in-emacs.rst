Mächtiger Dateimanager in Emacs
###############################
:date: 2007-04-15 10:38
:author: admin
:tags: Informatik
:slug: machtiger-dateimanager-in-emacs
:status: published

Mit ``Strg-x d`` erhält man im Emacs einen Dateimanager, der es in sich
hat. Eines der wohl mächtigsten (und leider wohl auch weniger bekannten)
Features ist das Kommando ``wdired-change-to-wdired-mode``, mit dem der
Buffer des angezeigten Verzeichnisses in einen gewöhnlichen Emacs-Buffer
verwandelt wird. Auf diesem kann man dann z.B. mittels regulärer
Ausdrücke die Verzeichnisnamen ändern und schließlich mit
``Strg-c Strg-c`` die Änderungen bestätigen und durchführen lassen.

Die Emacs eigene Hilfe sagt dazu

    | In this mode you can edit the names of the files, the target of
      the
    | links and the permission bits of the files.

Einige sehr schöne Folien mit einer generellen Einführung bis hin zu
fortgeschrittenen Konzepten gibt es übrigens als Material zu der
Vorlesung `Being Productive With
Emacs» <http://stuff.mit.edu/iap/emacs/>`__, die im Januar diesen Jahres
am MIT stattfand.

Weitere sinnvolle Tipps für Fortgeschrittene bietet `Effective
Emacs» <http://steve.yegge.googlepages.com/effective-emacs>`__ und
natürlich das sehr umfangreiche
`Emacs-Wiki» <http://www.emacswiki.org/>`__.
