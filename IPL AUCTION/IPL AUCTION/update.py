import streamlit as st
import pandas as pd
from database import view_all_players,view_all_awards,view_all_team,view_all_previous_records,view_only_players_names,view_only_awards_names,view_only_team_names,view_only_previous_records,get_players,get_awards,get_team,get_previous_records,edit_players_data,edit_awards_data,edit_team_data,edit_previous_records

def update_player():
    result = view_all_players()
    df = pd.DataFrame(result, columns=["Player ID", "Team Name","Base Price","Player Name","Player Type" ,"Wickets Taken","Runs Scored","Player Country","Year of Auction","Player Auction ID"])
    with st.expander("Current Players"):
        st.dataframe(df)

    list_of_players = [i[0] for i in view_only_players_names()]
    selected_players = st.selectbox("Players to edit", list_of_players)
    selected_result = get_players(selected_players)

    if selected_result:
        player_id=selected_result[0][0]
        player_team_name = selected_result[0][1]
        base_price = selected_result[0][2]
        player_name = selected_result[0][3]
        player_type = selected_result[0][4] 
        wickets_take=selected_result[0][5]
        runs_scored = selected_result[0][6]
        player_country=selected_result[0][7]
        year_of_auction=selected_result[0][8]
        player_auc_id=selected_result[0][9]
        col1, col2 = st.columns(2)
        with col1:
            new_player_id = st.text_input("Player ID", player_id)
            new_player_team_name = st.text_input("Team Name", player_team_name)
            new_base_price = st.text_input("Base Price",base_price)
            new_player_name = st.text_input("Player Name", player_name)
            new_player_type = st.text_input("Player Type",player_type)
        with col2:
            new_wickets_take = st.text_input("Wickets Taken", wickets_take)
            new_runs_scored = st.text_input("Runs Scored", runs_scored)
            new_player_country = st.text_input("Player Country", player_country)
            new_year_of_auction = st.text_input("Year of Auction", year_of_auction)
            new_player_auc_id = st.text_input("Player Auction ID", player_auc_id)
        if st.button("Update Players"):
            edit_players_data(new_player_id,new_player_team_name, new_player_name,new_base_price,new_player_type,new_wickets_take,new_runs_scored,
new_player_country,new_year_of_auction,new_player_auc_id,player_id)
            st.success("Successully updated ::{} to {}".format(player_id,new_player_id))
        result2 = view_all_players()
        df2 = pd.DataFrame(result2, columns=["Player ID", "Team Name","Base Price","Player Name","Player Type" ,"Wickets Taken","Runs Scored","Player Country","Year of Auction","Player Auction ID"])
        with st.expander("Updated data"):
            st.dataframe(df2) 
            
def update_award():
    result3 = view_all_awards()
    df3 = pd.DataFrame(result3, columns=["Award name", "Type of Award", "Cash In Rupees","Team Received For","Award Player ID"])
    with st.expander("Current Awards"):
        st.dataframe(df3)

    list_of_awards = [i[0] for i in view_only_awards_names()]
    selected_awards = st.selectbox("Awards to edit", list_of_awards)
    selected_result = get_awards(selected_awards)

    if selected_result:
        a_name=selected_result[0][0]
        type_of_award = selected_result[0][1]
        cash_prize_in_rupees = selected_result[0][2]
        team_received_for = selected_result[0][3]
        award_player_id=selected_result[0][4]
        
        col1, col2 = st.columns(2)
        with col1:
            new_a_name = st.text_input("Award name", a_name)
            new_type_of_award = st.text_input("Type of Award", type_of_award)
        with col2:
            new_cash_prize_in_rupees = st.text_input("Cash In Rupees",cash_prize_in_rupees)
            new_team_received_for = st.text_input("Team Received For", team_received_for)
            new_award_player_id = st.text_input("Award Player ID", award_player_id)
            
        if st.button("Update Awards"):
            edit_awards_data(new_a_name, new_type_of_award, new_cash_prize_in_rupees,
new_team_received_for,new_award_player_id, a_name)
            st.success("Successully updated ::{} to {}".format(a_name,new_a_name))
        result4 = view_all_awards()
        df4 = pd.DataFrame(result4, columns=["Award name", "Type of Award", "Cash In Rupees","Team Received For","Award Player ID"])
        with st.expander("Updated data"):
            st.dataframe(df4)
        
