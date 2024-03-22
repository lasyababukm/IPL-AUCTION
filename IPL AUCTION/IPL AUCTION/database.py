import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="",database="pes1ug20cs185_project")

c = mydb.cursor()

def add_data_player(player_id,player_team_name,base_price, player_name,player_type,wickets_take, runs_scored,player_country,year_of_auction, player_auc_id):
    c.execute("insert into player(player_id,player_team_name,base_price, player_name,player_type,wickets_take, runs_scored,player_country,year_of_auction, player_auc_id) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(player_id,player_team_name,base_price, player_name,player_type,wickets_take, runs_scored,player_country,year_of_auction, player_auc_id))
def add_data_award(a_name, type_of_award, cash_prize_in_rupees, team_received_for ,award_player_id):
    c.execute("insert into award(a_name, type_of_award, cash_prize_in_rupees, team_received_for ,award_player_id) values(%s,%s,%s,%s,%s)",(a_name, type_of_award, cash_prize_in_rupees, team_received_for ,award_player_id))
def add_data_team(team_name,budget_in_rupees,purse_remaining_in_rupees,purse_spent_in_rupees,
region_representing, team_owner_id, team_owner_type,team_owner_name,team_player_id):
    c.execute("insert into team(team_name,budget_in_rupees,purse_remaining_in_rupees,purse_spent_in_rupees,region_representing, team_owner_id, team_owner_type,team_owner_name,team_player_id) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(team_name,budget_in_rupees,purse_remaining_in_rupees,purse_spent_in_rupees,
region_representing, team_owner_id, team_owner_type,team_owner_name,team_player_id))
def add_data_previous_records(state_team, prev_team, no_of_teams_played_for_prev, debut_date,career_span_in_years,prevrec_player_id):    
    c.execute("insert into previous_records(state_team, prev_team, no_of_teams_played_for_prev, debut_date,career_span_in_years,prevrec_player_id) values(%s,%s,%s,%s,%s,%s)",(state_team, prev_team, no_of_teams_played_for_prev, debut_date,career_span_in_years,prevrec_player_id))


def view_all_players():
    c.execute("select * from player")
    data = c.fetchall()
    return data
def view_all_awards():
    c.execute("select * from award")
    data = c.fetchall()
    return data
def view_all_team():
    c.execute("select * from team")
    data = c.fetchall()
    return data
def view_all_previous_records():
    c.execute("select * from previous_records")
    data = c.fetchall()
    return data


def view_only_players_names():
    c.execute("select player_id from player")
    data = c.fetchall()
    return data
def view_only_awards_names():
    c.execute("select a_name from award")
    data = c.fetchall()
    return data
def view_only_team_names():
    c.execute("select team_owner_id from team")
    data = c.fetchall()
    return data
def view_only_previous_records():
    c.execute("select state_team from previous_records")
    data = c.fetchall()
    return data


def get_players(player_id):
    c.execute("select * from player where player_id='{}'".format(player_id))
    data = c.fetchall()
    return data
def get_awards(a_name):
    c.execute("select * from award where a_name='{}'".format(a_name))
    data = c.fetchall()
    return data
def get_team(team_owner_id):
    c.execute("select * from team where team_owner_id='{}'".format(team_owner_id))
    data = c.fetchall()
    return data
def get_previous_records(state_team):
    c.execute("select * from previous_records where state_team='{}'".format(state_team))
    data = c.fetchall()
    return data


def edit_players_data(new_player_id,new_player_team_name, new_player_name,new_base_price,new_player_type,new_wickets_take,new_runs_scored,
new_player_country,new_year_of_auction,new_player_auc_id,
player_id):
    c.execute("Update player set player_id=%s,player_team_name=%s, player_name=%s,base_price=%s,player_type=%s,wickets_take=%s, runs_scored=%s,player_country=%s,year_of_auction=%s,player_auc_id=%s where player_id=%s ",(new_player_id,new_player_team_name, new_player_name,new_base_price,new_player_type,new_wickets_take,new_runs_scored,
new_player_country,new_year_of_auction,new_player_auc_id,player_id))
    mydb.commit()
    c.execute("select player_id from player")
    data = c.fetchall()
    return data

