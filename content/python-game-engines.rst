Python Game-Engines im Vergleich
================================
:date: 2018-08-07 12:02
:author: marco.bakera
:tags: Programmierung, Python, Spiele
:status: published
:slug: python-game-engines


.. image:: {filename}images/2018/Gamepad-Black.svg
   :alt: Gamepad (Quelle: https://openclipart.org/detail/212647/gamepad-black)
   :width: 60%

Auf der Suche nach einer Spiele-Engine habe ich mir verschiedene Engines
für Python angeschaut. Die folgende Liste fasst Vor- und Nachteile zusammen.
Explizit ausgenommen habe ich 3D-Engines wie *Blender* oder *Panda 3D*.


`Pygame <http://pygame.org>`_
  :Pro: 
    Etabliert und weit verbreitet, Unterstützung für den Raspberry Pi, gut 
    dokumentiert, eingebaute Kollisionserkennung, breite 
    Hardware-Unterstützung (MIDI, Kamera, CD-ROM)
  
  :Contra: 
    API stellenweise schwer verständlich, wenig OOP, basiert auf SDL

`Pygame Zero <http://pygame-zero.readthedocs.io>`_
  :Pro: 
    Abstraktion basiert auf Pygame, durchdachte API, automatische 
    Ressourcenverwaltung für Bilder und Sounds, könnte in Zukunft Pygame ablösen
  
  :Contra: 
    kein Gamepad Support (aber 
    `geplant <https://github.com/lordmauve/pgzero/issues/70>`_)


`Cocos2d <http://cocos2d.org>`_
  :Pro:
    Professionelle Erscheinung, breite Toolunterstützung, Unterstützung
    für viele Programmiersprachen neben Pyhon, Game-Engine vom Spieledesigner 
    getrennt, Unterstützung für mehrere Zielplattformen (Desktop und Mobile)
  
  :Contra: 
    Designer für Spiele nur für Windows und Mac, nicht aber für Linux erhältlich,
    komplexe API, komplizierte Installation


`Arcade Academy <http://arcade.academy/>`_
  :Pro: 
    einfache API, integrierte Physik-Engine, basiert auf OpenGL, viel 
    Beispiel-Code.
  
  :Contra: 
    mindestens Python 3.6 notwendig, entwickelt von 1-2 Entwicklern


Fazit
-----

Derzeit scheint pygame mit seiner langen Tradition der defacto Standard für
kleine Spiele mit Python-Unterstützung zu sein. Es gibt viele Erweiterungen
und Dokumentationen an unterschiedlichen Stellen und es gut, die Bibliothek
zu kennen. Die Frischzellenkur *Pygame
Zero* tritt an, ein würdiger Nachfolger zu werden. Dezeit muss man jedoch 
noch Abstriche bei der Feature-Auswahl machen.

