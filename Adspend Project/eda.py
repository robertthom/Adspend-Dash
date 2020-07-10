import pandas as pd
creativestats = pd.read_csv("C:/Users/helli/Desktop/Github/Adspend Project/google-political-ads-creative-stats.csv", parse_dates=[['Date','Time'], ['Date_Range_Start', 'Date_Range_End','First_Served_Timestamp', 'Last_Served_Timestamp'], dtype={'Ad_ID': 'string', 'Ad_URL': 'string', 'Ad_Type': 'string', 'Regions': 'string', 'Advertiser_ID': 'string', 'Advertiser_Name': 'string', 'Ad_Campaigns_List': 'string', 'Date_Range_Start': 'object', 'Date_Range_End': 'object', 'Num_of_Days': 'int', 
'Impressions': 'string', 'Spend_USD': 'string', 'First_Served_Timestamp': 'object', 'Last_Served_Timestamp': 'object', 'Age_Targeting': 'string', 'Gender_Targeting': 'string', 'Geo_Targeting_Included': 'string', 
'Geo_Targeting_Excluded': 'string', 'Spend_Range_Min_USD': 'int', 'Spend_Range_Max_USD': 'int', 'Spend_Range_Min_EUR': 'int', 'Spend_Range_Max_EUR': 'int', 'Spend_Range_Min_INR': 'int', 
'Spend_Range_Max_INR': 'int', 'Spend_Range_Min_BGN': 'int', 'Spend_Range_Max_BGN': 'int', 'Spend_Range_Min_HRK': 'int', 'Spend_Range_Max_HRK': 'int', 'Spend_Range_Min_CZK': 'int', 
'Spend_Range_Max_CZK': 'int', 'Spend_Range_Min_DKK': 'int', 'Spend_Range_Max_DKK': 'int', 'Spend_Range_Min_HUF': 'int', 'Spend_Range_Max_HUF': 'int', 'Spend_Range_Min_PLN': 'string', 
'Spend_Range_Max_PLN': 'string', 'Spend_Range_Min_RON': 'string', 'Spend_Range_Max_RON': 'string', 'Spend_Range_Min_SEK': 'string', 'Spend_Range_Max_SEK': 'string', 'Spend_Range_Min_GBP': 'string', 'Spend_Range_Max_GBP': 'string'})
#mask = creativestats.Advertiser_Name == 'DONALD J. TRUMP FOR PRESIDENT, INC.'
#trumpdf = creativestats[mask] #creates df of Trump ads
#agedf = trumpdf.groupby('Age_Targeting')['Ad_ID'].nunique()#counts how many ads were targeted in each age range grouping
#import seaborn as sns
#import matplotlib.pyplot as plt
#sns.pairplot(creativestats[["Impressions", "Spend_USD", "Num_of_Days"]])
#plt.show()

#creativestats.Advertiser_Name[10000]
#[1] 'DONALD J. TRUMP FOR PRESIDENT, INC.'

#creativestats[Advertiser_Name]
#DONALD J. TRUMP FOR PRESIDENT, INC.
#Impressions,Regions, Advertiser_Name, Ad_Type, Age_Targeting, Gender_Targeting





