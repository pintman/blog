CTF - Kreuzworträtsel für Nerds
###############################
:date: 2018-01-02 09:50
:author: marco.bakera
:category: Informatik
:tags: 34c3, hacking
:slug: ctf-kreuzwortraetsel-fuer-nerds
:status: published

|image0|

CTF ist eine Abkürzung für "Capture the Flag". Auf dem Chaos
Communication Congress wird eine solche Veranstaltung traditionell immer
am Ende des Jahres durchgeführt. In diesem Jahr habe ich mich erstmals
auch bei der `Junior-Version <http://junior.34c3ctf.ccc.ac/>`__
beteiligt und in einem kleinen Team versucht, verschiedene Aufgaben aus
den folgenden Bereichen zu lösen: Reverse Engineering, Kryptographie,
Passwörter-Knacken, Web und Verschiedenes. Trotz der Klassifikation als
Einsteigerveranstaltung, waren die Aufgaben alles andere als leicht.
Über mehrere Schritte musste man gehen, um am Ende ein *flag* zu
erhalten - dies war ein String, der mit "34C3\_" beginnt und den man in
eine Weboberfläche eingeben kann, um damit die Aufgabe lösen.

|image1|

Unser Team *laborratten* hat am Ende den 147. Platz belegt - bei 435
teilnehmenden Teams ist das schon ein gutes Ergebnis, auf das sich
aufbauen lässt. Neben dem Konkurrenzaspekt, war das Lösen der Aufgaben
jedoch Ansporn genug, sodass es nicht unser letzter CTF gewesen sein
wird.

So etwas möchte ich auch einmal selbst veranstalten - vielleicht sogar
im Rahmen einer Schulveranstaltung oder bei einem GameJam. Die
einsteiger-freundlichen CTFs `picoCTF <https://picoctf.com/>`__,
`EasyCTF <https://www.easyctf.com/>`__, \ `OverTheWire:
Wargames <http://overthewire.org/wargames/>`__, \ `School
CTF <https://school-ctf.org>`__ und `Juniors
CTF <https://juniors.ctf.org.ru/>`__ könnten als Vorbild und
Aufgaben-Pool dienen.

| **Update**
| Das Buch `Kali Linux CTF
  Blueprints <https://www.packtpub.com/networking-and-servers/kali-linux-ctf-blueprints>`__
  zeigt, wie man selbst eine solche Challenge erstellen kann. Die Liste
  `Awesome CTF <https://github.com/apsdehal/awesome-ctf>`__ bei github
  stellt Frameworks, Tutorials und Software rund um CTF zusammen. Der
  `openflagserver von Jason
  Gillam <https://github.com/JGillam/openflagserver>`__ ist z.B. ein
  einfacher in Python geschrieberen und leicht anpassbarer Server, um
  Flags, User und Punkte zu verwalten.
| Auch die Formel zur Berechnung der Punktzahl in Abhängigkeit der
  Anzahl der Lösungen ist noch einen separaten Blick wert:
| int(round(30 + 470 / (1 + (max(0, solves - 1) / 11.92201) \*\*
  1.206069)))

.. |image0| image:: https://www.bakera.de/wp/wp-content/uploads/2018/01/Racing_Flag_Blue-800px-300x288.png
   :class: alignnone size-medium wp-image-2157
   :width: 300px
   :height: 288px
   :target: https://www.bakera.de/wp/wp-content/uploads/2018/01/Racing_Flag_Blue-800px.png
.. |image1| image:: https://www.bakera.de/wp/wp-content/uploads/2018/01/Screenshot-2018-1-1-https-junior-34c3ctf-ccc-ac.png
   :class: alignnone size-full wp-image-2160
   :width: 486px
   :height: 246px
   :target: https://www.bakera.de/wp/wp-content/uploads/2018/01/Screenshot-2018-1-1-https-junior-34c3ctf-ccc-ac.png
