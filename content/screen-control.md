---
title: BYOD in Klausuren
date: 2026-10-22 09:30
author: marco.bakera
tags: bildung, programmierung
status: published
slug: byod-in-klausuren
---

Schon eine ganze Weile schreibe ich Klausuren nach dem [BYOD](https://de.wikipedia.org/wiki/Bring_your_own_device)-Prinzip gerade im Bereich Programmieren auf den Geräten der Schüler:innen. Das hat bislang auch gut funktioniert. Mit dem Einzug von KI sind natürlich auch diese Systeme auf die Schüler-Rechner gewandert und so musste ich von einer vertrauensvollen Arbeitsweise zu einer stärkeren Überwachung wechseln. Eigentlich finde ich das schade und möchte das auch gar nicht machen.

So entstand die Idee, die Bildschirme der Schüler:innen während der Klausur überwachen zu können. Das macht man ja bei Papierklausuren auch so. Die vorhandenen Lösungen haben mir nicht so wirklich gut gefallen und so habe ich mich auf den Weg gemacht, ein eigenes System zu erstellen. Der technische Arbeitstitel für das Projekt lautet screen-control. Im Moment ist das bei GitHub nur als privates Repository gehostet. Aber mal schauen, wenn es irgendwann reif ist, kann ich das auch veröffentlichen.

Heutzutage macht man das natürlich nicht mehr per Hand, sondern nutzt KI-Systeme: genauer gesagt habe ich [Claude Code](https://claude.com/product/claude-code) als Harness genutzt und [OpenSpec](https://github.com/Fission-AI/OpenSpec) als Vorgehensmodell.

Zunächst habe ich mir grundsätzlich Gedanken gemacht, wie das System laufen soll. Die Schüler:innen sollen eine Webseite aufrufen und dann ihren kompletten Bildschirm darüber freigeben. Die Bildschirme werden dann auf einem Lehrer-PC in einer Kachelansicht angezeigt. Bei Beendigung der Freigabe oder Verbindungsabbrüchen soll es eine Warnung geben. Ebenso soll ein Archiv aus den gesammelten Screenshots entstehen.

Da ich hauptsächlich mit fachlichen Dingen beschäftigt war, musste ich mich gedanklich nicht um technische Details der Umsetzung sorgen. Das hat erstaunlich gut funktioniert.

In OpenSpec kann man mit *openspec-explore* erste Gedanken mit der KI untersuchen. Mit *openspec-proposal* kann man dann einen Vorschlag für eine Änderung erstellen, die im Anschluss mit *openspec-apply* umgesetzt wird. Nach der Umsetzung wird die Änderung mit *openspec-archive* archiviert.

Den Entwicklungsprozess habe ich als recht entspannend empfunden. Den Quelltext habe ich mir nur sehr rudimentär angeschaut - hauptsächlich die Test-Cases. Die Vorschläge, die durch diesen Prozess entstanden sind, waren durchaus kreativ: so soll etwa im Prozess des Deployments ein technisch versierter Kollege das System selbst einmal installieren.

