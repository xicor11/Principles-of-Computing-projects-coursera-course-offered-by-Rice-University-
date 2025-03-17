"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """

    num_multipler = [hand.count(idx) for idx in range(1, 7)] 
    
    max_list = [face * num_multipler[face-1] for face in range(1, 7)]
    
    max_num = max(max_list) if max_list else 0

    return max_num 


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    dice_sides = tuple(range(1, num_die_sides+1))

    dice_combo = gen_all_sequences(dice_sides, num_free_dice)
    
    combo_list = list(dice_combo)
    for idx, set in enumerate(combo_list):
        if held_dice == ():
            pass
        elif isinstance(held_dice, int):
            if held_dice in list(combo_list[idx]):
                temp_list = list(combo_list[idx])
                temp_list.append(int(held_dice))
                combo_list[idx] = tuple(temp_list)
        else:
            held_dice = list(held_dice)
            for idx2, val in enumerate(held_dice): 
                if held_dice[idx2] in list(combo_list[idx]):
                    temp_list = list(combo_list[idx])
                    temp_list.append(held_dice[idx2])
                    combo_list[idx] = tuple(temp_list)
    
    
    possible_scores = [score(combo_list[idx]) for idx in range(0, len(combo_list))]        

    for idx, val in enumerate(possible_scores):
        if isinstance(held_dice, int):
            if held_dice > val:
                possible_scores[idx] = held_dice
        else:
            if score(held_dice) > possible_scores[idx]:
                possible_scores[idx] = score(held_dice)   
            
    expected_value = sum(possible_scores)/(float(num_die_sides**num_free_dice))
     
    return expected_value

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    
    answer_set = set([()])
    for element in hand:
        temp_set = set()
        for partial_sequence in answer_set:
            new_sequence = list(partial_sequence)
            new_sequence.append(element)
            temp_set.add(tuple(new_sequence))
        answer_set.update(temp_set)
        
    return answer_set
        
def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    
    holds = gen_all_holds(hand)
    hold_list = list(holds)
    hand_length = len(list(hand))
    
    score_list = [score(set) for set in hold_list]
    
    expected_vals = []
    for idx, set in enumerate(hold_list):
        new_val = expected_value(set, num_die_sides, hand_length - len(set))
        expected_vals.append(new_val)
    
    max_expected = max(expected_vals)
    max_current_score = float(max(score_list))
    
    max_hold_index = 0
    if max_current_score > max_expected:
        for idx, vals in enumerate(score_list):
            if vals == max_current_score:
                max_hold_index = idx
                max_hold = hold_list[max_hold_index]
                return (max_current_score, max_hold)
    else:
        for idx, vals in enumerate(expected_vals):
            if vals == max_expected:
                max_hold_index = idx
                max_hold = hold_list[max_hold_index]
                return (max_expected, max_hold)


