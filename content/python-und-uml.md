---
title: Python und UML
date: 2026-11-09 14:52
author: marco.bakera
tags: Python, Programmierung, Bildung, Tools, llm
status: published
slug: python-und-uml
mastodon: https://chaos.social/@pintman/117586894804836526
---

Ich habe [wieder]({filename}screen-control.md) ein kleines Tool gebaut – genauer: bauen lassen. Heute macht man das ja mit KI. Ich habe hierfür [Claude Code](https://claude.com/product/claude-code) als Coding-Harness und [OpenSpec](https://github.com/Fission-AI/OpenSpec) als Vorgehensmodell genutzt. Details zum Quelltext liegen [hier](https://github.com/pintman/pyuml).

Welches Problem soll gelöst werden? Im Unterricht geht es im Bereich der objektorientierten Programmierung auch immer wieder um UML-Klassendiagramme. Um den Bezug zum Quelltext direkt sehen zu können, ist ein kleines Tool entstanden, das links den Quelltext und rechts das passende Klassendiagramm zeigt. Änderungen am Quelltext führen dann zu einer Änderung im Klassendiagramm.

![PyUML: links Python-Quelltext mit Klassen, rechts das daraus erzeugte UML-Klassendiagramm]({static}/images/2026/pyuml.png)

Probiert es gerne aus und nutzt es selbst für eure Zwecke.

PyUML ausprobieren:
<https://pintman.github.io/pyuml/>
