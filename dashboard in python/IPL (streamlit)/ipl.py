import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

matches=pd.read_csv('matches.csv')
deliveries=pd.read_csv('deliveries.csv')

st.set_page_config(page_title="IPL Dashboard", layout="wide")
st.title("🏏 IPL Data Analysis Dashboard")

st.sidebar.header("Filter")

team_list=sorted(matches['team1'].dropna().unique())
selected_team=st.sidebar.selectbox("Select a Team",["All"]+team_list)

season_list=sorted(matches['season'].dropna().unique())
selected_season=st.sidebar.selectbox("Select Season",["All"]+season_list)

#type_list=sorted(matches['match_type'].dropna().unique())
#selected_type=st.sidebar.selectbox("SElect Type",["All"]+type_list)

filtered_matches=matches.copy()
if selected_team !="All":
    filtered_matches=filtered_matches[(filtered_matches['team1']== selected_team)|(filtered_matches['team2']==selected_team)]
    
if selected_season!="All":
    filtered_matches=filtered_matches(filtered_matches['season'].astype(str)==str(selected_season))
    
total_matches=filtered_matches.shape[0]
st.metric("Total Matches",total_matches)

#wins by team
if selected_team=="All":
    win_count=filtered_matches['winner'].value_counts().reset_index()
    win_count.columns=["Team","Wins"]
else:
    win_count=filtered_matches[filtered_matches['winner']==selected_team].groupby('season')['winner'].count().reset_index()
    win_count.columns=['Season','Wins']
    
st.subheader("📊 Wins Overview")
fig1,ax1=plt.subplots()
if selected_team=="All":
    sns.barplot(win_count,x='Wins',y='Team',ax=ax1)
    ax1.set_title("wins by team")
else:
    sns.lineplot(win_count,x='Wins',y='Season',marker="o",ax=ax1)
    ax1.set_title(f"Wins by {selected_team} over the Season")
st.pyplot(fig1)

#top players(man of match(mom))
st.subheader("🏅 Top Man of the Match Winners")
mom=filtered_matches['player_of_match'].value_counts().head(10).reset_index()
mom.columns=['Players',"Awards"]
st.table(mom)

#runs destributionn
st.subheader("🎯 Total runs destribution")

match_ids=filtered_matches['id'].unique()
filtered_deliveries=deliveries[deliveries['match_id'].isin(match_ids)]

runs_by_batsman=filtered_deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)

fig2,ax2=plt.subplots()
runs_by_batsman.plot(kind='bar',ax=ax2,color='orange')
ax2.set_ylabel="Total runs"
ax2.set_title("Top 10 batsman (Runs Scored)")
st.pyplot(fig2)

#extra breakdown
st.subheader("🎁 Extras Breakdown")

st.write("Deliveries colummns:",deliveries.columns.to_list())

extra_columns=[col for col in ['wide_runs','noball_runs',"bye_runs","legby_runs"]if col in filtered_deliveries.columns]

if extra_columns:
    extra=filtered_deliveries[extra_columns].sum()
    
    fig3 = plt.figure()
    extra.plot(kind="pie", autopct='%1.1f%%', colors=['#FF9999', '#66B3FF', '#99FF99', '#FFD700'])
    plt.title("Distribution of Extras")
    st.pyplot(fig3)
else:
    st.warning("No extras columns found in the deliveries dataset.")



st.markdown("Made with ❤️ using Streamlit")