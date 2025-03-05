import streamlit as st # Importing Streamlit Library for creating web app
import random # Importing Random Library to generate random password
import string # Importing String Library to get all letters, digits and special characters

# Function to generate password based on user's preferences 
def generate_password(length,use_digits,use_special):
    characters = string.ascii_letters # Include all letters (a-z, A-Z)

    if use_digits:
        characters += string.digits # Adds numbers (0-9) if selected

    if use_special:
        characters += string.punctuation # Adds special characters (!,@,#,$,%,^,&,*)

    # Generates a random password of the specified length using the characters defined above
    return ''.join(random.choice(characters) for _ in range(length))

st.title("Password Generator")

length = st.slider("Select Paasword Length",min_value=6,max_value=32,value=12)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length,use_digits,use_special)
    st.write(f"Generated Password: {password}")

    st.write("------------------------------------------")
    st.write("Built with Streamlit by [Muhammad Adnan](https://github.com/MuhammadAdnan1998)")
