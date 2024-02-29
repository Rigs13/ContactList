import { useState, useEffect } from 'react';
import ContactList from "./ContactList.jsx";
import './App.css';
import ContactForm from "./ContactForm.jsx";

function App() {
    // state to store contacts
    const [contacts, setContacts] = useState([])

    // call to load contacts
    useEffect(() => {
        fetchContacts()
    },[]);

    // async function to fetch contacts
    const fetchContacts = async () => {
        // send a request for contact list
        const response = await fetch("http://127.0.0.1:5000/contacts");
        // get json data from response
        const data = await response.json();
        setContacts(data.contacts);
        console.log(data.contacts);
    }

  return (
      <>
      <ContactList contacts={contacts}/>
      <ContactForm />
      </>
  );
}

export default App;
