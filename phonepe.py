import os
import json
import pandas as pd
import psycopg2
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
from PIL import Image

#Here we are declaring the path where we cloned the data from github 

#To get data from Aggregated transaction here we taking transaction type, transaction count and transaction amount

Datapath_agg_t = "C:/Users/rajan/OneDrive/Desktop/Phonepe/pulse/data/aggregated/transaction/country/india/state/" 
Agg_State_list_t = os.listdir(Datapath_agg_t)

Agg_trans_list = {'State':[], 'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

#To extract all the data of state and converting them to data frame
for state in Agg_State_list_t: #this loop is to go after each state path
    path_states = Datapath_agg_t + state + "/"
    Agg_year_list = os.listdir(path_states)
    
    for year in Agg_year_list: #this loop to go after each year path
        path_year = path_states + year + "/"
        Agg_year_Json_file = os.listdir(path_year)
        
        for j_file in Agg_year_Json_file:#this loop to open each Json file
            path_json = path_year + j_file
            Data_agg_trans = open(path_json,'r')
            At = json.load(Data_agg_trans)
           
            for i in At['data']['transactionData']: #this loop is to extract data from above Json file and concert them to dataframe
                Name = i['name']
                Count = i['paymentInstruments'][0]['count']
                Amount = i['paymentInstruments'][0]['amount']
                Agg_trans_list['Transaction_type'].append(Name)
                Agg_trans_list['Transaction_count'].append(Count)
                Agg_trans_list['Transaction_amount'].append(Amount)
                Agg_trans_list['State'].append(state)
                Agg_trans_list['Year'].append(year)
                Agg_trans_list['Quarter'].append(int(j_file.strip('.json')))

Agg_trans = pd.DataFrame(Agg_trans_list)

#here we changing all the states name to match the GEO coordinates

Agg_trans['State'] = Agg_trans['State'].str.title()
Agg_trans['State'] = Agg_trans['State'].str.replace("-"," ")
Agg_trans['State'] = Agg_trans['State'].str.replace("Andaman & Nicobar Islands","Andaman & Nicobar")
Agg_trans['State'] = Agg_trans['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu","Dadra and Nagar Haveli and Daman and Diu")

#Here we are declaring the path where we cloned the data from github 

#To get data from Aggregated User here we taking Phone Brand, Phone count and user percentage

Datapath_agg_u = "C:/Users/rajan/OneDrive/Desktop/Phonepe/pulse/data/aggregated/user/country/india/state/" 
Agg_State_list_u = os.listdir(Datapath_agg_u)

Agg_User_list = {'State':[], 'Year':[],'Quarter':[],'Phone_Brand':[], 'Transaction_count':[],'User_Percentage':[]}

#To extract all the data of state and converting them to data frame
for state in Agg_State_list_u:#this loop is to go after each state path
    path_states = Datapath_agg_u + state + "/"
    Agg_year_list_user = os.listdir(path_states)
    
    for year in Agg_year_list_user:#this loop to go after each year path
        path_year = path_states + year + "/"
        Agg_year_Json_file_user = os.listdir(path_year)
        
        for j_file in Agg_year_Json_file_user:#this loop to open each Json file
            path_json = path_year + j_file
            Data_agg_user = open(path_json,'r')
            Au = json.load(Data_agg_user)
            
            try: # here we are using try and except function to avoid the error due to null value.
                for i in Au['data']['usersByDevice']: #this loop is to extract data from above Json file and concert them to dataframe
                    Brand = i['brand']
                    Count = i['count']
                    Percentage = i['percentage']
                    Agg_User_list['Phone_Brand'].append(Brand)
                    Agg_User_list['Transaction_count'].append(Count)
                    Agg_User_list['User_Percentage'].append(Percentage)
                    Agg_User_list['State'].append(state)
                    Agg_User_list['Year'].append(year)
                    Agg_User_list['Quarter'].append(int(j_file.strip('.json')))
            except:
                pass
            
Agg_User=pd.DataFrame(Agg_User_list)

#here we changing all the states name to match the GEO coordinates

Agg_User['State'] = Agg_User['State'].str.title()
Agg_User['State'] = Agg_User['State'].str.replace("-"," ")
Agg_User['State'] = Agg_User['State'].str.replace("Andaman & Nicobar Islands","Andaman & Nicobar")
Agg_User['State'] = Agg_User['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu","Dadra and Nagar Haveli and Daman and Diu")

#Here we are declaring the path where we cloned the data from github 

#To get data from Map transaction here we taking Districts, Transaction count and Transaction amount

Datapath_map_t = "C:/Users/rajan/OneDrive/Desktop/Phonepe/pulse/data/map/transaction/hover/country/india/state/" 
Map_State_list = os.listdir(Datapath_map_t)

Map_trans_list = {'State':[], 'Year':[],'Quarter':[],'Districts':[], 'Transaction_count':[], 'Transaction_amount':[]}

#To extract all the data of state and converting them to data frame
for state in Map_State_list:#this loop is to go after each state path
    path_states = Datapath_map_t +state + "/"
    Agg_year_list = os.listdir(path_states)
    
    for year in Agg_year_list:#this loop to go after each year path
        path_year = path_states + year + "/"
        Agg_year_Json_file = os.listdir(path_year)
        
        for j_file in Agg_year_Json_file:#this loop to open each Json file
            path_json = path_year + j_file
            Data_map_trans = open(path_json,'r')
            Mt = json.load(Data_map_trans)
           
            for i in Mt['data']['hoverDataList']:#this loop is to extract data from above Json file and concert them to dataframe
                Name = i['name']
                Count = i['metric'][0]['count']
                Amount = i['metric'][0]['amount']
                Map_trans_list['Districts'].append(Name)
                Map_trans_list['Transaction_count'].append(Count)
                Map_trans_list['Transaction_amount'].append(Amount)
                Map_trans_list['State'].append(state)
                Map_trans_list['Year'].append(year)
                Map_trans_list['Quarter'].append(int(j_file.strip('.json')))

Map_trans = pd.DataFrame(Map_trans_list)

#here we changing all the states name to match the GEO coordinates

Map_trans['State'] = Map_trans['State'].str.title()
Map_trans['State'] = Map_trans['State'].str.replace("-"," ")
Map_trans['State'] = Map_trans['State'].str.replace("Andaman & Nicobar Islands","Andaman & Nicobar")
Map_trans['State'] = Map_trans['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu","Dadra and Nagar Haveli and Daman and Diu")

#Here we are declaring the path where we cloned the data from github 

#To get data from Map User here we taking Districts, RegisteredUser and AppOpens

Datapath_map_u = "C:/Users/rajan/OneDrive/Desktop/Phonepe/pulse/data/map/user/hover/country/india/state/" 
Map_State_list_u = os.listdir(Datapath_map_u)

Map_user_list = {'State':[], 'Year':[],'Quarter':[],'Districts':[], 'RegisteredUser':[], 'AppOpens':[]}

#To extract all the data of state and converting them to data frame
for state in Map_State_list_u:#this loop is to go after each state path
    path_states = Datapath_map_u + state + "/"
    Agg_year_list = os.listdir(path_states)
    
    for year in Agg_year_list:#this loop to go after each year path
        path_year = path_states + year + "/"
        Agg_year_Json_file = os.listdir(path_year)
        
        for j_file in Agg_year_Json_file:#this loop to open each Json file
            path_json = path_year + j_file
            Data_map_user = open(path_json,'r')
            Mu = json.load(Data_map_user)

            #this loop is to extract data from above Json file and concert them to dataframe
            for i in Mu['data']['hoverData'].items():#here we need to take the keyvalue so we are using items() and index value of the specific key value
                Name = i[0]
                Registereduser = i[1]['registeredUsers']
                Appopens = i[1]['appOpens']
                Map_user_list['Districts'].append(Name)
                Map_user_list['RegisteredUser'].append(Registereduser)
                Map_user_list['AppOpens'].append(Appopens)
                Map_user_list['State'].append(state)
                Map_user_list['Year'].append(year)
                Map_user_list['Quarter'].append(int(j_file.strip('.json')))

Map_user = pd.DataFrame(Map_user_list)

#here we changing all the states name to match the GEO coordinates

Map_user['State'] = Map_user['State'].str.title()
Map_user['State'] = Map_user['State'].str.replace("-"," ")
Map_user['State'] = Map_user['State'].str.replace("Andaman & Nicobar Islands","Andaman & Nicobar")
Map_user['State'] = Map_user['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu","Dadra and Nagar Haveli and Daman and Diu")

#Here we are declaring the path where we cloned the data from github 

#To get data from Top transaction here we taking Transaction count and Transaction amount details with Pincodes

Datapath_top_t = "C:/Users/rajan/OneDrive/Desktop/Phonepe/pulse/data/top/transaction/country/india/state/" 
Top_State_list_t = os.listdir(Datapath_top_t)

Top_trans_list = {'State':[], 'Year':[],'Quarter':[],'Pincodes':[], 'Transaction_count':[], 'Transaction_amount':[]}

#To extract all the data of state and converting them to data frame
for state in Top_State_list_t:#this loop is to go after each state path
    path_states = Datapath_top_t + state + "/"
    Agg_year_list = os.listdir(path_states)
    
    for year in Agg_year_list:#this loop to go after each year path
        path_year = path_states + year + "/"
        Agg_year_Json_file = os.listdir(path_year)
        
        for j_file in Agg_year_Json_file:#this loop to open each Json file
            path_json = path_year + j_file
            Data_top_trans = open(path_json,'r')
            Tt = json.load(Data_top_trans)
            

            for i in Tt['data']['pincodes']:#this loop is to extract data from above Json file and concert them to dataframe
                Pincodes = i['entityName']
                Count = i['metric']['count']
                Amount = i['metric']['amount']
                Top_trans_list['Pincodes'].append(Pincodes)
                Top_trans_list['Transaction_count'].append(Count)
                Top_trans_list['Transaction_amount'].append(Amount)
                Top_trans_list['State'].append(state)
                Top_trans_list['Year'].append(year)
                Top_trans_list['Quarter'].append(int(j_file.strip('.json')))

Top_trans = pd.DataFrame(Top_trans_list) 

#here we changing all the states name to match the GEO coordinates

Top_trans['State'] = Top_trans['State'].str.title()
Top_trans['State'] = Top_trans['State'].str.replace("-"," ")
Top_trans['State'] = Top_trans['State'].str.replace("Andaman & Nicobar Islands","Andaman & Nicobar")
Top_trans['State'] = Top_trans['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu","Dadra and Nagar Haveli and Daman and Diu")

#Here we are declaring the path where we cloned the data from github 

#To get data from top User here we taking registereduser detail with picodes

Datapath_top_u = "C:/Users/rajan/OneDrive/Desktop/Phonepe/pulse/data/top/user/country/india/state/" 
Top_State_list_u = os.listdir(Datapath_top_u)

Top_user_list = {'State':[], 'Year':[],'Quarter':[],'Pincodes':[], 'RegisteredUser':[]}

#To extract all the data of state and converting them to data frame
for state in Top_State_list_u:#this loop is to go after each state path
    path_states = Datapath_top_u + state + "/"
    Agg_year_list = os.listdir(path_states)
    
    for year in Agg_year_list:#this loop to go after each year path
        path_year = path_states + year + "/"
        Agg_year_Json_file = os.listdir(path_year)
        
        for j_file in Agg_year_Json_file:#this loop to open each Json file
            path_json = path_year + j_file
            Data_top_user = open(path_json,'r')
            Tu = json.load(Data_top_user)
            

            for i in Tu['data']['pincodes']:#this loop is to extract data from above Json file and concert them to dataframe
                Pincodes = i['name']
                Registereduser = i['registeredUsers']
                Top_user_list['Pincodes'].append(Pincodes)
                Top_user_list['RegisteredUser'].append(Registereduser)
                Top_user_list['State'].append(state)
                Top_user_list['Year'].append(year)
                Top_user_list['Quarter'].append(int(j_file.strip('.json')))

Top_user = pd.DataFrame(Top_user_list)      

#here we changing all the states name to match the GEO coordinates

Top_user['State'] = Top_user['State'].str.title()
Top_user['State'] = Top_user['State'].str.replace("-"," ")
Top_user['State'] = Top_user['State'].str.replace("Andaman & Nicobar Islands","Andaman & Nicobar")
Top_user['State'] = Top_user['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu","Dadra and Nagar Haveli and Daman and Diu")

# To create Table in SQL for the extracted clone data from github

Data_Base = psycopg2.connect(host = "localhost",
                            user = "postgres",
                            password = "BNandy30",
                            port = "5432",
                            database = "PhonePe") # it is the connection to run SQL in backend

cursor = Data_Base.cursor() #Cursor is a Temporary Memory or Temporary Work Station.

# Aggregated transaction Table

Query = '''CREATE TABLE IF NOT EXISTS Agg_trans(State VARCHAR(255),  
                                                Year INT,
                                                Quarter INT,
                                                Transaction_type VARCHAR(255),
                                                Transaction_count INT,
                                                Transaction_amount FLOAT)''' #creating Aggregated transaction tables
cursor.execute(Query)
Data_Base.commit()

insert_Query = '''INSERT INTO Agg_trans(State,
                                        Year,
                                        Quarter,
                                        Transaction_type,
                                        Transaction_count,
                                        Transaction_amount) 
                                    
                                        values(%s,%s,%s,%s,%s,%s)''' 
# here we inserting the data we extracted from github after converting it to list.

data = Agg_trans.values.tolist()
cursor.executemany(insert_Query,data)
Data_Base.commit()

# Aggregated User table

Query1 = '''CREATE TABLE IF NOT EXISTS Agg_User(State VARCHAR(255),  
                                                Year INT,
                                                Quarter INT,
                                                Phone_Brand VARCHAR(255),
                                                Transaction_count INT,
                                                User_Percentage FLOAT)''' #creating Aggregated transaction tables
cursor.execute(Query1)
Data_Base.commit()

insert_Query1 = '''INSERT INTO Agg_User(State,
                                        Year,
                                        Quarter,
                                        Phone_Brand,
                                        Transaction_count,
                                        User_Percentage) 
                                    
                                        values(%s,%s,%s,%s,%s,%s)''' 
# here we inserting the data we extracted from github after converting it to list.

data = Agg_User.values.tolist()
cursor.executemany(insert_Query1,data)
Data_Base.commit()

# Map Transaction table

Query2 = '''CREATE TABLE IF NOT EXISTS Map_trans(State VARCHAR(255),  
                                                 Year INT,
                                                 Quarter INT,
                                                 Districts VARCHAR(255),
                                                 Transaction_count INT,
                                                 Transaction_amount FLOAT)''' #creating Aggregated transaction tables
cursor.execute(Query2)
Data_Base.commit()

insert_Query2 = '''INSERT INTO Map_trans(State,
                                        Year,
                                        Quarter,
                                        Districts,
                                        Transaction_count,
                                        Transaction_amount) 
                                    
                                        values(%s,%s,%s,%s,%s,%s)''' 
# here we inserting the data we extracted from github after converting it to list.

data = Map_trans.values.tolist()
cursor.executemany(insert_Query2,data)
Data_Base.commit()

# Map User table

Query3 = '''CREATE TABLE IF NOT EXISTS Map_user(State VARCHAR(255),  
                                                Year INT,
                                                Quarter INT,
                                                Districts VARCHAR(255),
                                                RegisteredUser INT,
                                                AppOpens INT)''' #creating Aggregated transaction tables
cursor.execute(Query3)
Data_Base.commit()

insert_Query3 = '''INSERT INTO Map_user(State,
                                        Year,
                                        Quarter,
                                        Districts,
                                        RegisteredUser,
                                        AppOpens) 
                                    
                                        values(%s,%s,%s,%s,%s,%s)''' 
# here we inserting the data we extracted from github after converting it to list.

data = Map_user.values.tolist()
cursor.executemany(insert_Query3,data)
Data_Base.commit()

# Top transaction table

Query4 = '''CREATE TABLE IF NOT EXISTS Top_trans(State VARCHAR(255),  
                                                Year INT,
                                                Quarter INT,
                                                Pincodes NUMERIC,
                                                Transaction_count INT,
                                                Transaction_amount FLOAT)''' #creating Aggregated transaction tables
cursor.execute(Query4)
Data_Base.commit()

insert_Query4 = '''INSERT INTO Top_trans(State,
                                        Year,
                                        Quarter,
                                        Pincodes,
                                        Transaction_count,
                                        Transaction_amount) 
                                    
                                        values(%s,%s,%s,%s,%s,%s)''' 
# here we inserting the data we extracted from github after converting it to list.

data = Top_trans.values.tolist()
cursor.executemany(insert_Query4,data)
Data_Base.commit()

# Top User table

Query5 = '''CREATE TABLE IF NOT EXISTS Top_user(State VARCHAR(255),  
                                                Year INT,
                                                Quarter INT,
                                                Pincodes INT,
                                                RegisteredUser INT)''' #creating Aggregated transaction tables
cursor.execute(Query5)
Data_Base.commit()

insert_Query5 = '''INSERT INTO Top_user(State,
                                        Year,
                                        Quarter,
                                        Pincodes,
                                        RegisteredUser) 
                                    
                                        values(%s,%s,%s,%s,%s)''' 
# here we inserting the data we extracted from github after converting it to list.

data = Top_user.values.tolist()
cursor.executemany(insert_Query5,data)
Data_Base.commit()

#Here we coverting the data which we stored in SQL to a Data Frame


Data_Base = psycopg2.connect(host = "localhost",
                            user = "postgres",
                            password = "BNandy30",
                            port = "5432",
                            database = "PhonePe") # it is the connection to run SQL in backend

cursor = Data_Base.cursor() #Cursor is a Temporary Memory or Temporary Work Station.

# Fetch data from the Agg_trans table

select_query = "SELECT * FROM Agg_trans"

cursor.execute(select_query)
Data_Base.commit()
agg_trans_table = cursor.fetchall()

Agg_trans_data = pd.DataFrame(agg_trans_table, columns = ('State', 'Year','Quarter','Transaction_type', 
                                                          'Transaction_count', 'Transaction_amount'))

# Fetch data from the Agg_user table 

select_query1 = "SELECT * FROM Agg_user"

cursor.execute(select_query1)
Data_Base.commit()
agg_user_table = cursor.fetchall()

Agg_user_data = pd.DataFrame(agg_user_table, columns = ('State', 'Year','Quarter','Phone_Brand', 
                                                          'Transaction_count', 'User_Percentage'))

# Fetch data from the Map_trans table 

select_query2 = "SELECT * FROM Map_trans"

cursor.execute(select_query2)
Data_Base.commit()
map_trans_table = cursor.fetchall()

Map_trans_data = pd.DataFrame(map_trans_table, columns = ('State', 'Year','Quarter','Districts', 
                                                          'Transaction_count', 'Transaction_amount'))

# Fetch data from the Map_user table 

select_query3 = "SELECT * FROM Map_user"

cursor.execute(select_query3)
Data_Base.commit()
map_user_table = cursor.fetchall()

Map_user_data = pd.DataFrame(map_user_table, columns = ('State', 'Year','Quarter','Districts', 
                                                          'RegisteredUser', 'AppOpens'))

# Fetch data from the Top_trans table 

select_query4 = "SELECT * FROM Top_trans"

cursor.execute(select_query4)
Data_Base.commit()
top_trans_table = cursor.fetchall()

Top_trans_data = pd.DataFrame(top_trans_table, columns = ('State', 'Year','Quarter','Pincodes', 
                                                          'Transaction_count', 'Transaction_amount'))

# Fetch data from the Top_user table 

select_query5 = "SELECT * FROM Top_user"

cursor.execute(select_query5)
Data_Base.commit()
top_user_table = cursor.fetchall()

Top_user_data = pd.DataFrame(top_user_table, columns = ('State', 'Year','Quarter','Pincodes','RegisteredUser'))

# Tansaction Data Analysis

def Ttansaction_count_amount_analysis(dataFrame,Year):

    Data_CA = dataFrame[dataFrame["Year"] == Year] #here we are taking only specific year to view

    # drop will remove the old Index and give new index value and Inplace will Keep the change in the dataframe
    Data_CA.reset_index(drop = True, inplace = True) 

    #here we grouping all states with transaction count & amount
    Data_CA_group = Data_CA.groupby("State")[["Transaction_count","Transaction_amount"]].sum()
    Data_CA_group.reset_index(inplace = True)

    column1, column2 = st.columns(2)

    with column1:

        fig_amount = px.bar(Data_CA_group, x= "State", y= "Transaction_amount", title= f"Transaction_amount of {Year}", 
                            color_discrete_sequence=px.colors.sequential.Magenta, height = 550, width =500)
        st.plotly_chart(fig_amount)

    with column2:

        fig_count = px.bar(Data_CA_group, x= "State", y= "Transaction_count", title= f"Transaction_count of {Year}" , 
                            color_discrete_sequence=px.colors.sequential.Magenta, height = 550, width =500)
        st.plotly_chart(fig_count)

    column1, column2 = st.columns(2)

    with column1:
           
           fig_amount_geo = px.choropleth(Data_CA_group,
                                title=f"GEO VISUALUATION OF TRANSACTION AMOUNT {Year}",
                                geojson = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                locations='State',
                                featureidkey='properties.ST_NM',
                                color='Transaction_amount',
                                color_continuous_scale='sunset',
                                range_color= (Data_CA_group['Transaction_amount'].min(),Data_CA_group['Transaction_amount'].max()),
                                hover_name='State',
                                height = 550,
                                width = 500)

           fig_amount_geo.update_geos(fitbounds="locations", visible=False)

           st.plotly_chart(fig_amount_geo)


    with column2:

         fig_count_geo = px.choropleth(Data_CA_group,
                            title=f"GEO VISUALUATION OF TRANSACTION COUNT {Year}",
                            geojson = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_count',
                            color_continuous_scale='sunset',
                            range_color= (Data_CA_group['Transaction_count'].min(),Data_CA_group['Transaction_count'].max()),
                            hover_name='State',
                            height = 550,
                            width = 500)

         fig_count_geo.update_geos(fitbounds="locations", visible=False)
         
         st.plotly_chart(fig_count_geo)

    return Data_CA

def Ttansaction_count_amount_analysis_Q(dataFrame, Quarter):

    Data_CA = dataFrame[dataFrame["Quarter"] == Quarter] #here we are taking only specific year to view

    # drop will remove the old Index and give new index value and Inplace will Keep the change in the dataframe
    Data_CA.reset_index(drop = True, inplace = True) 

    #here we grouping all states with transaction count & amount
    Data_CA_group = Data_CA.groupby("State")[["Transaction_count","Transaction_amount"]].sum()
    Data_CA_group.reset_index(inplace = True)

    column1, column2 = st.columns(2)

    with column1:

        fig_amount = px.bar(Data_CA_group, x= "State", y= "Transaction_amount", title= f"TRANSACTION COUNT QUARTER {Quarter} OF YEAR {Data_CA['Year'].unique()}", 
                                color_discrete_sequence=px.colors.sequential. Magenta, height = 550, width =500)

        st.plotly_chart(fig_amount)

    with column2:

        fig_count = px.bar(Data_CA_group, x= "State", y= "Transaction_count", title= f"TRANSACTION AMOUNT QUARTER {Quarter} OF YEAR {Data_CA['Year'].unique()}" , 
                                color_discrete_sequence=px.colors.sequential. Magenta, height = 550, width =500)

        st.plotly_chart(fig_count)

    column1, column2 = st.columns(2)

    with column1:

        fig_amount_geo = px.choropleth(Data_CA_group,
                                    title=f"TRANSACTION AMOUNT QUARTER {Quarter} OF YEAR {Data_CA['Year'].unique()}",
                                    geojson = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    locations='State',
                                    featureidkey='properties.ST_NM',
                                    color='Transaction_amount',
                                    color_continuous_scale='sunset',
                                    range_color= (Data_CA_group['Transaction_amount'].min(),Data_CA_group['Transaction_amount'].max()),
                                    hover_name='State',
                                    height = 550,
                                    width = 500)

        fig_amount_geo.update_geos(fitbounds="locations", visible=False)

        st.plotly_chart(fig_amount_geo)

    with column2:

        fig_count_geo = px.choropleth(Data_CA_group,
                                title=f"TRANSACTION COUNT QUARTER {Quarter} OF YEAR {Data_CA['Year'].unique()}",
                                geojson = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                featureidkey='properties.ST_NM',
                                locations='State',
                                color='Transaction_count',
                                color_continuous_scale='sunset',
                                range_color= (Data_CA_group['Transaction_count'].min(),Data_CA_group['Transaction_count'].max()),
                                hover_name='State',
                                height = 550,
                                width = 500)

        fig_count_geo.update_geos(fitbounds="locations", visible=False)
        
        st.plotly_chart(fig_count_geo)
    
    return Data_CA

# Transaction Type

def Transaction_type(dataframe, state):

    Data_tt = dataframe[dataframe['State'] == state]
    Data_tt.reset_index(drop = True, inplace = True)

    Data_tt_group = Data_tt.groupby('Transaction_type')[["Transaction_count","Transaction_amount"]].sum()
    Data_tt_group.reset_index(inplace = True)

    column1, column2 = st.columns(2)

    with column1:
        
        fig_type_a =px.pie(data_frame = Data_tt_group, names = 'Transaction_type', values='Transaction_amount', width =500,
                        title = f"{state}  TRANSACTION AMOUNT" , hole= 0.2)
        
        st.plotly_chart(fig_type_a)

    with column2:

        fig_type_c =px.pie(data_frame = Data_tt_group, names = 'Transaction_type', values='Transaction_count', width =500,
                        title = f"{state}  TRANSACTION COUNT" , hole= 0.2)
        
        st.plotly_chart(fig_type_c)

## Districts data analysis based on Transaction count & amount
        
def Districts(dataframe, state):

    Data_td = dataframe[dataframe['State'] == state]
    Data_td.reset_index(drop = True, inplace = True)

    Data_td_group = Data_td.groupby('Districts')[["Transaction_count","Transaction_amount"]].sum()
    Data_td_group.reset_index(inplace = True)

    column1, column2 = st.columns(2)

    with column1:
        
        fig_District_a =px.pie(data_frame = Data_td_group, names = 'Districts', values='Transaction_amount', width =500,
                        title = f"{state}  TRANSACTION AMOUNT" , hole= 0.2)
        
        st.plotly_chart(fig_District_a)

    with column2:

        fig_District_c =px.pie(data_frame = Data_td_group, names = 'Districts', values='Transaction_count', width =500,
                        title = f"{state}  TRANSACTION COUNT" , hole= 0.2)
        
        st.plotly_chart(fig_District_c)   

# AGG User Data Analysis
        
def User_count_Percentage_analysis(dataFrame,Year):

    Data_CP = dataFrame[dataFrame["Year"] == Year] #here we are taking only specific year to view

    # drop will remove the old Index and give new index value and Inplace will Keep the change in the dataframe
    Data_CP.reset_index(drop = True, inplace = True) 

    #here we grouping all states with transaction count & amount
    Data_CP_group = pd.DataFrame(Data_CP.groupby("Phone_Brand")['Transaction_count'].sum())
    Data_CP_group.reset_index(inplace = True)

    fig_cp = px.pie(data_frame = Data_CP_group, names= "Phone_Brand", values= "Transaction_count", title= f"TRANSACTION COUNT BASED ON PHONE BRAND OF {Year}", 
                        width =500, hole= 0.5)
    st.plotly_chart(fig_cp)

    return Data_CP 
     
def User_count_Percentage_analysis_Q(dataFrame,Quarter):

    Data_CP = dataFrame[dataFrame["Quarter"] == Quarter] #here we are taking only specific year to view

    # drop will remove the old Index and give new index value and Inplace will Keep the change in the dataframe
    Data_CP.reset_index(drop = True, inplace = True) 

    fig_cp_Q = px.bar(Data_CP, x= 'Phone_Brand', y= 'Transaction_count', hover_data= 'User_Percentage',
                    title= f'BRANDS, TRANSACTION COUNT, PERCENTAGE ANALYSIS based on Quarter Data {Quarter}', width= 1000)
    
    st.plotly_chart(fig_cp_Q)

    return Data_CP

def User_count_Percentage_analysis_S(dataFrame,State):

    Data_CPS = dataFrame[dataFrame["State"] == State] #here we are taking only specific year to view

    # drop will remove the old Index and give new index value and Inplace will Keep the change in the dataframe
    Data_CPS.reset_index(drop = True, inplace = True) 

    column1, column2 = st.columns(2)


    with column1:

        fig_cp_S = px.line_3d(data_frame= Data_CPS, x= 'Phone_Brand', y= 'Transaction_count',z= 'User_Percentage', hover_data= 'User_Percentage',
                        title= f'BRANDS, TRANSACTION COUNT, PERCENTAGE ANALYSIS based on STATE {State}',height=750, width= 700, markers= True )

        st.plotly_chart(fig_cp_S)

    with column2:

        fig_count_geo = px.choropleth(Data_CPS,
                                title="GEO VISUALUATION OF BRANDS, TRANSACTION COUNT, PERCENTAGE",
                                geojson = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                featureidkey='properties.ST_NM',
                                locations='State',
                                color='State',
                                color_continuous_scale='sunset',
                                range_color= (Data_CPS['State'].min(),Data_CPS['State'].max()),
                                hover_name='User_Percentage',
                                height = 550,
                                width = 500)

        fig_count_geo.update_geos(fitbounds="locations", visible=False)

        st.plotly_chart(fig_count_geo)

#MAP USER data Analysis

def Map_Registereduser_Appopens(dataFrame,Year):

    Data_map_ra = dataFrame[dataFrame["Year"] == Year] #here we are taking only specific year to view

    # drop will remove the old Index and give new index value and Inplace will Keep the change in the dataframe
    Data_map_ra.reset_index(drop = True, inplace = True) 

    #here we grouping all states with transaction count & amount
    Data_Map_ra_g = Data_map_ra.groupby("State")[["RegisteredUser","AppOpens"]].sum()
    Data_Map_ra_g.reset_index(inplace = True)


    fig_map_ra = px.line(Data_Map_ra_g, x= "State", y= ["RegisteredUser", "AppOpens" ], title= f"REGISTEREDUSER COUNT OF {Year}", 
                        color_discrete_sequence=px.colors.sequential. Magenta,height = 550, width =1000, markers= True)
    st.plotly_chart(fig_map_ra)
           
    fig_Ra_geo = px.choropleth(Data_Map_ra_g,
                        title=f"GEO VISUALUATION OF REGISTEREDUSER {Year}",
                        geojson = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        locations='State',
                        featureidkey='properties.ST_NM',
                        color='RegisteredUser',
                        color_continuous_scale='sunset',
                        range_color= (Data_Map_ra_g['RegisteredUser'].min(),Data_Map_ra_g['RegisteredUser'].max()),
                        hover_name='State',
                        hover_data='AppOpens',
                        height = 950,
                        width = 900)

    fig_Ra_geo.update_geos(fitbounds="locations", visible=False)

    st.plotly_chart(fig_Ra_geo)

    return Data_map_ra

def Map_Registereduser_Appopens_Q(dataFrame,Quarter):

    Data_map_ra = dataFrame[dataFrame["Quarter"] == Quarter] #here we are taking only specific year to view

    # drop will remove the old Index and give new index value and Inplace will Keep the change in the dataframe
    Data_map_ra.reset_index(drop = True, inplace = True) 

    #here we grouping all states with transaction count & amount
    Data_Map_ra_Qg = Data_map_ra.groupby("State")[["RegisteredUser","AppOpens"]].sum()
    Data_Map_ra_Qg.reset_index(inplace = True)

    fig_map_ra_Q = px.line(Data_Map_ra_Qg, x= "State", y= ["RegisteredUser","AppOpens"] , title= f"REGISTEREDUSER COUNT OF {Quarter}", 
                        color_discrete_sequence=px.colors.sequential. Magenta, width =1000, markers= True)
    st.plotly_chart(fig_map_ra_Q)
    
    fig_Ra_geo_Q = px.choropleth(Data_Map_ra_Qg,
                        title=f"GEO VISUALUATION OF TRANSACTION AMOUNT {Quarter}",
                        geojson = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        locations='State',
                        featureidkey='properties.ST_NM',
                        color='RegisteredUser',
                        color_continuous_scale='sunset',
                        range_color= (Data_Map_ra_Qg['RegisteredUser'].min(),Data_Map_ra_Qg['RegisteredUser'].max()),
                        hover_name='State',
                        height = 950,
                        width = 900)

    fig_Ra_geo_Q.update_geos(fitbounds="locations", visible=False)

    st.plotly_chart(fig_Ra_geo_Q)

    return Data_map_ra

# Districts data analysis based on Registereduser & Appopens

def Districts_RA(dataframe, state):

    Data_ra = dataframe[dataframe['State'] == state]
    Data_ra.reset_index(drop = True, inplace = True)

    Data_ra_group = Data_ra.groupby('Districts')[["RegisteredUser","AppOpens"]].sum()
    Data_ra_group.reset_index(inplace = True)

    column1, column2 = st.columns(2)

    with column1:
        
        fig_District_r =px.pie(data_frame = Data_ra_group, names = 'Districts', values='RegisteredUser', width =500,
                        title = f"{state}  REGISTERED USER" , hole= 0.2)
        
        st.plotly_chart(fig_District_r)

    with column2:

        fig_District_a =px.pie(data_frame = Data_ra_group, names = 'Districts', values='AppOpens', width =500,
                        title = f"{state}  APPOPENS" , hole= 0.2)
        
        st.plotly_chart(fig_District_a) 

# Analysing Transaction count and Amount based on Pincodes
        
def Pincodes(dataframe, state):

    Data_tP = dataframe[dataframe['State'] == state]
    Data_tP.reset_index(drop = True, inplace = True)

    Data_tP_group = Data_tP.groupby('Pincodes')[["Transaction_count","Transaction_amount"]].sum()
    Data_tP_group.reset_index(inplace = True)

    column1, column2 = st.columns(2)

    with column1:
        
        fig_type_a =px.pie(data_frame = Data_tP_group, names = 'Pincodes', values='Transaction_amount', width =500,
                        title = f"{state}  TRANSACTION AMOUNT" , hole= 0.2)
        
        st.plotly_chart(fig_type_a)

    with column2:

        fig_type_c =px.pie(data_frame = Data_tP_group, names = 'Pincodes', values='Transaction_count', width =500,
                        title = f"{state}  TRANSACTION COUNT" , hole= 0.2)
        
        st.plotly_chart(fig_type_c)

# TOP User Data Analysis
        
def TOP_Registereduser_analysis(dataFrame,Year):

    Data_rp = dataFrame[dataFrame["Year"] == Year] #here we are taking only specific year to view

    # drop will remove the old Index and give new index value and Inplace will Keep the change in the dataframe
    Data_rp.reset_index(drop = True, inplace = True) 

    #here we grouping all states with transaction count & amount
    Data_rp_group = pd.DataFrame(Data_rp.groupby(["State","Quarter"])['RegisteredUser'].sum())
    Data_rp_group.reset_index(inplace = True)

    fig_cp = px.bar(Data_rp_group, x= 'State', y= 'RegisteredUser', color="Quarter",  height=800, width= 1000, 
                color_discrete_sequence=px.colors.sequential.Magenta_r,
                title= f'REGISTEREDUSER DATA ANALYSIS based on state & Quarter Data {Year}',
                hover_name= 'State')
    
    st.plotly_chart(fig_cp)

    return Data_rp 
     
def TOP_Registereduser_analysis_S(dataFrame,State):

    Data_ruS = dataFrame[dataFrame["State"] == State] #here we are taking only specific year to view

    # drop will remove the old Index and give new index value and Inplace will Keep the change in the dataframe
    Data_ruS.reset_index(drop = True, inplace = True) 

    column1, column2 = st.columns(2)

    with column1:

        fig_ru_S = px.line_3d(data_frame= Data_ruS, x= 'State', y= 'Pincodes',z= 'RegisteredUser', hover_data= 'RegisteredUser',
                        title= f'REGISTEREDUSER DATA ANALYSIS based on state {State}',height=950, width= 900, markers= True,color='Pincodes' , 
                        color_discrete_sequence=px.colors.sequential.Agsunset_r)

        st.plotly_chart(fig_ru_S)

    with column2:

        fig_ru_geo = px.choropleth(Data_ruS,
                                title="GEO VISUALUATION OF REGISTEREDUSER DATA ANALYSIS based on state",
                                geojson = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                featureidkey='properties.ST_NM',
                                locations='State',
                                color='RegisteredUser',
                                color_continuous_scale='sunset',
                                range_color= (Data_ruS['RegisteredUser'].min(),Data_ruS['RegisteredUser'].max()),
                                hover_data='Pincodes',
                                height = 550,
                                width = 500)

        fig_ru_geo.update_geos(fitbounds="locations", visible=False)

        st.plotly_chart(fig_ru_geo)


# Streamlit Part

st.set_page_config(
    page_title="PhonePePlus data Analysis App",
    page_icon="🧊",
    layout="wide",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
st.title('PhonePe Plus :globe_with_meridians:',)
st.header('THE BEAT OF PROGRESS')

#[theme]
base="dark"
primaryColor="#090352"
backgroundColor="#4b3fef"
secondaryBackgroundColor="#638ce0"


with st.container():
    tab1, tab2, tab3 = st.tabs(["HOME", "EXPLORE DATA", "TOP CHARTS"])

    with tab1:
        
        column1, column2 = st.columns(2)

        with column1:

            st.header("PHONEPE",divider = 'gray')
            st.subheader("INDIA'S ONE OF THE BEST TRANSACTION APP")
            st.subheader("PhonePe is one of India's leading digital payment platforms, offering a wide range of financial services and products to users.",divider = 'gray')
            st.write("****ABOUT****")
            st.write("PhonePe is one of India's leading digital payment platforms, offering a wide range of financial services and products to users.")
            st.write("****SERVICES OFFERED****")
            st.write("1. Payments: PhonePe allows users to make various types of digital payments, including peer-to-peer (P2P) transfers, utility bill payments, mobile recharges, and payments at online and offline merchants.")
            st.write("2. UPI (Unfied Payments Interface): PhonePe leverages the UPI infrastructure to facilitate instant bank-to-bank transfers, enabling users to send and receive money using their mobile phones.")
            st.write("3. Banking Services: PhonePe offers banking services such as savings account opening, fixed deposits, and insurance products through partnerships with various banks and financial institutions.")
            st.write("4. Investments: Users can invest in mutual funds, stocks, gold, and other financial instruments directly from the PhonePe app, making it a convenient platform for both payments and investments.")
            st.write("5. Insurance: PhonePe provides users with the option to purchase insurance products such as health, life, and vehicle insurance, offering a one-stop solution for financial needs.")
            st.write("**Click bellow Button to DOWNLOAD OUR APP**")
            st.download_button("DOWNLOAD For Android","https://play.google.com/store/apps/details?id=com.phonepe.app")
            st.download_button("DOWNLOAD For IOS","https://apps.apple.com/in/app/phonepe-india-digital-wallet/id1179933476")

        with column2:

            st.image(Image.open(r"C:\Users\rajan\OneDrive\Desktop\Phonepe\pulse\New folder\PhonePe-Offers.png"))
            st.write("**User Base**")
            st.write("PhonePe has rapidly grown its user base since its inception and is among the leading digital payment platforms in India.")
            st.write("As of [latest available data], PhonePe reportedly has over [200 million registered users] and [15 million merchant partners], indicating its widespread adoption among both consumers and businesses.")

            st.video(r"C:\Users\rajan\OneDrive\Desktop\Phonepe\pulse\Video\copy_of_recharge_on_phonepe.mp4")
            st.subheader("****Recharge your phone on PhonePe****",divider = 'gray')
            st.write("Need to recharge your prepaid mobile number?")
            st.write("Watch this simple video to understand how it's done.")
            

        column3, column4 = st.columns(2)

        with column3:
            
            st.video(r"C:\Users\rajan\OneDrive\Desktop\Phonepe\pulse\Video\1st_Payment.mp4")
            st.subheader("****Make your first UPI payment****",divider = 'gray')
            st.write("Watch this simple video to help you get started with UPI payments on PhonePe.")

        with column4:
            
            st.write("**Technology**")
            st.write("PhonePe's platform is built on top of the UPI infrastructure, allowing seamless interoperability with other UPI-enabled apps and banks.")
            st.write("The app employs advanced security measures such as multi-factor authentication, encryption, and secure payment gateways to ensure the safety of user transactions and data.")
            st.write("**Partnerships**")
            st.write("PhonePe has forged strategic partnerships with various companies and merchants to expand its service offerings and enhance user experience.")
            st.write("It has collaborated with leading brands in e-commerce, retail, travel, and other sectors to offer exclusive discounts, cashback offers, and promotional deals to its users.")
            st.write("**Innovation**")
            st.write("PhonePe continues to innovate and introduce new features and services to cater to evolving user needs and preferences.")
            st.write("It has launched initiatives such as PhonePe for Business, which provides merchants with tools and solutions to accept digital payments and manage their businesses more efficiently.")


        
    with tab2:

        select = option_menu('Explore Data',['Aggregated Data','Map Data','Top Data'])

        if select == 'Aggregated Data':

            option = st.selectbox('Select a Data to Analysis', ['Transaction Data', 'User Data'])

            if option == 'Transaction Data':

                column1, column2 = st.columns(2)

                with column1:

                    years = st.radio("select the Year", Agg_trans_data["Year"].unique())
                Data_CA_Q = Ttansaction_count_amount_analysis(Agg_trans_data, years)
                
                with column2:
                    
                    quarters = st.radio("select the Quarter", Data_CA_Q['Quarter'].unique())
                Data_CA_S = Ttansaction_count_amount_analysis_Q(Data_CA_Q, quarters)


                states = st.selectbox("select the State for Analysing Transaction Type data(year)", Data_CA_Q["State"].unique())
                Transaction_type(Data_CA_Q, states)
   
                statesq = st.selectbox("select the State for Analysing Transaction Type data(Quarter)", Data_CA_S["State"].unique())
                Transaction_type(Data_CA_S, statesq)
                
            elif option == 'User Data':
                 
                 column1, column2 = st.columns(2)

                 with column1:

                     years = st.radio("select the Year", Agg_user_data["Year"].unique())
                 Data_CP_Q = User_count_Percentage_analysis(Agg_user_data, years)

                 with column2:
                
                      quarters = st.radio("select the Quarter", Data_CP_Q['Quarter'].unique())
                 Data_CA_S = User_count_Percentage_analysis_Q(Data_CP_Q, quarters)

                 states = st.selectbox("select the State", Data_CA_S["State"].unique())
                 User_count_Percentage_analysis_S(Data_CA_S, states)


        elif select == 'Map Data':

            option2 = st.selectbox('Select a Data to Analysis',[ 'Transaction Data', 'User Data'])

            if option2 == 'Transaction Data':

                column1, column2 = st.columns(2)
                
                with column1:

                    years = st.radio("select the Year", Map_trans_data["Year"].unique())
                Data_MAP_CA_Q = Ttansaction_count_amount_analysis(Map_trans_data, years)
                
                with column2:
                    
                    quarters = st.radio("select the Quarter", Data_MAP_CA_Q['Quarter'].unique())
                Data_MAP_CA_S = Ttansaction_count_amount_analysis_Q(Data_MAP_CA_Q, quarters)


                states = st.selectbox("select the State for Analysing Transaction Type data(year)", Data_MAP_CA_Q["State"].unique())
                Districts(Data_MAP_CA_Q, states)
   
                statesq = st.selectbox("select the State for Analysing Transaction Type data(Quarter)", Data_MAP_CA_S["State"].unique())
                Districts(Data_MAP_CA_S, statesq)

            elif option2 == 'User Data':

                column1, column2 = st.columns(2)
                
                with column1:

                    years = st.radio("select the Year", Map_user_data["Year"].unique())
                Data_MAP_RA_Q = Map_Registereduser_Appopens(Map_user_data, years)
                
                with column2:
                    
                    quarters = st.radio("select the Quarter", Data_MAP_RA_Q['Quarter'].unique())
                Data_MAP_RA_S = Map_Registereduser_Appopens_Q(Data_MAP_RA_Q, quarters)


                states = st.selectbox("select the State for Analysing District data(year)", Data_MAP_RA_Q["State"].unique())
                Districts_RA(Data_MAP_RA_Q, states)
   
                statesq = st.selectbox("select the State for Analysing District Type data(Quarter)", Data_MAP_RA_S["State"].unique())
                Districts_RA(Data_MAP_RA_S, statesq)

        elif select == 'Top Data':
           
            option3 = st.selectbox('Select a Data to Analysis',[ 'Transaction Data', 'User Data'])
          
            if option3 == 'Transaction Data':
                
                column1, column2 = st.columns(2)
                
                with column1:

                    years = st.radio("select the Year", Top_trans_data["Year"].unique())
                Data_TOP_CA_Q = Ttansaction_count_amount_analysis(Top_trans_data, years)
                
                with column2:
                    
                    quarters = st.radio("select the Quarter", Data_TOP_CA_Q['Quarter'].unique())
                Data_TOP_CA_S = Ttansaction_count_amount_analysis_Q(Data_TOP_CA_Q, quarters)


                states = st.selectbox("select the State for Analysing Transaction count and Amount based on Pincodes(year)", Data_TOP_CA_Q["State"].unique())
                Pincodes(Data_TOP_CA_Q, states)
   
                statesq = st.selectbox("select the State for Analysing Transaction count and Amount based on Pincodes(Quarter)", Data_TOP_CA_S["State"].unique())
                Pincodes(Data_TOP_CA_S, statesq)

            elif option3 == 'User Data':

                column1, column2 = st.columns(2)

                with column1:

                     years = st.radio("select the Year", Top_user_data["Year"].unique())
                Data_TOP_Ru_Y = TOP_Registereduser_analysis(Top_user_data, years)

                with column2:

                    states = st.selectbox("select the State for Analysing District data(year)", Data_TOP_Ru_Y["State"].unique())
                TOP_Registereduser_analysis_S(Data_TOP_Ru_Y, states)

    with tab3:

        Data_Base = psycopg2.connect(host = "localhost",
                            user = "postgres",
                            password = "BNandy30",
                            port = "5432",
                            database = "PhonePe") # it is the connection to run SQL in backend

        cursor = Data_Base.cursor() #Cursor is a Temporary Memory or Temporary Work Station.
        
        Questions = st.selectbox("Select the Questions:",['1. Give the Total transaction Amount and Count of Aggregated Transaction.',
                                                         '2. Give the Total transaction Count of Aggregated User.',
                                                         '3. Give the Total transaction Amount and Count of MAP Transaction.',
                                                         '4. Give the Total Registered User and AppOPens of MAP User.',
                                                         '5. Give the Total transaction Amount and Count of Top Transaction.',
                                                         '6. Give the Total Registered User of Top User.',
                                                         '7. Give the Top 10 States based on Transaction amount.',
                                                         '8. Give the Top 10 Districts based on Transaction amount.',
                                                         '9. Give the Phone Brand based on Aggregated User.',
                                                         '10. Give the Transaction Type based on Aggregated Transaction Data.'])
        
        if Questions == "1. Give the Total transaction Amount and Count of Aggregated Transaction." :
            if st.button("GET SOLUTION"):
                Answer = '''SELECT state, SUM(transaction_amount) as transaction_amount, 
                            SUM(transaction_count) as transaction_count from agg_trans 
                            GROUP BY state 
                            ORDER by transaction_amount DESC;'''
                cursor.execute(Answer)
                Q1 = cursor.fetchall()
                data_frame = pd.DataFrame(Q1,columns=['State', 'transaction_amount', 'transaction_count'])

                fig_Q1 = px.bar(data_frame, x= 'State', y= ['transaction_amount','transaction_count'], color="State",  height=800, width= 1000, 
                color_discrete_sequence=px.colors.sequential.Magenta_r,
                title='Total transaction Amount and Count of Aggregated Transaction',
                hover_name= 'State')

                st.plotly_chart(fig_Q1)
                st.success("The Total transaction Amount and Count of Aggregated Transaction")

        elif Questions == "2. Give the Total transaction Count of Aggregated User." :
            if st.button("GET SOLUTION"):
                Answer = '''SELECT state, SUM(transaction_count) as transaction_count, Phone_Brand
                            from agg_user
                            GROUP BY state , Phone_Brand
                            ORDER BY transaction_count DESC;'''
                cursor.execute(Answer)
                Q2 = cursor.fetchall()
                dataframe = pd.DataFrame(Q2,columns=['State', 'transaction_count', 'Phone_Brand'])

                fig_Q2 = px.line(data_frame = dataframe, x= 'State', y= 'transaction_count', color="Phone_Brand",  height=800, width= 1000, 
                color_discrete_sequence=px.colors.sequential.Magenta_r,
                title='Total transaction Count of Aggregated User',
                hover_name= 'State',hover_data='Phone_Brand',markers= True)
                
                st.plotly_chart(fig_Q2)
                st.success("The Total transaction Count of Aggregated User")

        elif Questions == "3. Give the Total transaction Amount and Count of MAP Transaction." :
            if st.button("GET SOLUTION"):
                Answer = '''SELECT state, SUM(transaction_amount) as transaction_amount, 
                            SUM(transaction_count) as transaction_count from map_trans
                            GROUP BY state 
                            ORDER by transaction_amount DESC;'''
                cursor.execute(Answer)
                Q3 = cursor.fetchall()
                dataframe = pd.DataFrame(Q3,columns=['State', 'transaction_amount', 'transaction_count'])

                fig_Q3 = px.bar(dataframe, x= 'transaction_amount', y= 'transaction_count', color="State",  height=800, width= 1000, 
                color_discrete_sequence=px.colors.sequential.Magenta_r,
                title='Total transaction Amount and Count of Map Transaction',
                hover_name= 'State')
                
                st.plotly_chart(fig_Q3)
                st.success("The Total transaction Amount and Count of Map Transaction.")

        
        elif Questions == "4. Give the Total Registered User and AppOPens of MAP User." :
            if st.button("GET SOLUTION"):
                Answer = '''SELECT state, SUM(RegisteredUser) as RegisteredUser, 
                            SUM(AppOpens) as AppOpens from map_user
                            GROUP BY state 
                            ORDER by RegisteredUser DESC;'''
                cursor.execute(Answer)
                Q4 = cursor.fetchall()
                dataframe = pd.DataFrame(Q4,columns=['State', 'RegisteredUser', 'AppOpens'])

                fig_Q4 = px.pie(dataframe, names= 'State', values= 'RegisteredUser', color="State", width= 1000, 
                color_discrete_sequence=px.colors.sequential.Magenta_r,
                title='Total Registered User and AppOPens of MAP User.',
                hover_name= 'State',hover_data='AppOpens', hole= 0.6)
                
                st.plotly_chart(fig_Q4)
                st.success("The Total Registered User and AppOPens of MAP User.")

        elif Questions == "5. Give the Total transaction Amount and Count of Top Transaction." :
            if st.button("GET SOLUTION"):
                Answer = '''SELECT state, SUM(transaction_amount) as transaction_amount, 
                            SUM(transaction_count) as transaction_count from top_trans
                            GROUP BY state 
                            ORDER by transaction_amount DESC;'''
                cursor.execute(Answer)
                Q5 = cursor.fetchall()
                dataframe = pd.DataFrame(Q5,columns=['State', 'transaction_amount', 'transaction_count'])

                fig_Q5 = px.line_3d(data_frame= dataframe, x= 'State', y= 'transaction_amount', z= 'transaction_count', width= 1000, height=900,
                color_discrete_sequence=px.colors.sequential.Magenta_r,
                title='Total transaction Amount and Count of Top Transaction.',
                hover_name= 'State',hover_data='transaction_count',markers= True)
                
                st.plotly_chart(fig_Q5)
                st.success("The Total transaction Amount and Count of Top Transaction.")

        elif Questions == "6. Give the Total Registered User of Top User." :
            if st.button("GET SOLUTION"):
                Answer = '''SELECT state, SUM(RegisteredUser) as RegisteredUser
                            from top_user
                            GROUP BY state 
                            ORDER by RegisteredUser DESC;'''
                cursor.execute(Answer)
                Q6 = cursor.fetchall()
                dataframe = pd.DataFrame(Q6,columns=['State', 'RegisteredUser'])

                fig_Q6 = px.bar(data_frame= dataframe, x= 'State', y= 'RegisteredUser',color='State' , width= 1000, height=900,
                color_discrete_sequence=px.colors.sequential.Magenta_r,
                title='Total Registered User of Top User.',
                hover_name= 'State',pattern_shape_sequence='+')
                
                st.plotly_chart(fig_Q6)
                st.success("The Total Registered User of Top User.")

        
        elif Questions == "7. Give the Top 10 States based on Transaction amount." :
            if st.button("GET SOLUTION"):
                Answer = '''SELECT state, SUM(transaction_amount) as transaction_amount
                            FROM agg_trans 
                            GROUP BY state 
                            ORDER by transaction_amount DESC
                            Limit 10;'''
                cursor.execute(Answer)
                Q7 = cursor.fetchall()
                dataframe = pd.DataFrame(Q7,columns=['State', 'transaction_amount'])

                fig_Q7 = px.choropleth(dataframe,
                                title=f"GEO VISUALUATION OF TOP 10 STATE",
                                geojson = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                locations='State',
                                featureidkey='properties.ST_NM',
                                color='transaction_amount',
                                color_continuous_scale='sunset',
                                range_color= (dataframe['transaction_amount'].min(),dataframe['transaction_amount'].max()),
                                hover_name='State',
                                height = 550,
                                width = 500)

                fig_Q7.update_geos(fitbounds="locations", visible=False)
                
                st.plotly_chart(fig_Q7)
                st.success("The Top 10 States based on Transaction amount.")

        elif Questions == "8. Give the Top 10 Districts based on Transaction amount." :
            if st.button("GET SOLUTION"):
                Answer = '''SELECT Districts, SUM(transaction_amount) as transaction_amount
                            FROM map_trans 
                            GROUP BY Districts 
                            ORDER by transaction_amount DESC
                            Limit 10;'''
                cursor.execute(Answer)
                Q8 = cursor.fetchall()
                dataframe = pd.DataFrame(Q8,columns=['Districts', 'transaction_amount'])

                fig_Q8 = px.scatter(data_frame= dataframe, x= 'Districts', y= 'transaction_amount' , color='transaction_amount', width= 1000, height=900,
                color_discrete_sequence=px.colors.sequential.Magenta_r,
                title='Top 10 Districts based on Transaction amount.',
                hover_name= 'Districts')

                st.plotly_chart(fig_Q8)
                st.success("The Top 10 Districts based on Transaction amount.")

        elif Questions == "9. Give the Phone Brand based on Aggregated User." :
            if st.button("GET SOLUTION"):
                Answer = '''Select State, Phone_Brand FROM agg_user
                            GROUP BY State, Phone_Brand;'''
                cursor.execute(Answer)
                Q9 = cursor.fetchall()
                dataframe = pd.DataFrame(Q9,columns=['State', 'Phone_Brand'])

                fig_Q9 = px.bar(data_frame= dataframe, x= 'State', y= 'Phone_Brand' , color='Phone_Brand', width= 1000, height=900,
                color_discrete_sequence=px.colors.sequential.Magenta_r,
                title='Phone Brand based on State.',
                hover_name= 'State', pattern_shape_sequence='\\')

                st.plotly_chart(fig_Q9)
                st.success("Phone Brand based on State.")

        elif Questions == "10. Give the Transaction Type based on Aggregated Transaction Data." :
            if st.button("GET SOLUTION"):
                Answer = '''Select State, transaction_type FROM agg_trans
                            GROUP BY State, transaction_type;'''
                cursor.execute(Answer)
                Q10 = cursor.fetchall()
                dataframe = pd.DataFrame(Q10,columns=['State', 'transaction_type'])

                fig_Q10 = px.line(data_frame= dataframe, x= 'State', y= 'transaction_type' , color='transaction_type', width= 1000, height=900,
                color_discrete_sequence=px.colors.sequential.Magenta_r,
                title='Transaction Type based on State',
                hover_name= 'State', markers= True)

                st.plotly_chart(fig_Q10)
                st.success("The Transaction Type based on State")
