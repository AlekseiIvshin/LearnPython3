# Greed algorithm
class Item:
    def __init__(self, weight, cost):
        self.weight = weight
        self.cost = cost

    def __str__(self):
        return "w = %d; c = %d" % (self.weight, self.cost)

def calculate(items, maxWeight):
    sortedItems = sorted(items, key = lambda i: i.weight/i.cost)
    res = []
    resWeight = 0
    while len(sortedItems) > 0 and resWeight < maxWeight:
        item = sortedItems.pop(0)
        if resWeight + item.weight <= maxWeight:
            res.append(item)
            resWeight += item.weight
    return res

items = [Item(2,6), Item(3,9), Item(5,10)]
print([str(i) for i in calculate(items, 9)])