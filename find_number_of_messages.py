from read_data import read_data

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    z=0
    for i in data["messages"]:
        if i["type"]=="message":
            z+=1
    return z
f=open("data/result.json","r",encoding='utf8')
x=f.read()
print(find_number_of_messages(read_data(x)))