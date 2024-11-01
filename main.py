def main():
    path = "books/frankenstein.txt"
    content = read_content(path)
    words = count_words(content)
    chars = count_characters(content)
    list_result = convert_to_sorted_list(chars)
    pretty_print(path, words, list_result)

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lower_text = text.lower()
    chars = {}
    for char in lower_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def convert_to_sorted_list(dict):
    new_list = []
    for k in dict:
        if k.isalpha():
            new_list.append({"char": k, "num": dict[k]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list

def read_content(path):
    with open(path) as f:
        file_content = f.read()
    return file_content

def pretty_print(path, w_count, ch_list):
    print(f"--- Begin report of {path} ---")
    print(f"{w_count} words found in the document")
    print()
    for item in ch_list:
        c = item["char"]
        n = item["num"]
        print(f"The '{c}' character was found {n} times")
    print("--- End report ---")


main()
