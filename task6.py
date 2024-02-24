def num_words(text):
    symbols_to_remove = ",!?."
    for symbol in symbols_to_remove:
        text = text.replace(symbol, "")
    words = text.split()
    return len(set(words))


print(num_words(text=""))
