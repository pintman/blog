Y f = f(Y f)
############
:date: 2006-01-13 10:28
:author: admin
:tags: Informatik
:slug: y-f-fy-f
:status: published

Heute mal etwas Theorie zum Thema λ-Kalkül. Hierbei handelt es sich um
eine von Alonzo Church etablierte Theorie zur Ausführung von Funktionen.
Hierbei nehmen wir Funktionen als anonyme Funktionen λ an und können die
Identität (also die Funktion, die alle Argumente auf sich selbst
abbildet) wie folgt darstellen:

::

        λx.x

Die anonyme Funktion λ bildet ihr einziges Argument x auf sich selbst
ab. Wir trennen in diesem Falle die Argumente (also x) von ihrer
Anwendung durch einen kleinen '.' ab.

Wenn wir eine Funktion nun auf ein Argument anwenden, schreiben wir es
einfach rechts daneben und erhalten im obigen Sinne der Definition der
Identität folgende Gleichung:

::

        (λx.x) 1 = 1

Diese erhalten wird, indem wir die Argumente für die an den λ-Operator
gebundenen Variablen einsetzen; die Funktion also auf 1 anwenden.

Nun können Argumente aber nicht nur einfach elementare Werte sein,
sondern selbst wiederum Funktionen. Wir könnten also die Identität auch
auf sich selbst anwenden und erhielten

::

        (λx.x)(λx.x) = (λx.x)

Die Identität verändert sich selbst also nicht. Ebenso sehen wir, dass
Ergebnisse von Funktionen ebenfalls wiederum Funktionen sein können.

Kommen wir nun zu einer etwas interessanteren Funktion

::

        Y = (λf.(λx. f(x x))(λx. f(x x)))

und nennen diese Y.

Was passiert nun, wenn wir Y auf f anwenden?

::

    (*) Y f = (λx. f(x x))(λx. f(x x))

Y f ist also eine Funktion, die auf eine Funktion angewendet wird.
Wollen wir diese Anwendung noch verfolgen und den rechten Teil der
obigen Gleichung etwas vereinfachen, so erhalten wir

::

        Y f = f((λx. f(x x)) (λx. f(x x)))

nachdem wir (λx. f(x x)) für x in f(x x) eingesetzt haben.

Nun erkennen wir aber, dass wir f auf der rechten Seite der Gleichung
gerade auf (\*), also auf Y f, anwenden und somit zu der interessanten
Gleichung

::

        Y f = f(Y f)

kommen. Y liefert uns also für eine gegebene Funktion f deren Fixpunkt.

Probieren wir diese Funktion nun einmal aus und versuchen den Fixpunkt
der Eins-Funktion (λx.1) zu bestimmen

::

        Y (λx.1) =
        (λf.(λx. f(x x))(λx. f(x x)))(λx.1) =
        (λx. (λx.1)(x x))(λx. (λx.1)(x x)) =
        (λx. 1)(λx. 1) =
        1

Juhu, es hat geklappt. Der Fixpunkt der Eins-Funktion ist demnach 1.

Wer Spaß daran gefunden hat, möge einmal versuchen, den Fixpunkt unserer
oben beschriebenen Identiät auf diese Weise zu berrechnen. Er wird
sicherlich erstaunt ob des bestimmten Fixpunktes sein. :)

Das wollte ich eigentlich nur mal gesagt haben. :)
