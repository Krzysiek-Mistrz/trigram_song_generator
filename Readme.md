# Trigram Song Generator

Aplikacja generuje nowy tekst piosenki na podstawie istniejącego tekstu przy użyciu modelu trójgramowego (trigram). Wystarczy że podasz swój tekst do pliku song.txt.

## Instalacja

```bash
pip3 install -r requirements.txt
```

Dodatkowo jednorazowo zainstaluj tokenizery NLTK:

import nltk
nltk.download('punkt')

## Uruchomienie

Wystarczy uruchomić:

```bash
python main.py
```

Wygenerowany tekst pojawi się w terminalu.

## Struktura

    data/song.txt — wejściowy tekst piosenki

    model/ — logika tokenizacji i budowy modelu

    app/ — kod generujący nowy tekst  

GNU GPL V3 @ Krzychu 2025