"Hallo Welt" HP 35s
###################
:date: 2014-06-19 14:03
:author: marco.bakera
:tags: Mathe, Programmierung, HP35s, Taschenrechner
:slug: hallo-welt-hp35s
:status: published

|(cc) Stefan Vorkoetter| 

(cc) Stefan Vorkoetter

Über
den \ `HP35s <http://www.bakera.de/dokuwiki/doku.php/schule/hp_35s>`__
habe ich `bereits
berichtet <{filename}bakera-packt-aus-einen-hp35s.rst>`__.
Nun folgt das obligatorische Hallo-Welt-Programm. Der Rechner kann
nämlich auch beliebigen Text anzeigen. Dies geschieht über das Flag 10.
Ist es gesetzt, werden Gleichungen nur angezeigt, aber nicht
ausgewertet. Das können wir für ein einfaches „Hallo-Welt“-Programm
nutzen.

::

     A001  LBL A
     A002  SF 10  Setzt Flag 10
     A003  HALLO  Eingabe mit der EQN-Taste
     A004  PSE    Nach einer Sekunde wird das Programm fortgesetzt
     A005  WELT
     A006  PSE
     A007  CF 10  Löscht Flag 10
     A008  RTN

 

.. |(cc) Stefan Vorkoetter| image:: {filename}images/2014/06/hp35s-oben.jpeg
   :class: size-full wp-image-1143
   :width: 406px
   :height: 138px
   :target: {filename}images/2014/06/hp35s-oben.jpeg
