def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_counts(text):
    counts = {}
    for c in text.lower():
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts


def get_sorted_char_counts(char_counts):
    alpha_counts = {char: count for char, count in char_counts.items() if char.isalpha()}
    sorted_counts = sorted(alpha_counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_counts
