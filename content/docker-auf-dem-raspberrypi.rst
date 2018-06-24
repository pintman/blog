Docker auf dem RaspberryPi
##########################
:date: 2018-01-20 15:49
:author: marco.bakera
:tags: Hardware, RaspberryPi
:slug: docker-auf-dem-raspberrypi
:status: published

|image0|

Mit `HyprioOS <https://blog.hypriot.com/>`__ gibt es seit einiger Zeit
ein Image für den RaspberryPi, das docker container auf den Pi holt. Man
muss beachten, dass die docker images für ARM-Architekturen gebaut sind.
Davon gibt es aber immer mehr -
`hypriot <https://hub.docker.com/r/hypriot/>`__ selbst stellt bereits
einige zur Verfügung. Man kann z.B. mit einem schlanken
alpine-Basisimage starten und sich darauf aufbauend mit Hilfe eines
`Dockerfile <https://manpages.debian.org/Dockerfile>`__ den Container
für den eigenen Bedarf stricken.

::

    $ docker build -t containername .

Mehrere Container können schließlich zu einem Service zusammengebaut
werden. Das macht docker-compose und ein
`docker-compose-yml-File <https://docs.docker.com/compose/compose-file/>`__.

::

    $ docker-compose up

Mehrere Services lassen sich schließlich `zu einem Swam
zusammenfügen <https://blog.hypriot.com/post/dockerconaustin2017/>`__
und auf mehrere Pis verteilen. HypriotOS bringt alle wichtigen Tools mit
und läuft zuverlässig.

.. |image0| image:: images/Docker-Pirates-ARMed-with-explosive-stuff.png
   :class: alignnone size-full wp-image-2234
   :width: 134px
   :height: 138px
   :target: images/Docker-Pirates-ARMed-with-explosive-stuff.png
