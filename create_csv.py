import pandas as pd
import random as rd
import datetime as dt
import numpy as np


data=pd.DataFrame([], columns=['Date','Market','Capital_used','ROI','Profit_Loss','Opened_trades','Closed_trades','Profitable_trades',
                            'Loosing_trades','Targets_met','Stoplosses_hit','broker_name','segment','trade_type','long_short','hourly_slots',
                            'pre_planned_or_adhoc','strategy_id'])

##create random variables
for ind in range(5000):
    df_row ={}
    df_row['Date'] = (dt.date(2021, 4, 1)+dt.timedelta(rd.randint(0,112))).strftime("%d/%m/%Y")
    df_row['Market'] = 'IND'
    df_row['Capital_used']=rd.randint(50000, 1500000)
    df_row['ROI']=0
    df_row['Profit_Loss']=round(rd.randint(10, 100)/2*(-1)**rd.randint(0,1)* df_row['Capital_used']/1000,2)
    #round(df_row['Capital_used']*df_row['ROI']/100,2)
    df_row['Opened_trades']=rd.randint(1, 50)
    df_row['Closed_trades']=rd.randint(1, 50)
    df_row['Profitable_trades']=rd.randint(0, df_row['Closed_trades'])
    df_row['Loosing_trades']=df_row['Closed_trades']-df_row['Profitable_trades']
    df_row['Targets_met']=rd.randint(0, df_row['Profitable_trades'])
    df_row['Stoplosses_hit']=rd.randint(0, df_row['Loosing_trades'])
    df_row['broker_name']=rd.choice(['A','B','C', 'D'])
    df_row['segment']=rd.choice([' Equity', 'FnO', 'Forex','Commodities', 'Shares'])
    df_row['trade_type']=rd.choice(['scalping','intraday', 'swing', 'positional'])
    df_row['long_short']=rd.choice(['Long','Short'])
    df_row['hourly_slots']=rd.randint(1, 4)
    df_row['pre_planned_or_adhoc']=rd.randint(1, 2)
    df_row['strategy_id']=rd.randint(1, 10)
    data=data.append(df_row,ignore_index=True)

#get an average Profit_Loss and Capital_used per day
data['Capital_used']=data['Capital_used'].astype(int)
tmp=data[["Date",'Profit_Loss','Capital_used']].groupby(by=["Date"]).mean()

#Calculate average ROI per day
tmp['ROI']=(tmp['Profit_Loss']/tmp['Capital_used']*100).round(2)
tmp=tmp.reset_index()

#update ROI in the main table
data['ROI']=data.apply(lambda x: tmp.loc[tmp['Date']==x['Date'],'ROI'].to_numpy()[0], axis = 1)    

#Save file as CSV
data.to_csv("5000_sample.csv")