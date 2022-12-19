def self_per(word):
    if len(word) <=1:
        return word
    str_list=[]
    for i in range(len(word)):
        for j in self_per(word[0:i] + word[i+1:]):
            str_list.append(word[i]+j)
    return str_list


print(self_per('abc'))
