---
title: LLM passt Gewichte direkt an
date: 2026-11-06 17:27
author: marco.bakera
tags: llm, Informatik, Wissenschaft
status: published
slug: llm-passt-gewichte-direkt-an
---

Der neue heiße Schice: Weight-Space-Programming. Hierbei schreiben LLMs direkt ins Hirn eines anderen LLM.

> We find that frontier LLMs are surprisingly good at natively reading and writing neural network weights, using a variety of recent tools and algorithms or even via direct weight editing. These results show sparks of Weight-Space Programming, which may extend beyond what we’d expect from humans or conventional algorithms. This might be a big deal for both optimization and interpretability.

Das LLM verändert die Gewichte des anderen Modells direkt und kann so die Mathe-Fähigkeiten eines eigentlich schwachen Modells verbessern:

> Likewise, asked to make Qwen3.5-0.8B better at math without gradients, Astra identifies an issue in its weights causing reasoning loops that Qwen’s own model card warns about, and fixes this by natively editing 0.016% of the weights. With the same sampling settings, this weight correction raises MATH-500 from 7.9% to 48.1% and generalizes out of the box to instruction following, raising IFEval by 3x.

[Rikiya Takehi, Jayden Teoh, Alex Zhang, and Omar Khattab. “Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights.” November 2026](https://rikiyat.github.io/blog/weight-space-programming/)
