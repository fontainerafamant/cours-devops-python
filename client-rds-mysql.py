import requests
import json

def get_all_items():
    response = requests.get('http://192.168.100.9:8080/books')
    items = response.json()
    return items


def create_item(item):
    response = requests.post('http://192.168.100.9:8080/books', json={'item': item})
    return response.json()


def delete_item(item_id):
    response = requests.delete(f'http://192.168.100.9:8080/books/{item_id}')
    return response.json()


def display_items():
    items = get_all_items()
    print('\nItem List:')
    if items:
        for item in items:
            print(item)
    else:
        print('No items found.')


def add_item():
    # item = {'id':10,'author':'Jean','title':'Mathematique','isbn':12151618}
    x =  '{ "author":"Jean", "isbn":12151618, "title":"Mathematique"}'
    item = json.loads(x)

    response = create_item(item)
    if 'message' in response:
        print('\nError:', response['message'])
    else:
        print('\nItem added successfully.')


def remove_item():
    display_items()
    item_id = input('\nEnter the ID of the item to remove: ')
    response = delete_item(item_id)
    if 'message' in response:
        print('\nOK:', response['message'])
    else:
        print('\nItem removed successfully.')


# CLI menu
while True:
    print('\n--- Item Menu ---')
    print('1. Display Items')
    print('2. Add Item')
    print('3. Remove Item')
    print('4. Exit')

    choice = input('\nEnter your choice (1-4): ')

    if choice == '1':
        display_items()
    elif choice == '2':
        add_item()
    elif choice == '3':
        remove_item()
    elif choice == '4':
        print('\nGoodbye!')
        break
    else:
        print('\nInvalid choice. Please try again.')
