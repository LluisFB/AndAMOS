# -*- coding: utf-8 -*-
# Alan Parson's code
"""
Created on Tue Dec 23 19:15:09 2025
 
@author: amich
"""
# %%
'''Data Wrangling'''
 
 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import xarray as xr
import netCDF4
import matplotlib.dates as mdates
#print(netCDF4.__version__)
 
 
 
 
 
# Load NetCDF file (ds1=Forecast, dsh=Hindcast/Climatology)
ds1 = xr.open_dataset("C:/Users/amich/SURE/Python/UKMetO_Zonal_FORE_MLs.nc", engine='netcdf4')
dsh1 = xr.open_dataset("C:/Users/amich/SURE/Python/UKMetO_Zonal_HIND_1ML.nc", engine='netcdf4')
 
ds2 = xr.open_dataset("C:/Users/amich/SURE/Python/ECMWF_Zonal_FORE_MLs.nc", engine='netcdf4')
dsh2 = xr.open_dataset("C:/Users/amich/SURE/Python/ECMWF_Zonal_HIND_1ML.nc", engine='netcdf4')
 
ds3 = xr.open_dataset("C:/Users/amich/SURE/Python/ECCC_Zonal_FORE_MLs.nc", engine='netcdf4')
dsh3 = xr.open_dataset("C:/Users/amich/SURE/Python/ECCC_Zonal_HIND_1ML.nc", engine='netcdf4')
 
ds4 = xr.open_dataset("C:/Users/amich/SURE/Python/MF_Zonal_FORE_MLs.nc", engine='netcdf4')
dsh4 = xr.open_dataset("C:/Users/amich/SURE/Python/MF_Zonal_HIND_1ML.nc", engine='netcdf4')
 
ds5 = xr.open_dataset("C:/Users/amich/SURE/Python/CMCC_Zonal_FORE_MLs.nc", engine='netcdf4')
dsh5 = xr.open_dataset("C:/Users/amich/SURE/Python/CMCC_Zonal_HIND_1ML.nc", engine='netcdf4')
 
dsE = xr.open_dataset("C:/Users/amich/SURE/Python/ERA5_Zonal_FORE.nc", engine='netcdf4')
dshE = xr.open_dataset("C:/Users/amich/SURE/Python/ERA5_Zonal_HIND.nc", engine='netcdf4')
 
 
# Convert to DataFrame
df1 = ds1.to_dataframe().reset_index()
dfh1 = dsh1.to_dataframe().reset_index()
 
df2 = ds2.to_dataframe().reset_index()
dfh2 = dsh2.to_dataframe().reset_index()
 
df3 = ds3.to_dataframe().reset_index()
dfh3 = dsh3.to_dataframe().reset_index()
 
df4 = ds4.to_dataframe().reset_index()
dfh4 = dsh4.to_dataframe().reset_index()
 
df5 = ds5.to_dataframe().reset_index()
dfh5 = dsh5.to_dataframe().reset_index()
 
dfE = dsE.to_dataframe().reset_index()
dfhE = dshE.to_dataframe().reset_index()
 
 
#Renaming Columns
df1.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','u':'uwind','v':'vwind'}, inplace=True)
dfh1.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','u':'uwind','v':'vwind'}, inplace=True)
 
df2.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','u':'uwind','v':'vwind'}, inplace=True)
dfh2.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','u':'uwind','v':'vwind'}, inplace=True)
 
df3.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','u':'uwind','v':'vwind'}, inplace=True)
dfh3.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','u':'uwind','v':'vwind'}, inplace=True)
 
df4.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','u':'uwind','v':'vwind'}, inplace=True)
dfh4.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','u':'uwind','v':'vwind'}, inplace=True)
 
df5.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','u':'uwind','v':'vwind'}, inplace=True)
dfh5.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','u':'uwind','v':'vwind'}, inplace=True)
 
