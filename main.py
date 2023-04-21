def main():
    file_path = "captions_text.vtt"

        #Take input words from user
    old_word = input("Enter the word you want to replace it: ")
    new_word = input("Enter the new word: ")

        #Find and replace the word in the file
    with open(file_path, 'r') as file:
        text = file.read()
        if old_word in text:
            print("The word '{}' exist in the file ".format(old_word))
            index = text.find(old_word)
            print(text[:index] + '\033[1m' + old_word + '\033[0m' + text[index + len(old_word):])
            text = text.replace(old_word, new_word)
            with open(file_path, 'w') as file:
                file.write(text)
            print("The word has been replaced with '{}' in the file.".format(new_word))
        else:
            print("The word '{}' does not exist in the file.".format(old_word))

        
main()
