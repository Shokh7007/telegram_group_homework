from read_data import read_data

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    z=0
    for i in data["messages"]:
        if i["type"]=="message":
            if i["from_id"]==users_id:
                z+=1
    return z
f=open("data/result.json","r",encoding='utf8')
x=f.read()
print(find_user_message_count(read_data(x),"user86775091"))
