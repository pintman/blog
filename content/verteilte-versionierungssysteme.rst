Verteilte Versionierungssysteme
###############################
:date: 2007-07-21 05:44
:author: admin
:tags: Film, Informatik, Programmierung
:slug: verteilte-versionierungssysteme
:status: published

In einem `Vortrag bei
Google <http://www.youtube.com/watch?v=4XpnKHJAok8>`__ erklärt Linus
Torvalds die Vorzüge seines selbst entwickelten
Versionsverwaltungssystems `git <http://git.or.cz/>`__. Das besondere
an git ist,
dass es, im Gegensatz zu Systemen wie etwa
`CVS <http://en.wikipedia.org/wiki/Concurrent_Versions_System>`__ oder
`Subversion
(SVN) <http://en.wikipedia.org/wiki/Subversion_%28software%29>`__,
kein zentrales Repository gibt, in dem alle Daten abgelegt
werden. Vielmehr hat jeder Entwickler sein eigenes Repository und kann
dieses ggf. mit den Repositories anderer Entwickler
synchronisieren.
Was sich zunächst einmal nach Chaos und vielen Problemen anhört,
entpuppt sich bei genauerer Betrachtung und radikaler Argumentation
von Linus Torvalds als Arbeitsweise, die dem menschlichen Verhalten
eher entspricht als die Verwendung eines zentralisierten Systems. Man
merged einfach die Änderungen derjenigen Entwickler in sein Repo,
denen man vertraut und die ein neues tolles Feature vorstellen.
Andere Vertreter dieser verteilten Systeme sind etwa
das etwas besser in Windows integrierte freie
`mercurial <http://www.selenic.com/mercurial>`__ und das
kommerzielle `BitKeeper <http://www.bitkeeper.com/>`__.
