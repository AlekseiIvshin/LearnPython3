def minCoverageSegments(checkSegment, segments):
    res = []
    sortedSegments = sorted(segments, key = lambda seg: seg[0])
    cur = (checkSegment[0],checkSegment[0])
    while cur[1] < checkSegment[1]:
        cur = max(filter(lambda seg: seg[0] <= cur[1], sortedSegments), key = lambda seg: seg[1])
        res.append(cur)
    return res


checkSegment = (0, 10)
segments = [(0,5),(2,6),(0,4),(4,7),(7,10),(8,10)]
res = minCoverageSegments(checkSegment, segments)
for m in res:
    print(m)