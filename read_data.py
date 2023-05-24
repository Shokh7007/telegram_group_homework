import json
def read_data(file_path: str)->dict:
    """
    This function will read the json file and return the data as a dictionary.
    
    Parameters:
        file_path (str): Path of the file to be read
    Returns:
        dict: Dictionary containing the data of the json file.
    
    """
    #open file
    y=json.loads(file_path)
    return y
f=open("data/result.json","r",encoding='utf8')
x=f.read()
read_data(x)