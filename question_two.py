import os 

contacts = {
    "1": {
        "name" : "John Lennon",
        "address" : "Imagine Street 10, London",
        "phone"   : "796123456",
    },
    "2":{
        "name" : "Paul McCartney",
        "address" : "Pennylane Street 12, London", 
        "phone"  : "796852147"
    },
    "3": {
        "name" : "George Harrison",
        "address" : "Eleanor Rigby alley 8, London",
        "phone" : "762318974",
    },
    "4" : {
        "name" : "Ringo Starr",
        "address" : "Abbey Road, London",
        "phone" : "792456789"
    }
}


def continueMenu():
    print('')
    input("Press enter to continue")

def menu():
    os.system("clear")
    print("Press 1 to search contact")
    print("Press 2 to show all contacts")
    print("Press 3 to add new contact")
    print("Press 4 to exit")


def printContact(inputname):
	isIn = False
	for contact in contacts.items():
		if contact[1]['name']==inputname:
			isIn = True
			print('\n'+'name: ' + contact[1]['name'] + '\n' + 'address: ' + contact[1]['address'] + '\n' + 'phone: '+ contact[1]['phone'])
	if not isIn:
		print('Contact not found')



def printAllContacts():
	for contact in contacts.items():
			print('\n'+'name: ' + contact[1]['name'] + '\n' + 'address: ' + contact[1]['address'] + '\n' + 'phone: '+ contact[1]['phone'])

def addContacts():
    name = input("Enter new contact name:")
    address = input("Enter new contact address:")
    phone = input("Enter new contact phone")
    contacts.update({len(contacts)+1: {"name":name,"address":address,"phone":phone}})

while True:
    menu()
    print('')
    option = input("select an option:")

    if option==1:
        printContact(input('name:'))
        continueMenu()
    elif option==2:
        printAllContacts()
        continueMenu()   
    elif option==3:
        addContacts()
        continueMenu() 
    elif option==4:
    
        break
