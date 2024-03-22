import streamlit as st
from database import add_data_player,add_data_award,add_data_team,add_data_previous_records

def create_player():
    col1, col2 = st.columns(2)
    with col1:
        player_id = st.text_input("Player ID")
        player_team_name = st.text_input("Team Name")
        base_price = st.text_input("Base Price")
        player_name = st.text_input("Player Name")
        player_type = st.text_input("Player Type")
    with col2:
        wickets_take = st.text_input("Wickets Taken")
        runs_scored = st.text_input("Runs Scored")
        player_country = st.text_input("Player Country")
        year_of_auction = st.text_input("Year of Auction")
        player_auc_id = st.text_input("Player Auction ID")
    if st.button("Add Data"):
        add_data_player(player_id,player_team_name,base_price, player_name,player_type,wickets_take, runs_scored,player_country,year_of_auction, player_auc_id)
        st.success("Successfully added Data: {}".format(player_id))
        
def create_award():
    col1, col2 = st.columns(2)
    with col1:
        a_name = st.text_input("Award name")
        type_of_award = st.selectbox("Type of Award",["Trophy and cash"])
    with col2:
        cash_prize_in_rupees = st.text_input("Cash In Rupees")
        team_received_for = st.text_input("Team Received For")
        award_player_id = st.text_input("Award Player ID")
    if st.button("Add Data"):
        add_data_award(a_name, type_of_award, cash_prize_in_rupees, team_received_for ,award_player_id)
        st.success("Successfully added Data: {}".format(a_name))
                
def create_team():
    col1, col2 = st.columns(2)
    with col1:
        team_name = st.text_input("Team Name")
        budget_in_rupees = st.text_input("Budget In Rupees")
        purse_remaining_in_rupees = st.text_input("Purse Remaining in Rupees")
        purse_spent_in_rupees = st.text_input("Purse Spent in Rupees")
        region_representing = st.text_input("Region Representing")
    with col2:
        team_owner_id = st.text_input("Team Owner ID")
        team_owner_type = st.selectbox("Team Owner Type",["Indian", "Overseas"])
        team_owner_name = st.text_input("Team Owner Name")
        team_player_id = st.text_input("Team Player ID")
    if st.button("Add Data"):
        add_data_team(team_name,budget_in_rupees,purse_remaining_in_rupees,purse_spent_in_rupees,region_representing, team_owner_id, team_owner_type,team_owner_name,team_player_id) 
        st.success("Successfully added Data: {}".format(team_owner_id))
        
def create_previous_records():
    col1, col2 = st.columns(2)
    with col1:
        state_team = st.text_input("State Team")
        prev_team = st.text_input("Previous Team")
    with col2:
        no_of_teams_played_for_prev = st.text_input("No of teams previously played for")
        debut_date = st.text_input("Debut Date")
        career_span_in_years = st.text_input("Career span in years")
        prevrec_player_id = st.text_input("Previous Record Player ID")    
    if st.button("Add Data"):
        add_data_previous_records(state_team, prev_team, no_of_teams_played_for_prev, debut_date,career_span_in_years,prevrec_player_id)
        st.success("Successfully added Data: {}".format(state_team))