from operator import itemgetter

users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]
    


def num_friends(user):
    cont = 0
    for i in range(len(friendship)):
        j = 0
        while j<2:
            if user == friendship[i][j]:
                cont += 1
            j+=1
    return cont
    
    
def sort_by_num_friends():
    cont = []
    for index in range(len(users)):
        cont.append((num_friends(index),index))
    cont = sorted(cont,key=itemgetter(0),reverse=True)
    print("Sorted by most number of friends to least number of friends:")
    for elem in cont :
        dict_value = users[elem[1]]
        print("Id = "+str(dict_value['id'])+" , Name = "+str(dict_value['name']))
    return None
       


if __name__ == "__main__":
    user = int(input('Enter the ID:'))
    cont = num_friends(user)
    print("No of friends is :" ,cont)
    sort_by_num_friends()


