Erneuter Blogumzug
##################
:date: 2018-06-26 12:20
:author: marco.bakera
:tags: bloggen, admin
:status: draft

.. image:: {filename}images/2018/07/Fragile-1.svg
   :alt: Umzug from https://openclipart.org/detail/86251/fragile
   :width: 50%

Nach dem letzten `Blogumzug <{filename}blogumzug.rst>`_ im Jahr 2013
steht nun ein erneuter Umzug an. Ich habe irgendwann um 2001 herum mit
einem eigenen Perlscript begonnen und vor kurzem auch in diesem Blog
`darüber gechrieben <{filename}blog2001_2003.rst>`_. 
Artefakte dieser ersten Versuche
lassen sich noch über die WayBack-Machine im 
`Internet-Archiv <https://web.archive.org/web/20040126011740/http://members.ping.de/~pintman/>`_
finden. Irgendwann bin ich dann auf die Plattform *blogspot.com* gewechselt.
Diese hieß später *blogger.com* und wurde irgendwann von Google gekauft.

Schließlich bin ich im Rahmen meiner 
`digitalen Emanzipation <{filename}digitale-emanzipation.rst>`_ zu einer 
eigenen Wordpress-Installation gewechselt und war
damit auch viele Jahre zufrieden. Problematisch war hier, dass die Artikel
in einer Datenbank verschwanden und ich bei komplexeren Suchanfragen oder
Bearbeitungen auf die Web-Oberfläche angewiesen war. Außerdem muss man sich
um eine solche Installation auch kümmern: PHP-Lücken müssen geschlossen,
die Wordpress-Software aktuell gehalten werden.

Nun bin ich bei einer statisch generierten Webseite gelandet. 
Alle meine Artikel liegen
als Textdateien in einem Github-Repo vor. Aus diesen kann ich sehr einfach eine
Webseite generieren lassen. Hierfür nutze ich den Generator 
`pelican <https://blog.getpelican.com/>`_. Da dieser Generator in Python 
geschrieben ist, kann ich bei Bedarf sogar einfach eingreifen. Die 
Quelldateien liegen alle als 
`reStructuredText <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_
vor und ermöglichen dadurch einen einfachen Umzug zu einem anderen Generator, 
wenn mir Pelican nicht mehr gefallen sollte.
Es gibt da eine Menge anderer Generatoren, die bestimmt genauso gut sind. 
Wichtig ist, dass die Webseite aus Textdateien generiert wird und ich keine
aktiven Komponenten wie PHP auf dem Webserver benötige.
