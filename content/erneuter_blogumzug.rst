Erneuter Blogumzug
##################
:date: 2018-06-26 12:20
:author: marco.bakera
:tags: bloggen, admin
:status: draft

.. noch ältere Seiten https://web.archive.org/web/20040126011740/http://members.ping.de/~pintman/

Nach dem letzten `Blogumzug <{filename}blogumzug.rst>`_ im Jahr 2013
steht nun ein erneuter Umzug an. Ich habe auf der Plattform
*blogspot.com* begonnen. Diese hieß später *blogger.com* und wurde 
irgendwann von Google gekauft. 

Ich bin dann zu einer eigenen Wordpress-Instalation gewechselt und war
damit auch viele Jahre zufrieden. Problematisch war hier, dass die Artikel
in einer Datenbank verschwanden und ich bei komplexeren Suchanfragen oder
Bearbeitungen auf die Web-Oberfläche angewiesen war.

Nun bin ich bei einer statisch generierten Webseite zu gelandet. 
Alle meine Artikel liegen
als Textdateien in einem Github-Repo vor. Aus diesen kann ich sehr einfach eine
Webseite generieren lassen. Hierfür nutze ich den Generator 
`pelican <https://blog.getpelican.com/>`_. Da er in Python geschrieben
ist, kann ich bei Bedarf sogar einfach eingreifen. Die Quelldateien liegen
alle als 
`reStructuredText <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_
und ermöglichen dadurch einen einfachen Umzug zu einem anderen Generator, wenn
mir Pelican nicht mehr gefallen sollte.
Es gibt da eine Menge anderer Generatoren, die bestimmt genauso gut sind. 
Wichtig ist, dass die Webseite aus Textdateien generiert wird und ich keine
aktiven Komponenten wie PHP auf dem Webserver benötige.
