from EditDistance import *


def main():
    word_one = "Dog"
    word_two = "Pencil"
    print("First String: " + word_one)
    print("Second String: " + word_two)
    print()
    print("Minimum number of edits to convert " + word_one + " to " + word_two + ": ", end="")
    print(edit_distance(word_one, word_two, len(word_one), len(word_two)))
    print()

    word_one = "Shoe"
    word_two = "Sure"
    print("First String: " + word_one)
    print("Second String: " + word_two)
    print()
    print("Minimum number of edits to convert " + word_one + " to " + word_two + ": ", end="")
    print(edit_distance(word_one, word_two, len(word_one), len(word_two)))


main()
