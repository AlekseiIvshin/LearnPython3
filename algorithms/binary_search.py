def binary_search(list, value):
  fromIndex = 0
  toIndex = len(list) 
  while fromIndex < toIndex:
    middleIndex = int((toIndex + fromIndex) / 2)
    #print("from %d mid %d to %d" % (fromIndex, middleIndex, toIndex))
    if list[middleIndex] < value:
      fromIndex = middleIndex + 1
    else:
      toIndex = middleIndex
  if fromIndex  == len(list) or list[fromIndex] != value:
    return -1
  return fromIndex
     
sorted_list = [1,2,3,4,6,7]
print("Value %d was found at %d in %s" % (1, binary_search(sorted_list, 1), sorted_list))
print("Value %d was found at %d in %s" % (2, binary_search(sorted_list, 2), sorted_list))
print("Value %d was found at %d in %s" % (3, binary_search(sorted_list, 3), sorted_list))
print("Value %d was found at %d in %s" % (4, binary_search(sorted_list, 4), sorted_list))
print("Value %d was found at %d in %s" % (6, binary_search(sorted_list, 6), sorted_list))
print("Value %d was found at %d in %s" % (-1, binary_search(sorted_list, -1), sorted_list))

print("Value %d was found at %d in %s" % (5, binary_search(sorted_list, 5), sorted_list))
