import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from tkinter import scrolledtext 

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address



    
    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}"
    
    
    def update_details(self, phone_number=None, email=None, address=None):
        if phone_number:
            self.phone_number = phone_number
        if email:
            self.email = email
        if address:
            self.address = address




class ContactList:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        self.contacts.append(contact)
    
    def view_contacts(self):
        if not self.contacts:
            return "No contacts found."
        else:
            return "\n-------------------\n".join(str(contact) for contact in self.contacts)
    
    def search_contact(self, keyword):
        result = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                result.append(str(contact))
        if not result:
            return "Contact not found."
        return "\n-------------------\n".join(result)
    
    def update_contact(self, name, phone_number=None, email=None, address=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.update_details(phone_number, email, address)
                return "Contact updated successfully."
        return "Contact not found."
    
    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                del self.contacts[i]
                return "Contact deleted successfully."
        return "Contact not found."

class ContactManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        
        self.contact_list = ContactList()
        self.create_widgets()
    
    def create_widgets(self):
      
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        button_frame.grid_rowconfigure(0, weight=1)
        button_frame.grid_columnconfigure(0, weight=1)
        
        self.text_area = scrolledtext.ScrolledText(self.root, width=40, height=15)
        self.text_area.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
       
        tk.Button(button_frame, text="Add Contact", command=self.add_contact).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        tk.Button(button_frame, text="View Contacts", command=self.view_contacts).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        tk.Button(button_frame, text="Search Contact", command=self.search_contact).grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        tk.Button(button_frame, text="Update Contact", command=self.update_contact).grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        tk.Button(button_frame, text="Delete Contact", command=self.delete_contact).grid(row=0, column=4, padx=5, pady=5, sticky="ew")
        tk.Button(button_frame, text="Exit", command=self.root.quit).grid(row=0, column=5, padx=5, pady=5, sticky="ew")
    
    def get_contact_details(self, action):
        contact_details = simpledialog.askstring("Contact Details",
            f"Enter details for {action}:\n\nFormat: Name, Phone, Email, Address")
        if contact_details:
            details = contact_details.split(',')
            if len(details) == 4:
                return tuple(detail.strip() for detail in details)
            else:
                messagebox.showwarning("Input Error", "Please enter all details in the format: Name, Phone, Email, Address.")
        return None, None, None, None
    
    def add_contact(self):
        name, phone_number, email, address = self.get_contact_details("Add Contact")
        if name:
            contact = Contact(name, phone_number, email, address)
            self.contact_list.add_contact(contact)
            messagebox.showinfo("Success", "Contact added successfully.")
    
    def view_contacts(self):
        contacts = self.contact_list.view_contacts()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, contacts)
    
    def search_contact(self):
        keyword = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if keyword:
            result = self.contact_list.search_contact(keyword)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, result)
    
    def update_contact(self):
        name = simpledialog.askstring("Update Contact", "Enter name of contact to update:")
        if name:
            phone_number = simpledialog.askstring("Update Contact", "Enter new phone number (leave blank to keep current):")
            email = simpledialog.askstring("Update Contact", "Enter new email (leave blank to keep current):")
            address = simpledialog.askstring("Update Contact", "Enter new address (leave blank to keep current):")
            result = self.contact_list.update_contact(name, phone_number, email, address)
            messagebox.showinfo("Update Status", result)
    
    def delete_contact(self):
        name = simpledialog.askstring("Delete Contact", "Enter name of contact to delete:")
        if name:
            result = self.contact_list.delete_contact(name)
            messagebox.showinfo("Delete Status", result)







            

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagementApp(root)
    root.mainloop()
