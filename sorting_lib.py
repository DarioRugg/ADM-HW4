
"""import string
alfabet = string.ascii_lowercase
strings = ["ciao", "ciaoo", "ai"]

for char in alfabet:
    print(char, ord(char), end="  ")

print("\n")

identifiers = []
for string in strings:
    identifier = [str(ord(char)).rjust(3, '0') for char in string] #we use rjust since we want al number of 3 digits
    identifier = int("".join(identifier).ljust(5*3, '0')) #adding 0s at the right, we want all numbers of equal lenght
    identifiers.append(identifier)
print(identifiers)
print(sorted(identifiers))

test = ["123", "123"]
print( "".join(test).ljust(5*3, '0'))

"""


def __max_len(list_of_strings):
    max_len = 0
    for string in list_of_strings:
        max_len = max(max_len, len(string))
    return max_len

def __to_ascii(list_of_strings, max_len):
    ascii_to_strings = dict()

    identifiers = [] #a list that will host the ascii identifier for each word of the test
    for string in list_of_strings: #for each word of the text
        """for each char of the string computing its ascii value and building a list of them, since we have no other 
        chars below the a, we can make the the count of the ascii character start from 1 decreasing all the ascii values 
        by the value of a-1"""
        identifier = [str(ord(char)-(ord("a")-1)).rjust(2, '0') for char in string] #we use rjust since we want al number of 2 digits
        """ransforming the list in a number"""
        identifier = int("".join(identifier).ljust(max_len*2, '0')) #adding 0s at the right, we want all numbers of equal lenght
        identifiers.append(identifier)

        #for easilly go back from ascii score to strigs
        ascii_to_strings[identifier] = string

    return (identifiers, ascii_to_strings)


def counting_sort(text):
    #getting a list of trings instead of the text
    strings = text.lower().split() #we don't need lower cases

    ascii_scores, ascii_to_strings = __to_ascii(strings, __max_len(strings))

    #creating the counter array, inizialyzed with zeros
    counter = [0 for i in range(max(ascii_scores)+1)]

    #full the counter list with the occurrences of the words, using the ascii_score of the words as index
    for ascii_score in ascii_scores:
        counter[ascii_score] += 1


    orderedlist = [] #creating the list that will host all the words in the right order

    # for each index of the counter (index that reppresents the ascii score of the related word
    for ascii_score in range(len(counter)):
        #add to the list the word a number of times equal to the times the word was encountered in the original text
        orderedlist += [ascii_to_strings[ascii_score] for i in range(counter[ascii_score])]

    #return the list in string format
    return " ".join(orderedlist)