def edit_awards_data(new_a_name, new_type_of_award, new_cash_prize_in_rupees,
new_team_received_for,new_award_player_id, a_name):
    c.execute("Update award set a_name=%s, type_of_award=%s, cash_prize_in_rupees=%s,team_received_for=%s,award_player_id=%s where a_name=%s",(new_a_name, new_type_of_award, new_cash_prize_in_rupees,
new_team_received_for,new_award_player_id, a_name))
    mydb.commit()
    c.execute("select a_name from award")
    data = c.fetchall()
    return data

def edit_team_data(new_team_name, new_budget_in_rupees,new_purse_remaining_in_rupees,new_purse_spent_in_rupees, new_region_representing,new_team_owner_id,
new_team_owner_type,new_team_owner_name,new_team_player_id,team_owner_id):
    c.execute("Update team set team_name=%s,budget_in_rupees=%s,purse_remaining_in_rupees=%s,purse_spent_in_rupees=%s,region_representing=%s, team_owner_id=%s,team_owner_type=%s,team_owner_name=%s,team_player_id=%s where team_owner_id=%s",
(new_team_name, new_budget_in_rupees,new_purse_remaining_in_rupees,new_purse_spent_in_rupees, new_region_representing,new_team_owner_id,
new_team_owner_type,new_team_owner_name,new_team_player_id,team_owner_id))
    mydb.commit()
    c.execute("select team_owner_id from team")
    data = c.fetchall()
    return data

def edit_previous_records(new_state_team, new_prev_team, new_no_of_teams_played_for_prev,
new_debut_date,new_career_span_in_years,new_prevrec_player_id, state_team):
    c.execute("Update previous_records set state_team=%s,  prev_team=%s, no_of_teams_played_for_prev=%s,debut_date=%s,career_span_in_years=%s,prevrec_player_id=%s where state_team=%s ",(new_state_team, new_prev_team, new_no_of_teams_played_for_prev,
new_debut_date,new_career_span_in_years,new_prevrec_player_id, state_team))
    mydb.commit()
    c.execute("select state_team from previous_records")
    data = c.fetchall()
    return data


def delete_player_data(player_id):
    c.execute("Delete from player where player_id='{}'".format(player_id))
    mydb.commit()
def delete_award_data(a_name):
    c.execute("Delete from award where a_name='{}'".format(a_name))
    mydb.commit()
def delete_team_data(team_owner_id):
    c.execute("Delete from team where team_owner_id='{}'".format(team_owner_id))
    mydb.commit()
def delete_previous_records_data(state_team):
    c.execute("Delete from previous_records where state_team='{}'".format(state_team))
    mydb.commit()
    
    
# def edit_players_data(new_player_id,new_player_team_name, new_player_name,new_base_price,new_player_type,new_wickets_take,new_runs_scored,
# new_player_country,new_year_of_auction,new_player_auc_id,
# player_id,player_team_name,base_price, player_name,player_type,wickets_take, runs_scored,player_country,year_of_auction, player_auc_id):
#     c.execute("Update player set player_id=%s,player_team_name=%s, player_name=%s,base_price=%s,player_type=%s,wickets_take=%s, runs_scored=%s,player_country=%s,year_of_auction=%s,player_auc_id=%s where player_id=%s and player_team_name=%s and player_name=%s and base_price=%s and player_type=%s and wickets_take=%s and  runs_scored=%s and player_country=%s and year_of_auction=%s and player_auc_id=%s ",(new_player_id,new_player_team_name, new_player_name,new_base_price,new_player_type,new_wickets_take,new_runs_scored,
# new_player_country,new_year_of_auction,new_player_auc_id,
# player_id,player_team_name,base_price, player_name,player_type,wickets_take, runs_scored,player_country,year_of_auction, player_auc_id))
#     mydb.commit()
#     c.execute("select player_id from player")
#     data = c.fetchall()
#     return data
    