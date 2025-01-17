def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
    print(file_content)
    count_words(file_content)

def count_words(txt):
    words = txt.split()
    count = 0
    for w in words:
        count += 1
    return str(count)


main()