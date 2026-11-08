---
title: socialspec
date: 2026-11-08 16:42
author: marco.bakera
tags: blog, socialweb, opml
status: published
slug: socialspec
mastodon: https://chaos.social/@pintman/117581625544937644
---

Über einen [Blogpost von wirres.net](https://wirres.net/articles/social-spec-und-social-browser) bin ich auf [socialspec.org](https://socialspec.org) gestoßen. Eine einfache API bzw. Konvention, um Blogs besser in das Social Web zu integrieren. Unter `example.com/feed.xml` (oder `feed.json`) sind die neuesten Postings/Artikel, unter `example.com/.well-known/following.opml` liegen die Blogs, denen ich folge (also meine (recht alte) [Blogroll]({filename}blogroll2018.rst)), unter `example.com/.well-known/about.md` steht meine Bio und unter `example.com/.well-known/contact.vcf` liegt meine virtuelle Visitenkarte. 

Die Spec ist erst im Oktober entstanden und noch recht neu. Feedreader sollen damit um weitere soziale Features ergänzt werden.

Eigentlich könnte ich das einfach integrieren, weil sich das System gut mit statischen Seiten wie diesem Blog verträgt. 

