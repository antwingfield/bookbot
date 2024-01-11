def main():
    book_name = "Frankenstein"
    book_location = "books/frankenstein.txt"

    content = open_file(book_location)

    print_report(book_name, word_count(content), letter_count(content))


def open_file(loc):
    with open(loc) as f:
        return f.read()


def word_count(text):
    words = text.split()
    return len(words)


def letter_count(text):
    text = text.lower()
    letters = {}
    for letter in text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters


def print_report(book, word_count, letter_count):
    letter_list = []

    for entry in letter_count:
        if entry.isalpha():
            letter_list.append((entry, letter_count[entry]))

    letter_list.sort()
    print()
    print(f"[----------------Report on {book}-----------------]")
    print()
    print(f"There are {word_count} words in the book.")
    print()
    print("The following lists the amount of times each letter appears in the book:")
    for letter in letter_list:
        print(f"The letter {letter[0]} apears {letter[1]} times")
    print()
    print(f"[--------------End Report on {book}---------------]")
    print()


main()
