Frohes neues Jahr
#################
:date: 2013-01-01 09:48
:author: admin
:tags: Mathe, Programmierung, Spaß, Spiele
:slug: frohes-neues-jahr
:status: published

Ein `Tweet von
@apfelkasten <https://twitter.com/apfelkasten/status/285894335894016000>`__
begrüßt das neue Jahr mit einer interessanten Eigenschaft:


|image0|

Könnt ihr das mt einem kleinen Programm überprüfen? Dann ab damit in
die Kommentare. :) Hier ist z.B. eine Variante in Smalltalk:

::

    2013 to: 1900 by: -1 do: [:jahreszahl |
      ziffern := Set new.
      jahreszahl asString do: [:ziffer | ziffern add: ziffer].
        (ziffern size) = 4
          ifTrue: [Transcript
                      show: jahreszahl;
                      cr]]

 
In diesem Sinne: Ein frohes neues Jahr!

.. |image0| image:: {filename}images/2013_tweet.PNG
