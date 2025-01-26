def get_num(dictionary):
    return dictionary["num"]

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars_dict = {}
    for t in text:
        lowered_t = t.lower()
        if lowered_t in chars_dict:
            chars_dict[lowered_t] += 1
        else:
            chars_dict[lowered_t] = 1
    return chars_dict

def main():    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    char_dict = count_chars(file_contents)
    
    # Convert dictionary to list and filter alphabets
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            new_dict = {"char": char, "num": count}
            char_list.append(new_dict)
    
    # Sort the list
    char_list.sort(key=get_num, reverse=True)
    
    # Now let's print the report
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    
    # Print each character count
    for char_info in char_list:
        print(f"The '{char_info['char']}' character was found {char_info['num']} times")
    
    print("--- End report ---")

if __name__ == "__main__":
    main()