import streamlit as st
import re


st.set_page_config(page_title="Shout Secure", page_icon="🛡️")
st.title("SHOUT SECURE 🔐")
st.write("Secure Your Accounts! Check Your Password Strength")

def passwordchecker(password):
    score = 0
    if len(password) >= 8:
        score += 1
    else:
        st.warning("🚫Password must contain at least 8 characters.")

        
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]",password):
        score += 1
    else:
        st.warning("🚫Include both uppercase and lowercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        st.warning("🚫Include at least one number.")

    if re.search(r"[!@#$%^&*/?<>]", password):
        score += 1
    else:
        st.warning("🚫Include at least one special character.")

    if score == 4 :
        st.success("✔️Password is strong")
        st.balloons()
    elif score ==3 :
        st.info("⚠️Password is moderately strong, could be stronger")
    else:
        st.info("❌Password is weak, try to make it stronger.")
    
password =st.text_input("Enter Pasword...🙈")

if st.button("Check"):
   passwordchecker(password)
