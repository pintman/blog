---
name: audio-blogpost
description: Transkribiert eine Audioaufnahme (Sprachnotiz, m4a/mp3/wav) lokal mit mlx-whisper und bereitet daraus einen Blogpost-Entwurf in content/ vor. Nur per /audio-blogpost aufrufen.
disable-model-invocation: true
---

# Audioaufnahme → Blogpost-Entwurf

## 1. Datei finden
- Pfad aus Argument verwenden, sonst neueste Audiodatei in `~/Downloads`:
  `ls -t ~/Downloads/*.{m4a,mp3,wav,ogg,opus} 2>/dev/null | head -1`
- Dateinamen nennen. Mehrere Kandidaten von heute → nachfragen.

## 2. Transkribieren (lokal, kein Upload)
Ausgabe in einen eigenen Ordner im Scratchpad (nicht ins Repo):

```bash
HF_HOME=~/data1/LLM/hugging_face uvx --from mlx-whisper mlx_whisper "<datei>" \
  --model mlx-community/whisper-large-v3-turbo \
  --language de --output-format txt --output-dir "<scratchpad>/transcript"
```

- `HF_HOME` immer auf `~/data1/LLM/hugging_face` setzen (gilt für alle Hugging-Face-Modelle). Modell wird beim ersten Lauf geladen (~1,6 GB).
- Benötigt ffmpeg (vorhanden via Homebrew).
- Transkript lesen und dem Nutzer kurz zeigen.

## 3. Post anlegen
- Titel und Tags aus dem Inhalt ableiten. Vorhandene Tags bevorzugen:
  `grep -h '^tags:' content/*.md | sed 's/^tags: *//' | tr ',' '\n' | sed 's/^ *//' | sort | uniq -c | sort -rn | head -50`
- `./newpost.sh -n "Titel" "tag1, tag2"` → legt `content/<slug>.md` mit `status: draft` an.

## 4. Text schreiben
- Geglättet in der Stimme des Autors: Füllwörter, Versprecher, Wiederholungen raus; Absätze, bei Bedarf Zwischenüberschriften (`##`).
- Ich-Perspektive, Tonfall und Inhalt erhalten. Nichts hinzuerfinden, keine Fakten ergänzen.
- Erwähnte Links/Projekte nur verlinken, wenn die URL sicher bekannt ist.
- Vermutlich falsch erkannte Begriffe (Eigennamen, Fachbegriffe) im Chat auflisten und nachfragen.
- Transkript und Audio nicht ins Repo kopieren.

## 5. Abschluss
- Pfad der Post-Datei nennen.
- Kein Commit, kein Statuswechsel auf `published`, kein Mastodon/LinkedIn – nur auf ausdrücklichen Wunsch (Workflow siehe CLAUDE.md).
