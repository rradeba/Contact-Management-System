import sys 
import os 
import re

#universal variables 
main_contact_dir = {"Name": [],"Phone Number": [], "Email Address": [], "Additional Information": []}
num_contact = 0 


#function to display the main menu 

def main_menu():
    while True:  
        try:
            main_menu_selection= input("-----------------------------------\n\tWelcome to the Contact Management System!\n Menu:\n 1. Add a new contact\n 2. Edit an existing contact\n 3. Delete a contact\n 4. Search for a contact\n 5. Display all contacts\n 6. Export contacts to a text file\n 8. Quit\n------------------------------------\n")
            possible_menu_values = [1,2,3,4,5,6,7]
        except TypeError: 
            main_menu_selection= input("Please type one of the listed")
        if main_menu_selection == "1":
            add_contact(main_contact_dir) 
        elif main_menu_selection == "2":
            edit_contact(main_contact_dir)  
        elif main_menu_selection == "3":
            delete_contact(main_contact_dir)   
        elif main_menu_selection == "4":
            search_contact(main_contact_dir)  
        elif main_menu_selection == "5":
            display_contact(main_contact_dir)  
        elif main_menu_selection == "6":
            export_contact(main_contact_dir)  
        elif main_menu_selection == "7":
            quit_program()

# function for adding a contanct
def add_contact(main_contact_dir): 
    global num_contact
    while True:
        while True:
            get_name = input("\nName (ex. John Smith): ")
            name_pattern = re.compile(r"^[A-Za-z]+(?: [A-Za-z]+)*$")
            if name_pattern.match(get_name):
                main_contact_dir["Name"].append(get_name)
                break
            else:
                print("Try again.") 
        while True: 
            get_phone = input("Phone Number (ex. (123) 456-7890): ")
            phone_pattern = re.compile(r'^\(\d{3}\) \d{3}-\d{4}$')
            if phone_pattern.match(get_phone):
                main_contact_dir["Phone Number"].append(get_phone)
                break
            else:
                print("Try again.")
        while True:  
            get_email = input("Email Address (ex. johnsmith@email.com): ")
            email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
            if email_pattern.match(get_email):
                main_contact_dir["Email Address"].append(get_email)
                break
            else:
                print("Try again.")
            get_additional_information = input("Additional Information(address, notes, e.g.): ")
            main_contact_dir["Additional Information"].append(get_additional_information)
            global num_contact
            num_contact += 1 
    
        try_again = input("\nWould you like to add another name (Y/N): ")
        while try_again not in ["Y", "N"]:
            try_again = input("Please type Y or N.")
        if try_again == "N": 
            break 

# function to edit a contact  
def edit_contact(main_contact_dir):
    global num_contact
    if num_contact == 0:
        print("\nNo contacts.\n")
        return    
    display_contact(main_contact_dir)
    
    while True:
        edit_num = input("What number contact would you like to edit?: ")
        try:
            edit_num = int(edit_num)
            if edit_num not in range(1, num_contact + 1):
                print("Please choose a valid number.")
            else:
                edit_num -= 1
                break
        except ValueError:
            print("Please enter a valid number.")
    
    get_name = input("\nNew Name: ")
    if get_name:
        main_contact_dir["Name"][edit_num] = get_name  
    get_phone = input("New Phone Number: ")
    if get_phone:
        main_contact_dir["Phone Number"][edit_num] = get_phone
    get_email = input("New Email Address: ")
    if get_email:
        main_contact_dir["Email Address"][edit_num] = get_email
    get_additional_information = input("New Additional Information: ")
    if get_additional_information:
        main_contact_dir["Additional Information"][edit_num] = get_additional_information
    
    print("Contact updated successfully")


#finction to delete a contact
def delete_contact(main_contact_dir):
    global num_contact
    if num_contact == 0:
        print("\nNo contacts.\n")
        return
    display_contact(main_contact_dir)
    while True:
        delete_num = input(f"\nWhich contact would you like to delete (1-{num_contact}): ")
        try:
            delete_num = int(delete_num)
            if delete_num not in range(1, num_contact + 1):
                print("Please choose a valid number.")
            else:
                delete_num -= 1
                for key in main_contact_dir:
                    del main_contact_dir[key][delete_num]
                num_contact -= 1
                print("Contact deleted successfully.")
                break
        except ValueError:
            print("Please enter a valid number.")
    try_again = input("\nWould you like to delete another contact (Y/N): ")
    while try_again not in ["Y", "N"]:
        try_again = input("Please type Y or N: ")
    if try_again == "N": 
        return
                
#finction to search a contact
def search_contact(main_contact_dir):
    global num_contact
    while True:
        search_type = input("Search by Name, Email Address, or Phone Number: ")
        while search_type not in ["Name", "Email Address", "Phone Number"]:
            search_type = input("Please type Name, Email Address, or Phone Number: ")
        
        search_value = input(f"Search by {search_type}: ")
        found = False
        for index in range(num_contact):
            if search_value == main_contact_dir[search_type][index]:
                print(f"\nContact {index+1}:")
                print(f"Name: {main_contact_dir['Name'][index]}")
                print(f"Phone Number: {main_contact_dir['Phone Number'][index]}")
                print(f"Email Address: {main_contact_dir['Email Address'][index]}")
                print(f"Additional Information: {main_contact_dir['Additional Information'][index]}\n")
                found = True
        if not found:
            print(f"No contact found with {search_type}: {search_value}")
        
        try_again = input("\nWould you like to search for another contact (Y/N): ")
        while try_again not in ["Y", "N"]:
            try_again = input("Please type Y or N: ")
        if try_again == "N": 
            break


#finction to delete a contact
def display_contact(main_contact_dir):
    global num_contact
    if num_contact == 0:
        print("\nNo contacts.\n")
    for i in range(num_contact):
        print(f"Contact {i+1}: \nName: {main_contact_dir['Name'][i]}")
        print(f"Phone Number: {main_contact_dir['Phone Number'][i]}")
        print(f"Email Address: {main_contact_dir['Email Address'][i]}") 
        print(f"Additional Information: {main_contact_dir['Additional Information'][i]}\n")      


#finction to export contacts
def export_contact(main_contact_dir):
    global num_contact
    with open('export_text_file.txt', 'w') as file:
        if num_contact == 0:
            file.write("No contacts.\n")
        else:
            for i in range(num_contact):
                file.write(f"Contact {i+1}:\n")
                file.write(f"Name: {main_contact_dir['Name'][i]}\n")
                file.write(f"Phone Number: {main_contact_dir['Phone Number'][i]}\n")
                file.write(f"Email Address: {main_contact_dir['Email Address'][i]}\n")
                file.write(f"Additional Information: {main_contact_dir['Additional Information'][i]}\n\n")
    print("Contacts exported successfully")


# function to quit the program
def quit_program():
    sys.exit(0)
        
        
main_menu()