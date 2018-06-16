def fill_space(str1,len_str):
    str2 = []
    for j in range(len(str1)):
        if str1[j] == " ":
            str2.append("%")
            str2.append("2")
            str2.append("0")
        else :
            str2.append(str1[j])

    a = ''.join(str2)
    print a

str1 ='mr john smith'
len_str = 13
fill_space(str1,len_str)
