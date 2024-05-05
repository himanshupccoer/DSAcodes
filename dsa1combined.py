size = 10
client_list_linear = [None] * size
client_list_quadratic = [None] * size

def insert_linear():
    id = int(input("Enter the client id : "))
    name = input("Enter the client name: ")
    tele = int(input("Enter the client telephone: "))
    detail = [id, name, tele]
    index = id % size
    for i in range(size):
        if(client_list_linear[index]==None):
            client_list_linear[index] = detail
            print("Client is added at index ", index)
            break
        else:
            index=(index+1)%size
       
def insert_quadratic():
    id = int(input("Enter the client id : "))
    name = input("Enter the client name: ")
    tele = int(input("Enter the client telephone: "))
    detail = [id, name, tele]
    index = id % size
    a = 1
    for i in range(size):
        if(client_list_quadratic[index]==None):
            client_list_quadratic[index] = detail
            print("Client is added at index ", index)
            break
        else:
            index=(index+a**2)%size
            a+=1

def search_linear(id):
    id=int(input("Enter the id to be searched"))
    index = id % size
    for i in range(size):
        if(client_list_linear[index]!=None):
            if(client_list_linear[index][0]==id):
                print("Client is found at location",index)
                break
        index=(index+1)%size
    else:
        print("Client is not present")        
    

def search_quadratic(id):
    id=int(input("Enter the id to be searched"))
    index = id % size
    a=1
    for i in range(size):
        if(client_list_quadratic[index]!=None):
            if(client_list_quadratic[index][0]==id):
                print("Client is found at location",index)
                break
        index=(index+a**2)%size
        a+=1
    else:
        print("Client is not present")
    
def delete_linear(id):
    id=int(input("ENter the Id to be deleted"))
    index=id % size
    for i in range(size):
        if(client_list_linear[index]!=None):
            if(client_list_linear[index][0]==id):
                print("Client deleted")
                client_list_linear[index]=None
                break
        index=(index+1)%size
    else:
        print("client not found")    
        
        
        
        
def delete_quadratic(id):
    id=int(input("ENter the Id to be deleted"))
    index=id % size
    a=1
    for i in range(size):
        if(client_list_quadratic[index]!=None):
            if(client_list_quadratic[index][0]==id):
                print("Client deleted")
                client_list_quadratic[index]=None
                break
        index=(index+a**2)%size
        a+=1
    else:
        print("client not found")    
        
        

def main():
    while True:
        print("1. Insert the client (linear probing)")
        print("2. Insert the client (quadratic probing)")
        print("3. Display the client list (linear probing)")
        print("4. Display the client list (quadratic probing)")
        print("5. Search the client (linear probing)")
        print("6. Search the client (quadratic probing)")
        print("7. Delete the client (linear probing)")
        print("8. Delete the client (quadratic probing)")
        print("9. Exit")
        ch = int(input("Enter the choice : "))
        if ch == 1:
            insert_linear()
        elif ch == 2:
            insert_quadratic()
        elif ch == 3:
            print(client_list_linear)
        elif ch == 4:
            print(client_list_quadratic)
        elif ch == 5:
            search_linear(id)
        elif ch == 6:
            search_quadratic(id)
        elif ch == 7:
            delete_linear(id)
        elif ch == 8:
            delete_quadratic(id)
        elif ch == 9:
            break
        else:
            print("Incorrect input")

main() 