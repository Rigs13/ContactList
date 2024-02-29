import {useState} from "react";

const ContactForm = ({}) => {
    // state of the form
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");

    // function for submit button
    const onSubmit = async (e) => {
        // prevent refresh page automation
        e.preventDefault()

        // post request

        // define data
        const data = {
            firstName,
            lastName,
            email
        }
        // define url
        const url = "http://127.0.0.1:5000/create_contact"

        // set options for request
        const options = {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }

        // send request
        const response = await fetch(url, options)
        // alert if error
        if (response.status !== 201 && response.status !== 200) {
            const data = await response.json()
            alert(data.message)
        } else {
            // success for response

        }
    }

    // return form
    return (
        <form onSubmit={onSubmit}>
            <div>
                <label htmlFor="firstName">First Name:</label>
                <input
                    type="text"
                    id="firstName"
                    value={firstName}
                    onChange={(e) => setFirstName(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="lastName">Last Name:</label>
                <input
                    type="text"
                    id="lastName"
                    value={lastName}
                    onChange={(e) => setLastName(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="email">Email:</label>
                <input
                    type="text"
                    id="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
            </div>
            <button type="submit">Create Contact</button>
        </form>
    );
};

// export form
export default ContactForm