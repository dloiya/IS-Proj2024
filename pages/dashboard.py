import streamlit as st

def dashboard():
    user = st.session_state.user
    button = ""
    if user:
        st.title(f"Welcome, {st.session_state.user['username']}!")

        user_access_level = st.session_state.user["access"]
        if user_access_level == "admin":
            st.write("You have admin access.")
            admin_options = ["Open Vault", "Register New User", "Open Logs"]
        else:
            st.write("You have user access.")
            admin_options = []

        st.subheader("Options")
        for option in admin_options:
            if st.button(option):
                if option == "Open Vault":
                    st.switch_page("pages/vault.py")
                elif option == "Register New User":
                    st.switch_page("pages/adduser.py")
                elif option == "Open Logs":
                    st.switch_page("pages/logs.py")
    else:
        st.warning("Please log in to access the dashboard.")

dashboard()
