'''
created by Jonas Schmidt on 1/8/2023
'''

# table = array of each entry of the table
table_file = open("braille_table.txt", "r", errors="ignore")
table = table_file.read().split("\t")

table_file.close()

# braille_dictionary.txt becomes a dictionary for ASCII characters and their braille dots code...
dict = open("braille_dictionary.txt", "w")

i = 1

while i + 1 < len(table):
    dict.writelines([table[i], " : ", table[i + 1], '\n'])
    i += 5
#...

dict.close()
