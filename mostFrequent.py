# Given a non-empty array of integers, return the k most frequent elements
# e.g. nums = [1,1,1,2,2,3], k = 2
#      output = [1,2]
# e.g. nums = [1], k=1
#      output = [1]
#
# Note: assume k is always valid. the input array will always have k most unique elements
# for example, if nums = [1,1,2,2,3,3], k cannot be 2
# only valid k is 3


# create an empty dictionary, and iterate through the list
# if element is in dictionary, add count, if not, add to dictionary and element:1
# return the k elements in the dictionary
def mostFrequent(lst: list, k: int) -> list:
    dic = dict()
    newLst = []
    
    for val in lst:
        if val not in dic:
            dic[val] = 1
        else:
            dic[val] +=1    
    sorted_x = sorted(dic.items(), key=dict_val)[::-1]

    for i in sorted_x[:k]:
        newLst.append(i[0])
    return newLst

    
def dict_val(x):
    return x[1]
