def count_words(text):
    return len(text.split())

def count_characters(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(dict):
    return dict["count"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)

    char_list = []

    for char, count in char_count.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})

    char_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")

if __name__ == "__main__":
    main()