dfE.rename(columns={'valid_time':'date','indexing_time':'date','forecastMonth':'lead_month','u':'uwind','v':'vwind'}, inplace=True)
dfhE.rename(columns={'valid_time':'date','indexing_time':'date','forecastMonth':'lead_month','u':'uwind','v':'vwind'}, inplace=True)
 
 
#Convert to datetime
df1['date'] = pd.to_datetime(df1['date'])
dfh1['date'] = pd.to_datetime(dfh1['date'])
 
df2['date'] = pd.to_datetime(df2['date'])
dfh2['date'] = pd.to_datetime(dfh2['date'])
 
df3['date'] = pd.to_datetime(df3['date'])
dfh3['date'] = pd.to_datetime(dfh3['date'])
 
df4['date'] = pd.to_datetime(df4['date'])
dfh4['date'] = pd.to_datetime(dfh4['date'])
 
df5['date'] = pd.to_datetime(df5['date'])
dfh5['date'] = pd.to_datetime(dfh5['date'])
 
dfE['date'] = pd.to_datetime(dfE['date'])
dfhE['date'] = pd.to_datetime(dfhE['date'])
 
 
#Find mean of chosen paramater by date and lead month
f_mean_uwind=df1.groupby(['date','lead_month'])['uwind'].transform('mean')
df1['monthly_mean_uwind'] = f_mean_uwind
h_mean_uwind=dfh1.groupby(['date','lead_month'])['uwind'].transform('mean')
dfh1['monthly_mean_uwind'] = h_mean_uwind
 
f_mean_uwind=df2.groupby(['date','lead_month'])['uwind'].transform('mean')
df2['monthly_mean_uwind'] = f_mean_uwind
h_mean_uwind=dfh2.groupby(['date','lead_month'])['uwind'].transform('mean')
dfh2['monthly_mean_uwind'] = h_mean_uwind
 
f_mean_uwind=df3.groupby(['date','lead_month'])['uwind'].transform('mean')
df3['monthly_mean_uwind'] = f_mean_uwind
h_mean_uwind=dfh3.groupby(['date','lead_month'])['uwind'].transform('mean')
dfh3['monthly_mean_uwind'] = h_mean_uwind
 
f_mean_uwind=df4.groupby(['date','lead_month'])['uwind'].transform('mean')
df4['monthly_mean_uwind'] = f_mean_uwind
h_mean_uwind=dfh4.groupby(['date','lead_month'])['uwind'].transform('mean')
dfh4['monthly_mean_uwind'] = h_mean_uwind
 
f_mean_uwind=df5.groupby(['date','lead_month'])['uwind'].transform('mean')
df5['monthly_mean_uwind'] = f_mean_uwind
h_mean_uwind=dfh5.groupby(['date','lead_month'])['uwind'].transform('mean')
dfh5['monthly_mean_uwind'] = h_mean_uwind
 
f_mean_uwind=dfE.groupby(['date'])['uwind'].transform('mean')
dfE['monthly_mean_uwind'] = f_mean_uwind
h_mean_uwind=dfhE.groupby(['date'])['uwind'].transform('mean')
dfhE['monthly_mean_uwind'] = h_mean_uwind
 
 
#Find mean of each unique month
df1['month'] = df1['date'].dt.month
dfh1['month'] = dfh1['date'].dt.month
 
df2['month'] = df2['date'].dt.month
dfh2['month'] = dfh2['date'].dt.month
 
df3['month'] = df3['date'].dt.month
dfh3['month'] = dfh3['date'].dt.month
 
df4['month'] = df4['date'].dt.month
dfh4['month'] = dfh4['date'].dt.month
 
df5['month'] = df5['date'].dt.month
dfh5['month'] = dfh5['date'].dt.month
 
dfE['month'] = dfE['date'].dt.month
dfhE['month'] = dfhE['date'].dt.month
 
 
h_uniq_mo_mean_U=dfh1.groupby('month')['monthly_mean_uwind'].transform('mean')
dfh1['uniq_mo_mean_U']=h_uniq_mo_mean_U
 
