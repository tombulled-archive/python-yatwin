"""
Contains:
    chunk
"""

def chunk(lst, chunk_len):
    """
    Yield successive {chunk_len}-sized chunks from {lst}.
    Reference: https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
    """

    for index in range(0, len(lst), chunk_len):
        yield lst[index:index + chunk_len]
