Backup für ein Android-Handy erstellen
######################################
:date: 2014-01-05 11:12
:author: marco.bakera
:category: Informatik, Tipp
:slug: backup-fuer-ein-android-handy-erstellen
:status: published

Nun habe ich schon seit einiger Zeit ein Android-Handy, habe mir
sträflicherweise jedoch bisher wenig Gedanken um ein Backup der Daten
auf diesem Handy gemacht. Dabei klappt es mit der `"Android Debug
Bridge" (adb) <https://developer.android.com/tools/help/adb.html>`__
sehr einfach.

Die Dokumentation zum Backupkommando lautet wir folgt:

::

    adb backup [-f <file>] [-apk|-noapk] [-shared|-noshared] [-all] [-system|-nosystem] [<packages...>]
       - write an archive of the device's data to <file>.
         If no -f option is supplied then the data is written
         to "backup.ab" in the current directory.
         (-apk|-noapk enable/disable backup of the .apks themselves
            in the archive; the default is noapk.)
         (-shared|-noshared enable/disable backup of the device's
            shared storage / SD card contents; the default is noshared.)
         (-all means to back up all installed applications)
         (-system|-nosystem toggles whether -all automatically includes
            system applications; the default is to include system apps)
         (<packages...> is the list of applications to be backed up.  If
            the -all or -shared flags are passed, then the package
            list is optional.  Applications explicitly given on the
            command line will be included even if -nosystem would
            ordinarily cause them to be omitted.)

Für Windows muss man das kleine Programm aus dem Android SDK erst
installieren, auf einem openSUSE ist es in der Standardinstallation
schon vorhanden.

Um adb benutzen zu können, muss das USB-Debugging zuvor im Handy bei den
Entwickleroptionen eingeschaltet werden.

Danach lässt sich ein Backup sehr einfach mit

::

    adb backup -all

erzeugen. Nun wird die Datei "backup.ab" im aktuellen Verzeichnis
erzeugt, Diese kann mit

::

    adb restore backup.ab

wieder zurück in das Gerät gespielt werden.

Neben Backups kann man adb auch für die Installation oder einen
Shell-Zugang auf das Gerät prima nutzen. Viele weitere Tipps stehen in
der aktuellen `c't (2/14) <http://www.heise.de/ct/inhalt/2014/2/74/>`__.
