Dateianhang für PDF
###################
:date: 2014-10-01 16:47
:author: marco.bakera
:category: Linux, Tipp
:slug: dateianhang-fuer-pdf
:status: published

Ein wenig bekanntes Feature ist, dass man PDF-Dokumenten Dateien
anhängen kann - wie auch bei E-Mails. So kann man immer die
Originaldokumente anhängen, aus denen das PDF entstanden ist. Hierfür
gibt es das `PDF
Toolkit <https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/>`__ - kurz
pdftk. Unter Linux klappt es mit der folgenden Kommandozeile.

::

    ~> pdftk datei.pdf attach_files anhang.odt to_page 1 output dateiMitAnhang.pdf

Hier findet ihr ein `Beispieldokument mit
Anhang <http://www.bakera.de/wp/wp-content/uploads/2014/10/PDFmitAnhang.pdf>`__.
