Backup über SSH und eine Pipe
#############################
:date: 2014-09-28 16:36
:author: marco.bakera
:category: Linux, Tipp
:slug: backup-ueber-ssh-und-eine-pipe
:status: published

Es ist schön, wenn es unter Linux mal ganz einfach geht, ein Backup via
Remotesteuerung zu erstellen. So habe ich ein kleines Script erstellt,
mit dem ich die Owncloud auf meinem RaspberryPi sichere. Via SSH wird
ein Tarball erzeugt, der auf meinen Rechner übertragen und dort durch
gzip-geleitet wird. Dadurch entstehen keine temporären Dateien auf dem
Pi und er wird auch nicht mit ZIP-Aufgaben belästigt.

::

    DATUM=$(date --iso)
    ssh pi@raspberrypi "tar cf - /var/www/owncloud/" | gzip -c > ${DATUM}-owncloud.tar.gz
