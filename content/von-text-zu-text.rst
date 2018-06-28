Von Text zu Text
################
:date: 2006-02-21 22:43
:author: admin
:tags: Informatik, LaTex
:slug: von-text-zu-text
:status: published

So ergab es sich am heutigen Tage, dass nach einiger Zeit der
Probierens, es (ja was denn eigentlich?) mir nun endgültig gelang, ein
mehr oder minder komplexes Dokument in |LaTeX| in ein mehr oder minder
anderes komplexes Dokument in HTML zu konvertieren. Schier unendlich
hohe Hürden mussten gemeistert werden, ehe das Dokument so stand, wie es
nun steht.

Doch immer langsam mitte Pferde. Eigentlich dachten wir
(`Clemens» <http://claimaster.de/>`__ und ich), dass es doch eine tolle
Sache wäre, wenn man die Dokumentation für ein
`Softwareprodukt» <http://jabc.cs.uni-dortmund.de/modelchecking/>`__
doch gerne nur einmal schreibt, gerade so, dass man sie auch ausdrucken
kann, und dass man dann eine Version für die Veröffentlichung im
Internet automatisch generieren lässt. Soweit so gut. Recht schnell war
dann auch schließlich das |LaTeX|-Dokument fertig gestellt. Also
\*zack\* wacker zu einem frickelig zusammengehackten Stück Software in
Perl gegriffen (auch bekannt unter dem vielversprechenden Namen
`latex2html» <http://www.latex2html.org/>`__). Irgendwie wollte das
jedoch überhaupt nicht hinhauen. Nach einer kleinen Suche, tauchte dann
noch ein kleines anderes Stück Software mit Namen
`tex2page» <http://www.ccs.neu.edu/home/dorai/tex2page/tex2page-doc.html>`__
auf. In Scheme geschrieben, schnell installiert und es macht genau das,
was man von ihm verlangt.

Danke für diese Eingebung. Ich werde niemals nie nimmer wieder auf
frickelige Perl-Software ausweichen und stets dem λ-kalkülisierten
Scheme treu bleiben. In tiefer Verbeugung und mit ewiger Dankbarkeit dem
Entwickler von
`tex2page» <http://www.ccs.neu.edu/home/dorai/tex2page/tex2page-doc.html>`__.

Wer die Ergebnisse einmal vergleichen möchte, findet unten die beiden
Links, die jeweils einmal auf das ursprüngliche PDF, das aus dem
|LaTeX|-Dokument erzeugt wurde, sowie die automatisch generierte
HTML-Version davon verweisen.

-  `PDF» <http://jabc.cs.uni-dortmund.de/modelchecking/pdf/gear-manual-0.9.04.pdf>`__
-  `HTML» <http://jabc.cs.uni-dortmund.de/modelchecking/gear.html>`__

.. |LaTeX| image:: {filename}images/latex-3347.png

