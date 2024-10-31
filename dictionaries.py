import csv

def load_contacts(filename):
    contacts = {}
    with open(filename, mode = 'r' , newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            
            first_name = row [0]
            last_name = row [1]
            phone_number = row[2]
            email = row [3]
            contacts[last_name] = [first_name, last_name, phone_number, email]
    return contacts

def display_contact_info(contact_info):
    if contact_info:
        print("\nContact Information:")
        print(f"First Name: {contact_info [0]} {contact_info[1]}")
        print(f"Phone Number: {contact_info[2]}")
        print(f"Email: {contact_info[3]}")
    else:
        print("No contact information found for this last name.")
     

def main():
    filename = 'dictionaries.csv' # Change this to your CSV file location
    
    contacts = load_contacts(filename)
    
    last_name = input('Please enter a last name to look up: ').strip() # .strip() is used to delete any whites
    contact_info = contacts.get(last_name)
    
    display_contact_info(contact_info)

if __name__ == "__main__":    
    main()
    