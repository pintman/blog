Structure and Interpretation of Computer Programs
#################################################
:date: 2006-01-06 08:24
:author: admin
:tags: Informatik
:slug: structure-and-interpretation-of-computer-programs
:status: published

Lange ist es her seit meine letzte Nachricht an die Menschheit in
dieses öffentliche Forum meiner Seite verkündet wurde. Nun bin ich
aber wieder zurück und wünsche in guter höflicher Manier allen meinen
Lesern - und ich weiß, dass es wenige sind - ein Frohes Neues Jahr.

|image0|

Um diesen Eintrag noch weiter begründen zu können, möchte ich auf eine
meiner tollsten Entdeckungen in der Informatiklandschaft hinweisen:
*Scheme*. Hierbei handelt es sich um eine Programmiersprache (genauer:
einen Lisp-Dialekt), der mich in seiner Eleganz und Mächtigkeit,
Probleme und deren Lösung zu beschreiben, schlichtweg umgehauen hat.
Neben dem Buch `Struktur und Interpretation von
Compterprogrammen» <http://www.amazon.de/exec/obidos/ASIN/3540520430/303-9962625-7020245>`__,
das unabhängig von der verwendeten Sprache ein grandioses Standardwerk
der Infoamtikausbildung am `MIT» <http://mit.edu/>`__ bildet, haben
mich die Autoren selbst in einer sehr `professionell gestalteten
Vorlesung» <http://swiss.csail.mit.edu/classes/6.001/abelson-sussman-lectures/>`__
auf Grundlage dieses Buches aus den 80er Jahren überzeugt. Neben
Videos dieser Veranstaltung, ist auch eine Textversion des o.g. Buches
auf dieser Seite zu finden, die sich "leider" zunehmender Beliebtheit
zu erfreuen scheint und daher nicht immer so gut erreichbar ist, wie
man es sich wünscht.
In diesem Sinne:

|image1|

::

  (define null
      (λ (f)
          (λ (x) x)))

  (define 1+ n
      (λ (f)
          (λ (x) (f ((n f) x)))))

(Alonzo Church)


.. |image0| image:: {filename}images/wizard.jpg
.. |image1| image:: {filename}images/Church.jpg
   :target: http://www-groups.dcs.st-and.ac.uk/~history/Mathematicians/Church.html
