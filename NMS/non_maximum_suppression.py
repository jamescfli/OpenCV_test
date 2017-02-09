import numpy as np

# Felzenszwalb et al.
def non_max_suppression_slow(boxes, overlap_th):
    if len(boxes) == 0:
        return []

    pick = []

    x1 = boxes[:,0]
    y1 = boxes[:,1]
    x2 = boxes[:,2]
    y2 = boxes[:,3]

    area = (x2 - x1 + 1)*(y2 - y1 + 1)
    idxs = np.argsort(y2)   # bottom right y-coordinate

    while len(idxs) > 0:
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)
        suppress = [last]

        for pos in xrange(0, last):
            j = idxs[pos]

            xx1 = max(x1[i],x1[j])
            yy1 = max(y1[i],y1[j])
            xx2 = max(x2[i],x2[j])
            yy2 = max(y2[i],y2[j])

            w = max(0, xx2-xx1+1)
            h = max(0, yy2-yy1+1)

            overlap = float(w*h) / area[j]

            if overlap > overlap_th:    # typical value of threshold is 0.3~0.5
                suppress.append(pos)    # suppress the current bbox

        idxs = np.delete(idxs, suppress)

    return boxes[pick]