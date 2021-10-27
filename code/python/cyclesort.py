from numba import jit

@jit(nopython=True)
def cyclesort(vector):
    "Sort a vector in place and return the number of writes."
 
    # Loop through the vector to find cycles to rotate.
    for cycleStart, item in enumerate(vector):
 
        # Find where to put the item.
        pos = cycleStart
        for item2 in vector[cycleStart + 1:]:
            if item2 < item:
                pos += 1
 
        # If the item is already there, this is not a cycle.
        if pos == cycleStart:
            continue
 
        # Otherwise, put the item there or right after any duplicates.
        while item == vector[pos]:
            pos += 1
        vector[pos], item = item, vector[pos]
 
        # Rotate the rest of the cycle.
        while pos != cycleStart:
 
            # Find where to put the item.
            pos = cycleStart
            for item2 in vector[cycleStart + 1:]:
                if item2 < item:
                    pos += 1
 
            # Put the item there or right after any duplicates.
            while item == vector[pos]:
                pos += 1
            vector[pos], item = item, vector[pos]
