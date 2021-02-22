import pandas

#TODO 1. Create a dictionary in this format:

data = pandas.read_csv('nato_phonetic_alphabet.csv')
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(data_dict)
#
# for (i,j) in data.iterrows():
#     print(j)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

while True:
    user_input = input("Type: ")
    output = [data_dict[i.upper()] for i in user_input]
    print(output)