import sys
def check_word(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        print(f"The word \'{word}\' is palindrome.")
    else:
        print(f"The word \'{word}\' is not palindrome.")

def main():
    word = sys.argv[1]
    check_word(word)

if __name__ == '__main__':
    main()
