
def main():
    path_of_book ="books/Frankenstein.txt"
    text = Read(path_of_book)
    number_of_words = Counter(text)
    print(number_of_words)
    charactersDictionary = Character_dict(text.lower())
    print ("--- Begin report of "+path_of_book+" --- ")
    print(str(number_of_words)+" words found in the document")
    print()
    for i in charactersDictionary:
        print("The '" + i[0] + "' character was found " + str(i[1]) + " times.")
    print("--- End report ---")
    


def Read(name):

    with open(name) as f:
        return f.read()

def Counter(text):
    list_of_words=text.split()
   
    return len(list_of_words)

def Character_dict(text):
    char_dict ={}
    for i in text:
        if i.isalpha():
            if i in char_dict.keys():
                char_dict[i] += 1
            else:
                char_dict[i] = 1

    char_dict = sorted(char_dict.items(), key= lambda x:x[1], reverse= True)

    return char_dict



main()
