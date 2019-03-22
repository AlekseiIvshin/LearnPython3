
# Longest common subsequence
def lcs(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return 0

    if str1[-1:] == str2[-1:]:
        return lcs(str1[:-1], str2[:-1])+1
    return max(lcs(str1[:-1],str2), lcs(str1, str2[:-1]))

class Node:
    def __init__(self, value, char):
        self.value = value
        self.char = char
        self.directions = []
    def __str__(self):
        strDir = ""
        for d in self.directions:
            if d[0]<0 and d[1]<0:
                strDir+= chr(8598)
            elif d[0]<0:
                strDir+=chr(8592)
            elif d[1]<0:
                strDir+=chr(8593)
        strDir+=" "*(2-len(strDir))
        return "%d (%s)" % (self.value, strDir)

    def update(self, value, dx, dy):
        self.value = value
        self.directions.append((dx, dy))

def func(str1, str2):
    rows = len(str1) + 1
    cols = len(str2) + 1
    # Init array of values
    values = []
    for i in range(0, rows):
        values.append([])
        for j in range(0, cols):
            char = ""
            if str1[i-1] == str2[j-1]:
                char = str1[i-1]
            values[i].append(Node(0, char))

    # Calculate values
    for i in range(1, rows):
        for j in range(1, cols):
            if str1[i-1] == str2[j-1]:
                values[i][j].update(values[i-1][j-1].value + 1, -1,-1)
            else:
                if values[i][j-1].value >= values[i-1][j].value:
                    values[i][j].update(values[i][j-1].value, 0, -1)
                    
                if values[i][j-1].value <= values[i-1][j].value:
                    values[i][j].update(values[i-1][j].value, -1, 0)

    return values

def extract(res, pos, value, store):
    cur = res[pos[0]][pos[1]]
    val = cur.char + value

    for d in cur.directions:
        if cur.value > 0:
            extract(res, (pos[0]+d[0], pos[1]+d[1]), val, store)
        else:
            store.add(val[::-1])

str1 = "DCBA"
str2 = "ABCAB"
res = func(str1,str2)
rbCorner = (len(str1), len(str2))

for row in res:
    print([str(i) for i in row])

store = set()

extract(res, rbCorner, "", store)

print(store)
