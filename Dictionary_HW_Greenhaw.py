outfile = open('text.txt', 'r')

#write dictionary that individ words are keys
#values are number of times each word appears
paragraph_list = outfile.read()
lower_content = paragraph_list.lower()

take_out = [',' , '.' ,'”' , '’' , '"' , "'"  , '?' , '!' , '&', '@', '*' , '#','1','2','3','4','5','6','7','8','9']    

for ch in take_out:
    prg_string = lower_content.replace(ch,"")

prg = prg_string.split()
words_dictionary = {}

for word in prg:
    value = prg.count(word)
    words_dictionary[word] = value
    
print('Here are the words and their frequencies:')

for word, frequency in words_dictionary.items():
    print('Word: ', word, 'Frequency: ', frequency)

outfile.close()