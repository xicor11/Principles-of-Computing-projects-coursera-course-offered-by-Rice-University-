"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """

    compare_line = list(line)
    
    #merge_index variable stores indexes that are merged so they can be ignored later
    merge_index = []
    
    #steps variable used to repeat functions in a while loop
    steps = 0
    
    #While loop of 2 because first a nonzero algorithm is used
    #to shift zero values to the right and then merge happens.
    #This is done two times as the merge will create new zeros
    #that need to be shifted to the right and not merge all 
    #values that can merge
    while steps < 2:
        right = 0        
        for left in range(len(compare_line)):   
            if compare_line[left] !=0:
                compare_line[left], compare_line[right] = compare_line[right], compare_line[left]
                right +=1
                #shifting zeros changes the merge indexes
            else:
                #shifting of zeros changes the merge index leftward
                for indexes in range(len(merge_index)):
                    if merge_index[indexes] >=right:
                       merge_index[indexes] -=1 
                               
        #-1 in for loop as there would not be a loop for last element        
        for item in range(len(compare_line)-1):
            if  compare_line[item] == compare_line[item+1] and item not in merge_index and (item+1) not in merge_index:
                compare_line[item] = compare_line[item] + compare_line[item]
                compare_line[item+1] = 0
                merge_index.append(item)
        
        steps +=1        
    
    return compare_line

