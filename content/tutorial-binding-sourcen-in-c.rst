Tutorial: Binding Sourcen in C#
###############################
:date: 2013-01-04 10:07
:author: admin
:tags: Programmierung
:slug: tutorial-binding-sourcen-in-c
:status: published

| Mit Hilfe von Bindings können in C# Datenobjekte an eine GUI gebunden
  werden. Wenn sich etwas an den Datenobjekten ändert, wird die GUI
  automatisch aktualisiert. Andererseits können Änderungen an den
  Objekten direkt über die GUI vorgenommen werden. Man muss sich nach
  der Bindung also keine Gedanken mehr machen, dass die GUI aktualisiert
  wird, wenn sich an den Daten etwas ändert. Für gewöhnlich würde man
  für diesen Zweck das Observer-Pattern verwenden, als Obeserver (GUI)
  beim Observable (den Datenklassen) registrieren und auf Änderungen
  horchen.
| ` <>`__
| Wir werden im Folgenden ein kleines Beispielprojekt in Visual Studio
  2010 erstellen, das diesen Zusammenhang veranschaulicht. Die
  Feinheiten erledigt Visual Studio im Hintergrund, wenn wir uns an ein
  paar Regeln halten.
| Dazu erstellen wir zunächst ein neues Projekt.

.. raw:: html

   <div>

|image0|

.. raw:: html

   </div>

.. raw:: html

   <div>

In dem neuen Projekt erstellen wir eine Klasse Person, die an drei
GUI-Elemente gebunden werden soll. In diesem kleinen Beispiel verwende
ich eine TextBox, ein NumericUpDown und ein DataGridView als
GUI-Elemente. Die Klasse Person hat lediglich die beiden Attribute
"name" und "alter".
Insgesamt ergibt sich das folgende Bild.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   <div>

|image1|

.. raw:: html

   </div>

.. raw:: html

   </div>

| 
| Zunächst erstellen wir die Klasse des Datenobjektes: Person.

.. raw:: html

   <div>

|image2|

.. raw:: html

   </div>

| 
| Wir geben den Namen der Datei an, in der die Klasse landen soll:
  Person.cs.

.. raw:: html

   <div>

|image3|

.. raw:: html

   </div>

| 
| Die neue erzeugte Klasse macht nicht viel. Sie hält lediglich unsere
  Daten. Neben den beiden Attributen name und alter existieren nur
  entsprechende Zugriffsmethoden, die in C# als Properties realisiert
  sind. Der Quelltext der Klasse sieht damit wie folgt aus.

.. raw:: html

   <div>

|image4|

.. raw:: html

   </div>

| 
| Die neu erstellte Klasse Person soll als Datenquelle dienen. Dazu
  fügen wir dem Projekt eine neue Datenquelle hinzu.

.. raw:: html

   <div>

|image5|

.. raw:: html

   </div>

| 

.. raw:: html

   <div>

Da es sich um eine Klasse, und nicht etwa um eine Datenbank handelt,
verwenden wir an dieser Stelle den Typ Objekt.

.. raw:: html

   </div>

| 

.. raw:: html

   <div>

|image6|

.. raw:: html

   </div>

| 

.. raw:: html

   <div>

In der sich zeigenden Liste, wählen wir unsere Klasse Person aus.

.. raw:: html

   </div>

| 

.. raw:: html

   <div>

|image7|

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Nun ist die Klasse bei den Datenquellen zu finden und wir können sie an
unsere Steuerelemente binden.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Damit die neue Datenquelle gefunden wird, muss das Projekt einmal
gestartet werden, indem wir auf den grünen Pfeil drücken.

.. raw:: html

   </div>

.. raw:: html

   <div>

|image8|

.. raw:: html

   </div>

| 

.. raw:: html

   <div>

.. raw:: html

   </div>

| 

.. raw:: html

   <div>

Wir beenden unser Programm sofort wieder. Nun taucht unsere Datenquelle
mit den entsprechenden Attributen bei den Datenquellen auf.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

|image9|

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Jetzt können wir endlich Hand an unsere GUI legen. Wir wählen eine
TextBox, ein NumericUpDown und ein DataGridView als Steuerelemente aus
und ziehen diese Elemente auf unseren Designer.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

|image10|

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Beim Einfügen des DataGridViews, fragt die Komponente direkt nach ihrer
Datenquelle. Die Datenquelle sorgt dafür, dass es in der Komponente
etwas zum Anzeigen gibt – wie der Name eigentlich schon sagt. Wir wählen
die Person als Datenquelle aus.

.. raw:: html

   </div>

| |image11|

.. raw:: html

   <div>

Es wird automatisch eine BindingSource hinzugefügt, die das
Steuerelement mit der Personenklasse verbindet.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

