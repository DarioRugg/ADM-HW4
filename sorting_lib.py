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
        ascii_score = 0
        power = max_len - 1 #we start from the max_len because the fist letter must weight as the others first letters
        for char in string: #from the fist (so the most important) to the last (the lesser) letter of the string
            """in some ways we count in base (ord("z") - (ord("a") - 1)), so the length of our possible chars so if for 
            example the word is made by three letters we will write them as 26^2*a 26^1*b 26^0*c. 
            So the moltiplicator is the number that will multiply the ascii value of the letter and change it's importance"""
            moltiplicator = (ord("z") - (ord("a") - 1)) ** power
            # we subtract by (ord("a") - 1) since we don't have any possible letter before a
            ascii_score += (ord(char) - (ord("a") - 1)) * moltiplicator
            power -= 1 # in the next iteration the moltipicator must be smaller, as the weight of the next letter

        identifiers.append(ascii_score) #now we add the asci value evaluated to the list

        #for easilly go back from ascii score to strigs
        ascii_to_strings[ascii_score] = string

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