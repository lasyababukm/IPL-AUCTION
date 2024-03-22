import streamlit as st
import pandas as pd
from database import view_all_players,delete_player_data, view_only_players_names,view_all_awards,view_only_awards_names,delete_award_data,view_all_team,view_only_team_names,delete_team_data,view_all_previous_records,view_only_previous_records,delete_previous_records_data

def delete_player():
    result = view_all_players()
    df = pd.DataFrame(result, columns=["Player ID", "Team Name","Base Price","Player Name","Player Type" ,"Wickets Taken","Runs Scored","Player Country","Year of Auction","Player Auction ID"])
    with st.expander("Current Players"):
        st.dataframe(df)

    list_of_players = [i[0] for i in view_only_players_names()]
    selected_players = st.selectbox("Data to edit", list_of_players)
    st.warning("Do you want to delete '{}'??".format(selected_players))
    if st.button("Delete Player Data"):
        delete_player_data(selected_players)
        st.success("Successfully deleted")

    result2 =  view_all_players()
    df2 = pd.DataFrame(result2, columns=["Player ID", "Team Name","Base Price","Player Name","Player Type" ,"Wickets Taken","Runs Scored","Player Country","Year of Auction","Player Auction ID"])
    with st.expander("Updated data"):
        st.dataframe(df2)
        
        
def delete_award():
    result3 = view_all_awards()
    df3 = pd.DataFrame(result3, columns=["Award name", "Type of Award", "Cash In Rupees","Team Received For","Award Player ID"])
    with st.expander("Current Awards"):
        st.dataframe(df3)

    list_of_awards = [i[0] for i in view_only_awards_names()]
    selected_awards = st.selectbox("Data to edit", list_of_awards)
    st.warning("Do you want to delete '{}'??".format(selected_awards))
    if st.button("Delete Award Data"):
        delete_award_data(selected_awards)
        st.success("Successfully deleted")

    result4 = view_all_awards()
    df4 = pd.DataFrame(result4, columns=["Award name", "Type of Award", "Cash In Rupees","Team Received For","Award Player ID"])
    with st.expander("Updated data"):
        st.dataframe(df4)
        
def delete_team():
    result5 = view_all_team()
    df5 = pd.DataFrame(result5, columns=["Team Name","Budget In Rupees","Purse Remaining in Rupees","Purse Spent in Rupees", "Region Representing", "Team Owner ID","Team Owner Type","Team Owner Name","Team Player ID"])
    with st.expander("Current Team"):
        st.dataframe(df5)

    list_of_team = [i[0] for i in view_only_team_names()]
    selected_team = st.selectbox("Data to edit", list_of_team)
    st.warning("Do you want to delete '{}'??".format(selected_team))
    if st.button("Delete Team Data"):
        delete_team_data(selected_team)
        st.success("Successfully deleted")

    result6 = view_all_team()
    df6 = pd.DataFrame(result6, columns=["Team Name","Budget In Rupees","Purse Remaining in Rupees","Purse Spent in Rupees", "Region Representing", "Team Owner ID","Team Owner Type","Team Owner Name","Team Player ID"])
    with st.expander("Updated data"):
        st.dataframe(df6)
        
def delete_previous_records():
    result7 = view_all_previous_records()
    df7 = pd.DataFrame(result7, columns=["State Team", "Previous Team", "No of teams previously played for","Debut Date","Career span in years","Previous Record Player ID"])
    with st.expander("Current Previous Records"):
        st.dataframe(df7)

    list_of_previous_records = [i[0] for i in view_only_previous_records()]
    selected_previous_records = st.selectbox("Data to edit", list_of_previous_records)
    st.warning("Do you want to delete '{}'??".format(selected_previous_records))
    if st.button("Delete Previous Records"):
        delete_previous_records_data(selected_previous_records)
        st.success("Successfully deleted")

    result8 = view_all_previous_records()
    df8 = pd.DataFrame(result8, columns=["State Team", "Previous Team", "No of teams previously played for","Debut Date","Career span in years","Previous Record Player ID"])
    with st.expander("Updated data"):
        st.dataframe(df8)