h_uniq_mo_mean_U=dfh2.groupby('month')['monthly_mean_uwind'].transform('mean')
dfh2['uniq_mo_mean_U']=h_uniq_mo_mean_U
 
h_uniq_mo_mean_U=dfh3.groupby('month')['monthly_mean_uwind'].transform('mean')
dfh3['uniq_mo_mean_U']=h_uniq_mo_mean_U
 
h_uniq_mo_mean_U=dfh4.groupby('month')['monthly_mean_uwind'].transform('mean')
dfh4['uniq_mo_mean_U']=h_uniq_mo_mean_U
 
h_uniq_mo_mean_U=dfh5.groupby('month')['monthly_mean_uwind'].transform('mean')
dfh5['uniq_mo_mean_U']=h_uniq_mo_mean_U
 
h_uniq_mo_mean_U=dfhE.groupby('month')['monthly_mean_uwind'].transform('mean')
dfhE['uniq_mo_mean_U']=h_uniq_mo_mean_U
 
 
#Climatology Monthly Means
month_means_1=dfh1[['month','uniq_mo_mean_U']].copy()
month_means_1=month_means_1.groupby('month').mean('uniq_mo_mean_U')
 
month_means_2=dfh2[['month','uniq_mo_mean_U']].copy()
month_means_2=month_means_2.groupby('month').mean('uniq_mo_mean_U')
 
month_means_3=dfh3[['month','uniq_mo_mean_U']].copy()
month_means_3=month_means_3.groupby('month').mean('uniq_mo_mean_U')
 
month_means_4=dfh4[['month','uniq_mo_mean_U']].copy()
month_means_4=month_means_4.groupby('month').mean('uniq_mo_mean_U')
 
month_means_5=dfh5[['month','uniq_mo_mean_U']].copy()
month_means_5=month_means_5.groupby('month').mean('uniq_mo_mean_U')
 
month_means_E=dfhE[['month','uniq_mo_mean_U']].copy()
month_means_E=month_means_E.groupby('month').mean('uniq_mo_mean_U')
 
 
#Take Climatology away from Forecast
df1.groupby('month')
df1=df1.merge(month_means_1, on='month',how='left')
df1['anomaly']=df1['monthly_mean_uwind']-df1['uniq_mo_mean_U']
 
df2.groupby('month')
df2=df2.merge(month_means_2, on='month',how='left')
df2['anomaly']=df2['monthly_mean_uwind']-df2['uniq_mo_mean_U']
 
df3.groupby('month')
df3=df3.merge(month_means_3, on='month',how='left')
df3['anomaly']=df3['monthly_mean_uwind']-df3['uniq_mo_mean_U']
 
df4.groupby('month')
df4=df4.merge(month_means_4, on='month',how='left')
df4['anomaly']=df4['monthly_mean_uwind']-df4['uniq_mo_mean_U']
 
df5.groupby('month')
df5=df5.merge(month_means_5, on='month',how='left')
df5['anomaly']=df5['monthly_mean_uwind']-df5['uniq_mo_mean_U']
 
dfE.groupby('month')
dfE=dfE.merge(month_means_E, on='month',how='left')
dfE['anomaly']=dfE['monthly_mean_uwind']-dfE['uniq_mo_mean_U']
 
 
#Sorting
df1 = df1.sort_values(by=['date','lead_month'])
df2 = df2.sort_values(by=['date','lead_month'])
df3 = df3.sort_values(by=['date','lead_month'])
df4 = df4.sort_values(by=['date','lead_month'])
df5 = df5.sort_values(by=['date','lead_month'])
 
 
#Extracting Lead Month Rows
LM1MOdf = df1[df1['lead_month'] == 1]
LM2MOdf = df1[df1['lead_month'] == 2]
LM3MOdf = df1[df1['lead_month'] == 3]
LM4MOdf = df1[df1['lead_month'] == 4]
LM5MOdf = df1[df1['lead_month'] == 5]
LM6MOdf = df1[df1['lead_month'] == 6]
 
