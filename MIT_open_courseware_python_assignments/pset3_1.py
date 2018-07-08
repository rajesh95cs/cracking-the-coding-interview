import string

def count_substring(target,key):
    index = 0
    new_index = 0
    count = 0
    while index != -1:

        index = string.find(target,key,new_index)
        print index
        if index == -1:
            break
        else:
            count += 1
        new_index = index + 1

    return count

target = "atgacatgcacaagtatgcat"
key = "atgc"
print(count_substring(target,key))
