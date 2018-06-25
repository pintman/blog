Einen eigenen Webserver programmieren
#####################################
:date: 2014-10-04 13:44
:author: marco.bakera
:tags: Programmierung
:slug: einen-eigenen-webserver-programmieren
:status: published

| |browser|
| Wie funktioniert eigentlich ein Webserver? Ich habe eine ungefähre
  Vorstellung davon, was mein Browser macht, wenn ich eine Webseite
  aufrufe. Aber die genauen Details blieben mir bisher immer verborgen.
  Ich wollte es daher genauer wissen und habe selbst eine Webserver
  programmiert. Das ist gar nicht so schwer und jeder kann es selbst
  ausprobieren.
| 
| Unten findet ihr den Quelltext für einen einfachen Webserver, den ich
  in C# geschrieben habe. Ich habe bewusst nur auf der Netzwerkebene
  gearbeitet und weitere Abstraktionsebenen sowie schon vorhandene
  Serverkomponenten, die es in .NET gibt, nicht verwendet.

Nach dem Start des Programms, kann man mit einem Browser auf die Adresse
http://localhost:12345 zugreifen und auf den Unterseiten
http://localhost:12345/ip die eigene IP-Adresse und unter
http://localhost:12345/datum das aktuelle Datum erfahren. Der Browser
läuft auf dem Port 12345, um nicht mit anderen Diensten, die auf dem
Rechner bereits laufen, in Konflikt zu geraten.

Das Programm kann nun noch beliebig erweitert werden. Im Moment wird Typ
des verschickten Inhalts noch nicht berücksichtigt und nur Text
verwendet. Hier könnten man natürlich auch HTML-Seiten übermitteln und
z.B. eine statische HTML-Seite wie index.html ausliefern, wenn sie
angefordert wird. Oder der Server führt ein Programm mit Parametern aus
und sendet das Ergebnis zurück an den Browser. Ihr merkt, dass ich nicht
so kreativ bin wie ihr.

::


    using System;
    using System.Net;
    using System.Net.Sockets;

    namespace WebServer
    {
      class MainClass
      {
          public static void Main(string[] args)
          {
            while (true)
            {
              // IP-Adresse und Port des Servers
              IPAddress ipAdresse = IPAddress.Parse("127.0.0.1");
              IPEndPoint ipEndpunkt = new IPEndPoint(ipAdresse, 12345);
              Console.WriteLine("EndPoint: " + ipEndpunkt);

              // Socket erstellen, mit Endpoint verbinden und auf Verbindung warten
              Socket socketServer = 
                new Socket(ipEndpunkt.AddressFamily, SocketType.Stream, ProtocolType.Tcp);
              socketServer.Bind(ipEndpunkt);
              socketServer.Listen(1); // Backlog = Anzahl wartender Verbindungen

              // Daten empfangen und in Byte-Array ablegen
              byte[] buffer = new byte[512];
              Socket socketClient = socketServer.Accept();
              Console.WriteLine(
                "Verbindung hergestellt mit " + socketClient.RemoteEndPoint);
              socketClient.Receive(buffer);

              // Empfangene Daten ausgeben
              Console.WriteLine("Empangene Daten:");
              string sDaten = "";
              for (int i = 0; i < buffer.Length && buffer[i] != 0; i++)
              {
                sDaten += (char)buffer [i];
              }
              Console.WriteLine(sDaten);

              // Daten auswerten und Anwort erstellen
              string sAntwort = "";
              if (sDaten.Contains("GET /ip"))
              {
                sAntwort = "Deine IP lautet " + socketClient.RemoteEndPoint;
              } 
              else if(sDaten.Contains("GET /datum"))
              {
                sAntwort = "Das heutige Datum ist " + DateTime.Now;
              }
              else
              {
                sAntwort = "Was willst du machen?";
              }

              // Antwort in Byte-Array konvertieren und senden
              buffer = new byte[sAntwort.Length];
              for (int i = 0; i < sAntwort.Length; i++)
              {
                buffer [i] = (byte) sAntwort[i];
              }
              socketClient.Send(buffer);

              // Sockets schließen
              socketClient.Close();
              socketServer.Close();
          }
        }
      }
    }

.. |browser| image:: {filename}images/2014/10/browser.png
   :class: alignright size-full wp-image-1433
   :width: 128px
   :height: 128px
