def print_upper_words (words, must_start_with):
    """Prints word in list of words all caps"""
    for letter in must_start_with:
         for word in words:
            if word.startswith(letter):
                print(word.upper())
                break