|image12|

.. raw:: html

   </div>

| 

.. raw:: html

   <div>

Alle Änderungen an einer Person werden nun nicht mehr direkt auf der
Klasse, sondern über die BindingSource geregelt. Andererseits werden
Änderungen an der Person über die BindingSource den GUI-Komponenten
bekannt gemacht. Die BindingSource fungiert als Vermittler zwischen der
Darstellung in der GUI und den Daten im Datenobjekt – also der Person.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <p>

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

| Für das Textfeld wählen wir das Attribut Name als Datenquelle in der
  BindingSource aus: das Textfeld soll immer den Namen der aktuellen
  Person anzeigen.

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

|image13|

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Für das NumericUpDown wird entsprechend das Alter gewählt.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

|image14|

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Damit ist die kleine Anwendung schon fertig. Wenn wir sie starten,
können neue Personen über das DatagridView eingegeben und geändert
werden. Gleichzeitig werden die beiden anderen Komponenten - die TextBox
mit dem Namen und das NumericUpDown mit dem Alter - automatisch
aktualisiert. 

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Spiele etwas mit der kleinen Anwendung herum und schau, wie mühelos die
Verbindung zwischen dem Datenobjekt Person und der Oberfläche
funktioniert.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

|image15|

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

An dieser Stelle kannst du `das vollständige Projekt als Visual Studio
2010
Solution <https://docs.google.com/open?id=0B7xDwPYvx9_LNV9fMXFKMmFDVEU>`__
herunterladen.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. |image0| image:: http://4.bp.blogspot.com/-sbD1ZkFJQSc/UOHDTbJea-I/AAAAAAAACOk/I_HukExFbAY/s1600/Binding+Source+Beispiel+-+quer_html_666c530d.png
   :target: http://4.bp.blogspot.com/-sbD1ZkFJQSc/UOHDTbJea-I/AAAAAAAACOk/I_HukExFbAY/s1600/Binding+Source+Beispiel+-+quer_html_666c530d.png
.. |image1| image:: http://4.bp.blogspot.com/-1_AnqVB63T0/UOHTUaGeERI/AAAAAAAACRE/JcjV1UpFBII/s1600/klassendiagramm_person_fenster.png
   :target: http://4.bp.blogspot.com/-1_AnqVB63T0/UOHTUaGeERI/AAAAAAAACRE/JcjV1UpFBII/s1600/klassendiagramm_person_fenster.png
.. |image2| image:: http://4.bp.blogspot.com/-RPvu9VMDgoM/UOHDVQ-sVdI/AAAAAAAACO0/CWrN47d5JiI/s1600/Binding+Source+Beispiel+-+quer_html_748a4276.png
   :target: http://4.bp.blogspot.com/-RPvu9VMDgoM/UOHDVQ-sVdI/AAAAAAAACO0/CWrN47d5JiI/s1600/Binding+Source+Beispiel+-+quer_html_748a4276.png
.. |image3| image:: http://4.bp.blogspot.com/-m1bBwUqEDok/UOHDXTRjE6I/AAAAAAAACPE/RSATyWuOc_8/s1600/Binding+Source+Beispiel+-+quer_html_m63807da4.png
   :target: http://4.bp.blogspot.com/-m1bBwUqEDok/UOHDXTRjE6I/AAAAAAAACPE/RSATyWuOc_8/s1600/Binding+Source+Beispiel+-+quer_html_m63807da4.png
.. |image4| image:: http://1.bp.blogspot.com/-_B_x-uRsIfs/UOHDPDZ229I/AAAAAAAACN4/sbWUcbAls4s/s1600/Binding+Source+Beispiel+-+quer_html_22f4e63.png
   :target: http://1.bp.blogspot.com/-_B_x-uRsIfs/UOHDPDZ229I/AAAAAAAACN4/sbWUcbAls4s/s1600/Binding+Source+Beispiel+-+quer_html_22f4e63.png
.. |image5| image:: http://3.bp.blogspot.com/-F8EcKO29Cmc/UOHDR_qOeEI/AAAAAAAACOY/uSxkaurVSLQ/s1600/Binding+Source+Beispiel+-+quer_html_5e8bcdd7.png
   :target: http://3.bp.blogspot.com/-F8EcKO29Cmc/UOHDR_qOeEI/AAAAAAAACOY/uSxkaurVSLQ/s1600/Binding+Source+Beispiel+-+quer_html_5e8bcdd7.png
.. |image6| image:: http://4.bp.blogspot.com/-Ds4M67cWtN4/UOHDOVDVRSI/AAAAAAAACN0/dqClLkk3vCE/s1600/Binding+Source+Beispiel+-+quer_html_10e97626.png
   :target: http://4.bp.blogspot.com/-Ds4M67cWtN4/UOHDOVDVRSI/AAAAAAAACN0/dqClLkk3vCE/s1600/Binding+Source+Beispiel+-+quer_html_10e97626.png
