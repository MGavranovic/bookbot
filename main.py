def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
    print(file_content)
    count_words(file_content)
    count_chars(file_content)

def count_words(txt):
    words = txt.split()
    count = 0
    for w in words:
        count += 1
    return str(count)

def count_chars(txt):
     chars = {}
     text = txt.lower()
     
     for char in text:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1

     print(chars)


main()