LM1EMdf = df2[df2['lead_month'] == 1]
LM2EMdf = df2[df2['lead_month'] == 2]
LM3EMdf = df2[df2['lead_month'] == 3]
LM4EMdf = df2[df2['lead_month'] == 4]
LM5EMdf = df2[df2['lead_month'] == 5]
LM6EMdf = df2[df2['lead_month'] == 6]
 
LM1ECdf = df3[df3['lead_month'] == 1]
LM2ECdf = df3[df3['lead_month'] == 2]
LM3ECdf = df3[df3['lead_month'] == 3]
LM4ECdf = df3[df3['lead_month'] == 4]
LM5ECdf = df3[df3['lead_month'] == 5]
LM6ECdf = df3[df3['lead_month'] == 6]
 
LM1MFdf = df4[df4['lead_month'] == 1]
LM2MFdf = df4[df4['lead_month'] == 2]
LM3MFdf = df4[df4['lead_month'] == 3]
LM4MFdf = df4[df4['lead_month'] == 4]
LM5MFdf = df4[df4['lead_month'] == 5]
LM6MFdf = df4[df4['lead_month'] == 6]
 
LM1CMdf = df5[df5['lead_month'] == 1]
LM2CMdf = df5[df5['lead_month'] == 2]
LM3CMdf = df5[df5['lead_month'] == 3]
LM4CMdf = df5[df5['lead_month'] == 4]
LM5CMdf = df5[df5['lead_month'] == 5]
LM6CMdf = df5[df5['lead_month'] == 6]
 
 
 
LM1MO = LM1MOdf[['date','lead_month','anomaly']].copy()
LM1MO = LM1MO.groupby('date', as_index=False).mean(numeric_only=True)
LM1MO['model']='UKMetOffice'
LM2MO = LM2MOdf[['date','lead_month','anomaly']].copy()
LM2MO = LM2MO.groupby('date', as_index=False).mean(numeric_only=True)
LM2MO['model']='UKMetOffice'
LM3MO = LM3MOdf[['date','lead_month','anomaly']].copy()
LM3MO = LM3MO.groupby('date', as_index=False).mean(numeric_only=True)
LM3MO['model']='UKMetOffice'
LM4MO = LM4MOdf[['date','lead_month','anomaly']].copy()
LM4MO = LM4MO.groupby('date', as_index=False).mean(numeric_only=True)
LM4MO['model']='UKMetOffice'
LM5MO = LM5MOdf[['date','lead_month','anomaly']].copy()
LM5MO = LM5MO.groupby('date', as_index=False).mean(numeric_only=True)
LM5MO['model']='UKMetOffice'
LM6MO = LM6MOdf[['date','lead_month','anomaly']].copy()
LM6MO = LM6MO.groupby('date', as_index=False).mean(numeric_only=True)
LM6MO['model']='UKMetOffice'
 
LM1EM = LM1EMdf[['date','lead_month','anomaly']].copy()
LM1EM = LM1EM.groupby('date', as_index=False).mean(numeric_only=True)
LM1EM['model']='ECMWF'
LM2EM = LM2EMdf[['date','lead_month','anomaly']].copy()
LM2EM = LM2EM.groupby('date', as_index=False).mean(numeric_only=True)
LM2EM['model']='ECMWF'
LM3EM = LM3EMdf[['date','lead_month','anomaly']].copy()
LM3EM = LM3EM.groupby('date', as_index=False).mean(numeric_only=True)
LM3EM['model']='ECMWF'
LM4EM = LM4EMdf[['date','lead_month','anomaly']].copy()
LM4EM = LM4EM.groupby('date', as_index=False).mean(numeric_only=True)
LM4EM['model']='ECMWF'
LM5EM = LM5EMdf[['date','lead_month','anomaly']].copy()
LM5EM = LM5EM.groupby('date', as_index=False).mean(numeric_only=True)
LM5EM['model']='ECMWF'
LM6EM = LM6EMdf[['date','lead_month','anomaly']].copy()
LM6EM = LM6EM.groupby('date', as_index=False).mean(numeric_only=True)
LM6EM['model']='ECMWF'
 
