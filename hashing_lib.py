
import time
import numpy as np

#Hello! that's our Bloom Filter!
#In the next lines I will explain everything about it, function per function, so have a seat and enjoy!

#Min_Max is our function to calculate the max ord of the charcter in the string, in our case we already know that it was 122, however we
#prefered to create something general and always implementable even with a different encoding or different use on characters on the strings

def min_max(minimum, maximum, string):           #Here we take the min and the max that we already know
    orders = list(map(lambda x: ord(x), string)) #Here we create a list where every character is converted into his ord
    minimum = min(min(orders), minimum)          #then we choose between those two, the min of the list and the min that we already have
    maximum = max(max(orders), maximum)          #samething here
    return (minimum, maximum)                    #and we return both, minimum and maximum


#Here we have our hash function, very smart and cool, the good thing about it is that you can create different indicies for the bloom filter just using a
#different prime number. We found this one and we thought it was easy to do and also fast.
    
def hashcii(string, minimum, coefficients): #So here we have it, we get the string (obviously), the minimum and the coefficients list (we will see it later)
    orders = np.array(list(map(lambda x: (ord(x)-(minimum-1)), string))) #We create and array that has the ord of the each character minus the minimum -1,
                                                                         #That's because if you take a string where the min is 10, every character 
                                                                         #you know that will starts with minimum 10, so if you have to order them, you can redure their value
                                                                         #by 9, and you will keep the order!                                                                     
    return np.dot(coefficients, orders) #Then we do a np.dot function using our coefficients and the array of ord that we got before and we return that

#Here we have the Bloomfilter_add, the function that we use to create the filter, it gets values created using the hash function, the bloomfilter already done and his lenght
def bloomfilter_add(hash_values, bloomfilter, length):

    for hash in hash_values: #It iterate the values created using the hascii and it changes inside the filter the single values
        bloomfilter[int(hash%length)] = 1 #using the rest of the mathematical division of the lenght of the bloom filter, that it's usefull to create a very specific and unique value
                                          #for each item inside a string

#Here we have a function similiar to BloomFilter_add, it takes the same values in fact.
def bloomfilter_check(hash_values, bloomfilter, length):
    is_inside = True                            #It has a difference here, this value, easy to understand
    for hash in hash_values:                    #if a value of a string is not a 1 inside of the bloom filter it's not a duplicate, so it's original!
                                                #So it's not in the filter, so we don't have to iterate more, we already know that it's good
        if bloomfilter[int(hash%length)] == 0:
            is_inside = False
            break
    return is_inside #So the funciton here gives True, if it's a duplicate and False if it's not!


#Finally here we start!
def BloomFilter(file1, file2):
    
    start = time.time()

    first_assignment = True #The first variable it's required to give to min_max the start values and we done it using a boolean variable
    with open(file1, "r") as file: #Here we take the first file, checking if there is a new min and max inside every string
        for line in file:
            if first_assignment:
                minimum = min(list(map(lambda x: ord(x), line.strip())))
                maximum = 0
                first_assignment = False

            minimum, maximum = min_max(minimum, maximum, line.strip())
            
            
    
    maximum -= minimum #The same as before, where we explained that the minimum starting values is just a number that we can use differently (check Hashii funciton)
                       #We have the samething here. If we have a maximum value that is 10, and the min is 5, of course every number has maximum a difference between max-min!
    

    hash_functions = [1 ,2, 3] #this one is the power of our hash function, dividing it with prime number, we get every time a different number that has a unique rest 
                                      #if we divide it fot the lenght of the Bloom Filter! Why it is a power? because you can create a powerfull filter just adding some prime numbers

    coefficients = np.array(list(map(lambda x: maximum ** x, [i for i in range(20)]))) #We already talked about coefficients, it's an array that has for each position the max value 
                                                                                       #powered to the indicies, it iterate to 20 because we already know that each pass3word has 20
                                                                                       #characters!
    start = time.time()                                                                                  
    length = 300000000 #That's the leght of the filter, unfortunally our machines can't execute large numbers
                      
    bloomfilter = np.zeros(length) #The bloomfilter start's with an array of zeros!

    #Let's built the filter!
    with open(file1, "r") as file: #here we get "passwords1.txt"
        for line in file:
            hash = []
            hash_temp=hashcii(line.strip(), minimum, coefficients) #we create a temporary values for the hash function
            for function in hash_functions: #we get the prime numbers
                
                hash.append(hash_temp/function) #and we collect them into hash
                
                
            bloomfilter_add(hash, bloomfilter, length) #Using hash, that takes the numbers divided by the prime numbers that we choose, we start creating the filter
    
    counter = 0 #here the counter starts, the one that will give use the number of duplicates detected

    passwords=0 #this is a counter that we need to calculate the probability of false positive
    with open(file2, "r") as file: #So here we open passwords2.txt and we start to do the samething as before, but here we have a change
        for line in file:
            passwords+=1
            hash = []
            hash_temp=hashcii(line.strip(), minimum, coefficients)
            for function in hash_functions:
                hash.append(hash_temp/function)
            
            if bloomfilter_check(hash, bloomfilter, length): #Here it's a check, if the bloomfilter check returns a True, so it doesn't detect a new unique element
                counter += 1 #the counter sign +1 and goes on

    end=time.time()
    print("Number of hash function used: ", len(hash_functions))
    print("Number of duplicates detected", counter) 
    print("Probability of false positive: ",(passwords-counter)/passwords) #The number of false positive has to be the rateo between the total tests (so the numbers of passwords in password2) minus how many duplicates we had on the totaltests done
    print("Execution time", end - start) #Expected running time 1835 sec (30 minutes!)
