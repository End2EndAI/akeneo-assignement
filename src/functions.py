import random
from itertools import groupby

def generate_draw(dict_, MAX_ATTEMPTS):
    """Generate a pairing for each participant in the dictionnary.
    The algorithm is a greedy algorithm. It will try to find a valid solution by attempting until it finds one.
    The intuition is to start with the participants with the longuest blacklist (constraint), and pair them to valid recipients with the longuest blacklist.
    
    Args:
        dico (dict): list of participants with their blacklist

    Returns:
        dict: shuffled dictionnary
    """
    for attempt in range(MAX_ATTEMPTS):
        pairs = {}
        valid = True
        
        participants = list(dict_.keys())
        recipients = participants[:]

        shuffled_dict = sort_shuffle_dict(dict_)

        for giver in shuffled_dict.keys():
            valid_recipients = [recipient for recipient in recipients if recipient != giver and recipient not in shuffled_dict[giver]]
            
            if not valid_recipients:
                valid = False
                break
            
            # Choose the valid recipient with the longuest blacklist. If same length, choose randomly.
            valid_recipients_dict = {key: shuffled_dict[key] for key in valid_recipients}
            shuffled_valid_recipients_dict = sort_shuffle_dict(valid_recipients_dict)
            
            recipient = list(shuffled_valid_recipients_dict.keys())[0]
            pairs[giver] = recipient
            recipients.remove(recipient)
        
        if valid:
            return pairs
    
    return None

def sort_shuffle_dict(dict_):
    """Sort the dictionnary by desc length of the blacklist (value) and shuffle the keys with same length.

    Args:
        dict_ (dict): list of participants with their blacklist

    Returns:
        dict: shuffled dictionnary
    """
    # Step 1: Sort the dictionary by the length of the value
    sorted_dict = sorted(dict_.items(), key=lambda item: len(item[1]), reverse=True)
    
    # Step 2: Group keys with the same length values
    grouped_dict = {k: list(v) for k, v in groupby(sorted_dict, key=lambda item: len(item[1]))}

    # Step 3: Shuffle keys within each group
    shuffled_dict = {}
    for length, items in grouped_dict.items():
        keys = [item[0] for item in items]
        random.shuffle(keys)
        for key in keys:
            shuffled_dict[key] = dict_[key]
    
    return shuffled_dict 

def convert_from_df_to_dict(df):
    """Convert a dataframe to a dict, in the format required by generate_draw().
        
    Example input :
    
    participant;excluded
    
    person_1;person_2,person_3


    Example output :
    
    {'person_1':['person_2','person_3']}

    Args:
        df (_type_): _description_
    """
    dict_ = {}
    
    for index, participant in enumerate(df["participant"]):
        if(type(df.loc[index, 'excluded']) != float):
            dict_[participant] = [x for x in df.loc[index, 'excluded'].split(',')]
        else:
            dict_[participant] = []

    return dict_