LM1EC = LM1ECdf[['date','lead_month','anomaly']].copy()
LM1EC = LM1EC.groupby('date', as_index=False).mean(numeric_only=True)
LM1EC['model']='ECCC'
LM2EC = LM2ECdf[['date','lead_month','anomaly']].copy()
LM2EC = LM2EC.groupby('date', as_index=False).mean(numeric_only=True)
LM2EC['model']='ECCC'
LM3EC = LM3ECdf[['date','lead_month','anomaly']].copy()
LM3EC = LM3EC.groupby('date', as_index=False).mean(numeric_only=True)
LM3EC['model']='ECCC'
LM4EC = LM4ECdf[['date','lead_month','anomaly']].copy()
LM4EC = LM4EC.groupby('date', as_index=False).mean(numeric_only=True)
LM4EC['model']='ECCC'
LM5EC = LM5ECdf[['date','lead_month','anomaly']].copy()
LM5EC = LM5EC.groupby('date', as_index=False).mean(numeric_only=True)
LM5EC['model']='ECCC'
LM6EC = LM6ECdf[['date','lead_month','anomaly']].copy()
LM6EC = LM6EC.groupby('date', as_index=False).mean(numeric_only=True)
LM6EC['model']='ECCC'
 
LM1MF = LM1MFdf[['date','lead_month','anomaly']].copy()
LM1MF = LM1MF.groupby('date', as_index=False).mean(numeric_only=True)
LM1MF['model']='MeteoFrance'
LM2MF = LM2MFdf[['date','lead_month','anomaly']].copy()
LM2MF = LM2MF.groupby('date', as_index=False).mean(numeric_only=True)
LM2MF['model']='MeteoFrance'
LM3MF = LM3MFdf[['date','lead_month','anomaly']].copy()
LM3MF = LM3MF.groupby('date', as_index=False).mean(numeric_only=True)
LM3MF['model']='MeteoFrance'
LM4MF = LM4MFdf[['date','lead_month','anomaly']].copy()
LM4MF = LM4MF.groupby('date', as_index=False).mean(numeric_only=True)
LM4MF['model']='MeteoFrance'
LM5MF = LM5MFdf[['date','lead_month','anomaly']].copy()
LM5MF = LM5MF.groupby('date', as_index=False).mean(numeric_only=True)
LM5MF['model']='MeteoFrance'
LM6MF = LM6MFdf[['date','lead_month','anomaly']].copy()
LM6MF = LM6MF.groupby('date', as_index=False).mean(numeric_only=True)
LM6MF['model']='MeteoFrance'
 
LM1CM = LM1CMdf[['date','lead_month','anomaly']].copy()
LM1CM = LM1CM.groupby('date', as_index=False).mean(numeric_only=True)
LM1CM['model']='CMCC'
LM2CM = LM2CMdf[['date','lead_month','anomaly']].copy()
LM2CM = LM2CM.groupby('date', as_index=False).mean(numeric_only=True)
LM2CM['model']='CMCC'
LM3CM = LM3CMdf[['date','lead_month','anomaly']].copy()
LM3CM = LM3CM.groupby('date', as_index=False).mean(numeric_only=True)
LM3CM['model']='CMCC'
LM4CM = LM4CMdf[['date','lead_month','anomaly']].copy()
LM4CM = LM4CM.groupby('date', as_index=False).mean(numeric_only=True)
LM4CM['model']='CMCC'
LM5CM = LM5CMdf[['date','lead_month','anomaly']].copy()
LM5CM = LM5CM.groupby('date', as_index=False).mean(numeric_only=True)
LM5CM['model']='CMCC'
LM6CM = LM6CMdf[['date','lead_month','anomaly']].copy()
LM6CM = LM6CM.groupby('date', as_index=False).mean(numeric_only=True)
LM6CM['model']='CMCC'
 
