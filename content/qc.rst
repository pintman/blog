Quantencomputer
===============
:date: 2019-01-22 21:20
:author: marco.bakera
:tags: programmierung, python, das labor
:status: published

Heute fand ein Vortrag und Workshop zum Thema Quantencomputer
im Bochumer Labor statt. Diese Dinger können schnell rechnen, aber vermutlich
nicht mehr Probleme lösen als klassische Computer. Statt
mit Bits, die entweder 0 oder 1 repräsentieren, wird mit
QBits gerechnet, die eine Wahrscheinlichkeitsverteilung
zwischen 0 und 1 einnehmen. Es gibt verschiedene
`Quanten-Algorithmen <https://en.wikipedia.org/wiki/Quantum_algorithm>`_
die verschiedene Probleme lösen. So generell scheinen die 
Probleme aber wiederum auch nicht zu sein, da die Probleme
immer in ähnlichen Problemgebieten wie der schnellen 
Fourier-Transformation liegen. Das Brechen von Kryptographie
ist ein prominentes Gebiet für Quantencomputer. So prominent, dass die
NIST derzeit 
`nach Algorithmen sucht <https://csrc.nist.gov/Projects/Post-Quantum-Cryptography/Round-1-Submissions>`_, 
die auch mit Quantencomputern eine sichere Verschlüsselung garantieren.

Beim Erstellen von Quantencomputern scheinen
`Controlled NOT gates <https://en.wikipedia.org/wiki/Controlled_NOT_gate>`_ 
eine wichtige Rolle zu spielen - grob funktionieren sie ähnlich
einem XOR-Gatter, im Detail ist es aber vermutlich komplizierter.

Beim BSI gibt es eine
`Einführung in Quantencomputing für Einsteiger <https://www.bsi.bund.de/qcstudie>`_
und einen ausführlicheren Bericht für Profis. Der ist dort als
238-seitiges PDF verlinkt.

Bei IBM kann man `einen Quantencomputer selbst programmieren <https://quantumexperience.ng.bluemix.net/qx/editor>`_. 
Das geht über einen Editor direkt im Browser. Dann bekommt man Rechenzeit nach 
einem Punkteschema zugewiesen und das Programm läuft auf dem
Quantencomputer. Es erinnert an die Batchverarbeitung von früher.
Für Python gibt es auch `eine Bibliothek <https://nbviewer.jupyter.org/github/Qiskit/qiskit-tutorial/blob/master/community/hello_world/hello_zero.ipynb>`_,
um auf den Quantencomputer zuzugreifen.

Eine echte Anwendung für Quantencomputer mit wenigen QBits gibt es heute 
bereits: die Berechnung von Energien in Molekülen.

