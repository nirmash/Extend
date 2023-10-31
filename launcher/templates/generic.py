import sys
import requests

todo_endpoint = "https://api-service.victorioussea-1e5e534f.eastus2.azurecontainerapps.io/lists/"

def CreateList(name, description):
    list = {
        "name" : name,
        "description" : description
    }
    response = requests.post(todo_endpoint,json=list)
    if response.status_code < 299:
        print("List Created")
        print(response.json())
        return response.json()
    else:
        print("List creation failed")
        return None

def GetLists():
    response = requests.get(todo_endpoint)
    if response.status_code == 200:
        print("Lists")
        print(response.json())
        return response.json()
    else:
        print("Lists get failed")
        return None

def GetList(list_id):
    response = requests.get(todo_endpoint + list_id)
    if response.status_code == 200:
        print("List information")
        print(response.json())
        return response.json()
    else:
        print("List get failed")
        return None
    
def UpdateList(list_id, name, description):
    list = {
        "name" : name,
        "description" : description
    }
    response = requests.put(todo_endpoint + list_id, json=list)
    if response.status_code == 200:
        print("List updated")
        print(response.json())
        return response.json()
    else:
        print("List update failed")
        return None
    
def DeleteList(list_id):
    response = requests.delete(todo_endpoint + list_id)
    if response.status_code == 204:
        print("List deleted")
    else:
        print("List deletion failed")
    print("Done")

def GetListItems(list_id):
    response = requests.get(todo_endpoint + list_id + "/items")
    if response.status_code == 200:
        print("List items")
        print(response.json())
        return response.json()
    else:
        print("List items get failed")
        return None
    
def CreateListItem(list_id, name, description, state):
    item = {
        "name" : name,
        "description" : description,
        "state" : state
    }
    response = requests.post(todo_endpoint + list_id + "/items", json=item)
    if response.status_code == 201:
        print("List item created")
        print(response.json())
        return response.json()
    else:
        print("List item creation failed")
        return None
    
def GetListItem(list_id, item_id):
    response = requests.get(todo_endpoint + list_id + "/items/" + item_id)
    if response.status_code == 200:
        print("List item information")
        print(response.json())
        return response.json()
    else:
        print("List item get failed")
        return None
    
#UpdateListItem('f1579047-e784-4349-9acb-c6db99aa830d','9700516d-16e2-4b7f-a2d3-c3b53cbe4570','changed','changed','todo','2021-04-01T00:00:00Z','2021-04-01T00:00:00Z')

def UpdateListItem(list_id, item_id, name, description, state,completedDate, dueDate):
    item = {
        "name" : name,
        "description" : description,
        "state" : state,
        "completedDate" : completedDate,
        "dueDate" : dueDate
    }
    response = requests.put(todo_endpoint + list_id + "/items/" + item_id, json=item)
    print(todo_endpoint + list_id + "/items/" + item_id)
    print(response.status_code)
    if response.status_code == 200:
        print("List item updated")
        print(response.json())
        return response.json()
    else:
        print("List item update failed")
        return None
       
def DeleteListItem(list_id, item_id):
    response = requests.delete(todo_endpoint + list_id + "/items/" + item_id)
    if response.status_code == 204:
        print("List item deleted")
    else:
        print("List item deletion failed")
    print("Done")

def GetListItemsByState(list_id, state):
    response = requests.get(todo_endpoint + list_id + "/items?state=" + state)
    if response.status_code == 200:
        print("List items")
        print(response.json())
        return response.json()
    else:
        print("List items get failed")
        return None

def injected (args):
    #$CODE$

def parse_args(args):
    try:
        str=args[2:len(sys.argv[1])-1]
        return str.replace("'", "").split(", ")
    except:
        return None


if __name__ == "__main__":

    if len(sys.argv) > 1:
        injected(parse_args(sys.argv[1]))
    else:
        injected (None)

