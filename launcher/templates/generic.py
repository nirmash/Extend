import sys
import requests
import json
import urllib.parse

todo_endpoint = "https://api-service.victorioussea-1e5e534f.eastus2.azurecontainerapps.io/lists/"

def CreateList(name, description):
    list = {
        "name" : name,
        "description" : description
    }
    custom_headers = {
        "call-source": "extension"
    }
    response = requests.post(todo_endpoint,json=list, headers=custom_headers)
    if response.status_code < 299:
        print(response.json())
        return response.json()
    else:
        print("List creation failed")
        return None

def GetLists():
    response = requests.get(todo_endpoint)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print("Lists get failed")
        return None

def GetList(list_id):
    response = requests.get(todo_endpoint + list_id)
    if response.status_code == 200:
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
    custom_headers = {
        "call-source": "extension"
    }
    response = requests.put(todo_endpoint + list_id, json=list, headers=custom_headers)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print("List update failed")
        return None
    
def DeleteList(list_id):

    custom_headers = {
        "call-source": "extension"
    }
    response = requests.delete(todo_endpoint + list_id, headers=custom_headers)
    if response.status_code == 204:
        print("List deleted")
    else:
        print("List deletion failed")
    print("Done")

def GetListItems(list_id):
    response = requests.get(todo_endpoint + list_id + "/items")
    if response.status_code == 200:
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
    custom_headers = {
        "call-source": "extension"
    }
    response = requests.post(todo_endpoint + list_id + "/items", json=item, headers=custom_headers)
    if response.status_code == 201:
        print(response.json())
        return response.json()
    else:
        print("List item creation failed")
        return None
    
def GetListItem(list_id, item_id):
    response = requests.get(todo_endpoint + list_id + "/items/" + item_id)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print("List item get failed")
        return None
    
def UpdateListItem(list_id, item_id, name, description, state,completedDate, dueDate, list):
    item = {
        "id" : item_id,
        "list": list,
        "listId": list_id,
        "name" : name,
        "description" : description,
        "state" : state,
        "completedDate" : completedDate,
        "dueDate" : dueDate        
    }
    custom_headers = {
        "call-source": "extension"
    }
    response = requests.put(todo_endpoint + list_id + "/items/" + item_id, json=item, headers=custom_headers)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print("List item update failed")
        return None
       
def DeleteListItem(list_id, item_id):

    custom_headers = {
        "call-source": "extension"
    }
    response = requests.delete(todo_endpoint + list_id + "/items/" + item_id,headers=custom_headers)
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

#remember to push the container

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