.. |image7| image:: http://2.bp.blogspot.com/-gheQTeUrvPc/UOHFIzZdAtI/AAAAAAAACQk/VdptjoEYyxM/s1600/Binding+Source+Beispiel+-+quer_html_m750ee31b.png
   :target: http://2.bp.blogspot.com/-gheQTeUrvPc/UOHFIzZdAtI/AAAAAAAACQk/VdptjoEYyxM/s1600/Binding+Source+Beispiel+-+quer_html_m750ee31b.png
.. |image8| image:: http://3.bp.blogspot.com/-_KSG_ajIeHo/UOHDYDoCA_I/AAAAAAAACPI/6E4cA3HQq58/s1600/Binding+Source+Beispiel+-+quer_html_m6a054a16.png
   :target: http://3.bp.blogspot.com/-_KSG_ajIeHo/UOHDYDoCA_I/AAAAAAAACPI/6E4cA3HQq58/s1600/Binding+Source+Beispiel+-+quer_html_m6a054a16.png
.. |image9| image:: http://1.bp.blogspot.com/-3bUIF8EtZSs/UOHDZpn-YbI/AAAAAAAACPY/j5s21-sINk4/s1600/Binding+Source+Beispiel+-+quer_html_m79564e59.png
   :target: http://1.bp.blogspot.com/-3bUIF8EtZSs/UOHDZpn-YbI/AAAAAAAACPY/j5s21-sINk4/s1600/Binding+Source+Beispiel+-+quer_html_m79564e59.png
.. |image10| image:: http://2.bp.blogspot.com/-9ojvrak_GME/UOHDUS8587I/AAAAAAAACOs/B6RnmQeLWCc/s1600/Binding+Source+Beispiel+-+quer_html_6e7677c5.png
   :target: http://2.bp.blogspot.com/-9ojvrak_GME/UOHDUS8587I/AAAAAAAACOs/B6RnmQeLWCc/s1600/Binding+Source+Beispiel+-+quer_html_6e7677c5.png
.. |image11| image:: http://3.bp.blogspot.com/-1XPyx2UR8_Q/UOHDRKcCY4I/AAAAAAAACOQ/i8-76D7GzX4/s1600/Binding+Source+Beispiel+-+quer_html_457a6f8.png
   :target: http://3.bp.blogspot.com/-1XPyx2UR8_Q/UOHDRKcCY4I/AAAAAAAACOQ/i8-76D7GzX4/s1600/Binding+Source+Beispiel+-+quer_html_457a6f8.png
.. |image12| image:: http://2.bp.blogspot.com/--ePmtk9zR6M/UOHDV5f5YvI/AAAAAAAACO4/2tFibWYOdyA/s1600/Binding+Source+Beispiel+-+quer_html_ecbbb66.png
   :target: http://2.bp.blogspot.com/--ePmtk9zR6M/UOHDV5f5YvI/AAAAAAAACO4/2tFibWYOdyA/s1600/Binding+Source+Beispiel+-+quer_html_ecbbb66.png
.. |image13| image:: http://2.bp.blogspot.com/-KwFJVcB9DVM/UOHDaTWXS9I/AAAAAAAACPg/LFFvY1vgJ2I/s1600/Binding+Source+Beispiel+-+quer_html_maf43c17.png
   :target: http://2.bp.blogspot.com/-KwFJVcB9DVM/UOHDaTWXS9I/AAAAAAAACPg/LFFvY1vgJ2I/s1600/Binding+Source+Beispiel+-+quer_html_maf43c17.png
.. |image14| image:: http://1.bp.blogspot.com/-B-796v7RNy4/UOHDcFcKhwI/AAAAAAAACPw/QGVNyfmK1JU/s1600/Binding+Source+Beispiel_html_27ce6f3b.png
   :target: http://1.bp.blogspot.com/-B-796v7RNy4/UOHDcFcKhwI/AAAAAAAACPw/QGVNyfmK1JU/s1600/Binding+Source+Beispiel_html_27ce6f3b.png
.. |image15| image:: http://2.bp.blogspot.com/-C3T6OamXqUg/UOHGZP7Sq6I/AAAAAAAACQ0/Ddvvu5FRVgc/s1600/Binding+Source+Beispiel+-+quer_html_34c4ed4b.png
   :target: http://2.bp.blogspot.com/-C3T6OamXqUg/UOHGZP7Sq6I/AAAAAAAACQ0/Ddvvu5FRVgc/s1600/Binding+Source+Beispiel+-+quer_html_34c4ed4b.png
