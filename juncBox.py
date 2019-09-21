def orderedJunctionBoxes(numberOfBoxes, boxList):
    def hasNumbers(inputString):
        return any(char.isdigit() for char in inputString)
    def Sort(sub_li): 
        sub_li.sort(key = lambda x: x[1])
    def sortJunctionBoxes(boxes):
        result = []
        minLength = len(min(boxes))
        for i in range(len(boxes) - 1):

    old = []
    new = []
    result = []
    for box2 in boxList:
        for box in box2:
            box = box.split(' ')
            if box[1].isnumeric():
                old.append(box)
            else:
                new.append(box)
    print(sortJunctionBoxes(sorted(old)))

def o(a,b,c):
    return a

def optimalUtilization(deviceCapacity, foregroundAppList, backgroundAppList):
    maxMemory = 0
    result = []
    for foregroundApp in foregroundAppList:
        for backgroundApp in backgroundAppList:
            memory = foregroundApp[1] + backgroundApp[1]
            if memory > deviceCapacity:
                continue
            if memory > maxMemory:
                maxMemory = memory
                result = []
                result.append([foregroundApp[0], backgroundApp[0]])
            elif memory == maxMemory:
                result.append([foregroundApp[0], backgroundApp[0]])
    return result

if __name__ == '__main__':
    print(orderedJunctionBoxes(6, [['ykc 82 01'],['eo first qpx'],['09z cat hamster'],['06f 12 25 6'],['az0 first qpx'],['236 cat dog rabbit snake']]))
    print(o(7, [[1,2],[2,4],[3,6]], [[1,2]])) # 3 1
    print(o(20, [[1,8],[2,7],[3,14]], [[1,5],[2,10],[3,14]])) # 3 1
    print(o(20, [[1,8],[2,15],[3,9]], [[1,8],[2,11],[3,12]])) # 1 3, 3 2