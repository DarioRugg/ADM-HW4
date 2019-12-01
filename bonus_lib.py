#Here we have our Bonus task, unfortunally it needs a looot of time to iterate, so that's just the code
import hashing_lib #here we import the bloom dilter
def bonus(name):
    l=[] #here we create a new list with all the items of l
    with open("passwords1.txt", "r") as file:
        for line in file:
            l.append(line.strip())
    f=open(name, "w+") #we create a new file
    with open("passwords2.txt","r") as file:
        for line in file:
            if line.strip() not in l: #if an element is not in the list, it's original, so we put it into the new file
                f.write(line)
    BloomFilter("passwords1.txt",name)
