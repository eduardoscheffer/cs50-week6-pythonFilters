from cs50 import get_string

def main():

    text = get_text()

    numLetters = get_letters(text)

    numWords = get_words(text)

    numSentences = get_sentences(text)

    L = numLetters / numWords * 100
    S = numSentences / numWords * 100

    readibility = round(0.0588 * L - 0.296 * S - 15.8)

    if readibility < 1:
        print("Before Grade 1")
    elif readibility > 16:
        print("Total: 16+")
    else:
        print(f"Total: {readibility}")


def get_text():
    txt = get_string("Text: ")
    return txt


def get_letters(text):
    l = 0
    for c in text:
        if c.isalpha():
            l += 1
    return l

def get_words(text):
    w = 0
    for c in text:
        if c == " ":
            w += 1
    w += 1
    return w

def get_sentences(text):
    s = 0
    for c in text:
        if c in [".", "!", "?"]:
            s += 1
    return s

main()