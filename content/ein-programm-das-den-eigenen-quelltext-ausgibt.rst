Ein Programm, das den eigenen Quelltext ausgibt
###############################################
:date: 2014-05-02 18:15
:author: marco.bakera
:tags: Programmierung, Spaß
:slug: ein-programm-das-den-eigenen-quelltext-ausgibt
:status: published

|icon_commandline|

Ein
`Quine <https://de.wikipedia.org/wiki/Quine_%28Computerprogramm%29>`__
ist ein Programm, das den eigenen Quelltext ausgibt. Dabei darf nicht
auf Dateioperationen zurückgegriffen werden. Sonst wäre es zu einfach.
Dann könnte man einfach nur die Datei ausgeben, die den Quelltext
enthält.

Das schöne an dieser Aufgabenstellung ist, dass sie zunächst sehr
einfach und nach ein paar Versuchen faktisch unmöglich erscheint. Für
ein C#-Programm habe ich einen solchen Quine einmal selbst programmiert.
Es ist nicht die kürzeste Version, aber sie stellt recht gut das Prinzip
dar, nach dem derartige Programme aufgebaut sind: Daten und Programm
werden getrennt. Das Programm ist hierbei jedoch auch Teil der Daten.

::

        class MainClass {
            static string[] daten = {
                "  public static void Main(string[] args) {",
                "    Console.WriteLine(\"class MainClass{\");",
                "    Console.WriteLine(\"  static string[] daten = {\");",
                "    for (int i=0; i<daten.Length; i++) ",
                "      Console.WriteLine(\"  \\\"\"+daten[i]+\"\\\",\");",
                "    Console.WriteLine(\"  };\");",
                "    for (int i=0; i<daten.Length; i++)",
                "      Console.WriteLine(daten [i]);",
                "  }",
                "}" };

            public static void Main(string[] args) {
                Console.WriteLine("class MainClass{");
                Console.WriteLine("  static string[] daten = {");
                for (int i=0; i<daten.Length; i++)
                    Console.WriteLine("  \"" + daten[i] + "\",");
                Console.WriteLine("  };");
                for (int i=0; i<daten.Length; i++)
                    Console.WriteLine(daten [i]);
            }
        }

.. |icon_commandline| image:: {filename}images/2014/05/icon_16654.png
   :class: alignnone size-full wp-image-988
   :width: 300px
   :target: images/2014/05/icon_16654.png