ERA5df = dfE[['date','anomaly']].copy()
ERA5df = ERA5df.groupby('date', as_index=False).mean(numeric_only=True)
ERA5df['model']='ERA5'
ERA5df['lead_month']='0'
 
 
twLM1=pd.concat([LM1MO,LM1EM,LM1EC,LM1MF,LM1CM])
twLM1['date'] = pd.to_datetime(twLM1['date']).dt.date
twLM1.reset_index(drop=True,inplace=True)
 
twLM2=pd.concat([LM2MO,LM2EM,LM2EC,LM2MF,LM2CM])
twLM2['date'] = pd.to_datetime(twLM2['date']).dt.date
twLM2.reset_index(drop=True,inplace=True)
 
twLM3=pd.concat([LM3MO,LM3EM,LM3EC,LM3MF,LM3CM])
twLM3['date'] = pd.to_datetime(twLM3['date']).dt.date
twLM3.reset_index(drop=True,inplace=True)
 
twLM4=pd.concat([LM4MO,LM4EM,LM4EC,LM4MF,LM4CM])
twLM4['date'] = pd.to_datetime(twLM4['date']).dt.date
twLM4.reset_index(drop=True,inplace=True)
 
twLM5=pd.concat([LM5MO,LM5EM,LM5EC,LM5MF,LM5CM])
twLM5['date'] = pd.to_datetime(twLM5['date']).dt.date
twLM5.reset_index(drop=True,inplace=True)
 
twLM6=pd.concat([LM6MO,LM6EM,LM6EC,LM6MF,LM6CM])
twLM6['date'] = pd.to_datetime(twLM6['date']).dt.date
twLM6.reset_index(drop=True,inplace=True)
 
 
 
TWlms=pd.concat([ERA5df,twLM1,twLM2,twLM3,twLM4,twLM5,twLM6])
TWlms['date'] = pd.to_datetime(TWlms['date']).dt.date
TWlms.reset_index(drop=True,inplace=True)
 
TWlms['lead_month'] = pd.to_numeric(TWlms['lead_month'], downcast='integer', errors='coerce')
 
TWlms['date'] = pd.to_datetime(TWlms['date'], errors='coerce')
TWlms['date'] = TWlms['date'].dt.to_period('M')
 
 
# Save to CSV
TWlms.to_csv("TWlms.csv", index=False)
 
 
# %%
'''Heatmaps'''
 
import seaborn as sns
import pandas as pd
 
 
#SSTlms["plot_date"] = SSTlms.apply(
	#lambda r: r["date"] - pd.DateOffset(months=r["lead_month"]),
	#axis=1)
 
#SSTlms['plot_date'] = pd.to_datetime(SSTlms['plot_date']).dt.date
 
 
heatmap_data = TWlms.pivot(
	index=['lead_month', 'model'],
	columns="date",
	values="anomaly"
).sort_index(ascending=False)
 
 
#plt.style.use("dark_background")
plt.figure(figsize=(40, 20))
 
 
sns.heatmap(
	heatmap_data,
	cmap='RdBu_r',  	# good for anomalies
	center=0,       	# zero-centered color scale
	annot=False,
	xticklabels=True,
	yticklabels=True,
	vmax=5,
	vmin=-5,
	cbar_kws={'label': 'Trade Winds Anomaly (m/s)'},
)
 
 
sns.set_style("whitegrid")
plt.tick_params(left=True, bottom=True)
 
cbar = plt.gca().collections[0].colorbar
cbar.ax.tick_params(labelsize=30)
cbar.set_label("Trade Winds Anomaly (m/s)", fontsize=30, weight="bold")
 
plt.xlabel('Date', fontsize=35, fontweight='bold')
plt.xticks(rotation=70, fontsize=30, horizontalalignment='center')
plt.ylabel('Month Leadtime - Model Centre', fontsize=35, fontweight='bold')
plt.yticks(fontsize=30)
 
#plt.title('Trade Winds Anomaly (10°N - 20°N, 70°W - 40°W)', fontsize=50, fontweight='bold')
 
 
#plt.tight_layout()
plt.show()

