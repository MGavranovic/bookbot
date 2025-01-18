def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
    count_words(file_content)
    for_report = count_chars(file_content)
    create_report(for_report)

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

     return chars

def sort_on(dict):
    return dict["count"]

def create_report(dict):
    list_dict = []
    for i in dict:
        list_dict.append({"char": i, "count": dict[i]})
    
    list_dict.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    for i in list_dict:
        if i["char"].isalpha():
            print(f"The '{i["char"]}' character was found {i["count"]} times")
    print("--- End report ---")

main()