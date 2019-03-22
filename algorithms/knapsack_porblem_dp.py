# Dynamic programming
class Item:
    def __init__(self, weight, cost):
        self.weight = weight
        self.cost = cost

    def __str__(self):
        return "w = %d; c = %d" % (self.weight, self.cost)

def calculate(items, maxWeight):
    size = maxWeight+1
    res = [0]*size
    selectedItems = [None]*size    

    for i in range(1, size):
        suitedItems = list(filter(lambda k: k.weight<=i, items))
        if len(suitedItems)==0:
            res[i] = 0
        else:
            itemVal = max([(item, item.cost + res[max(0, i - item.weight)]) for item in suitedItems], key=lambda x: x[1])
            res[i] = itemVal[1]
            selectedItems[i] = itemVal[0]

    return selectedItems[::-1]

def printRes(selectedItems):
    index = 0
    item = selectedItems[index]
    while item:
        print(item)
        index = index+item.weight
        item = selectedItems[index]

items = [Item(2,6),Item(3,9),  Item(5,10)]
printRes(calculate(items, 9))