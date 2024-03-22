import streamlit as st
#from database import create_table
from create import create_player,create_award,create_team,create_previous_records
from read import read1,read2,read3,read4
from update import update_player,update_award,update_team,update_previous_records
from delete import delete_player,delete_award,delete_team,delete_previous_records

def main():
    st.title("IPL AUCTION SYSTEM")
    menu = ["Player", "Award", "Team", "Previous Records"]
    choice1 = st.sidebar.selectbox("Menu", menu)
    #create_table()
    if choice1 == "Create":
        st.subheader("Player")
                
    elif choice1 == "Read":
        st.subheader("Award")
       
        
    elif choice1 == "Update":
        st.subheader("Team")
        
        
    elif choice1 == "Previous Records":
        st.subheader("Previous Records")
        
    
    menu = ["Create", "Read", "Update", "Delete"]
    choice2 = st.sidebar.selectbox("Menu", menu)

    
    if choice2 == "Create":
        st.subheader("Create")
        #create()
        if choice1 == "Player":
            create_player()
        if choice1 == "Award":
            create_award()
        if choice1 == "Team":
            create_team()
        if choice1 == "Previous Records":
            create_previous_records()
            
    elif choice2 == "Read":
        st.subheader("Read")
        #read()
        if choice1 == "Player":
            read1()
        if choice1 == "Award":
            read2()
        if choice1 == "Team":
            read3()
        if choice1 == "Previous Records":
            read4()
        
    elif choice2 == "Update":
        st.subheader("Update")
        #update()
        if choice1 == "Player":
            update_player()
        if choice1 == "Award":
            update_award()
        if choice1 == "Team":
            update_team()
        if choice1 == "Previous Records":
            update_previous_records()
        
    elif choice2 == "Delete":
        st.subheader("Delete")
        #delete()
        #create()
        if choice1 == "Player":
            delete_player()
        if choice1 == "Award":
            delete_award()
        if choice1 == "Team":
            delete_team()
        if choice1 == "Previous Records":
            delete_previous_records()
        
if __name__ == '__main__':
    main()