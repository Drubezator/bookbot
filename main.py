from stats import get_num_words
from stats import get_char_counts
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_char_counts(text)
    return book_path, num_words, char_counts

def get_book_text(path):
    with open(path) as f:
        return f.read()

cesta, slova, pocty_pismen = main()


print(f"============ BOOKBOT ============\nAnalyzing book found at {cesta}\n----------- Word Count ----------\nFound {slova} total words\n--------- Character Count -------")
for pismeno in sorted(pocty_pismen):
    pocet = pocty_pismen[pismeno]
    print(f"{pismeno}: {pocty_pismen[pismeno]}")
print("============= END ===============")

    

