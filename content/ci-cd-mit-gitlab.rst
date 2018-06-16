CI/CD mit Gitlab
################
:date: 2018-03-23 18:08
:author: marco.bakera
:category: Informatik, Programmierung, Python
:slug: ci-cd-mit-gitlab
:status: published

`Gitlab <http://gitlab.com/>`__ ist neben github eine der großen
Plattformen für Softwareentwickler, um Quelltext in Git-Repos zu
verwalten. Mir hat immer gut gefallen, dass die Plattform keine Probleme
mit privaten Repos hat - github stellt sich etwas an und möchte hier nur
ein privates Repo pro Nutzer kostenlos zur Verfügung stellen. Auch die
`Terms of Service <https://tosdr.org/#github>`__ von github bereiten mir
zunehmend Bauchschmerzen. Hinzu kommt, dass sich github nicht auf
eigener Infrastruktur hosten lässt. Gitlab dagegen bietet eine mächtige
`Community-Edition <https://about.gitlab.com/installation/>`__ an. Das
Projekt `edugit <https://edugit.org/>`__ des Teckids e.V. ist ein
Vorstoß in die Richtung, diesen Dienst datenschutzkonform auch im
Bildungsbereich in Deutschland anbieten zu können.

Zurück zu den Vorzügen von Gitlab. Ein tolles mir neues Feature sind
sogenannte Runner. Das sind virtuelle Maschinen, Rechner oder
Docker-Container, die meinen Quelltext automatisch prüfen können. Dieses
Feature heißt CI/CD (für Continuous Integration/Continuous Delivery) und
wird durch die Datei *.gitlab-ci.yml* konfiguriert. Ein Beispiel, das
einen Pythontest in einem Python-Container auf alpine-Basis ausführt,
sieht so aus.

::

    image: python:alpine  # Das Basisimage des Containers

    before_script:  # Wird vor jedem Task ausgeführt
     - echo nothing to do

    tests:    # Ein Task mit Namen 'tests'
     script:  # Das Script hat mehrere Befehle
     - find ex.py test.py
     - python3 test.py
     - python3 -m doctest ex.py

Sobald nun Quelltext in das Repo gepusht wird, läuft ein sogenannter
Runner und führt die Tasks einzeln aus. Gitlab selbst stellt auf seiner
Plattform verschiedene Runner zur Verfügung, die von Digital Ocean
gesponsert werden und in ihrer Laufzeit auf generöse 2000 CPU-Minuten
pro Monat und User beschränkt sind. Wem das nicht reicht, der kann auch
selbst einen `Runner bei sich
installieren <https://docs.gitlab.com/runner/install/>`__, laufen lassen
und darin die Tests ausführen. Wem Gitlab nicht behagt, der kann auch
einen Runner mit `drone.io <http://docs.drone.io>`__ betreiben. Diese
haben den Vorzug, nicht auf Gitlab beschränkt zu sein und integrieren
sich auch in andere Plattformen wie etwa
`github <https://github.com>`__, `gitea <http://gitea.io/>`__ oder
`gogs <https://gogs.io/>`__.
