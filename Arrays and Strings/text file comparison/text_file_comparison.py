#function defined to compare two files .the comparison is done by checking
#whether the frequecies of occurance of a word in one file is equal or almost
#same this found out taking the differences of the occurance words in each files
#so here we use a hash data structure to implement the program
#hashing or dictionaries which is used in python is used to store the word and
#its corresponding number of occurences ie the key here is the word and the
#value is its occurance
def file_comparisons(file_words1,file_words2):
#an empty dictionary f1_dict which is created for file 1
    f1_dict = {}
#relword_count dictionary is declared to store the words which occur in both
#the files as keys and relative count as values.the relative count is found by
#taking the difference of counts which are stored in the dictionary
    relword_count = {}
#loop through the file_words1 list to see whether the word exist in the
#dictionary if the condition is satisfied the the value of occurence of the
#word is incremented else it is set to 1 .this is how the dictionary is made
    for word in file_words1:
        if word in f1_dict:
            f1_dict[word] += 1
        else:
            f1_dict[word] = 1
#loop through the file_words2 list which contains the list of words of the file
#2 here the dictionary for file2 is not made because it is not necessary and to
#increase the efficiency of the algorithm
    for word in file_words2:
#here word in file 2 is compared with keys of relword_count dictionary
#if the word exist in the keys just decrease the value to the corresponding key
#by 1 else if it exist in file 2 word dictionary decrement the value and store
#the key value in relword_count dictionary
        if word in relword_count:
            relword_count[word] -= 1
        elif word in f1_dict:
            relword_count[word] = f1_dict[word] - 1
#the sum of the relword_count dictionary values gives the factor which tell
#whether text files are almost same
    sum = 0
    for value in relword_count.values():
        sum += abs(value)

    return sum
