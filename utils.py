MAX_CHARACTERS = 5000

def get_counts(text):
    if text is None:
        text = ""

    char_count = len(text)
    word_count = len(text.split())

    return (
        f"<div class='counter'>📝 Characters: {char_count} / {MAX_CHARACTERS}</div>",
        f"<div class='counter'>📖 Words: {word_count}</div>"
    )