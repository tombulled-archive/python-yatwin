"""
Library containing utility functions for 'decoder'

Contains:
    chunks
"""

def chunks(l, n):
    """
    Yield successive n-sized chunks from l.
    Reference: https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
    """
    
    for i in range(0, len(l), n):
        yield l[i:i + n]
