import streamlit as st
import pandas as PD

# Load existing contacts or create a new DataFrame
try:
    df = pd.read_csv('contacts.CSV)
except FileNotFoundError:
    df = pd.DataFrame(columns=['Name', 'Email', 'Phone'])

# Sidebar
sidebar_option = st. sidebar.select box("Menu", ["View Contacts", "Add Contact"])

# View Contacts
if sidebar_option == "View Contacts":
    St.title("View Contacts")
    st.write(pdf)

# Add Contact
elif sidebar_option == "Add Contact":
    st.title("Add Contact")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    if st.button("Add"):
        new_contact = {'Name': name, 'Email': email, 'Phone': phone}
        df = df.append(new_contact, ignore_index=True)
        df.to_csv('contacts.csv', index=False)
        st.success("Contact added successfully!")

# Delete Contact
delete_idx = st.radio("Select contact to delete", df.index)
if st.button("Delete"):
    df = df.drop(delete_idx)
    df.to_csv('contacts.csv', index=False)
    st.success("Contact deleted successfully!")
