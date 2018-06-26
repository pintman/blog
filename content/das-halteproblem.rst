Das Halteproblem
################
:date: 2006-02-11 11:59
:author: admin
:tags: Informatik
:slug: das-halteproblem
:status: published

Das Halteproblem, beschreibt die Tatsache, dass es kein Programm geben
kann, das für ein anderes Programm entscheiden kann, ob dieses hält oder
nicht. Endlosschleifen lassen sich für den allgemeinen Fall also nicht
durch einen einfachen (oder auch komplizierten) Algorithmus ausfindig
machen. Dass noch nicht einmal Namen, die man für Aufrufe verfolgen
könnte, notwendig für eine Endlosschleife sind, zeigt das folgende
Beispiel.

::

        (λ () . (λ x. (x x)) (λ x. (x x)))

Einen anschaulichen Beweis für dieses Problem habe ich heute bei
`Structure & Interpretation of Computer
Programs <{filename}structure-and-interpretation-of-computer-programs.rst>`__
wiedergefunden, den ich kurz vorführen möchte.

Angenommen, es gäbe eine Funktion safe(f, a), die für eine Funktion f
und ein Argument a, herausfindet, ob f(a) definiert ist oder nicht - ob
ein die Funktion f berechnendes Programm also irgendwann zu einem
Ergebnis kommt, oder ewig lange in einer Endlosschleife verharrt und
damit kein Resultat liefert. Formal beschreiben wir die Funktion safe
wie folgt.

::

                  / tt    falls f(a)≠⊥
    safe(f, a) = |
                  \ ff    sonst

Die Annahme einer solchen Funktion führt jedoch zu einem Widerspruch,
wenn wir folgende Funktion betrachten.

::

            / ⊥    falls safe(d, d)
    d(x) = |
            \ 3    sonst

Doch wozu wertet nun d(d) aus? Dies hängt von safe und insbesondere von
safe(d, d) ab. Wir schauen uns die beiden Fälle einfach mal an.

| safe(d, d)=true
| Dann gilt d(d)=⊥. safe würde jedoch nur true liefern, wenn d(d)≠⊥
  gilt. Als kann nicht gelten safe(d, d)=true.

| safe(d, d)=false
| Dann jedoch gilt d(d)=3. safe kann jedoch nur false liefern, wenn gilt
  d(d)=⊥. Es kann also auch nicht gelten safe(d, d)=false.

In beiden Fällen haben wir einen Widerspruch produziert und können daher
nur annehmen, dass eine gewünschte Funktion safe mit besagten
Eigenschaften nicht existieren kann. Schade.
