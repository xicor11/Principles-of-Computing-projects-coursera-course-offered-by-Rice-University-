"""
Clone of 2048 game.
"""

#import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

def merge(line):
    """
    Helper function that merges a single row or column in 2048
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
def all_nonzero(matrix):
    """
    Helper function determines whether any zeros are left in grid
    """
    for row in matrix:
        for element in row:
            if element == 0:
                return False
    return True

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._gridheight_ = grid_height
        self._gridwidth_ = grid_width
        self.reset()
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        
        self._tilegrid_ = [[0 for col in range(self._gridwidth_)]
                   for row in range(self._gridheight_)]
        
        self.new_tile()
        self.new_tile()
            
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        grid_str = ""
        
        for row in range(self._gridheight_):
            grid_str = grid_str +  str(self._tilegrid_[row]) + " \n"
        
        return grid_str
    
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return  self._gridheight_ 

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._gridwidth_

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        compare_grid = list(self._tilegrid_)
        merge_lists = []
        #UP = 1
        if direction == 1 or  direction == "UP":
            for col in range(self._gridwidth_):
                temp_list = []
                for row in range(self._gridheight_): 
                    temp_list.append(self._tilegrid_[row][col])                
                merge_lists.append(temp_list)        
            
            merged_tiles = []
            for col in range(self._gridwidth_): 
                merged_tiles.append(merge(merge_lists[col]))
            
            
            self._tilegrid_ = [[merged_tiles[col][row] for col in range(self._gridwidth_)]
                                  for row in range(self._gridheight_)]

          
        #DOWN = 2
        elif direction == 2:
            for col in range(self._gridwidth_):
                temp_list = []
                for row in range(self._gridheight_): 
                    temp_list.append(self._tilegrid_[-(row+1)][col])                
                merge_lists.append(temp_list)        
            
            merged_tiles = []
            for col in range(self._gridwidth_): 
                merged_tiles.append(merge(merge_lists[col]))
            
            for col in range(self._gridwidth_):
                merged_tiles[col].reverse()

            self._tilegrid_ = [[merged_tiles[col][row] for col in range(self._gridwidth_)]
                                  for row in range(self._gridheight_)]

        
        #LEFT = 3
        elif direction == 3:            
            for row in range(self._gridheight_):
                temp_list = []
                for col in range(self._gridwidth_): 
                    temp_list.append(self._tilegrid_[row][col])                
                merge_lists.append(temp_list) 
            
            for row in range(self._gridheight_): 
                self._tilegrid_[row] = merge(merge_lists[row])

        
        #RIGHT = 4
        elif direction == 4:
            for row in range(self._gridheight_):
                temp_list = []
                for col in range(self._gridwidth_): 
                    temp_list.append(self._tilegrid_[row][-(col+1)])                
                merge_lists.append(temp_list) 

            for row in range(self._gridheight_): 
                self._tilegrid_[row] = merge(merge_lists[row])
                self._tilegrid_[row].reverse()
        
        if compare_grid !=self._tilegrid_:
            self.new_tile()
        
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        
        full_grid = all_nonzero(self._tilegrid_)
        
        num_chance = random.randrange(0, 10)

        if num_chance !=0:
            tile = 2
        else:
            tile = 4
        
        random_column = random.randrange(0,self._gridwidth_)
        random_row = random.randrange(0,self._gridheight_) 
        
        if  self._tilegrid_[random_row][random_column] == 0:
            self._tilegrid_[random_row][random_column] = tile
        elif full_grid == True:
            return "No more moves can happen in the game!"
        else:
            while self._tilegrid_[random_row][random_column] != 0:
                random_column = random.randrange(0,self._gridwidth_)
                random_row = random.randrange(0,self._gridheight_)
            self._tilegrid_[random_row][random_column] = tile
              
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._tilegrid_[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._tilegrid_[row][col] 


#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))