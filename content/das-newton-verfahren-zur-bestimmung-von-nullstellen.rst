Das Newton-Verfahren zur Bestimmung von Nullstellen
###################################################
:date: 2014-06-18 17:08
:author: marco.bakera
:tags: Mathe, Programmierung
:tags: Nullstellen, Python
:slug: das-newton-verfahren-zur-bestimmung-von-nullstellen
:status: published

 

|(cc) Stefan Vorkoetter| 

(cc) Stefan Vorkoetter

Isaac Newton hat vor über 300 Jahren ein
`Verfahren <https://de.wikipedia.org/wiki/Newton-Verfahren>`__
vorgeschlagen, um nicht-lineare Gleichungen zu lösen. So findet das
Verfahren etwa eine Lösung für die folgende Gleichung

x² - 6 x + 5 = 0

Das Verfahren beginnt mit einer Schätzung und verbessert diese mit jedem
Schritt ein wenig. Die erste Schätzung heißt x0, die zweite dann x1, und
so weiter. Die Verbesserung x1 ergibt sich aus der Schätzung x0 wie
folgt.

x1 = x0 - f(x0) / f´(x0)

In dieser Gleichung ist f(x) = x² - 6x + 5 und f´(x) die Ableitung von
f(x) - also f´(x) = 2x - 6.

Schaue wir uns einmal an, wie sich die Werte entwickeln, wenn wir mit
der Schätzung x=10 beginnen.

::

    x      f(x)   f´(x)   x-f(x)/f´(x)
    10.0   45.0   14.0    6.79
    6.79   10.33  7.57    5.42
    5.42   1.86   4.84    5.04
    5.04   0.15   4.07    5.0003
    5.0003 0.001  4.0006  5.00000003

Man kann gut erkennen, wie sich die X-Werte langsam der 5 annähern,
während die Werte von f(x) gegen 0 streben. Wir schauen, ob es nicht
noch eine weitere Lösungen gibt. Immerhin haben quadratische Gleichungen
ja bis zu zwei Lösungen. Wir probieren es diesmal mit dem Startwert -10.

::

    x      f(x)   f´(x)   x-f(x)/f´(x)
    -10.0  165.0  -26.0   -3.65
    -3.65  40.27  -13.31  -0.63
    -0.63  9.16   -7.26   0.63
     0.63  1.59   -4.73   0.97
     0.97  0.11   -4.06   0.99
     0.99  0.0008 -4.0003 0.9999999904

Hier erkennen wir, wie die Werte von x gegen 1 streben, während f(x)
gegen 0 strebt. Einsetzen von x=1 und x=5 ergibt auch tatsächlich in
beiden Fällen den Wert 0. Wir haben unsere Lösungen gefunden.

Leider funktioniert das Verfahren nicht immer. Prüfe doch einmal, was
für die Gleichung f(x) = x³ - 2x + 2 und den Startwert x=0 passiert. Was
kannst du feststellen?

Man kann das Verfahren natürlich auch mit beliebigen anderen Gleichungen
durchführen. Und weil es so einfach ist, habe ich ein kleines
Python-Programm geschrieben, das für quadratische Gleichungen die Lösung
ermittelt. Versuche doch einmal, das Programm für kubische Gleichungen
oder Gleichungen vierten Grades zu erweitern.

::

    MAX_ITERATIONEN = 100
    GENAUIGKEIT = 0.1

    def newton(a, b, c, startwert):
        """  Bestimmt eine Lösung der Gleichung    ax² + bx + c = 0    
             für einen gegebenen Startwert.    """

        xn = startwert * 1.0
        fx = 1.0
        numIterationen = 0

        while abs(fx) > GENAUIGKEIT and numIterationen < MAX_ITERATIONEN:
            fx = f(a, b, c, xn)        
            fx_ = f_(a,b,c, xn)
            xn = xn - fx / fx_

            numIterationen += 1

        if numIterationen >= MAX_ITERATIONEN:
            return float('NaN')
        else:
            return xn


    def f(a,b,c, x):
        """    Berechne f(x) = ax² + bx + c    """
        return a*x*x + b*x + c

    def f_(a,b,c, x):
        """Berechne f'(x) = 2ax + b"""
        return 2*a*x + b

Das Programm kann nun mit newton(a,b,c, startwert) aufgerufen werden,
wobei a,b,c und d für die Koeffizienten in f(x) = ax² + bx + c stehen.

 

.. |(cc) Stefan Vorkoetter| image:: http://www.bakera.de/wp/wp-content/uploads/2014/06/hp35s-Tasten.jpeg
   :class: size-full wp-image-1171
   :width: 408px
   :height: 150px