def update_team():
    result5 = view_all_team()
    df5 = pd.DataFrame(result5, columns=["Team Name","Budget In Rupees","Purse Remaining in Rupees","Purse Spent in Rupees", "Region Representing", "Team Owner ID","Team Owner Type","Team Owner Name","Team Player ID"])
    with st.expander("Current Team"):
        st.dataframe(df5)

    list_of_team = [i[0] for i in view_only_team_names()]
    selected_team = st.selectbox("Team to edit", list_of_team)
    selected_result = get_team(selected_team)

    if selected_result:
        team_name=selected_result[0][0]
        budget_in_rupees=selected_result[0][1]
        purse_remaining_in_rupees=selected_result[0][2]
        purse_spent_in_rupees=selected_result[0][3]
        region_representing = selected_result[0][4]
        team_owner_id = selected_result[0][5]
        team_owner_type=selected_result[0][6]
        team_owner_name=selected_result[0][7]
        team_player_id=selected_result[0][8]        
        
        col1, col2 = st.columns(2)
        with col1:
            new_team_name = st.text_input("Team Name", team_name)
            new_budget_in_rupees = st.text_input("Budget In Rupees", budget_in_rupees)
            new_purse_remaining_in_rupees=st.text_input("Purse Remaining in Rupees", purse_remaining_in_rupees)
            new_purse_spent_in_rupees=st.text_input("Purse Spent in Rupees", purse_spent_in_rupees)
            new_region_representing = st.text_input("Region Representing", region_representing)
        with col2:
            new_team_owner_id = st.text_input("Team Owner ID",team_owner_id)
            new_team_owner_type = st.selectbox("Team Owner Type", ["Indian", "Overseas"])
            new_team_owner_name = st.text_input("Team Owner Name", team_owner_name)
            new_team_player_id = st.text_input("Team Player ID", team_player_id)
                        
        if st.button("Update Team"):
            edit_team_data(new_team_name, new_budget_in_rupees,new_purse_remaining_in_rupees,new_purse_spent_in_rupees, new_region_representing,new_team_owner_id,
new_team_owner_type,new_team_owner_name,new_team_player_id,team_owner_id)
            st.success("Successully updated ::{} to {}".format(team_owner_id,new_team_owner_id))
        result6 = view_all_team()
        df6 = pd.DataFrame(result6, columns=["Team Name","Budget In Rupees","Purse Remaining in Rupees","Purse Spent in Rupees", "Region Representing", "Team Owner ID","Team Owner Type","Team Owner Name","Team Player ID" ])
        with st.expander("Updated data"):
            st.dataframe(df6) 
        
def update_previous_records():
    result7 = view_all_previous_records()
    df7 = pd.DataFrame(result7, columns=["State Team", "Previous Team", "No of teams previously played for","Debut Date","Career span in years","Previous Record Player ID"])
    with st.expander("Current previous_records"):
        st.dataframe(df7)


    list_of_previous_data = [i[0] for i in view_only_previous_records()]
    selected_previous_data = st.selectbox("previous_records to edit", list_of_previous_data)
    selected_result = get_previous_records(selected_previous_data)

    if selected_result:
        state_team=selected_result[0][0]
        prev_team = selected_result[0][1]
        no_of_teams_played_for_prev = selected_result[0][2]
        debut_date = selected_result[0][3]
        career_span_in_years=selected_result[0][4]
        prevrec_player_id=selected_result[0][5]
        
        col1, col2 = st.columns(2)
        with col1:
            new_state_team = st.text_input("State Team", state_team)
            new_prev_team = st.text_input("Previous Team", prev_team)
        with col2:
            new_no_of_teams_played_for_prev = st.text_input("No of teams previously played for",no_of_teams_played_for_prev)
            new_debut_date = st.text_input("Debut Date", debut_date)
            new_career_span_in_years = st.text_input("Career span in years", career_span_in_years)
            new_prevrec_player_id = st.text_input("Previous Record Player ID", prevrec_player_id)
            
        if st.button("Update Previous Records"):
            edit_previous_records(new_state_team, new_prev_team, new_no_of_teams_played_for_prev,
new_debut_date,new_career_span_in_years,new_prevrec_player_id, state_team)
            st.success("Successully updated ::{} to {}".format(state_team,new_state_team))
        result8 = view_all_previous_records()
        df8 = pd.DataFrame(result8, columns=["State Team", "Previous Team", "No of teams previously played for","Debut Date","Career span in years","Previous Record Player ID"])
        with st.expander("Updated data"):
            st.dataframe(df8)
            
#             edit_players_data(new_player_id,new_player_team_name, new_player_name,new_base_price,new_player_type,new_wickets_take,new_runs_scored,
# new_player_country,new_year_of_auction,new_player_auc_id,
# player_id,player_team_name,base_price, player_name,player_type,wickets_take, runs_scored,player_country,year_of_auction, player_auc_id)