#! /usr/bin/env python
from InputGenerator import inputGenerator
from HashTable import HashTable
import random

class Worker():
    def __init__(self):
        self.random_strings = []
        self.gen = inputGenerator()
        self.test_strings = []
        self.error_strings = []

    def genStrings(self,count):
        """makes a list of strings for later use"""
        self.random_strings = self.gen.make(count) #generates 5000 unique strings
        return

    def cherryPick(self,count):
        """returns list of indices of random selected for testing"""
        #for i in range(count):
        #    random_list.append(random.randint(1,stringcount))

        self.test_strings =  random.sample(self.random_strings, count)
        return

    def genErrorString(self):
       
        gen_string = self.gen.generateString()
        while(gen_string in self.random_strings):
            #try again
            gen_string = self.gen.generateString()

        #now we have the string we want
        return gen_string

    def genErrorStringList(self,count):
        for i in range(count):
            tmp = self.genErrorString()
            self.error_strings.append(tmp)

        return

    def build(self,string_count,valid_test_count,invalid_test_count):
        self.genStrings(string_count)
        self.cherryPick(valid_test_count)
        self.genErrorStringList(invalid_test_count)
        return


#now run this
w = Worker()
search_item_count = 900
invalid_item_count = 900
string_count = 1000
w.build(string_count,search_item_count,invalid_item_count)



#------HASH TABLE------#

#some timeit shit here
#now we insert
print("Adding items to hash table....")
h = HashTable(13)
for i in w.random_strings:
    h.add(i)

print("Printing hash table....")
h.pprint()

t = 0
f = 0
for i in w.test_strings:
    result = h.search(i)
    if(result):
        t+=1
    else:
        f+=1

print("Test strings:")
print("true: %s false: %s" %(t,f))

t=0
f=0
for i in w.error_strings:
    result = h.search(i)
    if(result):
        t+=1
    else:
        f+=1
print("invalid test strings:")
print("true: %s false: %s" %(t,f))


