Funktionen und Mengen
#####################
:date: 2006-02-17 20:57
:author: admin
:category: Informatik
:slug: funktionen-und-mengen
:status: published

Da habe ich mir doch mal wieder ein paar Gedanken zu den guten alten
Konzepten der Mengen gemacht und bin zu der Überzeugung gekommen, dass
Mengen nicht nur durch ihre Aufzählung allein genügend charakterisiert
sind. Vielmehr sollte es doch auch eine implizite Möglichkeit geben,
Mengen zu beschreiben. Dies passiert eben ganz einfach durch die
Verwendung von Funktionen. So lässt sich etwa die Menge {1, 2, 3} mit
den Element 1, 2 und 3 ja auch durch eine Prädikatsfunktion wie folgt
beschreiben.

::

             / tt  falls x∈{1, 2, 3}
      f x = |
             \ ff  sonst

Zunächst scheint es, als hätten wir die Aufzählung nur einfach
wegabstrahiert. Jedoch kann die Aussage x∈{1, 2, 3} ebenso in eine
äquivalente Form x=1 ∨ x=2 &or x=3 gebracht werden.

Schauen wir nun, was bei Negation dieser impliziten Charakterisierung
passiert. Welche Menge beschreibt etwa die Funktion g x = ¬(f x)?
Schauen wir einmal, welche Elemente alle darin enthalten sind.

::

    g 1 = ¬(f 1) = ¬tt = ff
    g f = ¬(f f) = ¬ff = tt
    g g = ¬(f g) = ¬ff = tt

Interessanterweise enthält g also nicht nur alle natürlichen Zahlen
außer der 1, 2 oder 3, sondern enthält auch alle Funktionen,
insbesondere also auch f und sich selbst. Wir haben also mit g eine
Menge beschrieben, die sich selbst enthält - und sich insbesondere echt
enthält, also eine echte Teilmenge von sich selbst ist. Ein Widerspruch?

Sollte die Verwirrung noch nicht ausreichend sein, versuchen wir nun
einmal eine Menge zu konstruieren, die sich selbst beschreibt - die also
nicht nur eine (echte) Teilmenge von sich selbst ist, sondern sich
selbst ist. Wir benötigen also eine Funktion, die, wenn auf sich selbst
angewendet, tt als Ergebnis liefert, und ansonsten eben ff. Versuchen
wir es also mit der folgenden Definition.

::

           / tt  falls x = h
    h x = |
           \ ff  sonst

Die Funktion scheint soweit zu funktionieren, erzeugt jedoch das neue
Problem, etwas über die Vergleichbarkeit zweier Funktionen aussagen zu
müssen. Im strengen Sinne sind zwei Funktionen genau dann gleich, wenn
sie gleiche Urbild- und Bildmengen besitzen. Es spielt also keine Rolle,
in welcher Art und Weise die Mengen zueinander erzeugt werden. Lediglich
die Beschreibung des Verhältnisses der beiden Mengen ist entscheidend.
Nicht jedoch die Berechnungsvorschrift. So sind inbesondere die
folgenden Funktionen im Sinne dieses Verständnisses alle gleich:

::

    m1 x = x + x
    m2 x = 2 * x
    m3 x = (x + x + x + x) / 4

Verträgt sich dies denn auch mit unserer Definition von h? Ich würde
behaupten ja. Denn wenngleich ich eine scheinbar andere Funktion als
Argument von h auf h anwenden würde, liefert h bei den entsprechenden
Eingaben, das intendierte Verhalten. Insbesondere folgt damit aber auch,
dass h bei syntaktisch unterschiedlichen Eingaben jeweils tt liefert,
die Menge jedoch trotzdem nur eine Element (eben h) enthält.

Fazit: Wir haben es also geschafft, uns von einer expliziten
Mengendarstellung hin zu einer impliziten Darstellung zu bewegen und
können nun etwas beschreiben, dessen Beschreibung sich selbst enthält.
Ob das nur gut geht?!
