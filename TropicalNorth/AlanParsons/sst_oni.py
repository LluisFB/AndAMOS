# -*- coding: utf-8 -*-
# Alan Parson's code
"""
Created on Tue Jul 14 13:48:38 2026
 
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
 
 
# Load NetCDF file
dsh1 = xr.open_dataset("C:/Users/amich/SURE/Python/UKMetO_ONI_HIND_1ML.nc", engine='netcdf4')
ds1 = xr.open_dataset("C:/Users/amich/SURE/Python/UKMetO_ONI_FORE_MLs.nc", engine='netcdf4')
 
dsh2 = xr.open_dataset("C:/Users/amich/SURE/Python/ECMWF_ONI_HIND_1ML.nc", engine='netcdf4')
ds2 = xr.open_dataset("C:/Users/amich/SURE/Python/ECMWF_ONI_FORE_MLs.nc", engine='netcdf4')
 
dsh3 = xr.open_dataset("C:/Users/amich/SURE/Python/ECCC_ONI_HIND_1ML.nc", engine='netcdf4')
ds3 = xr.open_dataset("C:/Users/amich/SURE/Python/ECCC_ONI_FORE_MLs.nc", engine='netcdf4')
 
dsh4 = xr.open_dataset("C:/Users/amich/SURE/Python/MF_ONI_HIND_1ML.nc", engine='netcdf4')
ds4 = xr.open_dataset("C:/Users/amich/SURE/Python/MF_ONI_FORE_MLs.nc", engine='netcdf4')
 
dsh5 = xr.open_dataset("C:/Users/amich/SURE/Python/CMCC_ONI_HIND_1ML.nc", engine='netcdf4')
ds5 = xr.open_dataset("C:/Users/amich/SURE/Python/CMCC_ONI_FORE_MLs.nc", engine='netcdf4')
 
dshE = xr.open_dataset("C:/Users/amich/SURE/Python/ERA5_ONI_HIND_1ML.nc", engine='netcdf4')
dsE = xr.open_dataset("C:/Users/amich/SURE/Python/ERA5_ONI_FORE_MLs.nc", engine='netcdf4')
 
 
# Convert to DataFrame
dfh1 = dsh1.to_dataframe().reset_index()
df1 = ds1.to_dataframe().reset_index()
 
dfh2 = dsh2.to_dataframe().reset_index()
df2 = ds2.to_dataframe().reset_index()
 
dfh3 = dsh3.to_dataframe().reset_index()
df3 = ds3.to_dataframe().reset_index()
 
dfh4 = dsh4.to_dataframe().reset_index()
df4 = ds4.to_dataframe().reset_index()
 
dfh5 = dsh5.to_dataframe().reset_index()
df5 = ds5.to_dataframe().reset_index()
 
dfhE = dshE.to_dataframe().reset_index()
dfE = dsE.to_dataframe().reset_index()
 
 
#Renaming Columns
dfh1.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat'}, inplace=True)
df1.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat'}, inplace=True)
 
dfh2.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat'}, inplace=True)
df2.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat'}, inplace=True)
 
dfh3.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat'}, inplace=True)
df3.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat'}, inplace=True)
 
dfh4.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat'}, inplace=True)
df4.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat'}, inplace=True)
 
dfh5.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat'}, inplace=True)
df5.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat'}, inplace=True)
 
dfhE.rename(columns={'valid_time':'date','indexing_time':'date','longitude':'long','latitude':'lat'}, inplace=True)
dfE.rename(columns={'valid_time':'date','indexing_time':'date','longitude':'long','latitude':'lat'}, inplace=True)
 
 
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
 
 
#Convert to Celsius from Kelvin
df1['sst'] = df1['sst']-273
dfh1['sst'] = dfh1['sst']-273
 
df2['sst'] = df2['sst']-273
dfh2['sst'] = dfh2['sst']-273
 
df3['sst'] = df3['sst']-273
dfh3['sst'] = dfh3['sst']-273
 
df4['sst'] = df4['sst']-273
dfh4['sst'] = dfh4['sst']-273
 
df5['sst'] = df5['sst']-273
dfh5['sst'] = dfh5['sst']-273
 
dfE['sst'] = dfE['sst']-273
dfhE['sst'] = dfhE['sst']-273
 
#Find mean of chosen paramater by Date and Lead Month
f_mean_sst=df1.groupby(['date','lead_month'])['sst'].transform('mean')
df1['monthly_mean_sst'] = f_mean_sst
h_mean_sst=dfh1.groupby(['date','lead_month'])['sst'].transform('mean')
dfh1['monthly_mean_sst'] = h_mean_sst
 
f_mean_sst=df2.groupby(['date','lead_month'])['sst'].transform('mean')
df2['monthly_mean_sst'] = f_mean_sst
h_mean_sst=dfh2.groupby(['date','lead_month'])['sst'].transform('mean')
dfh2['monthly_mean_sst'] = h_mean_sst
 
f_mean_sst=df3.groupby(['date','lead_month'])['sst'].transform('mean')
df3['monthly_mean_sst'] = f_mean_sst
h_mean_sst=dfh3.groupby(['date','lead_month'])['sst'].transform('mean')
dfh3['monthly_mean_sst'] = h_mean_sst
 
f_mean_sst=df4.groupby(['date','lead_month'])['sst'].transform('mean')
df4['monthly_mean_sst'] = f_mean_sst
h_mean_sst=dfh4.groupby(['date','lead_month'])['sst'].transform('mean')
dfh4['monthly_mean_sst'] = h_mean_sst
 
f_mean_sst=df5.groupby(['date','lead_month'])['sst'].transform('mean')
df5['monthly_mean_sst'] = f_mean_sst
h_mean_sst=dfh5.groupby(['date','lead_month'])['sst'].transform('mean')
dfh5['monthly_mean_sst'] = h_mean_sst
 
f_mean_sst=dfE.groupby(['date'])['sst'].transform('mean')
dfE['monthly_mean_sst'] = f_mean_sst
h_mean_sst=dfhE.groupby(['date'])['sst'].transform('mean')
dfhE['monthly_mean_sst'] = h_mean_sst
 
 
#Find mean of each unique month
df1['month'] = df1['date'].dt.month
dfh1['month'] = dfh1['date'].dt.month
h_uniq_mo_mean=dfh1.groupby('month')['monthly_mean_sst'].transform('mean')
dfh1['uniq_mo_mean']=h_uniq_mo_mean
 
df2['month'] = df2['date'].dt.month
dfh2['month'] = dfh2['date'].dt.month
h_uniq_mo_mean=dfh2.groupby('month')['monthly_mean_sst'].transform('mean')
dfh2['uniq_mo_mean']=h_uniq_mo_mean
 
df3['month'] = df3['date'].dt.month
dfh3['month'] = dfh3['date'].dt.month
h_uniq_mo_mean=dfh3.groupby('month')['monthly_mean_sst'].transform('mean')
dfh3['uniq_mo_mean']=h_uniq_mo_mean
 
df4['month'] = df4['date'].dt.month
dfh4['month'] = dfh4['date'].dt.month
h_uniq_mo_mean=dfh4.groupby('month')['monthly_mean_sst'].transform('mean')
dfh4['uniq_mo_mean']=h_uniq_mo_mean
 
df5['month'] = df5['date'].dt.month
dfh5['month'] = dfh5['date'].dt.month
h_uniq_mo_mean=dfh5.groupby('month')['monthly_mean_sst'].transform('mean')
dfh5['uniq_mo_mean']=h_uniq_mo_mean
 
dfE['month'] = dfE['date'].dt.month
dfhE['month'] = dfhE['date'].dt.month
h_uniq_mo_mean=dfhE.groupby('month')['monthly_mean_sst'].transform('mean')
dfhE['uniq_mo_mean']=h_uniq_mo_mean
 
 
#Climatology Monthly Means
month_means1=dfh1[['month','uniq_mo_mean']].copy()
month_means1=month_means1.groupby('month').mean('uniq_mo_mean')
 
month_means2=dfh2[['month','uniq_mo_mean']].copy()
month_means2=month_means2.groupby('month').mean('uniq_mo_mean')
 
month_means3=dfh3[['month','uniq_mo_mean']].copy()
month_means3=month_means3.groupby('month').mean('uniq_mo_mean')
 
month_means4=dfh4[['month','uniq_mo_mean']].copy()
month_means4=month_means4.groupby('month').mean('uniq_mo_mean')
 
month_means5=dfh5[['month','uniq_mo_mean']].copy()
month_means5=month_means5.groupby('month').mean('uniq_mo_mean')
 
month_meansE=dfhE[['month','uniq_mo_mean']].copy()
month_meansE=month_meansE.groupby('month').mean('uniq_mo_mean')
 
 
#Take Climatology away from Forecast
df1.groupby('month')
df1=df1.merge(month_means1, on='month',how='left')
df1['anomaly']=df1['monthly_mean_sst']-df1['uniq_mo_mean']
 
df2.groupby('month')
df2=df2.merge(month_means2, on='month',how='left')
df2['anomaly']=df2['monthly_mean_sst']-df2['uniq_mo_mean']
 
df3.groupby('month')
df3=df3.merge(month_means3, on='month',how='left')
df3['anomaly']=df3['monthly_mean_sst']-df3['uniq_mo_mean']
 
df4.groupby('month')
df4=df4.merge(month_means4, on='month',how='left')
df4['anomaly']=df4['monthly_mean_sst']-df4['uniq_mo_mean']
 
df5.groupby('month')
df5=df5.merge(month_means5, on='month',how='left')
df5['anomaly']=df5['monthly_mean_sst']-df5['uniq_mo_mean']
 
dfE.groupby('month')
dfE=dfE.merge(month_meansE, on='month',how='left')
dfE['anomaly']=dfE['monthly_mean_sst']-dfE['uniq_mo_mean']
 
 
#%%
'''Z-Scores Prep'''
 
MO = df1[['date','month','lead_month','anomaly']].copy()
MO = MO.groupby(['date','lead_month'], as_index=False).mean(numeric_only=True)
 
EU = df2[['date','month','lead_month','anomaly']].copy()
EU = EU.groupby(['date','lead_month'], as_index=False).mean(numeric_only=True)
 
EC = df3[['date','month','lead_month','anomaly']].copy()
EC = EC.groupby(['date','lead_month'], as_index=False).mean(numeric_only=True)
 
MF = df4[['date','month','lead_month','anomaly']].copy()
MF = MF.groupby(['date','lead_month'], as_index=False).mean(numeric_only=True)
 
CM = df5[['date','month','lead_month','anomaly']].copy()
CM = CM.groupby(['date','lead_month'], as_index=False).mean(numeric_only=True)
 
E = dfE[['date','month','anomaly']].copy()
E = E.groupby('date', as_index=False).mean(numeric_only=True)
 
 
'''Standardise/Z-Scores'''
 
MO['sd']=np.std(df1['sst'])
MO['z_score']=MO['anomaly']/MO['sd']
 
EU['sd']=np.std(df2['sst'])
EU['z_score']=EU['anomaly']/EU['sd']
 
EC['sd']=np.std(df3['sst'])
EC['z_score']=EC['anomaly']/EC['sd']
 
MF['sd']=np.std(df4['sst'])
MF['z_score']=MF['anomaly']/MF['sd']
 
CM['sd']=np.std(df5['sst'])
CM['z_score']=CM['anomaly']/CM['sd']
 
E['sd']=np.std(dfE['sst'])
E['z_score']=E['anomaly']/E['sd']
 
 
'''Rolling 3 month avg'''
 
MO['rolling_z']=MO['z_score'].rolling(window=3,center=True).mean()	
#ERA5df.insert(0,'mon',['DJF 2023','JFM 2023','FMA 2023','MAM 2023','AMJ 2023','MJJ 2023','JJA 2023','JAS 2023','ASO 2023','SON 2023','OND 2023','NDJ 2023','DJF 2024','JFM 2024','FMA 2024','MAM 2024','AMJ 2024','MJJ 2024','JJA 2024','JAS 2024','ASO 2024','SON 2024','OND 2024','NDJ 2024'])
MO['year']=MO['date'].dt.year
 
EU['rolling_z']=EU['z_score'].rolling(window=3,center=True).mean()	
#ERA5df.insert(0,'mon',['DJF 2023','JFM 2023','FMA 2023','MAM 2023','AMJ 2023','MJJ 2023','JJA 2023','JAS 2023','ASO 2023','SON 2023','OND 2023','NDJ 2023','DJF 2024','JFM 2024','FMA 2024','MAM 2024','AMJ 2024','MJJ 2024','JJA 2024','JAS 2024','ASO 2024','SON 2024','OND 2024','NDJ 2024'])
EU['year']=EU['date'].dt.year
 
EC['rolling_z']=EC['z_score'].rolling(window=3,center=True).mean()	
#ERA5df.insert(0,'mon',['DJF 2023','JFM 2023','FMA 2023','MAM 2023','AMJ 2023','MJJ 2023','JJA 2023','JAS 2023','ASO 2023','SON 2023','OND 2023','NDJ 2023','DJF 2024','JFM 2024','FMA 2024','MAM 2024','AMJ 2024','MJJ 2024','JJA 2024','JAS 2024','ASO 2024','SON 2024','OND 2024','NDJ 2024'])
EC['year']=EC['date'].dt.year
 
MF['rolling_z']=MF['z_score'].rolling(window=3,center=True).mean()	
#ERA5df.insert(0,'mon',['DJF 2023','JFM 2023','FMA 2023','MAM 2023','AMJ 2023','MJJ 2023','JJA 2023','JAS 2023','ASO 2023','SON 2023','OND 2023','NDJ 2023','DJF 2024','JFM 2024','FMA 2024','MAM 2024','AMJ 2024','MJJ 2024','JJA 2024','JAS 2024','ASO 2024','SON 2024','OND 2024','NDJ 2024'])
MF['year']=MF['date'].dt.year
 
CM['rolling_z']=CM['z_score'].rolling(window=3,center=True).mean()	
#ERA5df.insert(0,'mon',['DJF 2023','JFM 2023','FMA 2023','MAM 2023','AMJ 2023','MJJ 2023','JJA 2023','JAS 2023','ASO 2023','SON 2023','OND 2023','NDJ 2023','DJF 2024','JFM 2024','FMA 2024','MAM 2024','AMJ 2024','MJJ 2024','JJA 2024','JAS 2024','ASO 2024','SON 2024','OND 2024','NDJ 2024'])
CM['year']=CM['date'].dt.year
 
E['rolling_z']=E['z_score'].rolling(window=3,center=True).mean()	
#ERA5df.insert(0,'mon',['DJF 2023','JFM 2023','FMA 2023','MAM 2023','AMJ 2023','MJJ 2023','JJA 2023','JAS 2023','ASO 2023','SON 2023','OND 2023','NDJ 2023','DJF 2024','JFM 2024','FMA 2024','MAM 2024','AMJ 2024','MJJ 2024','JJA 2024','JAS 2024','ASO 2024','SON 2024','OND 2024','NDJ 2024'])
E['year']=E['date'].dt.year
 
 
#%%
 
#Sorting
MO = MO.sort_values(by=['date','lead_month'])
EU = EU.sort_values(by=['date','lead_month'])
EC = EC.sort_values(by=['date','lead_month'])
MF = MF.sort_values(by=['date','lead_month'])
CM = CM.sort_values(by=['date','lead_month'])
 
#Extracting Lead Month Rows
LM1MOdf = MO[MO['lead_month'] == 1]
LM2MOdf = MO[MO['lead_month'] == 2]
LM3MOdf = MO[MO['lead_month'] == 3]
LM4MOdf = MO[MO['lead_month'] == 4]
LM5MOdf = MO[MO['lead_month'] == 5]
LM6MOdf = MO[MO['lead_month'] == 6]
 
LM1EUdf = EU[EU['lead_month'] == 1]
LM2EUdf = EU[EU['lead_month'] == 2]
LM3EUdf = EU[EU['lead_month'] == 3]
LM4EUdf = EU[EU['lead_month'] == 4]
LM5EUdf = EU[EU['lead_month'] == 5]
LM6EUdf = EU[EU['lead_month'] == 6]
 
LM1ECdf = EC[EC['lead_month'] == 1]
LM2ECdf = EC[EC['lead_month'] == 2]
LM3ECdf = EC[EC['lead_month'] == 3]
LM4ECdf = EC[EC['lead_month'] == 4]
LM5ECdf = EC[EC['lead_month'] == 5]
LM6ECdf = EC[EC['lead_month'] == 6]
 
LM1MFdf = MF[MF['lead_month'] == 1]
LM2MFdf = MF[MF['lead_month'] == 2]
LM3MFdf = MF[MF['lead_month'] == 3]
LM4MFdf = MF[MF['lead_month'] == 4]
LM5MFdf = MF[MF['lead_month'] == 5]
LM6MFdf = MF[MF['lead_month'] == 6]
 
LM1CMdf = CM[CM['lead_month'] == 1]
LM2CMdf = CM[CM['lead_month'] == 2]
LM3CMdf = CM[CM['lead_month'] == 3]
LM4CMdf = CM[CM['lead_month'] == 4]
LM5CMdf = CM[CM['lead_month'] == 5]
LM6CMdf = CM[CM['lead_month'] == 6]
 
 
LM1MO = LM1MOdf[['date','lead_month','rolling_z']].copy()
LM1MO = LM1MO.groupby('date', as_index=False).mean(numeric_only=True)
LM1MO['model']='UKMetOffice'
LM2MO = LM2MOdf[['date','lead_month','rolling_z']].copy()
LM2MO = LM2MO.groupby('date', as_index=False).mean(numeric_only=True)
LM2MO['model']='UKMetOffice'
LM3MO = LM3MOdf[['date','lead_month','rolling_z']].copy()
LM3MO = LM3MO.groupby('date', as_index=False).mean(numeric_only=True)
LM3MO['model']='UKMetOffice'
LM4MO = LM4MOdf[['date','lead_month','rolling_z']].copy()
LM4MO = LM4MO.groupby('date', as_index=False).mean(numeric_only=True)
LM4MO['model']='UKMetOffice'
LM5MO = LM5MOdf[['date','lead_month','rolling_z']].copy()
LM5MO = LM5MO.groupby('date', as_index=False).mean(numeric_only=True)
LM5MO['model']='UKMetOffice'
LM6MO = LM6MOdf[['date','lead_month','rolling_z']].copy()
LM6MO = LM6MO.groupby('date', as_index=False).mean(numeric_only=True)
LM6MO['model']='UKMetOffice'
 
LM1EU = LM1EUdf[['date','lead_month','rolling_z']].copy()
LM1EU = LM1EU.groupby('date', as_index=False).mean(numeric_only=True)
LM1EU['model']='ECMWF'
LM2EU = LM2EUdf[['date','lead_month','rolling_z']].copy()
LM2EU = LM2EU.groupby('date', as_index=False).mean(numeric_only=True)
LM2EU['model']='ECMWF'
LM3EU = LM3EUdf[['date','lead_month','rolling_z']].copy()
LM3EU = LM3EU.groupby('date', as_index=False).mean(numeric_only=True)
LM3EU['model']='ECMWF'
LM4EU = LM4EUdf[['date','lead_month','rolling_z']].copy()
LM4EU = LM4EU.groupby('date', as_index=False).mean(numeric_only=True)
LM4EU['model']='ECMWF'
LM5EU = LM5EUdf[['date','lead_month','rolling_z']].copy()
LM5EU = LM5EU.groupby('date', as_index=False).mean(numeric_only=True)
LM5EU['model']='ECMWF'
LM6EU = LM6EUdf[['date','lead_month','rolling_z']].copy()
LM6EU = LM6EU.groupby('date', as_index=False).mean(numeric_only=True)
LM6EU['model']='ECMWF'
 
LM1EC = LM1ECdf[['date','lead_month','rolling_z']].copy()
LM1EC = LM1EC.groupby('date', as_index=False).mean(numeric_only=True)
LM1EC['model']='ECCC'
LM2EC = LM2ECdf[['date','lead_month','rolling_z']].copy()
LM2EC = LM2EC.groupby('date', as_index=False).mean(numeric_only=True)
LM2EC['model']='ECCC'
LM3EC = LM3ECdf[['date','lead_month','rolling_z']].copy()
LM3EC = LM3EC.groupby('date', as_index=False).mean(numeric_only=True)
LM3EC['model']='ECCC'
LM4EC = LM4ECdf[['date','lead_month','rolling_z']].copy()
LM4EC = LM4EC.groupby('date', as_index=False).mean(numeric_only=True)
LM4EC['model']='ECCC'
LM5EC = LM5ECdf[['date','lead_month','rolling_z']].copy()
LM5EC = LM5EC.groupby('date', as_index=False).mean(numeric_only=True)
LM5EC['model']='ECCC'
LM6EC = LM6ECdf[['date','lead_month','rolling_z']].copy()
LM6EC = LM6EC.groupby('date', as_index=False).mean(numeric_only=True)
LM6EC['model']='ECCC'
 
LM1MF = LM1MFdf[['date','lead_month','rolling_z']].copy()
LM1MF = LM1MF.groupby('date', as_index=False).mean(numeric_only=True)
LM1MF['model']='MeteoFrance'
LM2MF = LM2MFdf[['date','lead_month','rolling_z']].copy()
LM2MF = LM2MF.groupby('date', as_index=False).mean(numeric_only=True)
LM2MF['model']='MeteoFrance'
LM3MF = LM3MFdf[['date','lead_month','rolling_z']].copy()
LM3MF = LM3MF.groupby('date', as_index=False).mean(numeric_only=True)
LM3MF['model']='MeteoFrance'
LM4MF = LM4MFdf[['date','lead_month','rolling_z']].copy()
LM4MF = LM4MF.groupby('date', as_index=False).mean(numeric_only=True)
LM4MF['model']='MeteoFrance'
LM5MF = LM5MFdf[['date','lead_month','rolling_z']].copy()
LM5MF = LM5MF.groupby('date', as_index=False).mean(numeric_only=True)
LM5MF['model']='MeteoFrance'
LM6MF = LM6MFdf[['date','lead_month','rolling_z']].copy()
LM6MF = LM6MF.groupby('date', as_index=False).mean(numeric_only=True)
LM6MF['model']='MeteoFrance'
 
LM1CM = LM1CMdf[['date','lead_month','rolling_z']].copy()
LM1CM = LM1CM.groupby('date', as_index=False).mean(numeric_only=True)
LM1CM['model']='CMCC'
LM2CM = LM2CMdf[['date','lead_month','rolling_z']].copy()
LM2CM = LM2CM.groupby('date', as_index=False).mean(numeric_only=True)
LM2CM['model']='CMCC'
LM3CM = LM3CMdf[['date','lead_month','rolling_z']].copy()
LM3CM = LM3CM.groupby('date', as_index=False).mean(numeric_only=True)
LM3CM['model']='CMCC'
LM4CM = LM4CMdf[['date','lead_month','rolling_z']].copy()
LM4CM = LM4CM.groupby('date', as_index=False).mean(numeric_only=True)
LM4CM['model']='CMCC'
LM5CM = LM5CMdf[['date','lead_month','rolling_z']].copy()
LM5CM = LM5CM.groupby('date', as_index=False).mean(numeric_only=True)
LM5CM['model']='CMCC'
LM6CM = LM6CMdf[['date','lead_month','rolling_z']].copy()
LM6CM = LM6CM.groupby('date', as_index=False).mean(numeric_only=True)
LM6CM['model']='CMCC'
 
 
ERA5df = E[['date','rolling_z']].copy()
ERA5df = ERA5df.groupby('date', as_index=False).mean(numeric_only=True)
ERA5df['model']='ERA5'
ERA5df['lead_month']='0'
 
 
sstLM1=pd.concat([LM1MO,LM1EU,LM1EC,LM1MF,LM1CM])
sstLM1['date'] = pd.to_datetime(sstLM1['date']).dt.date
sstLM1.reset_index(drop=True,inplace=True)
 
sstLM2=pd.concat([LM2MO,LM2EU,LM2EC,LM2MF,LM2CM])
sstLM2['date'] = pd.to_datetime(sstLM2['date']).dt.date
sstLM2.reset_index(drop=True,inplace=True)
 
sstLM3=pd.concat([LM3MO,LM3EU,LM3EC,LM3MF,LM3CM])
sstLM3['date'] = pd.to_datetime(sstLM3['date']).dt.date
sstLM3.reset_index(drop=True,inplace=True)
 
sstLM4=pd.concat([LM4MO,LM4EU,LM4EC,LM4MF,LM4CM])
sstLM4['date'] = pd.to_datetime(sstLM4['date']).dt.date
sstLM4.reset_index(drop=True,inplace=True)
 
sstLM5=pd.concat([LM5MO,LM5EU,LM5EC,LM5MF,LM5CM])
sstLM5['date'] = pd.to_datetime(sstLM5['date']).dt.date
sstLM5.reset_index(drop=True,inplace=True)
 
sstLM6=pd.concat([LM6MO,LM6EU,LM6EC,LM6MF,LM6CM])
sstLM6['date'] = pd.to_datetime(sstLM6['date']).dt.date
sstLM6.reset_index(drop=True,inplace=True)
 
 
SSTlms=pd.concat([ERA5df,sstLM1,sstLM2,sstLM3,sstLM4,sstLM5,sstLM6])
SSTlms['date'] = pd.to_datetime(SSTlms['date']).dt.date
SSTlms.reset_index(drop=True,inplace=True)
 
SSTlms['lead_month'] = pd.to_numeric(SSTlms['lead_month'], downcast='integer', errors='coerce')
 
SSTlms['date'] = pd.to_datetime(SSTlms['date'], errors='coerce')
SSTlms['date'] = SSTlms['date'].dt.to_period('M')
 
 
# Save to CSV
SSTlms.to_csv("SSTlms.csv", index=False)
 
 
 
 
# %%
'''Heatmaps'''
 
import seaborn as sns
import pandas as pd
 
 
#SSTlms["plot_date"] = SSTlms.apply(
	#lambda r: r["date"] - pd.DateOffset(months=r["lead_month"]),
	#axis=1)
 
#SSTlms['plot_date'] = pd.to_datetime(SSTlms['plot_date']).dt.date
 
 
heatmap_data = SSTlms.pivot(
	index=['lead_month', 'model'],
	columns="date",
	values="rolling_z"
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
	vmax=3,
	vmin=-3,
	cbar_kws={'label': 'Sea Surface Temperature Anomaly (°C)'},
)
 
 
sns.set_style("whitegrid")
plt.tick_params(left=True, bottom=True)
 
cbar = plt.gca().collections[0].colorbar
cbar.ax.tick_params(labelsize=30)
cbar.set_label("SST 3-month Rolling Z-Score", fontsize=30, weight="bold")
 
plt.xlabel('Date', fontsize=35, fontweight='bold')
plt.xticks(rotation=70, fontsize=30, horizontalalignment='center')
plt.ylabel('Month Leadtime - Model Centre', fontsize=35, fontweight='bold')
plt.yticks(fontsize=30)
 
#plt.title('Sea Surface Temperature Anomaly (5°N – 5°S, 170°W - 120°W)', fontsize=50, fontweight='bold')
 
 
#plt.tight_layout()
plt.show()

