import re       #import regex library

#open textfile with reading function, will output list with strings ['Abbauprofil', 'Abbauprofile', 'Abbauprofilen',...]
with open('germanTest.txt','r') as fd:
    all_words = fd.read().splitlines()

#join all_words list into a string (for later using the rexex function)
all_words=' '.join(all_words)

#make all words lowercase (only works for strings)
all_words=all_words.casefold()

#check
#print(type(all_words))
#print(all_words[:3])




#get needed word as user input, will output list with string ['.xam.le']-> use . as this can be replaced by any character
needed_word=str(input("Enter needed word using '.' for unknown letters. Example: e_am__e: ").lower().strip())

#check output
#print(needed_word)
#print(type(needed_word))

#find needed word with regex

regex = re.compile(needed_word)     #re.compile=seach by pattern
matches = regex.findall(all_words) #, iterate through all_words string and look for a matching pattern
print("possible match: ", matches)
