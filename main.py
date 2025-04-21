from app.generate import generate_text

if __name__ == '__main__':
    with open("data/song.txt", "r", encoding="utf-8") as file:
        song_text = file.read()
    generated = generate_text(song_text)
    print("\nWygenerowany tekst:\n")
    print(generated)
