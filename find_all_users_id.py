from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    z=[]
    a=0
    for i in data["messages"]:
        if i["type"]=="message":
            z.append(i["from_id"])
    return z

f=open("data/result.json","r",encoding='utf8')
x=f.read()
print(find_all_users_id(read_data(x)))