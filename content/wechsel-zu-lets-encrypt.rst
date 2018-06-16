Wechsel zu "let's encrypt"
##########################
:date: 2017-04-13 16:20
:author: marco.bakera
:category: Linux
:slug: wechsel-zu-lets-encrypt
:status: published

Nachdem Google seine Drohungen nun wahr gemacht und auch alte
StartSSL-Zertifikate im Google Chrome nicht mehr unterstützt werden, bin
ich zu let's encrypt gewechselt. Der Wechsel mit Hilfe des certbot
verlief erstaunlich beschwerdefrei, wenngleich ich mich über die 10 MB
Abhängigkeiten und über eine Neu(!)-Entwicklung in Python2 sehr
gewundert habe. Ebenso ist die Support für Apache derzeit immer noch im
Beta-Stadium, weshalb ich die Zertifikate generieren aber nicht
automatisch in meine Konfiguration einbinden lasse.

Hier ist noch einmal meine Anleitung für ein Ubuntu 16.04 LTS:

#. Vorgehen gemäß
   `Anleitung <https://certbot.eff.org/#ubuntuxenial-apache>`__
#. PPA für das Paket add-apt-repository
   sudo apt install software-properties-common
#. sudo add-apt-repository ppa:certbot/certbot
#. sudo apt-get update
#. sudo apt install python-certbot-apache
#. Zertifikate generieren: sudo certbot --apache certonly
   Certs werden nach /etc/letsencrypt/www.bakera.de gespeichert
#. apache config angepasst gemäß `Anleitung <https://certbot.eff.org/docs/using.html#where-are-my-certificates>`__\ SSLCertificateFile
   /etc/letsencrypt/live/www.bakera.de/fullchain.pem
   SSLCertificateKeyFile /etc/letsencrypt/live/www.bakera.de/privkey.pem
#. Cronjob für die Erneuerung der Zertifiakte angelegt gemäß
   `Anleitung <https://certbot.eff.org/docs/using.html#re-creating-and-updating-existing-certificates>`__.
   42 3 \* \* \* /usr/bin/certbot renew --post-hook "service apache2
   restart"
