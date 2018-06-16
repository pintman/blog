Spielereien auf der Kommandozeile: Temperaturanzeige
####################################################
:date: 2014-01-26 18:02
:author: marco.bakera
:tags: Linux, Programmierung
:slug: spielereien-auf-der-kommandozeile-temperaturanzeige
:status: published

Ich fragte mich, wie schwer es ist, die aktuelle Temperatur für meinem
Wohnort Dortmund zu bestimmen. Mit der Bash und mit Hilfe der
`Yahoo-Weather-API <http://developer.yahoo.com/weather/>`__ lies sich
das Problem mit einer Zeile lösen. Die API benutzt eine sogenannte WOEID
(Where On Earth ID), die ich mir aus der Adresszeile der
`Yahoo-Wetterseite <http://weather.yahoo.com/>`__ geliehen habe. Für
Dortmund lautet sie 645458.

::

    curl -s 'http://weather.yahooapis.com/forecastrss?w=645458&u=c' 
      | grep yweather:condition 
      | sed -e 's/.*temp="//' 
      | sed -e 's/".*//'

#. Zunächst hole ich mir mit curl den RSS-Feed für meinen Ort und wähle
   mit u=c die Einheit Celsius für die Temperaturen. Die Option -s
   (silent) unterdrückt die Fortschrittsanzeige von curl.
#. Mit grep extrahiere ich die Zeile mit den aktuellen
   Wetterinformationen.
#. Sed schneidet anschließend den vorderen Teil der Anzeige bis zur
   Temperatur ab.
#. Zum Schluss löscht das zweite sed alles ab dem Anführungszeichen
   hinter der Temperaturangabe.

Ich weiß natürlich, dass die Lösung eher schnell und pragmatisch, denn
erweiterbar und robust ist. Ich hoffe, sie zeigt dennoch das
Zusammenspiel verschiedener Linux-Tools und die Macht von Pipes.
