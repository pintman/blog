Erste Programme für den HP 35s
##############################
:date: 2014-06-14 12:16
:author: marco.bakera
:tags: Informatik, Mathe, Programmierung, HP35s, Taschenrechner
:slug: erste-programme-fuer-den-hp35s
:status: published

|cc: Stefan Vorkoetter| 

cc: Stefan Vorkoetter

Erst `kürzlich habe ich einen neuen Taschenrechner
erhalten <{filename}bakera-packt-aus-einen-hp35s.rst>`__
- den HP 35s. Natürlich habe ich zunächst die Möglichkeiten erforscht,
das Gerät zu programmieren. Ein paar erste Programme möchte ich hier
vorstellen.

IHK-Notenschlüssel
~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="level3">

Ein kleines Programm zur Berechnung eines Notenschlüssels gemäß des
IHK-Schlüssels.

.. code::

    I001 LBL I
    I002 STO P               Wert im aktuellen Register in P speichern
    I003 Px[0.92,0.81,0.67]  Nötige Punkte berechnen und 
    I004 Px[0.50,0.30,0.00]  in zwei Vektoren abspeichern
    I005 RTN

Der Aufruf erfolgt wie folgt:

#. 

   .. raw:: html

      <div class="li">

   Punktzahl eingeben

   .. raw:: html

      </div>

#. 

   .. raw:: html

      <div class="li">

   XEQ I ENTER

   .. raw:: html

      </div>

Dann werden die Punkte angezeigt.

.. raw:: html

   </div>

.. raw:: html

   <div class="secedit editbutton_section editbutton_3">

.. raw:: html

   </div>

pq-Formel
~~~~~~~~~

.. raw:: html

   <div class="level3">

Zunächst werden die Werte für p und q auf dem Stack gespeichert.
Anschließend kann das folgende Programm ausgeführt werden, das die
reellen Nullstellen berechnet.

.. code::

    P001  LBL P
    P002  STO Q
    P003  x<>y
    P004  STO P
    P005  -P÷2+SQRT((P÷2)^2-Q)
    P006  -P÷2-SQRT((P÷2)^2-Q)  
    P007  RTN

.. raw:: html

   </div>

.. raw:: html

   <div class="secedit editbutton_section editbutton_4">

.. raw:: html

   </div>

Nullstellen kubischer Gleichungen - Version 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="level3">

Die Nullstellen einer Funktion der Form f(x) = ax³ + bx² +cx +d lassen
sich mit Hilfe des
`Weierstraß-(Durand-Kerner)-Verfahren <http://de.wikipedia.org/wiki/Weierstra%C3%9F-%28Durand-Kerner%29-Verfahren>`__
berechnen. Leider verwendet das Verfahren komplexe Zahlen und ist daher
etwas langsam auf dem HP35s. Nach Beendigung des Algorithmus stehen die
Ergebnisse in den Registern X, Y und Z.

.. code::

    K001 LBL K
    K002 INPUT A
    K003 INPUT B
    K004 INPUT C
    K005 INPUT D
    K006 1          Die Startwerte für P, Q und R werden
    K007 STO P      mit beliebigen Werten initialisiert.
    K008 0.4i0.9
    K009 STO Q
    K010 -0.65i0.72
    K011 STO R
    K012 0.006      Die Variable Z dient als Schleifenvariable
    K013 STO Z      und wird von 0 bis 6 gezählt.
    K014 P-(AxP^3+BxP^2+CxP+D)÷(P-Q)÷(P-R)
    K015 STO P
    K016 Q-(AxQ^3+BxQ^2+CxQ+D)÷(Q-P)÷(Q-R)
    K017 STO Q
    K018 R-(AxR^3+BxR^2+CxR+D)÷(R-P)÷(R-Q)
    K019 STO R
    K020 ISG Z      
    K021 GTO K014
    K022 RTN

.. raw:: html

   </div>

.. raw:: html

   <div class="secedit editbutton_section editbutton_5">

.. raw:: html

   </div>

Nullstellen kubischer Gleichungen - Version 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="level3">

Mit Hilfe des
`Horner-Schema <http://de.wikipedia.org/wiki/Horner-Schema>`__\ s, der
Solve-Funktion und der pq-Formel lässt sich auch eine kubische Gleichung
der Form f(x) = ax³+bx²+cx+d lösen.

Damit in einem Programm auf die zu lösende Funktion zugegriffen werden
kann, legen wir sie in Programm F ab.

.. code::

    F001  LBL F
    F002  INPUT X
    F003  INPUT A
    F004  INPUT B
    F005  INPUT C
    F006  INPUT D
    F007  AxX^3+Bx^2+CxX+D
    F008  RTN

Nun wird mit dem Programm C eine Nullstelle mittels SOLVE bestimmt und
das Restpolynom mit dem Hornerschema ermittelt.

.. code::

    C001  LBL C
    C002  FN= F    
    C003  1        Festlegen einer Anfangsschätzung
    C004  STO X
    C005  SOLVE X
    C006  VIEW X   Das erste Ergebnis wird angezeigt
    C007  STO X

.. code::

    C008  XxA      Bestimmung des Restpolynoms mit 
    C009  STO+ B   dem Horner-Schema
    C010  XxB
    C011  STO+ C

.. code::

    C012  B÷A      Normalform für pq-Formel herstellen.
    C013  C÷A
    C014  XEQ P001
    C015  RTN

.. raw:: html

   </div>

.. raw:: html

   <div class="secedit editbutton_section editbutton_6">

.. raw:: html

   </div>

Komplexe Wurzeln
~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="level3">

Die komplexe Wurzel lässt sich mit dem folgenden kleinen Programm
berechnen.

Durch die Verwendung von LASTx wird der Stack nicht verändert. CLx
löscht den Inhalt des X-Registers auf dem Stack.

.. code::

    K001 LBL K
    K002 1/x
    K003 CLx   
    K004 LASTx^0.5i0  
    K005 RTN

.. raw:: html

   </div>

 

.. |cc: Stefan Vorkoetter| image:: images/2014/06/hp35s-oben.jpeg
   :class: size-full wp-image-1143
   :width: 406px
   :height: 138px
