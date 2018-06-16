Frohes neues Jahr
#################
:date: 2013-01-01 09:48
:author: admin
:tags: Mathe, Programmierung, Spaß, Spiele
:slug: frohes-neues-jahr
:status: published

| Ein `Tweet von
  @apfelkasten <https://twitter.com/apfelkasten/status/285894335894016000>`__
  begrüßt das neue Jahr mit einer interessanten Eigenschaft:

.. raw:: html

   <div>

|image0|

.. raw:: html

   </div>

| 
| Könnt ihr das mt einem kleinen Programm überprüfen? Dann ab damit in
  die Kommentare. :) Hier ist z.B. eine Variante in Smalltalk:

::

    2013 to: 1900 by: -1 do: [:jahreszahl |
      ziffern := Set new.
      jahreszahl asString do: [:ziffer | ziffern add: ziffer].
        (ziffern size) = 4
          ifTrue: [Transcript
                      show: jahreszahl;
                      cr]]

| 
| In diesem Sinne: Ein frohes neues Jahr!

.. |image0| image:: http://2.bp.blogspot.com/-xuCZJs_-nxE/UOKwDh-tJTI/AAAAAAAACRU/9AE0dFpa4lU/s1600/Unbenannt.PNG
   :target: http://2.bp.blogspot.com/-xuCZJs_-nxE/UOKwDh-tJTI/AAAAAAAACRU/9AE0dFpa4lU/s1600/Unbenannt.PNG
