from errors.notfound_exception import NotFoundContact


class AddressBook:
    def __init__(self):
        self.contacts = []
        
        
    def get_contacts(self):
        print('\n')
        if len(self.contacts) == 0:
            print('No contacts found')
        else:
            for contact in self.contacts:
                print('Contact Info :')
                print('name : {}'.format(contact.name))
                print('number : {}'.format(contact.number))
                print('email : {}'.format(contact.email))
                print('\n')
                
    # CRUD
    def add_contact(self,contact):
        try:
            self.contacts.append(contact)
        except:
            print('Something went wrong')
        
    # def get_search_contacts(self,search_value):
        # if len(self.contacts) == 0:
        #     print('No contacts found')
        #     print('\n')
        # else:
        #     searched_contacts = []
        #     for contact in self.contacts:
        #         if (contact.name.lower() in search_value.lower() or contact.number.lower() in search_value.lower()):
        #             searched_contacts.append(contact)
        #     if not searched_contacts:
        #         print(f"No Contact With Name : {search_value}\n")
        #     else:
        #         for contact in searched_contacts:
        #             print('Contact Info :')
        #             print('name : {}'.format(contact.name))
        #             print('number : {}'.format(contact.number))
        #             print('email : {}'.format(contact.email))
        #             print('\n')
                
    def get_search_contacts(self, search_value):
        if not self.contacts:
            print('No contacts found')
            print('\n')
        else:
            searched_contacts = []
            for contact in self.contacts:
                if (search_value.lower() in contact.name.lower()) or (search_value in contact.number):
                    searched_contacts.append(contact)
            if not searched_contacts:
                print(f"No Contact Matching: {search_value}\n")
            else:
                for contact in searched_contacts:
                    print('Contact Info:')
                    print('name: {}'.format(contact.name))
                    print('number: {}'.format(contact.number))
                    print('email: {}'.format(contact.email))
                    print('\n')

    
                
