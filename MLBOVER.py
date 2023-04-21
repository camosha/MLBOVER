
import pybaseball
from pybaseball import schedule_and_record
import pandas as pd
import math
import streamlit as st
st.header('MLB Overs Project')
st.subheader('Input Team Name and Run Total Projected')
mlb_team_abbreviations = [
    'ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE',
    'COL', 'DET', 'HOU', 'KC', 'LAA', 'LAD', 'MIA', 'MIL',
    'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SD', 'SEA',
    'SF', 'STL', 'TB', 'TEX', 'TOR', 'WAS'
]

team = st.selectbox("Select a Team",mlb_team_abbreviations)

data = schedule_and_record(2023,team)
data = pd.DataFrame(data)
runs = data['R']
list = []
for x in runs:
  if type(x) == float:
    list += [x]

# Remove NaN values using a for loop
cleaned_list = []
for value in list:
    if not math.isnan(value):
        cleaned_list.append(value)

print(cleaned_list)
last5 = cleaned_list[-5:]
PRElast5 = cleaned_list[-6:-1]
lat5Average = math.fsum(last5) / len(last5)
pre5avg = math.fsum(PRElast5) / len(PRElast5)
#print(last5)
#print(PRElast5)
#print(lat5Average)
#print(pre5avg)
check1 ='no'
if lat5Average > pre5avg:
  check1 = 'yes'
#print(check1)
last8 = cleaned_list[-8:]
PRElast8 = cleaned_list[-9:-1]
lat8Average = math.fsum(last8) / len(last8)
pre8avg = math.fsum(PRElast8) / len(PRElast8)
#print(last8)
#print(PRElast8)
#print(lat8Average)
#print(pre8avg)
check2 ='no'
if lat8Average > pre8avg:
  check2 = 'yes'
#print(check2)
#check for 13
last13 = cleaned_list[-13:]
PRElast13 = cleaned_list[-14:-1]
lat13Average = math.fsum(last13) / len(last13)
pre13avg = math.fsum(PRElast13) / len(PRElast13)
#print(last13)
#print(PRElast13)
#print(lat13Average)
#print(pre13avg)
check3 ='no'
if lat13Average > pre13avg:
  check3 = 'yes'
#print(check3)
check4 = 'no'
if lat5Average > lat8Average and lat5Average > lat13Average:
  check4='yes'
x = 'no'
if check1 =='yes' and check2 == "yes" and check3 == 'yes' and check4=='yes':
  #print("This is a target teamn ")
  x = 'y'

team = st.text_input("What is their run total for today: ", value=int(0))
team = float(team)
dog = st.button("Analyze")
if dog:
    st.balloons()
    if team < lat5Average and x =='y':
        st.write('Bet This')
    else:
        st.write("No Action")
        
