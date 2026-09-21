# Alan Parson's code
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
dsh1 = xr.open_dataset("C:/Users/amich/SURE/Python/UKMetO_SST_HIND_1ML.nc", engine='netcdf4')
ds1 = xr.open_dataset("C:/Users/amich/SURE/Python/UKMetO_SST_FORE_MLs.nc", engine='netcdf4')
 
dsh2 = xr.open_dataset("C:/Users/amich/SURE/Python/ECMWF_SST_HIND_1ML.nc", engine='netcdf4')
ds2 = xr.open_dataset("C:/Users/amich/SURE/Python/ECMWF_SST_FORE_MLs.nc", engine='netcdf4')
 
dsh3 = xr.open_dataset("C:/Users/amich/SURE/Python/ECCC_SST_HIND_1ML.nc", engine='netcdf4')
ds3 = xr.open_dataset("C:/Users/amich/SURE/Python/ECCC_SST_FORE_MLs.nc", engine='netcdf4')
 
dsh4 = xr.open_dataset("C:/Users/amich/SURE/Python/MF_SST_HIND_1ML.nc", engine='netcdf4')
ds4 = xr.open_dataset("C:/Users/amich/SURE/Python/MF_SST_FORE_MLs.nc", engine='netcdf4')
 
dsh5 = xr.open_dataset("C:/Users/amich/SURE/Python/CMCC_SST_HIND_1ML.nc", engine='netcdf4')
ds5 = xr.open_dataset("C:/Users/amich/SURE/Python/CMCC_SST_FORE_MLs.nc", engine='netcdf4')
 
dshE = xr.open_dataset("C:/Users/amich/SURE/Python/ERA5_SST_HIND.nc", engine='netcdf4')
dsE = xr.open_dataset("C:/Users/amich/SURE/Python/ERA5_SST_FORE.nc", engine='netcdf4')
 
 
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
 
 
#Find mean of each unique month in Climatology
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
	vmax=2,
	vmin=-2,
	cbar_kws={'label': 'Anomaly (°C)'},
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
 
#plt.title('Sea Surface Temperature Anomaly (5°N – 25°N, 60°W - 20°W)', fontsize=50, fontweight='bold')
 
 
#plt.tight_layout()
plt.show()

SST (ONI)

# -*- coding: utf-8 -*-
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

Land Sea Contrast

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 17:26:57 2025
 
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
MOdsHsea = xr.open_dataset("C:/Users/amich/SURE/Python/UKMetO_LSC_Sea_HIND_1ML.nc", engine='netcdf4')
MOdsFsea = xr.open_dataset("C:/Users/amich/SURE/Python/UKMetO_LSC_Sea_FORE_MLs.nc", engine='netcdf4')
MOdsHland = xr.open_dataset("C:/Users/amich/SURE/Python/UKMetO_LSC_Land_HIND_1ML.nc", engine='netcdf4')
MOdsFland = xr.open_dataset("C:/Users/amich/SURE/Python/UKMetO_LSC_Land_FORE_MLs.nc", engine='netcdf4')
 
EUdsHsea = xr.open_dataset("C:/Users/amich/SURE/Python/ECMWF_LSC_Sea_HIND_1ML.nc", engine='netcdf4')
EUdsFsea = xr.open_dataset("C:/Users/amich/SURE/Python/ECMWF_LSC_Sea_FORE_MLs.nc", engine='netcdf4')
EUdsHland = xr.open_dataset("C:/Users/amich/SURE/Python/ECMWF_LSC_Land_HIND_1ML.nc", engine='netcdf4')
EUdsFland = xr.open_dataset("C:/Users/amich/SURE/Python/ECMWF_LSC_Land_FORE_MLs.nc", engine='netcdf4')
 
ECdsHsea = xr.open_dataset("C:/Users/amich/SURE/Python/ECCC_LSC_Sea_HIND_1ML.nc", engine='netcdf4')
ECdsFsea = xr.open_dataset("C:/Users/amich/SURE/Python/ECCC_LSC_Sea_FORE_MLs.nc", engine='netcdf4')
ECdsHland = xr.open_dataset("C:/Users/amich/SURE/Python/ECCC_LSC_Land_HIND_1ML.nc", engine='netcdf4')
ECdsFland = xr.open_dataset("C:/Users/amich/SURE/Python/ECCC_LSC_Land_FORE_MLs.nc", engine='netcdf4')
 
MFdsHsea = xr.open_dataset("C:/Users/amich/SURE/Python/MF_LSC_Sea_HIND_1ML.nc", engine='netcdf4')
MFdsFsea = xr.open_dataset("C:/Users/amich/SURE/Python/MF_LSC_Sea_FORE_MLs.nc", engine='netcdf4')
MFdsHland = xr.open_dataset("C:/Users/amich/SURE/Python/MF_LSC_Land_HIND_1ML.nc", engine='netcdf4')
MFdsFland = xr.open_dataset("C:/Users/amich/SURE/Python/MF_LSC_Land_FORE_MLs.nc", engine='netcdf4')
 
CMdsHsea = xr.open_dataset("C:/Users/amich/SURE/Python/CMCC_LSC_Sea_HIND_1ML.nc", engine='netcdf4')
CMdsFsea = xr.open_dataset("C:/Users/amich/SURE/Python/CMCC_LSC_Sea_FORE_MLs.nc", engine='netcdf4')
CMdsHland = xr.open_dataset("C:/Users/amich/SURE/Python/CMCC_LSC_Land_HIND_1ML.nc", engine='netcdf4')
CMdsFland = xr.open_dataset("C:/Users/amich/SURE/Python/CMCC_LSC_Land_FORE_MLs.nc", engine='netcdf4')
 
E5dsHsea = xr.open_dataset("C:/Users/amich/SURE/Python/ERA5_LSC_Sea_HIND.nc", engine='netcdf4')
E5dsFsea = xr.open_dataset("C:/Users/amich/SURE/Python/ERA5_LSC_Sea_FORE.nc", engine='netcdf4')
E5dsHland = xr.open_dataset("C:/Users/amich/SURE/Python/ERA5_LSC_Land_HIND.nc", engine='netcdf4')
E5dsFland = xr.open_dataset("C:/Users/amich/SURE/Python/ERA5_LSC_Land_FORE.nc", engine='netcdf4')
 
 
# Convert to DataFrame
MOdfHsea = MOdsHsea.to_dataframe().reset_index()
MOdfFsea = MOdsFsea.to_dataframe().reset_index()
MOdfHland = MOdsHland.to_dataframe().reset_index()
MOdfFland = MOdsFland.to_dataframe().reset_index()
 
EUdfHsea = EUdsHsea.to_dataframe().reset_index()
EUdfFsea = EUdsFsea.to_dataframe().reset_index()
EUdfHland = EUdsHland.to_dataframe().reset_index()
EUdfFland = EUdsFland.to_dataframe().reset_index()
 
ECdfHsea = ECdsHsea.to_dataframe().reset_index()
ECdfFsea = ECdsFsea.to_dataframe().reset_index()
ECdfHland = ECdsHland.to_dataframe().reset_index()
ECdfFland = ECdsFland.to_dataframe().reset_index()
 
MFdfHsea = MFdsHsea.to_dataframe().reset_index()
MFdfFsea = MFdsFsea.to_dataframe().reset_index()
MFdfHland = MFdsHland.to_dataframe().reset_index()
MFdfFland = MFdsFland.to_dataframe().reset_index()
 
CMdfHsea = CMdsHsea.to_dataframe().reset_index()
CMdfFsea = CMdsFsea.to_dataframe().reset_index()
CMdfHland = CMdsHland.to_dataframe().reset_index()
CMdfFland = CMdsFland.to_dataframe().reset_index()
 
E5dfHsea = E5dsHsea.to_dataframe().reset_index()
E5dfFsea = E5dsFsea.to_dataframe().reset_index()
E5dfHland = E5dsHland.to_dataframe().reset_index()
E5dfFland = E5dsFland.to_dataframe().reset_index()
 
 
#Renaming Columns
MOdfHsea.rename(columns={'indexing_time':'date','forecast_reference_time':'date', 'forecastMonth':'lead_month','longitude':'long','latitude':'lat'}, inplace=True)
MOdfFsea.rename(columns={'forecast_reference_time':'date','forecastMonth':'lead_month', 'longitude':'long','latitude':'lat'}, inplace=True)
MOdfHland.rename(columns={'indexing_time':'date','forecast_reference_time':'date', 'forecastMonth':'lead_month','longitude':'long','latitude':'lat', 'stl1':'lst'}, inplace=True)
MOdfFland.rename(columns={'forecast_reference_time':'date','forecastMonth':'lead_month', 'longitude':'long','latitude':'lat', 'stl1':'lst'}, inplace=True)
 
EUdfHsea.rename(columns={'forecast_reference_time':'date', 'forecastMonth':'lead_month','longitude':'long','latitude':'lat'}, inplace=True)
EUdfFsea.rename(columns={'forecast_reference_time':'date','forecastMonth':'lead_month', 'longitude':'long','latitude':'lat'}, inplace=True)
EUdfHland.rename(columns={'forecast_reference_time':'date', 'forecastMonth':'lead_month','longitude':'long','latitude':'lat', 'stl1':'lst'}, inplace=True)
EUdfFland.rename(columns={'forecast_reference_time':'date','forecastMonth':'lead_month', 'longitude':'long','latitude':'lat', 'stl1':'lst'}, inplace=True)
 
ECdfHsea.rename(columns={'indexing_time':'date', 'forecast_reference_time':'date', 'forecastMonth':'lead_month','longitude':'long','latitude':'lat'}, inplace=True)
ECdfFsea.rename(columns={'forecast_reference_time':'date','forecastMonth':'lead_month', 'longitude':'long','latitude':'lat'}, inplace=True)
ECdfHland.rename(columns={'forecast_reference_time':'date', 'forecastMonth':'lead_month','longitude':'long','latitude':'lat', 'stl1':'lst'}, inplace=True)
ECdfFland.rename(columns={'forecast_reference_time':'date','forecastMonth':'lead_month', 'longitude':'long','latitude':'lat', 'stl1':'lst'}, inplace=True)
 
MFdfHsea.rename(columns={'forecast_reference_time':'date', 'forecastMonth':'lead_month','longitude':'long','latitude':'lat'}, inplace=True)
MFdfFsea.rename(columns={'forecast_reference_time':'date','forecastMonth':'lead_month', 'longitude':'long','latitude':'lat'}, inplace=True)
MFdfHland.rename(columns={'forecast_reference_time':'date', 'forecastMonth':'lead_month','longitude':'long','latitude':'lat', 'stl1':'lst'}, inplace=True)
MFdfFland.rename(columns={'forecast_reference_time':'date','forecastMonth':'lead_month', 'longitude':'long','latitude':'lat', 'stl1':'lst'}, inplace=True)
 
CMdfHsea.rename(columns={'forecast_reference_time':'date', 'forecastMonth':'lead_month','longitude':'long','latitude':'lat'}, inplace=True)
CMdfFsea.rename(columns={'forecast_reference_time':'date','forecastMonth':'lead_month', 'longitude':'long','latitude':'lat'}, inplace=True)
CMdfHland.rename(columns={'forecast_reference_time':'date', 'forecastMonth':'lead_month','longitude':'long','latitude':'lat', 'stl1':'lst'}, inplace=True)
CMdfFland.rename(columns={'forecast_reference_time':'date','forecastMonth':'lead_month', 'longitude':'long','latitude':'lat', 'stl1':'lst'}, inplace=True)
 
E5dfHsea.rename(columns={'valid_time':'date', 'forecastMonth':'lead_month','longitude':'long','latitude':'lat'}, inplace=True)
E5dfFsea.rename(columns={'valid_time':'date','forecastMonth':'lead_month', 'longitude':'long','latitude':'lat'}, inplace=True)
E5dfHland.rename(columns={'valid_time':'date', 'forecastMonth':'lead_month','longitude':'long','latitude':'lat', 'stl1':'lst'}, inplace=True)
E5dfFland.rename(columns={'valid_time':'date','forecastMonth':'lead_month', 'longitude':'long','latitude':'lat', 'stl1':'lst'}, inplace=True)
 
 
#Convert to datetime
MOdfFsea['date'] = pd.to_datetime(MOdfFsea['date'])
MOdfHsea['date'] = pd.to_datetime(MOdfHsea['date'])
MOdfFland['date'] = pd.to_datetime(MOdfFland['date'])
MOdfHland['date'] = pd.to_datetime(MOdfHland['date'])
 
EUdfFsea['date'] = pd.to_datetime(EUdfFsea['date'])
EUdfHsea['date'] = pd.to_datetime(EUdfHsea['date'])
EUdfFland['date'] = pd.to_datetime(EUdfFland['date'])
EUdfHland['date'] = pd.to_datetime(EUdfHland['date'])
 
ECdfFsea['date'] = pd.to_datetime(ECdfFsea['date'])
ECdfHsea['date'] = pd.to_datetime(ECdfHsea['date'])
ECdfFland['date'] = pd.to_datetime(ECdfFland['date'])
ECdfHland['date'] = pd.to_datetime(ECdfHland['date'])
 
MFdfFsea['date'] = pd.to_datetime(MFdfFsea['date'])
MFdfHsea['date'] = pd.to_datetime(MFdfHsea['date'])
MFdfFland['date'] = pd.to_datetime(MFdfFland['date'])
MFdfHland['date'] = pd.to_datetime(MFdfHland['date'])
 
CMdfFsea['date'] = pd.to_datetime(CMdfFsea['date'])
CMdfHsea['date'] = pd.to_datetime(CMdfHsea['date'])
CMdfFland['date'] = pd.to_datetime(CMdfFland['date'])
CMdfHland['date'] = pd.to_datetime(CMdfHland['date'])
 
E5dfFsea['date'] = pd.to_datetime(E5dfFsea['date'])
E5dfHsea['date'] = pd.to_datetime(E5dfHsea['date'])
E5dfFland['date'] = pd.to_datetime(E5dfFland['date'])
E5dfHland['date'] = pd.to_datetime(E5dfHland['date'])
 
 
#Convert from Kelvin to Celsius
MOdfFsea['sst'] = MOdfFsea['sst']-273
MOdfHsea['sst'] = MOdfHsea['sst']-273
MOdfFland['lst'] = MOdfFland['lst']-273
MOdfHland['lst'] = MOdfHland['lst']-273
 
EUdfFsea['sst'] = EUdfFsea['sst']-273
EUdfHsea['sst'] = EUdfHsea['sst']-273
EUdfFland['lst'] = EUdfFland['lst']-273
EUdfHland['lst'] = EUdfHland['lst']-273
 
ECdfFsea['sst'] = ECdfFsea['sst']-273
ECdfHsea['sst'] = ECdfHsea['sst']-273
ECdfFland['lst'] = ECdfFland['lst']-273
ECdfHland['lst'] = ECdfHland['lst']-273
 
MFdfFsea['sst'] = MFdfFsea['sst']-273
MFdfHsea['sst'] = MFdfHsea['sst']-273
MFdfFland['lst'] = MFdfFland['lst']-273
MFdfHland['lst'] = MFdfHland['lst']-273
 
CMdfFsea['sst'] = CMdfFsea['sst']-273
CMdfHsea['sst'] = CMdfHsea['sst']-273
CMdfFland['lst'] = CMdfFland['lst']-273
CMdfHland['lst'] = CMdfHland['lst']-273
 
E5dfFsea['sst'] = E5dfFsea['sst']-273
E5dfHsea['sst'] = E5dfHsea['sst']-273
E5dfFland['lst'] = E5dfFland['lst']-273
E5dfHland['lst'] = E5dfHland['lst']-273
 
 
#Month Number
MOdfFsea['month'] = MOdfFsea['date'].dt.month
MOdfHsea['month'] = MOdfHsea['date'].dt.month
MOdfFland['month'] = MOdfFland['date'].dt.month
MOdfHland['month'] = MOdfHland['date'].dt.month
 
EUdfFsea['month'] = EUdfFsea['date'].dt.month
EUdfHsea['month'] = EUdfHsea['date'].dt.month
EUdfFland['month'] = EUdfFland['date'].dt.month
EUdfHland['month'] = EUdfHland['date'].dt.month
 
ECdfFsea['month'] = ECdfFsea['date'].dt.month
ECdfHsea['month'] = ECdfHsea['date'].dt.month
ECdfFland['month'] = ECdfFland['date'].dt.month
ECdfHland['month'] = ECdfHland['date'].dt.month
 
MFdfFsea['month'] = MFdfFsea['date'].dt.month
MFdfHsea['month'] = MFdfHsea['date'].dt.month
MFdfFland['month'] = MFdfFland['date'].dt.month
MFdfHland['month'] = MFdfHland['date'].dt.month
 
CMdfFsea['month'] = CMdfFsea['date'].dt.month
CMdfHsea['month'] = CMdfHsea['date'].dt.month
CMdfFland['month'] = CMdfFland['date'].dt.month
CMdfHland['month'] = CMdfHland['date'].dt.month
 
E5dfFsea['month'] = E5dfFsea['date'].dt.month
E5dfHsea['month'] = E5dfHsea['date'].dt.month
E5dfFland['month'] = E5dfFland['date'].dt.month
E5dfHland['month'] = E5dfHland['date'].dt.month
 
 
#Find mean of each parameter
#Hind Sea
MO_h_mean_sst=MOdfHsea.groupby('date')['sst'].transform('mean')
MOdfHsea['h_monthly_mean_sst'] = MO_h_mean_sst
MO_h_mean_sst=MOdfHsea[['month','h_monthly_mean_sst']].copy()
MO_h_mean_sst=MO_h_mean_sst.groupby('month').mean('h_monthly_mean_sst')
 
EU_h_mean_sst=EUdfHsea.groupby('date')['sst'].transform('mean')
EUdfHsea['h_monthly_mean_sst'] = EU_h_mean_sst
EU_h_mean_sst=EUdfHsea[['month','h_monthly_mean_sst']].copy()
EU_h_mean_sst=EU_h_mean_sst.groupby('month').mean('h_monthly_mean_sst')
 
EC_h_mean_sst=ECdfHsea.groupby('date')['sst'].transform('mean')
ECdfHsea['h_monthly_mean_sst'] = EC_h_mean_sst
EC_h_mean_sst=ECdfHsea[['month','h_monthly_mean_sst']].copy()
EC_h_mean_sst=EC_h_mean_sst.groupby('month').mean('h_monthly_mean_sst')
 
MF_h_mean_sst=MFdfHsea.groupby('date')['sst'].transform('mean')
MFdfHsea['h_monthly_mean_sst'] = MF_h_mean_sst
MF_h_mean_sst=MFdfHsea[['month','h_monthly_mean_sst']].copy()
MF_h_mean_sst=MF_h_mean_sst.groupby('month').mean('h_monthly_mean_sst')
 
CM_h_mean_sst=CMdfHsea.groupby('date')['sst'].transform('mean')
CMdfHsea['h_monthly_mean_sst'] = CM_h_mean_sst
CM_h_mean_sst=CMdfHsea[['month','h_monthly_mean_sst']].copy()
CM_h_mean_sst=CM_h_mean_sst.groupby('month').mean('h_monthly_mean_sst')
 
E5_h_mean_sst=E5dfHsea.groupby('date')['sst'].transform('mean')
E5dfHsea['h_monthly_mean_sst'] = E5_h_mean_sst
E5_h_mean_sst=E5dfHsea[['month','h_monthly_mean_sst']].copy()
E5_h_mean_sst=E5_h_mean_sst.groupby('month').mean('h_monthly_mean_sst')
 
 
#Hind Land
MO_h_mean_lst=MOdfHland.groupby('date',)['lst'].transform('mean')
MOdfHland['h_monthly_mean_lst'] = MO_h_mean_lst
MO_h_mean_lst=MOdfHland[['month','h_monthly_mean_lst']].copy()
MO_h_mean_lst=MO_h_mean_lst.groupby('month').mean('h_monthly_mean_lst')
 
EU_h_mean_lst=EUdfHland.groupby('date',)['lst'].transform('mean')
EUdfHland['h_monthly_mean_lst'] = EU_h_mean_lst
EU_h_mean_lst=EUdfHland[['month','h_monthly_mean_lst']].copy()
EU_h_mean_lst=EU_h_mean_lst.groupby('month').mean('h_monthly_mean_lst')
 
EC_h_mean_lst=ECdfHland.groupby('date',)['lst'].transform('mean')
ECdfHland['h_monthly_mean_lst'] = EC_h_mean_lst
EC_h_mean_lst=ECdfHland[['month','h_monthly_mean_lst']].copy()
EC_h_mean_lst=EC_h_mean_lst.groupby('month').mean('h_monthly_mean_lst')
 
MF_h_mean_lst=MFdfHland.groupby('date',)['lst'].transform('mean')
MFdfHland['h_monthly_mean_lst'] = MF_h_mean_lst
MF_h_mean_lst=MFdfHland[['month','h_monthly_mean_lst']].copy()
MF_h_mean_lst=MF_h_mean_lst.groupby('month').mean('h_monthly_mean_lst')
 
CM_h_mean_lst=CMdfHland.groupby('date',)['lst'].transform('mean')
CMdfHland['h_monthly_mean_lst'] = CM_h_mean_lst
CM_h_mean_lst=CMdfHland[['month','h_monthly_mean_lst']].copy()
CM_h_mean_lst=CM_h_mean_lst.groupby('month').mean('h_monthly_mean_lst')
 
E5_h_mean_lst=E5dfHland.groupby('date',)['lst'].transform('mean')
E5dfHland['h_monthly_mean_lst'] = E5_h_mean_lst
E5_h_mean_lst=E5dfHland[['month','h_monthly_mean_lst']].copy()
E5_h_mean_lst=E5_h_mean_lst.groupby('month').mean('h_monthly_mean_lst')
 
 
#Fore Sea
MO_f_mean_sst=MOdfFsea.groupby(['date','lead_month'])['sst'].transform('mean')
MOdfFsea['f_monthly_mean_sst'] = MO_f_mean_sst
MO_f_mean_sst=MOdfFsea[['month','lead_month','f_monthly_mean_sst']].copy()
MO_f_mean_sst=MO_f_mean_sst.groupby('month').mean('f_monthly_mean_sst')
 
EU_f_mean_sst=EUdfFsea.groupby(['date','lead_month'])['sst'].transform('mean')
EUdfFsea['f_monthly_mean_sst'] = EU_f_mean_sst
EU_f_mean_sst=EUdfFsea[['month','lead_month','f_monthly_mean_sst']].copy()
EU_f_mean_sst=EU_f_mean_sst.groupby('month').mean('f_monthly_mean_sst')
 
EC_f_mean_sst=ECdfFsea.groupby(['date','lead_month'])['sst'].transform('mean')
ECdfFsea['f_monthly_mean_sst'] = EC_f_mean_sst
EC_f_mean_sst=ECdfFsea[['month','lead_month','f_monthly_mean_sst']].copy()
EC_f_mean_sst=EC_f_mean_sst.groupby('month').mean('f_monthly_mean_sst')
 
MF_f_mean_sst=MFdfFsea.groupby(['date','lead_month'])['sst'].transform('mean')
MFdfFsea['f_monthly_mean_sst'] = MF_f_mean_sst
MF_f_mean_sst=MFdfFsea[['month','lead_month','f_monthly_mean_sst']].copy()
MF_f_mean_sst=MF_f_mean_sst.groupby('month').mean('f_monthly_mean_sst')
 
CM_f_mean_sst=CMdfFsea.groupby(['date','lead_month'])['sst'].transform('mean')
CMdfFsea['f_monthly_mean_sst'] = CM_f_mean_sst
CM_f_mean_sst=CMdfFsea[['month','lead_month','f_monthly_mean_sst']].copy()
CM_f_mean_sst=CM_f_mean_sst.groupby('month').mean('f_monthly_mean_sst')
 
E5_f_mean_sst=E5dfFsea.groupby(['date'])['sst'].transform('mean')
E5dfFsea['f_monthly_mean_sst'] = E5_f_mean_sst
E5_f_mean_sst=E5dfFsea[['month','f_monthly_mean_sst']].copy()
E5_f_mean_sst=E5_f_mean_sst.groupby('month').mean('f_monthly_mean_sst')
 
 
#Fore Land
MO_f_mean_lst=MOdfFland.groupby(['date','lead_month'])['lst'].transform('mean')
MOdfFland['f_monthly_mean_lst'] = MO_f_mean_lst
MO_f_mean_lst=MOdfFland[['month','lead_month','f_monthly_mean_lst']].copy()
MO_f_mean_lst=MO_f_mean_lst.groupby('month').mean('f_monthly_mean_lst')
 
EU_f_mean_lst=EUdfFland.groupby(['date','lead_month'])['lst'].transform('mean')
EUdfFland['f_monthly_mean_lst'] = EU_f_mean_lst
EU_f_mean_lst=EUdfFland[['month','lead_month','f_monthly_mean_lst']].copy()
EU_f_mean_lst=EU_f_mean_lst.groupby('month').mean('f_monthly_mean_lst')
 
EC_f_mean_lst=ECdfFland.groupby(['date','lead_month'])['lst'].transform('mean')
ECdfFland['f_monthly_mean_lst'] = EC_f_mean_lst
EC_f_mean_lst=ECdfFland[['month','lead_month','f_monthly_mean_lst']].copy()
EC_f_mean_lst=EC_f_mean_lst.groupby('month').mean('f_monthly_mean_lst')
 
MF_f_mean_lst=MFdfFland.groupby(['date','lead_month'])['lst'].transform('mean')
MFdfFland['f_monthly_mean_lst'] = MF_f_mean_lst
MF_f_mean_lst=MFdfFland[['month','lead_month','f_monthly_mean_lst']].copy()
MF_f_mean_lst=MF_f_mean_lst.groupby('month').mean('f_monthly_mean_lst')
 
CM_f_mean_lst=CMdfFland.groupby(['date','lead_month'])['lst'].transform('mean')
CMdfFland['f_monthly_mean_lst'] = CM_f_mean_lst
CM_f_mean_lst=CMdfFland[['month','lead_month','f_monthly_mean_lst']].copy()
CM_f_mean_lst=CM_f_mean_lst.groupby('month').mean('f_monthly_mean_lst')
 
E5_f_mean_lst=E5dfFland.groupby(['date'])['lst'].transform('mean')
E5dfFland['f_monthly_mean_lst'] = E5_f_mean_lst
E5_f_mean_lst=E5dfFland[['month','f_monthly_mean_lst']].copy()
E5_f_mean_lst=E5_f_mean_lst.groupby('month').mean('f_monthly_mean_lst')
 
 
#Minus Hind Sea from Hind Land = Climatology Contrast
MOdfHland.groupby('month')
MOdfHland=MOdfHland.merge(MO_h_mean_sst, on='month',how='left')
MOdfHland['h_contrast']=MOdfHland['h_monthly_mean_lst']-MOdfHland['h_monthly_mean_sst']
MO_h_contrast=MOdfHland[['month','h_contrast']].copy()
MO_h_contrast=MO_h_contrast.groupby('month').mean('h_contrast').reset_index()
 
EUdfHland.groupby('month')
EUdfHland=EUdfHland.merge(EU_h_mean_sst, on='month',how='left')
EUdfHland['h_contrast']=EUdfHland['h_monthly_mean_lst']-EUdfHland['h_monthly_mean_sst']
EU_h_contrast=EUdfHland[['month','h_contrast']].copy()
EU_h_contrast=EU_h_contrast.groupby('month').mean('h_contrast').reset_index()
 
ECdfHland.groupby('month')
ECdfHland=ECdfHland.merge(EC_h_mean_sst, on='month',how='left')
ECdfHland['h_contrast']=ECdfHland['h_monthly_mean_lst']-ECdfHland['h_monthly_mean_sst']
EC_h_contrast=ECdfHland[['month','h_contrast']].copy()
EC_h_contrast=EC_h_contrast.groupby('month').mean('h_contrast').reset_index()
 
MFdfHland.groupby('month')
MFdfHland=MFdfHland.merge(MF_h_mean_sst, on='month',how='left')
MFdfHland['h_contrast']=MFdfHland['h_monthly_mean_lst']-MFdfHland['h_monthly_mean_sst']
MF_h_contrast=MFdfHland[['month','h_contrast']].copy()
MF_h_contrast=MF_h_contrast.groupby('month').mean('h_contrast').reset_index()
 
CMdfHland.groupby('month')
CMdfHland=CMdfHland.merge(CM_h_mean_sst, on='month',how='left')
CMdfHland['h_contrast']=CMdfHland['h_monthly_mean_lst']-CMdfHland['h_monthly_mean_sst']
CM_h_contrast=CMdfHland[['month','h_contrast']].copy()
CM_h_contrast=CM_h_contrast.groupby('month').mean('h_contrast').reset_index()
 
E5dfHland.groupby('month')
E5dfHland=E5dfHland.merge(E5_h_mean_sst, on='month',how='left')
E5dfHland['h_contrast']=E5dfHland['h_monthly_mean_lst']-E5dfHland['h_monthly_mean_sst']
E5_h_contrast=E5dfHland[['month','h_contrast']].copy()
E5_h_contrast=E5_h_contrast.groupby('month').mean('h_contrast').reset_index()
 
 
#Minus Fore Sea from Fore Land = Forecast Contrast
 
MOdfFland.groupby('month')
MOdfFland=MOdfFland.merge(MO_f_mean_sst, on='month',how='left')
MOdfFland['f_contrast']=MOdfFland['f_monthly_mean_lst']-MOdfFland['f_monthly_mean_sst']
 
EUdfFland.groupby('month')
EUdfFland=EUdfFland.merge(EU_f_mean_sst, on='month',how='left')
EUdfFland['f_contrast']=EUdfFland['f_monthly_mean_lst']-EUdfFland['f_monthly_mean_sst']
 
ECdfFland.groupby('month')
ECdfFland=ECdfFland.merge(EC_f_mean_sst, on='month',how='left')
ECdfFland['f_contrast']=ECdfFland['f_monthly_mean_lst']-ECdfFland['f_monthly_mean_sst']
 
MFdfFland.groupby('month')
MFdfFland=MFdfFland.merge(MF_f_mean_sst, on='month',how='left')
MFdfFland['f_contrast']=MFdfFland['f_monthly_mean_lst']-MFdfFland['f_monthly_mean_sst']
 
CMdfFland.groupby('month')
CMdfFland=CMdfFland.merge(CM_f_mean_sst, on='month',how='left')
CMdfFland['f_contrast']=CMdfFland['f_monthly_mean_lst']-CMdfFland['f_monthly_mean_sst']
 
E5dfFland.groupby('month')
E5dfFland=E5dfFland.merge(E5_f_mean_sst, on='month',how='left')
E5dfFland['f_contrast']=E5dfFland['f_monthly_mean_lst']-E5dfFland['f_monthly_mean_sst']
 
 
#Minus Hindcast Contrast (Climatology) from Forecast Contrast = Final Anomaly Contrast
 
MO_anomaly_master=MOdfFland[['date','month','lead_month_x','f_contrast']].copy()
MO_anomaly_master=MO_anomaly_master.merge(MO_h_contrast, on='month',how='left')
MO_anomaly_master['anomaly']=MO_anomaly_master['f_contrast']-MO_anomaly_master['h_contrast']
 
EU_anomaly_master=EUdfFland[['date','month','lead_month_x','f_contrast']].copy()
EU_anomaly_master=EU_anomaly_master.merge(EU_h_contrast, on='month',how='left')
EU_anomaly_master['anomaly']=EU_anomaly_master['f_contrast']-EU_anomaly_master['h_contrast']
 
EC_anomaly_master=ECdfFland[['date','month','lead_month_x','f_contrast']].copy()
EC_anomaly_master=EC_anomaly_master.merge(EC_h_contrast, on='month',how='left')
EC_anomaly_master['anomaly']=EC_anomaly_master['f_contrast']-EC_anomaly_master['h_contrast']
 
MF_anomaly_master=MFdfFland[['date','month','lead_month_x','f_contrast']].copy()
MF_anomaly_master=MF_anomaly_master.merge(MF_h_contrast, on='month',how='left')
MF_anomaly_master['anomaly']=MF_anomaly_master['f_contrast']-MF_anomaly_master['h_contrast']
 
CM_anomaly_master=CMdfFland[['date','month','lead_month_x','f_contrast']].copy()
CM_anomaly_master=CM_anomaly_master.merge(CM_h_contrast, on='month',how='left')
CM_anomaly_master['anomaly']=CM_anomaly_master['f_contrast']-CM_anomaly_master['h_contrast']
 
E5_anomaly_master=E5dfFland[['date','month','f_contrast']].copy()
E5_anomaly_master=E5_anomaly_master.merge(E5_h_contrast, on='month',how='left')
E5_anomaly_master['anomaly']=E5_anomaly_master['f_contrast']-E5_anomaly_master['h_contrast']
 
 
#Sorting
MO_anomaly_master = MO_anomaly_master.sort_values(by=['date','lead_month_x'])
EU_anomaly_master = EU_anomaly_master.sort_values(by=['date','lead_month_x'])
EC_anomaly_master = EC_anomaly_master.sort_values(by=['date','lead_month_x'])
MF_anomaly_master = MF_anomaly_master.sort_values(by=['date','lead_month_x'])
CM_anomaly_master = CM_anomaly_master.sort_values(by=['date','lead_month_x'])
 
 
#Extracting Lead Month Rows
LM1MOdf = MO_anomaly_master[MO_anomaly_master['lead_month_x'] == 1]
LM2MOdf = MO_anomaly_master[MO_anomaly_master['lead_month_x'] == 2]
LM3MOdf = MO_anomaly_master[MO_anomaly_master['lead_month_x'] == 3]
LM4MOdf = MO_anomaly_master[MO_anomaly_master['lead_month_x'] == 4]
LM5MOdf = MO_anomaly_master[MO_anomaly_master['lead_month_x'] == 5]
LM6MOdf = MO_anomaly_master[MO_anomaly_master['lead_month_x'] == 6]
 
LM1EMdf = EU_anomaly_master[EU_anomaly_master['lead_month_x'] == 1]
LM2EMdf = EU_anomaly_master[EU_anomaly_master['lead_month_x'] == 2]
LM3EMdf = EU_anomaly_master[EU_anomaly_master['lead_month_x'] == 3]
LM4EMdf = EU_anomaly_master[EU_anomaly_master['lead_month_x'] == 4]
LM5EMdf = EU_anomaly_master[EU_anomaly_master['lead_month_x'] == 5]
LM6EMdf = EU_anomaly_master[EU_anomaly_master['lead_month_x'] == 6]
 
LM1ECdf = EC_anomaly_master[EC_anomaly_master['lead_month_x'] == 1]
LM2ECdf = EC_anomaly_master[EC_anomaly_master['lead_month_x'] == 2]
LM3ECdf = EC_anomaly_master[EC_anomaly_master['lead_month_x'] == 3]
LM4ECdf = EC_anomaly_master[EC_anomaly_master['lead_month_x'] == 4]
LM5ECdf = EC_anomaly_master[EC_anomaly_master['lead_month_x'] == 5]
LM6ECdf = EC_anomaly_master[EC_anomaly_master['lead_month_x'] == 6]
 
LM1MFdf = MF_anomaly_master[MF_anomaly_master['lead_month_x'] == 1]
LM2MFdf = MF_anomaly_master[MF_anomaly_master['lead_month_x'] == 2]
LM3MFdf = MF_anomaly_master[MF_anomaly_master['lead_month_x'] == 3]
LM4MFdf = MF_anomaly_master[MF_anomaly_master['lead_month_x'] == 4]
LM5MFdf = MF_anomaly_master[MF_anomaly_master['lead_month_x'] == 5]
LM6MFdf = MF_anomaly_master[MF_anomaly_master['lead_month_x'] == 6]
 
LM1CMdf = CM_anomaly_master[CM_anomaly_master['lead_month_x'] == 1]
LM2CMdf = CM_anomaly_master[CM_anomaly_master['lead_month_x'] == 2]
LM3CMdf = CM_anomaly_master[CM_anomaly_master['lead_month_x'] == 3]
LM4CMdf = CM_anomaly_master[CM_anomaly_master['lead_month_x'] == 4]
LM5CMdf = CM_anomaly_master[CM_anomaly_master['lead_month_x'] == 5]
LM6CMdf = CM_anomaly_master[CM_anomaly_master['lead_month_x'] == 6]
 
 
LM1MO = LM1MOdf[['date','lead_month_x','anomaly']].copy()
LM1MO = LM1MO.groupby('date', as_index=False).mean(numeric_only=True)
LM1MO['model']='UKMetOffice'
LM2MO = LM2MOdf[['date','lead_month_x','anomaly']].copy()
LM2MO = LM2MO.groupby('date', as_index=False).mean(numeric_only=True)
LM2MO['model']='UKMetOffice'
LM3MO = LM3MOdf[['date','lead_month_x','anomaly']].copy()
LM3MO = LM3MO.groupby('date', as_index=False).mean(numeric_only=True)
LM3MO['model']='UKMetOffice'
LM4MO = LM4MOdf[['date','lead_month_x','anomaly']].copy()
LM4MO = LM4MO.groupby('date', as_index=False).mean(numeric_only=True)
LM4MO['model']='UKMetOffice'
LM5MO = LM5MOdf[['date','lead_month_x','anomaly']].copy()
LM5MO = LM5MO.groupby('date', as_index=False).mean(numeric_only=True)
LM5MO['model']='UKMetOffice'
LM6MO = LM6MOdf[['date','lead_month_x','anomaly']].copy()
LM6MO = LM6MO.groupby('date', as_index=False).mean(numeric_only=True)
LM6MO['model']='UKMetOffice'
 
LM1EM = LM1EMdf[['date','lead_month_x','anomaly']].copy()
LM1EM = LM1EM.groupby('date', as_index=False).mean(numeric_only=True)
LM1EM['model']='ECMWF'
LM2EM = LM2EMdf[['date','lead_month_x','anomaly']].copy()
LM2EM = LM2EM.groupby('date', as_index=False).mean(numeric_only=True)
LM2EM['model']='ECMWF'
LM3EM = LM3EMdf[['date','lead_month_x','anomaly']].copy()
LM3EM = LM3EM.groupby('date', as_index=False).mean(numeric_only=True)
LM3EM['model']='ECMWF'
LM4EM = LM4EMdf[['date','lead_month_x','anomaly']].copy()
LM4EM = LM4EM.groupby('date', as_index=False).mean(numeric_only=True)
LM4EM['model']='ECMWF'
LM5EM = LM5EMdf[['date','lead_month_x','anomaly']].copy()
LM5EM = LM5EM.groupby('date', as_index=False).mean(numeric_only=True)
LM5EM['model']='ECMWF'
LM6EM = LM6EMdf[['date','lead_month_x','anomaly']].copy()
LM6EM = LM6EM.groupby('date', as_index=False).mean(numeric_only=True)
LM6EM['model']='ECMWF'
 
LM1EC = LM1ECdf[['date','lead_month_x','anomaly']].copy()
LM1EC = LM1EC.groupby('date', as_index=False).mean(numeric_only=True)
LM1EC['model']='ECCC'
LM2EC = LM2ECdf[['date','lead_month_x','anomaly']].copy()
LM2EC = LM2EC.groupby('date', as_index=False).mean(numeric_only=True)
LM2EC['model']='ECCC'
LM3EC = LM3ECdf[['date','lead_month_x','anomaly']].copy()
LM3EC = LM3EC.groupby('date', as_index=False).mean(numeric_only=True)
LM3EC['model']='ECCC'
LM4EC = LM4ECdf[['date','lead_month_x','anomaly']].copy()
LM4EC = LM4EC.groupby('date', as_index=False).mean(numeric_only=True)
LM4EC['model']='ECCC'
LM5EC = LM5ECdf[['date','lead_month_x','anomaly']].copy()
LM5EC = LM5EC.groupby('date', as_index=False).mean(numeric_only=True)
LM5EC['model']='ECCC'
LM6EC = LM6ECdf[['date','lead_month_x','anomaly']].copy()
LM6EC = LM6EC.groupby('date', as_index=False).mean(numeric_only=True)
LM6EC['model']='ECCC'
 
LM1MF = LM1MFdf[['date','lead_month_x','anomaly']].copy()
LM1MF = LM1MF.groupby('date', as_index=False).mean(numeric_only=True)
LM1MF['model']='MeteoFrance'
LM2MF = LM2MFdf[['date','lead_month_x','anomaly']].copy()
LM2MF = LM2MF.groupby('date', as_index=False).mean(numeric_only=True)
LM2MF['model']='MeteoFrance'
LM3MF = LM3MFdf[['date','lead_month_x','anomaly']].copy()
LM3MF = LM3MF.groupby('date', as_index=False).mean(numeric_only=True)
LM3MF['model']='MeteoFrance'
LM4MF = LM4MFdf[['date','lead_month_x','anomaly']].copy()
LM4MF = LM4MF.groupby('date', as_index=False).mean(numeric_only=True)
LM4MF['model']='MeteoFrance'
LM5MF = LM5MFdf[['date','lead_month_x','anomaly']].copy()
LM5MF = LM5MF.groupby('date', as_index=False).mean(numeric_only=True)
LM5MF['model']='MeteoFrance'
LM6MF = LM6MFdf[['date','lead_month_x','anomaly']].copy()
LM6MF = LM6MF.groupby('date', as_index=False).mean(numeric_only=True)
LM6MF['model']='MeteoFrance'
 
LM1CM = LM1CMdf[['date','lead_month_x','anomaly']].copy()
LM1CM = LM1CM.groupby('date', as_index=False).mean(numeric_only=True)
LM1CM['model']='CMCC'
LM2CM = LM2CMdf[['date','lead_month_x','anomaly']].copy()
LM2CM = LM2CM.groupby('date', as_index=False).mean(numeric_only=True)
LM2CM['model']='CMCC'
LM3CM = LM3CMdf[['date','lead_month_x','anomaly']].copy()
LM3CM = LM3CM.groupby('date', as_index=False).mean(numeric_only=True)
LM3CM['model']='CMCC'
LM4CM = LM4CMdf[['date','lead_month_x','anomaly']].copy()
LM4CM = LM4CM.groupby('date', as_index=False).mean(numeric_only=True)
LM4CM['model']='CMCC'
LM5CM = LM5CMdf[['date','lead_month_x','anomaly']].copy()
LM5CM = LM5CM.groupby('date', as_index=False).mean(numeric_only=True)
LM5CM['model']='CMCC'
LM6CM = LM6CMdf[['date','lead_month_x','anomaly']].copy()
LM6CM = LM6CM.groupby('date', as_index=False).mean(numeric_only=True)
LM6CM['model']='CMCC'
 
ERA5df = E5_anomaly_master[['date','anomaly']].copy()
ERA5df = ERA5df.groupby('date', as_index=False).mean(numeric_only=True)
ERA5df['model']='ERA5'
ERA5df['lead_month_x']='0'
 
 
sstLM1=pd.concat([LM1MO,LM1EM,LM1EC,LM1MF,LM1CM])
sstLM1['date'] = pd.to_datetime(sstLM1['date']).dt.date
sstLM1.reset_index(drop=True,inplace=True)
 
sstLM2=pd.concat([LM2MO,LM2EM,LM2EC,LM2MF,LM2CM])
sstLM2['date'] = pd.to_datetime(sstLM2['date']).dt.date
sstLM2.reset_index(drop=True,inplace=True)
 
sstLM3=pd.concat([LM3MO,LM3EM,LM3EC,LM3MF,LM3CM])
sstLM3['date'] = pd.to_datetime(sstLM3['date']).dt.date
sstLM3.reset_index(drop=True,inplace=True)
 
sstLM4=pd.concat([LM4MO,LM4EM,LM4EC,LM4MF,LM4CM])
sstLM4['date'] = pd.to_datetime(sstLM4['date']).dt.date
sstLM4.reset_index(drop=True,inplace=True)
 
sstLM5=pd.concat([LM5MO,LM5EM,LM5EC,LM5MF,LM5CM])
sstLM5['date'] = pd.to_datetime(sstLM5['date']).dt.date
sstLM5.reset_index(drop=True,inplace=True)
 
sstLM6=pd.concat([LM6MO,LM6EM,LM6EC,LM6MF,LM6CM])
sstLM6['date'] = pd.to_datetime(sstLM6['date']).dt.date
sstLM6.reset_index(drop=True,inplace=True)
 
 
 
LSClms=pd.concat([ERA5df,sstLM1,sstLM2,sstLM3,sstLM4,sstLM5,sstLM6])
LSClms['date'] = pd.to_datetime(LSClms['date']).dt.date
LSClms.reset_index(drop=True,inplace=True)
 
LSClms['lead_month_x'] = pd.to_numeric(LSClms['lead_month_x'], downcast='integer', errors='coerce')
 
LSClms['date'] = pd.to_datetime(LSClms['date'], errors='coerce')
LSClms['date'] = LSClms['date'].dt.to_period('M')
 
 
# Save to CSV
LSClms.to_csv("SSTlms.csv", index=False)
 
 
 
# %%
'''Heatmaps'''
 
import seaborn as sns
import pandas as pd
 
#LSClms["plot_date"] = LSClms.apply(
	#lambda r: r["date"] - pd.DateOffset(months=r["lead_month_x"]),
	#axis=1)
 
#LSClms["plot_date"] = LSClms["plot_date"].dt.date
 
 
heatmap_data = LSClms.pivot(
	index=['lead_month_x', 'model'],
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
	vmax=6,
	vmin=-6,
	cbar_kws={'label': 'Land Sea Contrast Anomaly (°C)'},
)
 
 
sns.set_style("whitegrid")
plt.tick_params(left=True, bottom=True)
 
cbar = plt.gca().collections[0].colorbar
cbar.ax.tick_params(labelsize=30)
cbar.set_label("Land Sea Contrast Anomaly (°C)", fontsize=30, weight="bold")
 
plt.xlabel('Date', fontsize=35, fontweight='bold')
plt.xticks(rotation=70, fontsize=30, horizontalalignment='center')
plt.ylabel('Month Leadtime - Model Centre', fontsize=35, fontweight='bold')
plt.yticks(fontsize=30)
 
#plt.title('Land Sea Contrast Anomaly (Sea: 60°W–30°W, 5°N–25°N, Land : 80°W - 60°W, 10°S - 0°N)', fontsize=50, fontweight='bold')
 
plt.tight_layout()
plt.show()

Trade Winds

# -*- coding: utf-8 -*-
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

Moisture Transport

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 20:51:16 2025
 
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
ds1 = xr.open_dataset("C:/Users/amich/SURE/Python/UKMetO_MTran_FORE_MLs.nc", engine='netcdf4')
dsh1 = xr.open_dataset("C:/Users/amich/SURE/Python/UKMetO_MTran_HIND_1ML.nc", engine='netcdf4')
 
ds2 = xr.open_dataset("C:/Users/amich/SURE/Python/ECMWF_MTran_FORE_MLs.nc", engine='netcdf4')
dsh2 = xr.open_dataset("C:/Users/amich/SURE/Python/ECMWF_MTran_HIND_1ML.nc", engine='netcdf4')
 
ds3 = xr.open_dataset("C:/Users/amich/SURE/Python/ECCC_MTran_FORE_MLs.nc", engine='netcdf4')
dsh3 = xr.open_dataset("C:/Users/amich/SURE/Python/ECCC_MTran_HIND_1ML.nc", engine='netcdf4')
 
ds4 = xr.open_dataset("C:/Users/amich/SURE/Python/MF_MTran_FORE_MLs.nc", engine='netcdf4')
dsh4 = xr.open_dataset("C:/Users/amich/SURE/Python/MF_MTran_HIND_1ML.nc", engine='netcdf4')
 
ds5 = xr.open_dataset("C:/Users/amich/SURE/Python/CMCC_MTran_FORE_MLs.nc", engine='netcdf4')
dsh5 = xr.open_dataset("C:/Users/amich/SURE/Python/CMCC_MTran_HIND_1ML.nc", engine='netcdf4')
 
dsE = xr.open_dataset("C:/Users/amich/SURE/Python/ERA5_MTran_FORE.nc", engine='netcdf4')
dshE = xr.open_dataset("C:/Users/amich/SURE/Python/ERA5_MTran_HIND.nc", engine='netcdf4')
 
 
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
df1.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','v':'v_wind','q':'spec_humidity'}, inplace=True)
dfh1.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','v':'v_wind','q':'spec_humidity'}, inplace=True)
 
df2.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','v':'v_wind','q':'spec_humidity'}, inplace=True)
dfh2.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','v':'v_wind','q':'spec_humidity'}, inplace=True)
 
df3.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','v':'v_wind','q':'spec_humidity'}, inplace=True)
dfh3.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','v':'v_wind','q':'spec_humidity'}, inplace=True)
 
df4.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','v':'v_wind','q':'spec_humidity'}, inplace=True)
dfh4.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','v':'v_wind','q':'spec_humidity'}, inplace=True)
 
df5.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','v':'v_wind','q':'spec_humidity'}, inplace=True)
dfh5.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','v':'v_wind','q':'spec_humidity'}, inplace=True)
 
dfE.rename(columns={'valid_time':'date','indexing_time':'date','forecastMonth':'lead_month','v':'v_wind','q':'spec_humidity'}, inplace=True)
dfhE.rename(columns={'valid_time':'date','indexing_time':'date','forecastMonth':'lead_month','v':'v_wind','q':'spec_humidity'}, inplace=True)
 
 
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
 
 
#Cleaning
df1=df1[df1['spec_humidity']<1.1]
dfh1=dfh1[dfh1['spec_humidity']<1.1]
 
df2=df2[df2['spec_humidity']<1.1]
dfh2=dfh2[dfh2['spec_humidity']<1.1]
 
df3=df3[df3['spec_humidity']<1.1]
dfh3=dfh3[dfh3['spec_humidity']<1.1]
 
df4=df4[df4['spec_humidity']<1.1]
dfh4=dfh4[dfh4['spec_humidity']<1.1]
 
df5=df5[df5['spec_humidity']<1.1]
dfh5=dfh5[dfh5['spec_humidity']<1.1]
 
dfE=dfE[dfE['spec_humidity']<1.1]
dfhE=dfhE[dfhE['spec_humidity']<1.1]
 
 
#Find Moisture Transport (Humidity x v_wind)
df1['mtran']=df1['spec_humidity']*df1['v_wind']
df1['mtran']=abs(df1['mtran'])
dfh1['mtran']=dfh1['spec_humidity']*dfh1['v_wind']
dfh1['mtran']=abs(dfh1['mtran'])
 
df2['mtran']=df2['spec_humidity']*df2['v_wind']
df2['mtran']=abs(df2['mtran'])
dfh2['mtran']=dfh2['spec_humidity']*dfh2['v_wind']
dfh2['mtran']=abs(dfh2['mtran'])
 
df3['mtran']=df3['spec_humidity']*df3['v_wind']
df3['mtran']=abs(df3['mtran'])
dfh3['mtran']=dfh3['spec_humidity']*dfh3['v_wind']
dfh3['mtran']=abs(dfh3['mtran'])
 
df4['mtran']=df4['spec_humidity']*df4['v_wind']
df4['mtran']=abs(df4['mtran'])
dfh4['mtran']=dfh4['spec_humidity']*dfh4['v_wind']
dfh4['mtran']=abs(dfh4['mtran'])
 
df5['mtran']=df5['spec_humidity']*df5['v_wind']
df5['mtran']=abs(df5['mtran'])
dfh5['mtran']=dfh5['spec_humidity']*dfh5['v_wind']
dfh5['mtran']=abs(dfh5['mtran'])
 
dfE['mtran']=dfE['spec_humidity']*dfE['v_wind']
dfE['mtran']=abs(dfE['mtran'])
dfhE['mtran']=dfhE['spec_humidity']*dfhE['v_wind']
dfhE['mtran']=abs(dfhE['mtran'])
 
 
#Find mean of chosen paramater by date and lead month
f_mean_mtran=df1.groupby(['date','lead_month'])['mtran'].transform('mean')
df1['monthly_mean_mtran'] = f_mean_mtran
h_mean_mtran=dfh1.groupby(['date','lead_month'])['mtran'].transform('mean')
dfh1['monthly_mean_mtran'] = h_mean_mtran
 
f_mean_mtran=df2.groupby(['date','lead_month'])['mtran'].transform('mean')
df2['monthly_mean_mtran'] = f_mean_mtran
h_mean_mtran=dfh2.groupby(['date','lead_month'])['mtran'].transform('mean')
dfh2['monthly_mean_mtran'] = h_mean_mtran
 
f_mean_mtran=df3.groupby(['date','lead_month'])['mtran'].transform('mean')
df3['monthly_mean_mtran'] = f_mean_mtran
h_mean_mtran=dfh3.groupby(['date','lead_month'])['mtran'].transform('mean')
dfh3['monthly_mean_mtran'] = h_mean_mtran
 
f_mean_mtran=df4.groupby(['date','lead_month'])['mtran'].transform('mean')
df4['monthly_mean_mtran'] = f_mean_mtran
h_mean_mtran=dfh4.groupby(['date','lead_month'])['mtran'].transform('mean')
dfh4['monthly_mean_mtran'] = h_mean_mtran
 
f_mean_mtran=df5.groupby(['date','lead_month'])['mtran'].transform('mean')
df5['monthly_mean_mtran'] = f_mean_mtran
h_mean_mtran=dfh5.groupby(['date','lead_month'])['mtran'].transform('mean')
dfh5['monthly_mean_mtran'] = h_mean_mtran
 
f_mean_mtran=dfE.groupby(['date'])['mtran'].transform('mean')
dfE['monthly_mean_mtran'] = f_mean_mtran
h_mean_mtran=dfhE.groupby(['date'])['mtran'].transform('mean')
dfhE['monthly_mean_mtran'] = h_mean_mtran
 
 
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
 
 
h_uniq_mo_mean=dfh1.groupby('month')['monthly_mean_mtran'].transform('mean')
dfh1['uniq_mo_mean']=h_uniq_mo_mean
 
h_uniq_mo_mean=dfh2.groupby('month')['monthly_mean_mtran'].transform('mean')
dfh2['uniq_mo_mean']=h_uniq_mo_mean
 
h_uniq_mo_mean=dfh3.groupby('month')['monthly_mean_mtran'].transform('mean')
dfh3['uniq_mo_mean']=h_uniq_mo_mean
 
h_uniq_mo_mean=dfh4.groupby('month')['monthly_mean_mtran'].transform('mean')
dfh4['uniq_mo_mean']=h_uniq_mo_mean
 
h_uniq_mo_mean=dfh5.groupby('month')['monthly_mean_mtran'].transform('mean')
dfh5['uniq_mo_mean']=h_uniq_mo_mean
 
h_uniq_mo_mean=dfhE.groupby('month')['monthly_mean_mtran'].transform('mean')
dfhE['uniq_mo_mean']=h_uniq_mo_mean
 
 
#Climatology Monthly Means
month_means_1=dfh1[['month','uniq_mo_mean']].copy()
month_means_1=month_means_1.groupby('month').mean('uniq_mo_mean')
 
month_means_2=dfh2[['month','uniq_mo_mean']].copy()
month_means_2=month_means_2.groupby('month').mean('uniq_mo_mean')
 
month_means_3=dfh3[['month','uniq_mo_mean']].copy()
month_means_3=month_means_3.groupby('month').mean('uniq_mo_mean')
 
month_means_4=dfh4[['month','uniq_mo_mean']].copy()
month_means_4=month_means_4.groupby('month').mean('uniq_mo_mean')
 
month_means_5=dfh5[['month','uniq_mo_mean']].copy()
month_means_5=month_means_5.groupby('month').mean('uniq_mo_mean')
 
month_means_E=dfhE[['month','uniq_mo_mean']].copy()
month_means_E=month_means_E.groupby('month').mean('uniq_mo_mean')
 
 
#Take Climatology away from Forecast
df1.groupby('month')
df1=df1.merge(month_means_1, on='month',how='left')
df1['anomaly']=df1['monthly_mean_mtran']-df1['uniq_mo_mean']
 
df2.groupby('month')
df2=df2.merge(month_means_2, on='month',how='left')
df2['anomaly']=df2['monthly_mean_mtran']-df2['uniq_mo_mean']
 
df3.groupby('month')
df3=df3.merge(month_means_3, on='month',how='left')
df3['anomaly']=df3['monthly_mean_mtran']-df3['uniq_mo_mean']
 
df4.groupby('month')
df4=df4.merge(month_means_4, on='month',how='left')
df4['anomaly']=df4['monthly_mean_mtran']-df4['uniq_mo_mean']
 
df5.groupby('month')
df5=df5.merge(month_means_5, on='month',how='left')
df5['anomaly']=df5['monthly_mean_mtran']-df5['uniq_mo_mean']
 
dfE.groupby('month')
dfE=dfE.merge(month_means_E, on='month',how='left')
dfE['anomaly']=dfE['monthly_mean_mtran']-dfE['uniq_mo_mean']
 
 
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
 
 
mtLM1=pd.concat([LM1MO,LM1EM,LM1EC,LM1MF,LM1CM])
mtLM1['date'] = pd.to_datetime(mtLM1['date']).dt.date
mtLM1.reset_index(drop=True,inplace=True)
 
mtLM2=pd.concat([LM2MO,LM2EM,LM2EC,LM2MF,LM2CM])
mtLM2['date'] = pd.to_datetime(mtLM2['date']).dt.date
mtLM2.reset_index(drop=True,inplace=True)
 
mtLM3=pd.concat([LM3MO,LM3EM,LM3EC,LM3MF,LM3CM])
mtLM3['date'] = pd.to_datetime(mtLM3['date']).dt.date
mtLM3.reset_index(drop=True,inplace=True)
 
mtLM4=pd.concat([LM4MO,LM4EM,LM4EC,LM4MF,LM4CM])
mtLM4['date'] = pd.to_datetime(mtLM4['date']).dt.date
mtLM4.reset_index(drop=True,inplace=True)
 
mtLM5=pd.concat([LM5MO,LM5EM,LM5EC,LM5MF,LM5CM])
mtLM5['date'] = pd.to_datetime(mtLM5['date']).dt.date
mtLM5.reset_index(drop=True,inplace=True)
 
mtLM6=pd.concat([LM6MO,LM6EM,LM6EC,LM6MF,LM6CM])
mtLM6['date'] = pd.to_datetime(mtLM6['date']).dt.date
mtLM6.reset_index(drop=True,inplace=True)
 
 
 
MTlms=pd.concat([ERA5df,mtLM1,mtLM2,mtLM3,mtLM4,mtLM5,mtLM6])
MTlms['date'] = pd.to_datetime(MTlms['date']).dt.date
MTlms.reset_index(drop=True,inplace=True)
 
MTlms['lead_month'] = pd.to_numeric(MTlms['lead_month'], downcast='integer', errors='coerce')
 
MTlms['date'] = pd.to_datetime(MTlms['date'], errors='coerce')
MTlms['date'] = MTlms['date'].dt.to_period('M')
 
 
# Save to CSV
MTlms.to_csv("MTlms.csv", index=False)
 
 
# %%
'''Heatmaps'''
 
import seaborn as sns
import pandas as pd
 
 
#SSTlms["plot_date"] = SSTlms.apply(
	#lambda r: r["date"] - pd.DateOffset(months=r["lead_month"]),
	#axis=1)
 
#SSTlms['plot_date'] = pd.to_datetime(SSTlms['plot_date']).dt.date
 
 
heatmap_data = MTlms.pivot(
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
	vmax=0.015,
	vmin=-0.015,
	cbar_kws={'label': 'Moisture Transport Anomaly (kg/m/s)'},
)
 
 
sns.set_style("whitegrid")
plt.tick_params(left=True, bottom=True)
 
cbar = plt.gca().collections[0].colorbar
cbar.ax.tick_params(labelsize=30)
cbar.set_label("Moisture Transport Anomaly (kg/m/s)", fontsize=30, weight="bold")
 
plt.xlabel('Date', fontsize=35, fontweight='bold')
plt.xticks(rotation=70, fontsize=30, horizontalalignment='center')
plt.ylabel('Month Leadtime - Model Centre', fontsize=35, fontweight='bold')
plt.yticks(fontsize=30)
 
#plt.title('Moisture Transport Anomaly (0°N - 20°N, 70°W - 40°W)', fontsize=50, fontweight='bold')
 
#plt.tight_layout()
plt.show()

Cross Equatorial Flow

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 21:25:13 2025
 
@author: amich
"""
# %%
 
 
 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import xarray as xr
import netCDF4
import matplotlib.dates as mdates
#print(netCDF4.__version__)
 
 
 
 
 
# Load NetCDF file
ds1 = xr.open_dataset("C:/Users/amich/SURE/Python/UKMetO_Equa_FORE_MLs.nc", engine='netcdf4')
dsh1 = xr.open_dataset("C:/Users/amich/SURE/Python/UKMetO_Equa_HIND_1ML.nc", engine='netcdf4')
 
ds2 = xr.open_dataset("C:/Users/amich/SURE/Python/ECMWF_Equa_FORE_MLs.nc", engine='netcdf4')
dsh2 = xr.open_dataset("C:/Users/amich/SURE/Python/ECMWF_Equa_HIND_1ML.nc", engine='netcdf4')
 
ds3 = xr.open_dataset("C:/Users/amich/SURE/Python/ECCC_Equa_FORE_MLs.nc", engine='netcdf4')
dsh3 = xr.open_dataset("C:/Users/amich/SURE/Python/ECCC_Equa_HIND_1ML.nc", engine='netcdf4')
 
ds4 = xr.open_dataset("C:/Users/amich/SURE/Python/MF_Equa_FORE_MLs.nc", engine='netcdf4')
dsh4 = xr.open_dataset("C:/Users/amich/SURE/Python/MF_Equa_HIND_1ML.nc", engine='netcdf4')
 
ds5 = xr.open_dataset("C:/Users/amich/SURE/Python/CMCC_Equa_FORE_MLs.nc", engine='netcdf4')
dsh5 = xr.open_dataset("C:/Users/amich/SURE/Python/CMCC_Equa_HIND_1ML.nc", engine='netcdf4')
 
dsE = xr.open_dataset("C:/Users/amich/SURE/Python/ERA5_Equa_FORE.nc", engine='netcdf4')
dshE = xr.open_dataset("C:/Users/amich/SURE/Python/ERA5_Equa_HIND.nc", engine='netcdf4')
 
 
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
df1.rename(columns={'forecast_reference_time':'date','forecastMonth':'lead_month','v':'v_wind'}, inplace=True)
dfh1.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','v':'v_wind'}, inplace=True)
 
df2.rename(columns={'forecast_reference_time':'date','forecastMonth':'lead_month','v':'v_wind'}, inplace=True)
dfh2.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','v':'v_wind'}, inplace=True)
 
df3.rename(columns={'forecast_reference_time':'date','forecastMonth':'lead_month','v':'v_wind'}, inplace=True)
dfh3.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','v':'v_wind'}, inplace=True)
 
df4.rename(columns={'forecast_reference_time':'date','forecastMonth':'lead_month','v':'v_wind'}, inplace=True)
dfh4.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','v':'v_wind'}, inplace=True)
 
df5.rename(columns={'forecast_reference_time':'date','forecastMonth':'lead_month','v':'v_wind'}, inplace=True)
dfh5.rename(columns={'forecast_reference_time':'date','indexing_time':'date','forecastMonth':'lead_month','v':'v_wind'}, inplace=True)
 
dfE.rename(columns={'valid_time':'date','forecastMonth':'lead_month','v':'v_wind'}, inplace=True)
dfhE.rename(columns={'valid_time':'date','indexing_time':'date','forecastMonth':'lead_month','v':'v_wind'}, inplace=True)
 
 
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
f_mean_vwind=df1.groupby(['date','lead_month'])['v_wind'].transform('mean')
df1['monthly_mean_v_wind'] = f_mean_vwind
h_mean_vwind=dfh1.groupby(['date','lead_month'])['v_wind'].transform('mean')
dfh1['monthly_mean_v_wind'] = h_mean_vwind
 
f_mean_vwind=df2.groupby(['date','lead_month'])['v_wind'].transform('mean')
df2['monthly_mean_v_wind'] = f_mean_vwind
h_mean_vwind=dfh2.groupby(['date','lead_month'])['v_wind'].transform('mean')
dfh2['monthly_mean_v_wind'] = h_mean_vwind
 
f_mean_vwind=df3.groupby(['date','lead_month'])['v_wind'].transform('mean')
df3['monthly_mean_v_wind'] = f_mean_vwind
h_mean_vwind=dfh3.groupby(['date','lead_month'])['v_wind'].transform('mean')
dfh3['monthly_mean_v_wind'] = h_mean_vwind
 
f_mean_vwind=df4.groupby(['date','lead_month'])['v_wind'].transform('mean')
df4['monthly_mean_v_wind'] = f_mean_vwind
h_mean_vwind=dfh4.groupby(['date','lead_month'])['v_wind'].transform('mean')
dfh4['monthly_mean_v_wind'] = h_mean_vwind
 
f_mean_vwind=df5.groupby(['date','lead_month'])['v_wind'].transform('mean')
df5['monthly_mean_v_wind'] = f_mean_vwind
h_mean_vwind=dfh5.groupby(['date','lead_month'])['v_wind'].transform('mean')
dfh5['monthly_mean_v_wind'] = h_mean_vwind
 
f_mean_vwind=dfE.groupby(['date'])['v_wind'].transform('mean')
dfE['monthly_mean_v_wind'] = f_mean_vwind
h_mean_vwind=dfhE.groupby(['date'])['v_wind'].transform('mean')
dfhE['monthly_mean_v_wind'] = h_mean_vwind
 
 
#Find mean of each unique month (Forecast)
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
 
 
h_uniq_mo_mean=dfh1.groupby('month')['monthly_mean_v_wind'].transform('mean')
dfh1['uniq_mo_mean']=h_uniq_mo_mean
 
h_uniq_mo_mean=dfh2.groupby('month')['monthly_mean_v_wind'].transform('mean')
dfh2['uniq_mo_mean']=h_uniq_mo_mean
 
h_uniq_mo_mean=dfh3.groupby('month')['monthly_mean_v_wind'].transform('mean')
dfh3['uniq_mo_mean']=h_uniq_mo_mean
 
h_uniq_mo_mean=dfh4.groupby('month')['monthly_mean_v_wind'].transform('mean')
dfh4['uniq_mo_mean']=h_uniq_mo_mean
 
h_uniq_mo_mean=dfh5.groupby('month')['monthly_mean_v_wind'].transform('mean')
dfh5['uniq_mo_mean']=h_uniq_mo_mean
 
h_uniq_mo_mean=dfhE.groupby('month')['monthly_mean_v_wind'].transform('mean')
dfhE['uniq_mo_mean']=h_uniq_mo_mean
 
 
#Climatology Monthly Means
month_means_1=dfh1[['month','uniq_mo_mean']].copy()
month_means_1=month_means_1.groupby('month').mean('uniq_mo_mean')
 
month_means_2=dfh2[['month','uniq_mo_mean']].copy()
month_means_2=month_means_2.groupby('month').mean('uniq_mo_mean')
 
month_means_3=dfh3[['month','uniq_mo_mean']].copy()
month_means_3=month_means_3.groupby('month').mean('uniq_mo_mean')
 
month_means_4=dfh4[['month','uniq_mo_mean']].copy()
month_means_4=month_means_4.groupby('month').mean('uniq_mo_mean')
 
month_means_5=dfh5[['month','uniq_mo_mean']].copy()
month_means_5=month_means_5.groupby('month').mean('uniq_mo_mean')
 
month_means_E=dfhE[['month','uniq_mo_mean']].copy()
month_means_E=month_means_E.groupby('month').mean('uniq_mo_mean')
 
 
#Take Climatology away from Forecast
df1.groupby('month')
df1=df1.merge(month_means_1, on='month',how='left')
df1['anomaly']=df1['monthly_mean_v_wind']-df1['uniq_mo_mean']
 
df2.groupby('month')
df2=df2.merge(month_means_2, on='month',how='left')
df2['anomaly']=df2['monthly_mean_v_wind']-df2['uniq_mo_mean']
 
df3.groupby('month')
df3=df3.merge(month_means_3, on='month',how='left')
df3['anomaly']=df3['monthly_mean_v_wind']-df3['uniq_mo_mean']
 
df4.groupby('month')
df4=df4.merge(month_means_4, on='month',how='left')
df4['anomaly']=df4['monthly_mean_v_wind']-df4['uniq_mo_mean']
 
df5.groupby('month')
df5=df5.merge(month_means_5, on='month',how='left')
df5['anomaly']=df5['monthly_mean_v_wind']-df5['uniq_mo_mean']
 
dfE.groupby('month')
dfE=dfE.merge(month_means_E, on='month',how='left')
dfE['anomaly']=dfE['monthly_mean_v_wind']-dfE['uniq_mo_mean']
 
 
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
 
 
eqLM1=pd.concat([LM1MO,LM1EM,LM1EC,LM1MF,LM1CM])
eqLM1['date'] = pd.to_datetime(eqLM1['date']).dt.date
eqLM1.reset_index(drop=True,inplace=True)
 
eqLM2=pd.concat([LM2MO,LM2EM,LM2EC,LM2MF,LM2CM])
eqLM2['date'] = pd.to_datetime(eqLM2['date']).dt.date
eqLM2.reset_index(drop=True,inplace=True)
 
eqLM3=pd.concat([LM3MO,LM3EM,LM3EC,LM3MF,LM3CM])
eqLM3['date'] = pd.to_datetime(eqLM3['date']).dt.date
eqLM3.reset_index(drop=True,inplace=True)
 
eqLM4=pd.concat([LM4MO,LM4EM,LM4EC,LM4MF,LM4CM])
eqLM4['date'] = pd.to_datetime(eqLM4['date']).dt.date
eqLM4.reset_index(drop=True,inplace=True)
 
eqLM5=pd.concat([LM5MO,LM5EM,LM5EC,LM5MF,LM5CM])
eqLM5['date'] = pd.to_datetime(eqLM5['date']).dt.date
eqLM5.reset_index(drop=True,inplace=True)
 
eqLM6=pd.concat([LM6MO,LM6EM,LM6EC,LM6MF,LM6CM])
eqLM6['date'] = pd.to_datetime(eqLM6['date']).dt.date
eqLM6.reset_index(drop=True,inplace=True)
 
 
 
EQlms=pd.concat([ERA5df,eqLM1,eqLM2,eqLM3,eqLM4,eqLM5,eqLM6])
EQlms['date'] = pd.to_datetime(EQlms['date']).dt.date
EQlms.reset_index(drop=True,inplace=True)
 
EQlms['lead_month'] = pd.to_numeric(EQlms['lead_month'], downcast='integer', errors='coerce')
 
EQlms['date'] = pd.to_datetime(EQlms['date'], errors='coerce')
EQlms['date'] = EQlms['date'].dt.to_period('M')
 
 
# Save to CSV
EQlms.to_csv("MTlms.csv", index=False)
 
 
# %%
'''Heatmaps'''
 
import seaborn as sns
import pandas as pd
 
 
#SSTlms["plot_date"] = SSTlms.apply(
	#lambda r: r["date"] - pd.DateOffset(months=r["lead_month"]),
	#axis=1)
 
#SSTlms['plot_date'] = pd.to_datetime(SSTlms['plot_date']).dt.date
 
 
heatmap_data = EQlms.pivot(
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
	cbar_kws={'label': 'Cross Equatorial Wind Anomaly (m/s)'},
)
 
 
sns.set_style("whitegrid")
plt.tick_params(left=True, bottom=True)
 
cbar = plt.gca().collections[0].colorbar
cbar.ax.tick_params(labelsize=30)
cbar.set_label("Cross Equatorial Wind Anomaly (m/s)", fontsize=30, weight="bold")
 
plt.xlabel('Date', fontsize=35, fontweight='bold')
plt.xticks(rotation=70, fontsize=30, horizontalalignment='center')
plt.ylabel('Month Leadtime - Model Centre', fontsize=35, fontweight='bold')
plt.yticks(fontsize=30)
 
#plt.title('Cross Equatorial Wind Anomaly (5°N - 5°S, 75°W – 65°W)', fontsize=50, fontweight='bold')
 
#plt.tight_layout()
plt.show()

Latitudinal Flow

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 16:08:12 2025
 
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
MOdsh1EC = xr.open_dataset("C:/Users/amich/SURE/Python/UKMetO_LatFlow_EC_HIND_1ML.nc", engine='netcdf4')
MOds1EC = xr.open_dataset("C:/Users/amich/SURE/Python/UKMetO_LatFlow_EC_FORE_MLs.nc", engine='netcdf4')
MOdsh1AZ = xr.open_dataset("C:/Users/amich/SURE/Python/UKMetO_LatFlow_AZ_HIND_1ML.nc", engine='netcdf4')
MOds1AZ = xr.open_dataset("C:/Users/amich/SURE/Python/UKMetO_LatFlow_AZ_FORE_MLs.nc", engine='netcdf4')
 
EUdsh1EC = xr.open_dataset("C:/Users/amich/SURE/Python/ECMWF_LatFlow_EC_HIND_1ML.nc", engine='netcdf4')
EUds1EC = xr.open_dataset("C:/Users/amich/SURE/Python/ECMWF_LatFlow_EC_FORE_MLs.nc", engine='netcdf4')
EUdsh1AZ = xr.open_dataset("C:/Users/amich/SURE/Python/ECMWF_LatFlow_AZ_HIND_1ML.nc", engine='netcdf4')
EUds1AZ = xr.open_dataset("C:/Users/amich/SURE/Python/ECMWF_LatFlow_AZ_FORE_MLs.nc", engine='netcdf4')
 
ECdsh1EC = xr.open_dataset("C:/Users/amich/SURE/Python/ECCC_LatFlow_EC_HIND_1ML.nc", engine='netcdf4')
ECds1EC = xr.open_dataset("C:/Users/amich/SURE/Python/ECCC_LatFlow_EC_FORE_MLs.nc", engine='netcdf4')
ECdsh1AZ = xr.open_dataset("C:/Users/amich/SURE/Python/ECCC_LatFlow_AZ_HIND_1ML.nc", engine='netcdf4')
ECds1AZ = xr.open_dataset("C:/Users/amich/SURE/Python/ECCC_LatFlow_AZ_FORE_MLs.nc", engine='netcdf4')
 
CMdsh1EC = xr.open_dataset("C:/Users/amich/SURE/Python/CMCC_LatFlow_EC_HIND_1ML.nc", engine='netcdf4')
CMds1EC = xr.open_dataset("C:/Users/amich/SURE/Python/CMCC_LatFlow_EC_FORE_MLs.nc", engine='netcdf4')
CMdsh1AZ = xr.open_dataset("C:/Users/amich/SURE/Python/CMCC_LatFlow_AZ_HIND_1ML.nc", engine='netcdf4')
CMds1AZ = xr.open_dataset("C:/Users/amich/SURE/Python/CMCC_LatFlow_AZ_FORE_MLs.nc", engine='netcdf4')
 
MFdsh1EC = xr.open_dataset("C:/Users/amich/SURE/Python/MF_LatFlow_EC_HIND_1ML.nc", engine='netcdf4')
MFds1EC = xr.open_dataset("C:/Users/amich/SURE/Python/MF_LatFlow_EC_FORE_MLs.nc", engine='netcdf4')
MFdsh1AZ = xr.open_dataset("C:/Users/amich/SURE/Python/MF_LatFlow_AZ_HIND_1ML.nc", engine='netcdf4')
MFds1AZ = xr.open_dataset("C:/Users/amich/SURE/Python/MF_LatFlow_AZ_FORE_MLs.nc", engine='netcdf4')
 
Edsh1EC = xr.open_dataset("C:/Users/amich/SURE/Python/ERA5_LatFlow_EC_HIND.nc", engine='netcdf4')
Eds1EC = xr.open_dataset("C:/Users/amich/SURE/Python/ERA5_LatFlow_EC_FORE.nc", engine='netcdf4')
Edsh1AZ = xr.open_dataset("C:/Users/amich/SURE/Python/ERA5_LatFlow_AZ_HIND.nc", engine='netcdf4')
Eds1AZ = xr.open_dataset("C:/Users/amich/SURE/Python/ERA5_LatFlow_AZ_FORE.nc", engine='netcdf4')
 
 
# Convert to DataFrame
MOdf1EC = MOds1EC.to_dataframe().reset_index()
MOdf1AZ = MOds1AZ.to_dataframe().reset_index()
MOdfh1EC = MOdsh1EC.to_dataframe().reset_index()
MOdfh1AZ = MOdsh1AZ.to_dataframe().reset_index()
 
EUdf1EC = EUds1EC.to_dataframe().reset_index()
EUdf1AZ = EUds1AZ.to_dataframe().reset_index()
EUdfh1EC = EUdsh1EC.to_dataframe().reset_index()
EUdfh1AZ = EUdsh1AZ.to_dataframe().reset_index()
 
ECdf1EC = ECds1EC.to_dataframe().reset_index()
ECdf1AZ = ECds1AZ.to_dataframe().reset_index()
ECdfh1EC = ECdsh1EC.to_dataframe().reset_index()
ECdfh1AZ = ECdsh1AZ.to_dataframe().reset_index()
 
CMdf1EC = CMds1EC.to_dataframe().reset_index()
CMdf1AZ = CMds1AZ.to_dataframe().reset_index()
CMdfh1EC = CMdsh1EC.to_dataframe().reset_index()
CMdfh1AZ = CMdsh1AZ.to_dataframe().reset_index()
 
MFdf1EC = MFds1EC.to_dataframe().reset_index()
MFdf1AZ = MFds1AZ.to_dataframe().reset_index()
MFdfh1EC = MFdsh1EC.to_dataframe().reset_index()
MFdfh1AZ = MFdsh1AZ.to_dataframe().reset_index()
 
Edf1EC = Eds1EC.to_dataframe().reset_index()
Edf1AZ = Eds1AZ.to_dataframe().reset_index()
Edfh1EC = Edsh1EC.to_dataframe().reset_index()
Edfh1AZ = Edsh1AZ.to_dataframe().reset_index()
 
 
#Renaming Columns
MOdf1EC.rename(columns={'indexing_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
MOdf1AZ.rename(columns={'indexing_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
MOdfh1EC.rename(columns={'indexing_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
MOdfh1AZ.rename(columns={'indexing_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
 
EUdf1EC.rename(columns={'indexing_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
EUdf1AZ.rename(columns={'indexing_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
EUdfh1EC.rename(columns={'indexing_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
EUdfh1AZ.rename(columns={'indexing_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
 
ECdf1EC.rename(columns={'indexing_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
ECdf1AZ.rename(columns={'indexing_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
ECdfh1EC.rename(columns={'indexing_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
ECdfh1AZ.rename(columns={'indexing_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
 
CMdf1EC.rename(columns={'indexing_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
CMdf1AZ.rename(columns={'indexing_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
CMdfh1EC.rename(columns={'indexing_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
CMdfh1AZ.rename(columns={'indexing_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
 
MFdf1EC.rename(columns={'indexing_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
MFdf1AZ.rename(columns={'indexing_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
MFdfh1EC.rename(columns={'indexing_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
MFdfh1AZ.rename(columns={'indexing_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
 
Edf1EC.rename(columns={'valid_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
Edf1AZ.rename(columns={'valid_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
Edfh1EC.rename(columns={'valid_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
Edfh1AZ.rename(columns={'valid_time':'date','forecast_reference_time':'date','forecastMonth':'lead_month'}, inplace=True)
 
 
#Convert to datetime
MOdf1EC['date'] = pd.to_datetime(MOdf1EC['date'])
MOdf1AZ['date'] = pd.to_datetime(MOdf1AZ['date'])
MOdfh1EC['date'] = pd.to_datetime(MOdfh1EC['date'])
MOdfh1AZ['date'] = pd.to_datetime(MOdfh1AZ['date'])
 
EUdf1EC['date'] = pd.to_datetime(EUdf1EC['date'])
EUdf1AZ['date'] = pd.to_datetime(EUdf1AZ['date'])
EUdfh1EC['date'] = pd.to_datetime(EUdfh1EC['date'])
EUdfh1AZ['date'] = pd.to_datetime(EUdfh1AZ['date'])
 
ECdf1EC['date'] = pd.to_datetime(ECdf1EC['date'])
ECdf1AZ['date'] = pd.to_datetime(ECdf1AZ['date'])
ECdfh1EC['date'] = pd.to_datetime(ECdfh1EC['date'])
ECdfh1AZ['date'] = pd.to_datetime(ECdfh1AZ['date'])
 
CMdf1EC['date'] = pd.to_datetime(CMdf1EC['date'])
CMdf1AZ['date'] = pd.to_datetime(CMdf1AZ['date'])
CMdfh1EC['date'] = pd.to_datetime(CMdfh1EC['date'])
CMdfh1AZ['date'] = pd.to_datetime(CMdfh1AZ['date'])
 
MFdf1EC['date'] = pd.to_datetime(MFdf1EC['date'])
MFdf1AZ['date'] = pd.to_datetime(MFdf1AZ['date'])
MFdfh1EC['date'] = pd.to_datetime(MFdfh1EC['date'])
MFdfh1AZ['date'] = pd.to_datetime(MFdfh1AZ['date'])
 
Edf1EC['date'] = pd.to_datetime(Edf1EC['date'])
Edf1AZ['date'] = pd.to_datetime(Edf1AZ['date'])
Edfh1EC['date'] = pd.to_datetime(Edfh1EC['date'])
Edfh1AZ['date'] = pd.to_datetime(Edfh1AZ['date'])
 
 
#Month Number
MOdf1EC['month'] = MOdf1EC['date'].dt.month
MOdf1AZ['month'] = MOdf1AZ['date'].dt.month
MOdfh1EC['month'] = MOdfh1EC['date'].dt.month
MOdfh1AZ['month'] = MOdfh1AZ['date'].dt.month
 
EUdf1EC['month'] = EUdf1EC['date'].dt.month
EUdf1AZ['month'] = EUdf1AZ['date'].dt.month
EUdfh1EC['month'] = EUdfh1EC['date'].dt.month
EUdfh1AZ['month'] = EUdfh1AZ['date'].dt.month
 
ECdf1EC['month'] = ECdf1EC['date'].dt.month
ECdf1AZ['month'] = ECdf1AZ['date'].dt.month
ECdfh1EC['month'] = ECdfh1EC['date'].dt.month
ECdfh1AZ['month'] = ECdfh1AZ['date'].dt.month
 
CMdf1EC['month'] = CMdf1EC['date'].dt.month
CMdf1AZ['month'] = CMdf1AZ['date'].dt.month
CMdfh1EC['month'] = CMdfh1EC['date'].dt.month
CMdfh1AZ['month'] = CMdfh1AZ['date'].dt.month
 
MFdf1EC['month'] = MFdf1EC['date'].dt.month
MFdf1AZ['month'] = MFdf1AZ['date'].dt.month
MFdfh1EC['month'] = MFdfh1EC['date'].dt.month
MFdfh1AZ['month'] = MFdfh1AZ['date'].dt.month
 
Edf1EC['month'] = Edf1EC['date'].dt.month
Edf1AZ['month'] = Edf1AZ['date'].dt.month
Edfh1EC['month'] = Edfh1EC['date'].dt.month
Edfh1AZ['month'] = Edfh1AZ['date'].dt.month
 
#Find mean of each parameter
#Hind EC
MO_h_EC_mean_v=MOdfh1EC.groupby('date')['v'].transform('mean')
MOdfh1EC['h_monthly_mean_v'] = MO_h_EC_mean_v
MO_h_EC_mean_v=MOdfh1EC[['month','h_monthly_mean_v']].copy()
MO_h_EC_mean_v=MO_h_EC_mean_v.groupby('month').mean('h_monthly_mean_v')
 
EU_h_EC_mean_v=EUdfh1EC.groupby('date')['v'].transform('mean')
EUdfh1EC['h_monthly_mean_v'] = EU_h_EC_mean_v
EU_h_EC_mean_v=EUdfh1EC[['month','h_monthly_mean_v']].copy()
EU_h_EC_mean_v=EU_h_EC_mean_v.groupby('month').mean('h_monthly_mean_v')
 
EC_h_EC_mean_v=ECdfh1EC.groupby('date')['v'].transform('mean')
ECdfh1EC['h_monthly_mean_v'] = EC_h_EC_mean_v
EC_h_EC_mean_v=ECdfh1EC[['month','h_monthly_mean_v']].copy()
EC_h_EC_mean_v=EC_h_EC_mean_v.groupby('month').mean('h_monthly_mean_v')
 
CM_h_EC_mean_v=CMdfh1EC.groupby('date')['v'].transform('mean')
CMdfh1EC['h_monthly_mean_v'] = CM_h_EC_mean_v
CM_h_EC_mean_v=CMdfh1EC[['month','h_monthly_mean_v']].copy()
CM_h_EC_mean_v=CM_h_EC_mean_v.groupby('month').mean('h_monthly_mean_v')
 
MF_h_EC_mean_v=MFdfh1EC.groupby('date')['v'].transform('mean')
MFdfh1EC['h_monthly_mean_v'] = MF_h_EC_mean_v
MF_h_EC_mean_v=MFdfh1EC[['month','h_monthly_mean_v']].copy()
MF_h_EC_mean_v=MF_h_EC_mean_v.groupby('month').mean('h_monthly_mean_v')
 
E_h_EC_mean_v=Edfh1EC.groupby('date')['v'].transform('mean')
Edfh1EC['h_monthly_mean_v'] = E_h_EC_mean_v
E_h_EC_mean_v=Edfh1EC[['month','h_monthly_mean_v']].copy()
E_h_EC_mean_v=E_h_EC_mean_v.groupby('month').mean('h_monthly_mean_v')
 
 
#Hind AZ
MO_h_AZ_mean_v=MOdfh1AZ.groupby('date',)['v'].transform('mean')
MOdfh1AZ['h_monthly_mean_v'] = MO_h_AZ_mean_v
MO_h_AZ_mean_v=MOdfh1AZ[['month','h_monthly_mean_v']].copy()
MO_h_AZ_mean_v=MO_h_AZ_mean_v.groupby('month').mean('h_monthly_mean_v')
 
EU_h_AZ_mean_v=EUdfh1AZ.groupby('date',)['v'].transform('mean')
EUdfh1AZ['h_monthly_mean_v'] = EU_h_AZ_mean_v
EU_h_AZ_mean_v=EUdfh1AZ[['month','h_monthly_mean_v']].copy()
EU_h_AZ_mean_v=EU_h_AZ_mean_v.groupby('month').mean('h_monthly_mean_v')
 
EC_h_AZ_mean_v=ECdfh1AZ.groupby('date',)['v'].transform('mean')
ECdfh1AZ['h_monthly_mean_v'] = EC_h_AZ_mean_v
EC_h_AZ_mean_v=ECdfh1AZ[['month','h_monthly_mean_v']].copy()
EC_h_AZ_mean_v=EC_h_AZ_mean_v.groupby('month').mean('h_monthly_mean_v')
 
CM_h_AZ_mean_v=CMdfh1AZ.groupby('date',)['v'].transform('mean')
CMdfh1AZ['h_monthly_mean_v'] = CM_h_AZ_mean_v
CM_h_AZ_mean_v=CMdfh1AZ[['month','h_monthly_mean_v']].copy()
CM_h_AZ_mean_v=CM_h_AZ_mean_v.groupby('month').mean('h_monthly_mean_v')
 
MF_h_AZ_mean_v=MFdfh1AZ.groupby('date',)['v'].transform('mean')
MFdfh1AZ['h_monthly_mean_v'] = MF_h_AZ_mean_v
MF_h_AZ_mean_v=MFdfh1AZ[['month','h_monthly_mean_v']].copy()
MF_h_AZ_mean_v=MF_h_AZ_mean_v.groupby('month').mean('h_monthly_mean_v')
 
E_h_AZ_mean_v=Edfh1AZ.groupby('date',)['v'].transform('mean')
Edfh1AZ['h_monthly_mean_v'] = E_h_AZ_mean_v
E_h_AZ_mean_v=Edfh1AZ[['month','h_monthly_mean_v']].copy()
E_h_AZ_mean_v=E_h_AZ_mean_v.groupby('month').mean('h_monthly_mean_v')
 
 
#Fore EC
MO_f_EC_mean_v=MOdf1EC.groupby(['date','lead_month'])['v'].transform('mean')
MOdf1EC['f_monthly_mean_v'] = MO_f_EC_mean_v
MO_f_EC_mean_v=MOdf1EC[['month','lead_month','f_monthly_mean_v']].copy()
MO_f_EC_mean_v=MO_f_EC_mean_v.groupby('month').mean('f_monthly_mean_v')
 
EU_f_EC_mean_v=EUdf1EC.groupby(['date','lead_month'])['v'].transform('mean')
EUdf1EC['f_monthly_mean_v'] = EU_f_EC_mean_v
EU_f_EC_mean_v=EUdf1EC[['month','lead_month','f_monthly_mean_v']].copy()
EU_f_EC_mean_v=EU_f_EC_mean_v.groupby('month').mean('f_monthly_mean_v')
 
EC_f_EC_mean_v=ECdf1EC.groupby(['date','lead_month'])['v'].transform('mean')
ECdf1EC['f_monthly_mean_v'] = EC_f_EC_mean_v
EC_f_EC_mean_v=ECdf1EC[['month','lead_month','f_monthly_mean_v']].copy()
EC_f_EC_mean_v=EC_f_EC_mean_v.groupby('month').mean('f_monthly_mean_v')
 
CM_f_EC_mean_v=CMdf1EC.groupby(['date','lead_month'])['v'].transform('mean')
CMdf1EC['f_monthly_mean_v'] = CM_f_EC_mean_v
CM_f_EC_mean_v=CMdf1EC[['month','lead_month','f_monthly_mean_v']].copy()
CM_f_EC_mean_v=CM_f_EC_mean_v.groupby('month').mean('f_monthly_mean_v')
 
MF_f_EC_mean_v=MFdf1EC.groupby(['date','lead_month'])['v'].transform('mean')
MFdf1EC['f_monthly_mean_v'] = MF_f_EC_mean_v
MF_f_EC_mean_v=MFdf1EC[['month','lead_month','f_monthly_mean_v']].copy()
MF_f_EC_mean_v=MF_f_EC_mean_v.groupby('month').mean('f_monthly_mean_v')
 
E_f_EC_mean_v=Edf1EC.groupby(['date'])['v'].transform('mean')
Edf1EC['f_monthly_mean_v'] = E_f_EC_mean_v
E_f_EC_mean_v=Edf1EC[['month','f_monthly_mean_v']].copy()
E_f_EC_mean_v=E_f_EC_mean_v.groupby('month').mean('f_monthly_mean_v')
 
 
#Fore AZ
MO_f_AZ_mean_v=MOdf1AZ.groupby(['date','lead_month'])['v'].transform('mean')
MOdf1AZ['f_monthly_mean_v'] = MO_f_AZ_mean_v
MO_f_AZ_mean_v=MOdf1AZ[['month','lead_month','f_monthly_mean_v']].copy()
MO_f_AZ_mean_v=MO_f_AZ_mean_v.groupby('month').mean('f_monthly_mean_v')
 
EU_f_AZ_mean_v=EUdf1AZ.groupby(['date','lead_month'])['v'].transform('mean')
EUdf1AZ['f_monthly_mean_v'] = EU_f_AZ_mean_v
EU_f_AZ_mean_v=EUdf1AZ[['month','lead_month','f_monthly_mean_v']].copy()
EU_f_AZ_mean_v=EU_f_AZ_mean_v.groupby('month').mean('f_monthly_mean_v')
 
EC_f_AZ_mean_v=ECdf1AZ.groupby(['date','lead_month'])['v'].transform('mean')
ECdf1AZ['f_monthly_mean_v'] = EC_f_AZ_mean_v
EC_f_AZ_mean_v=ECdf1AZ[['month','lead_month','f_monthly_mean_v']].copy()
EC_f_AZ_mean_v=EC_f_AZ_mean_v.groupby('month').mean('f_monthly_mean_v')
 
CM_f_AZ_mean_v=CMdf1AZ.groupby(['date','lead_month'])['v'].transform('mean')
CMdf1AZ['f_monthly_mean_v'] = CM_f_AZ_mean_v
CM_f_AZ_mean_v=CMdf1AZ[['month','lead_month','f_monthly_mean_v']].copy()
CM_f_AZ_mean_v=CM_f_AZ_mean_v.groupby('month').mean('f_monthly_mean_v')
 
MF_f_AZ_mean_v=MFdf1AZ.groupby(['date','lead_month'])['v'].transform('mean')
MFdf1AZ['f_monthly_mean_v'] = MF_f_AZ_mean_v
MF_f_AZ_mean_v=MFdf1AZ[['month','lead_month','f_monthly_mean_v']].copy()
MF_f_AZ_mean_v=MF_f_AZ_mean_v.groupby('month').mean('f_monthly_mean_v')
 
E_f_AZ_mean_v=Edf1AZ.groupby(['date'])['v'].transform('mean')
Edf1AZ['f_monthly_mean_v'] = E_f_AZ_mean_v
E_f_AZ_mean_v=Edf1AZ[['month','f_monthly_mean_v']].copy()
E_f_AZ_mean_v=E_f_AZ_mean_v.groupby('month').mean('f_monthly_mean_v')
 
 
#Minus Hind AZ from Hind EC = Hindcast Flow
MOdfh1EC.groupby('month')
MOdfh1EC=MOdfh1EC.merge(MO_h_AZ_mean_v, on='month',how='left')
MOdfh1EC['h_flow']=MOdfh1EC['h_monthly_mean_v_x']-MOdfh1EC['h_monthly_mean_v_y']
MO_h_flow=MOdfh1EC[['month','h_flow']].copy()
MO_h_flow=MO_h_flow.groupby('month').mean('h_flow').reset_index()
 
EUdfh1EC.groupby('month')
EUdfh1EC=EUdfh1EC.merge(EU_h_AZ_mean_v, on='month',how='left')
EUdfh1EC['h_flow']=EUdfh1EC['h_monthly_mean_v_x']-EUdfh1EC['h_monthly_mean_v_y']
EU_h_flow=EUdfh1EC[['month','h_flow']].copy()
EU_h_flow=EU_h_flow.groupby('month').mean('h_flow').reset_index()
 
ECdfh1EC.groupby('month')
ECdfh1EC=ECdfh1EC.merge(EC_h_AZ_mean_v, on='month',how='left')
ECdfh1EC['h_flow']=ECdfh1EC['h_monthly_mean_v_x']-ECdfh1EC['h_monthly_mean_v_y']
EC_h_flow=ECdfh1EC[['month','h_flow']].copy()
EC_h_flow=EC_h_flow.groupby('month').mean('h_flow').reset_index()
 
CMdfh1EC.groupby('month')
CMdfh1EC=CMdfh1EC.merge(CM_h_AZ_mean_v, on='month',how='left')
CMdfh1EC['h_flow']=CMdfh1EC['h_monthly_mean_v_x']-CMdfh1EC['h_monthly_mean_v_y']
CM_h_flow=CMdfh1EC[['month','h_flow']].copy()
CM_h_flow=CM_h_flow.groupby('month').mean('h_flow').reset_index()
 
MFdfh1EC.groupby('month')
MFdfh1EC=MFdfh1EC.merge(MF_h_AZ_mean_v, on='month',how='left')
MFdfh1EC['h_flow']=MFdfh1EC['h_monthly_mean_v_x']-MFdfh1EC['h_monthly_mean_v_y']
MF_h_flow=MFdfh1EC[['month','h_flow']].copy()
MF_h_flow=MF_h_flow.groupby('month').mean('h_flow').reset_index()
 
Edfh1EC.groupby('month')
Edfh1EC=Edfh1EC.merge(E_h_AZ_mean_v, on='month',how='left')
Edfh1EC['h_flow']=Edfh1EC['h_monthly_mean_v_x']-Edfh1EC['h_monthly_mean_v_y']
E_h_flow=Edfh1EC[['month','h_flow']].copy()
E_h_flow=E_h_flow.groupby('month').mean('h_flow').reset_index()
 
 
#Minus Fore AZ from Fore EC = Forecast Flow
 
MOdf1EC.groupby('month')
MOdf1EC=MOdf1EC.merge(MO_f_AZ_mean_v, on='month',how='left')
MOdf1EC['f_flow']=MOdf1EC['f_monthly_mean_v_x']-MOdf1EC['f_monthly_mean_v_y']
MO_f_flow=MOdf1EC[['month','f_flow']].copy()
MO_f_flow=MO_f_flow.groupby('month').mean('f_flow').reset_index()
 
EUdf1EC.groupby('month')
EUdf1EC=EUdf1EC.merge(EU_f_AZ_mean_v, on='month',how='left')
EUdf1EC['f_flow']=EUdf1EC['f_monthly_mean_v_x']-EUdf1EC['f_monthly_mean_v_y']
EU_f_flow=EUdf1EC[['month','f_flow']].copy()
EU_f_flow=EU_f_flow.groupby('month').mean('f_flow').reset_index()
 
ECdf1EC.groupby('month')
ECdf1EC=ECdf1EC.merge(EC_f_AZ_mean_v, on='month',how='left')
ECdf1EC['f_flow']=ECdf1EC['f_monthly_mean_v_x']-ECdf1EC['f_monthly_mean_v_y']
EC_f_flow=ECdf1EC[['month','f_flow']].copy()
EC_f_flow=EC_f_flow.groupby('month').mean('f_flow').reset_index()
 
CMdf1EC.groupby('month')
CMdf1EC=CMdf1EC.merge(CM_f_AZ_mean_v, on='month',how='left')
CMdf1EC['f_flow']=CMdf1EC['f_monthly_mean_v_x']-CMdf1EC['f_monthly_mean_v_y']
CM_f_flow=CMdf1EC[['month','f_flow']].copy()
CM_f_flow=CM_f_flow.groupby('month').mean('f_flow').reset_index()
 
MFdf1EC.groupby('month')
MFdf1EC=MFdf1EC.merge(MF_f_AZ_mean_v, on='month',how='left')
MFdf1EC['f_flow']=MFdf1EC['f_monthly_mean_v_x']-MFdf1EC['f_monthly_mean_v_y']
MF_f_flow=MFdf1EC[['month','f_flow']].copy()
MF_f_flow=MF_f_flow.groupby('month').mean('f_flow').reset_index()
 
Edf1EC.groupby('month')
Edf1EC=Edf1EC.merge(E_f_AZ_mean_v, on='month',how='left')
Edf1EC['f_flow']=Edf1EC['f_monthly_mean_v_x']-Edf1EC['f_monthly_mean_v_y']
E_f_flow=Edf1EC[['month','f_flow']].copy()
E_f_flow=E_f_flow.groupby('month').mean('f_flow').reset_index()
 
 
#Minus Hindcast Flow (Climatology) from Forecast Flow
 
MO_anomaly_master=MOdf1EC[['date','month','lead_month_x','f_flow']].copy()
MO_anomaly_master=MO_anomaly_master.merge(MO_h_flow, on='month',how='left')
MO_anomaly_master['anomaly']=MO_anomaly_master['f_flow']-MO_anomaly_master['h_flow']
 
EU_anomaly_master=EUdf1EC[['date','month','lead_month_x','f_flow']].copy()
EU_anomaly_master=EU_anomaly_master.merge(EU_h_flow, on='month',how='left')
EU_anomaly_master['anomaly']=EU_anomaly_master['f_flow']-EU_anomaly_master['h_flow']
 
EC_anomaly_master=ECdf1EC[['date','month','lead_month_x','f_flow']].copy()
EC_anomaly_master=EC_anomaly_master.merge(EC_h_flow, on='month',how='left')
EC_anomaly_master['anomaly']=EC_anomaly_master['f_flow']-EC_anomaly_master['h_flow']
 
CM_anomaly_master=CMdf1EC[['date','month','lead_month_x','f_flow']].copy()
CM_anomaly_master=CM_anomaly_master.merge(CM_h_flow, on='month',how='left')
CM_anomaly_master['anomaly']=CM_anomaly_master['f_flow']-CM_anomaly_master['h_flow']
 
MF_anomaly_master=MFdf1EC[['date','month','lead_month_x','f_flow']].copy()
MF_anomaly_master=MF_anomaly_master.merge(MF_h_flow, on='month',how='left')
MF_anomaly_master['anomaly']=MF_anomaly_master['f_flow']-MF_anomaly_master['h_flow']
 
E_anomaly_master=Edf1EC[['date','month','f_flow']].copy()
E_anomaly_master=E_anomaly_master.merge(E_h_flow, on='month',how='left')
E_anomaly_master['anomaly']=E_anomaly_master['f_flow']-E_anomaly_master['h_flow']
 
 
#Sorting
MO_anomaly_master = MO_anomaly_master.sort_values(by=['date','lead_month_x'])
EU_anomaly_master = EU_anomaly_master.sort_values(by=['date','lead_month_x'])
EC_anomaly_master = EC_anomaly_master.sort_values(by=['date','lead_month_x'])
CM_anomaly_master = CM_anomaly_master.sort_values(by=['date','lead_month_x'])
MF_anomaly_master = MF_anomaly_master.sort_values(by=['date','lead_month_x'])
 
 
#Extracting Lead Month Rows
LM1MOdf = MO_anomaly_master[MO_anomaly_master['lead_month_x'] == 1]
LM2MOdf = MO_anomaly_master[MO_anomaly_master['lead_month_x'] == 2]
LM3MOdf = MO_anomaly_master[MO_anomaly_master['lead_month_x'] == 3]
LM4MOdf = MO_anomaly_master[MO_anomaly_master['lead_month_x'] == 4]
LM5MOdf = MO_anomaly_master[MO_anomaly_master['lead_month_x'] == 5]
LM6MOdf = MO_anomaly_master[MO_anomaly_master['lead_month_x'] == 6]
 
LM1EMdf = EU_anomaly_master[EU_anomaly_master['lead_month_x'] == 1]
LM2EMdf = EU_anomaly_master[EU_anomaly_master['lead_month_x'] == 2]
LM3EMdf = EU_anomaly_master[EU_anomaly_master['lead_month_x'] == 3]
LM4EMdf = EU_anomaly_master[EU_anomaly_master['lead_month_x'] == 4]
LM5EMdf = EU_anomaly_master[EU_anomaly_master['lead_month_x'] == 5]
LM6EMdf = EU_anomaly_master[EU_anomaly_master['lead_month_x'] == 6]
 
LM1ECdf = EC_anomaly_master[EC_anomaly_master['lead_month_x'] == 1]
LM2ECdf = EC_anomaly_master[EC_anomaly_master['lead_month_x'] == 2]
LM3ECdf = EC_anomaly_master[EC_anomaly_master['lead_month_x'] == 3]
LM4ECdf = EC_anomaly_master[EC_anomaly_master['lead_month_x'] == 4]
LM5ECdf = EC_anomaly_master[EC_anomaly_master['lead_month_x'] == 5]
LM6ECdf = EC_anomaly_master[EC_anomaly_master['lead_month_x'] == 6]
 
LM1MFdf = MF_anomaly_master[MF_anomaly_master['lead_month_x'] == 1]
LM2MFdf = MF_anomaly_master[MF_anomaly_master['lead_month_x'] == 2]
LM3MFdf = MF_anomaly_master[MF_anomaly_master['lead_month_x'] == 3]
LM4MFdf = MF_anomaly_master[MF_anomaly_master['lead_month_x'] == 4]
LM5MFdf = MF_anomaly_master[MF_anomaly_master['lead_month_x'] == 5]
LM6MFdf = MF_anomaly_master[MF_anomaly_master['lead_month_x'] == 6]
 
LM1CMdf = CM_anomaly_master[CM_anomaly_master['lead_month_x'] == 1]
LM2CMdf = CM_anomaly_master[CM_anomaly_master['lead_month_x'] == 2]
LM3CMdf = CM_anomaly_master[CM_anomaly_master['lead_month_x'] == 3]
LM4CMdf = CM_anomaly_master[CM_anomaly_master['lead_month_x'] == 4]
LM5CMdf = CM_anomaly_master[CM_anomaly_master['lead_month_x'] == 5]
LM6CMdf = CM_anomaly_master[CM_anomaly_master['lead_month_x'] == 6]
 
 
 
LM1MO = LM1MOdf[['date','lead_month_x','anomaly']].copy()
LM1MO = LM1MO.groupby('date', as_index=False).mean(numeric_only=True)
LM1MO['model']='UKMetOffice'
LM2MO = LM2MOdf[['date','lead_month_x','anomaly']].copy()
LM2MO = LM2MO.groupby('date', as_index=False).mean(numeric_only=True)
LM2MO['model']='UKMetOffice'
LM3MO = LM3MOdf[['date','lead_month_x','anomaly']].copy()
LM3MO = LM3MO.groupby('date', as_index=False).mean(numeric_only=True)
LM3MO['model']='UKMetOffice'
LM4MO = LM4MOdf[['date','lead_month_x','anomaly']].copy()
LM4MO = LM4MO.groupby('date', as_index=False).mean(numeric_only=True)
LM4MO['model']='UKMetOffice'
LM5MO = LM5MOdf[['date','lead_month_x','anomaly']].copy()
LM5MO = LM5MO.groupby('date', as_index=False).mean(numeric_only=True)
LM5MO['model']='UKMetOffice'
LM6MO = LM6MOdf[['date','lead_month_x','anomaly']].copy()
LM6MO = LM6MO.groupby('date', as_index=False).mean(numeric_only=True)
LM6MO['model']='UKMetOffice'
 
LM1EM = LM1EMdf[['date','lead_month_x','anomaly']].copy()
LM1EM = LM1EM.groupby('date', as_index=False).mean(numeric_only=True)
LM1EM['model']='ECMWF'
LM2EM = LM2EMdf[['date','lead_month_x','anomaly']].copy()
LM2EM = LM2EM.groupby('date', as_index=False).mean(numeric_only=True)
LM2EM['model']='ECMWF'
LM3EM = LM3EMdf[['date','lead_month_x','anomaly']].copy()
LM3EM = LM3EM.groupby('date', as_index=False).mean(numeric_only=True)
LM3EM['model']='ECMWF'
LM4EM = LM4EMdf[['date','lead_month_x','anomaly']].copy()
LM4EM = LM4EM.groupby('date', as_index=False).mean(numeric_only=True)
LM4EM['model']='ECMWF'
LM5EM = LM5EMdf[['date','lead_month_x','anomaly']].copy()
LM5EM = LM5EM.groupby('date', as_index=False).mean(numeric_only=True)
LM5EM['model']='ECMWF'
LM6EM = LM6EMdf[['date','lead_month_x','anomaly']].copy()
LM6EM = LM6EM.groupby('date', as_index=False).mean(numeric_only=True)
LM6EM['model']='ECMWF'
 
LM1EC = LM1ECdf[['date','lead_month_x','anomaly']].copy()
LM1EC = LM1EC.groupby('date', as_index=False).mean(numeric_only=True)
LM1EC['model']='ECCC'
LM2EC = LM2ECdf[['date','lead_month_x','anomaly']].copy()
LM2EC = LM2EC.groupby('date', as_index=False).mean(numeric_only=True)
LM2EC['model']='ECCC'
LM3EC = LM3ECdf[['date','lead_month_x','anomaly']].copy()
LM3EC = LM3EC.groupby('date', as_index=False).mean(numeric_only=True)
LM3EC['model']='ECCC'
LM4EC = LM4ECdf[['date','lead_month_x','anomaly']].copy()
LM4EC = LM4EC.groupby('date', as_index=False).mean(numeric_only=True)
LM4EC['model']='ECCC'
LM5EC = LM5ECdf[['date','lead_month_x','anomaly']].copy()
LM5EC = LM5EC.groupby('date', as_index=False).mean(numeric_only=True)
LM5EC['model']='ECCC'
LM6EC = LM6ECdf[['date','lead_month_x','anomaly']].copy()
LM6EC = LM6EC.groupby('date', as_index=False).mean(numeric_only=True)
LM6EC['model']='ECCC'
 
LM1MF = LM1MFdf[['date','lead_month_x','anomaly']].copy()
LM1MF = LM1MF.groupby('date', as_index=False).mean(numeric_only=True)
LM1MF['model']='MeteoFrance'
LM2MF = LM2MFdf[['date','lead_month_x','anomaly']].copy()
LM2MF = LM2MF.groupby('date', as_index=False).mean(numeric_only=True)
LM2MF['model']='MeteoFrance'
LM3MF = LM3MFdf[['date','lead_month_x','anomaly']].copy()
LM3MF = LM3MF.groupby('date', as_index=False).mean(numeric_only=True)
LM3MF['model']='MeteoFrance'
LM4MF = LM4MFdf[['date','lead_month_x','anomaly']].copy()
LM4MF = LM4MF.groupby('date', as_index=False).mean(numeric_only=True)
LM4MF['model']='MeteoFrance'
LM5MF = LM5MFdf[['date','lead_month_x','anomaly']].copy()
LM5MF = LM5MF.groupby('date', as_index=False).mean(numeric_only=True)
LM5MF['model']='MeteoFrance'
LM6MF = LM6MFdf[['date','lead_month_x','anomaly']].copy()
LM6MF = LM6MF.groupby('date', as_index=False).mean(numeric_only=True)
LM6MF['model']='MeteoFrance'
 
LM1CM = LM1CMdf[['date','lead_month_x','anomaly']].copy()
LM1CM = LM1CM.groupby('date', as_index=False).mean(numeric_only=True)
LM1CM['model']='CMCC'
LM2CM = LM2CMdf[['date','lead_month_x','anomaly']].copy()
LM2CM = LM2CM.groupby('date', as_index=False).mean(numeric_only=True)
LM2CM['model']='CMCC'
LM3CM = LM3CMdf[['date','lead_month_x','anomaly']].copy()
LM3CM = LM3CM.groupby('date', as_index=False).mean(numeric_only=True)
LM3CM['model']='CMCC'
LM4CM = LM4CMdf[['date','lead_month_x','anomaly']].copy()
LM4CM = LM4CM.groupby('date', as_index=False).mean(numeric_only=True)
LM4CM['model']='CMCC'
LM5CM = LM5CMdf[['date','lead_month_x','anomaly']].copy()
LM5CM = LM5CM.groupby('date', as_index=False).mean(numeric_only=True)
LM5CM['model']='CMCC'
LM6CM = LM6CMdf[['date','lead_month_x','anomaly']].copy()
LM6CM = LM6CM.groupby('date', as_index=False).mean(numeric_only=True)
LM6CM['model']='CMCC'
 
ERA5df = E_anomaly_master[['date','anomaly']].copy()
ERA5df = ERA5df.groupby('date', as_index=False).mean(numeric_only=True)
ERA5df['model']='ERA5'
ERA5df['lead_month_x']='0'
 
 
lfLM1=pd.concat([LM1MO,LM1EM,LM1EC,LM1MF,LM1CM])
lfLM1['date'] = pd.to_datetime(lfLM1['date']).dt.date
lfLM1.reset_index(drop=True,inplace=True)
 
lfLM2=pd.concat([LM2MO,LM2EM,LM2EC,LM2MF,LM2CM])
lfLM2['date'] = pd.to_datetime(lfLM2['date']).dt.date
lfLM2.reset_index(drop=True,inplace=True)
 
lfLM3=pd.concat([LM3MO,LM3EM,LM3EC,LM3MF,LM3CM])
lfLM3['date'] = pd.to_datetime(lfLM3['date']).dt.date
lfLM3.reset_index(drop=True,inplace=True)
 
lfLM4=pd.concat([LM4MO,LM4EM,LM4EC,LM4MF,LM4CM])
lfLM4['date'] = pd.to_datetime(lfLM4['date']).dt.date
lfLM4.reset_index(drop=True,inplace=True)
 
lfLM5=pd.concat([LM5MO,LM5EM,LM5EC,LM5MF,LM5CM])
lfLM5['date'] = pd.to_datetime(lfLM5['date']).dt.date
lfLM5.reset_index(drop=True,inplace=True)
 
lfLM6=pd.concat([LM6MO,LM6EM,LM6EC,LM6MF,LM6CM])
lfLM6['date'] = pd.to_datetime(lfLM6['date']).dt.date
lfLM6.reset_index(drop=True,inplace=True)
 
 
 
LFlms=pd.concat([ERA5df,lfLM1,lfLM2,lfLM3,lfLM4,lfLM5,lfLM6])
LFlms['date'] = pd.to_datetime(LFlms['date']).dt.date
LFlms.reset_index(drop=True,inplace=True)
 
LFlms['lead_month_x'] = pd.to_numeric(LFlms['lead_month_x'], downcast='integer', errors='coerce')
 
LFlms['date'] = pd.to_datetime(LFlms['date'], errors='coerce')
LFlms['date'] = LFlms['date'].dt.to_period('M')
 
# Save to CSV
LFlms.to_csv("LFlms.csv", index=False)
 
 
# %%
'''Heatmaps'''
 
import seaborn as sns
import pandas as pd
 
 
#SSTlms["plot_date"] = SSTlms.apply(
	#lambda r: r["date"] - pd.DateOffset(months=r["lead_month"]),
	#axis=1)
 
#SSTlms['plot_date'] = pd.to_datetime(SSTlms['plot_date']).dt.date
 
 
heatmap_data = LFlms.pivot(
	index=['lead_month_x', 'model'],
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
	vmax=4,
	vmin=-4,
	cbar_kws={'label': 'Latitudinal Flow Anomaly (m/s)'},
)
 
 
sns.set_style("whitegrid")
plt.tick_params(left=True, bottom=True)
 
cbar = plt.gca().collections[0].colorbar
cbar.ax.tick_params(labelsize=30)
cbar.set_label("Latitudinal Flow Anomaly (m/s)", fontsize=30, weight="bold")
 
plt.xlabel('Date', fontsize=35, fontweight='bold')
plt.xticks(rotation=70, fontsize=30, horizontalalignment='center')
plt.ylabel('Month Leadtime - Model Centre', fontsize=35, fontweight='bold')
plt.yticks(fontsize=30)
 
#plt.title('Latitudinal Flow Anomaly (Ecuador & Piedemonte: [4°S-1°N, 78.5°W-73.5°W], Amazon: [4°S-1°N, 61.5°W-56.5°W])', fontsize=45, fontweight='bold')
 
 
#plt.tight_layout()
plt.show()

Total Precipitation (Ecuador)

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:51:42 2026
 
@author: amich
"""
#%%
'''Data Wrangling'''
 
 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import xarray as xr
import netCDF4
import matplotlib.dates as mdates
from matplotlib.ticker import AutoMinorLocator
 
#Load NetCDF4 file
dshMO = xr.open_dataset("C:/Users/amich/SURE/Python/UKMetO_EC_tprecip_HIND_1ML.nc", engine='netcdf4')
dsMO = xr.open_dataset("C:/Users/amich/SURE/Python/UKMetO_EC_tprecip_FORE_MLs.nc", engine='netcdf4')
 
dshEU = xr.open_dataset("C:/Users/amich/SURE/Python/ECMWF_EC_tprecip_HIND_1ML.nc", engine='netcdf4')
dsEU = xr.open_dataset("C:/Users/amich/SURE/Python/ECMWF_EC_tprecip_FORE_MLs.nc", engine='netcdf4')
 
dshEC = xr.open_dataset("C:/Users/amich/SURE/Python/ECCC_EC_tprecip_HIND_1ML.nc", engine='netcdf4')
dsEC = xr.open_dataset("C:/Users/amich/SURE/Python/ECCC_EC_tprecip_FORE_MLs.nc", engine='netcdf4')
 
dshMF = xr.open_dataset("C:/Users/amich/SURE/Python/MF_EC_tprecip_HIND_1ML.nc", engine='netcdf4')
dsMF = xr.open_dataset("C:/Users/amich/SURE/Python/MF_EC_tprecip_FORE_MLs.nc", engine='netcdf4')
 
dshCM = xr.open_dataset("C:/Users/amich/SURE/Python/CMCC_EC_tprecip_HIND_1ML.nc", engine='netcdf4')
dsCM = xr.open_dataset("C:/Users/amich/SURE/Python/CMCC_EC_tprecip_FORE_MLs.nc", engine='netcdf4')
 
dshE = xr.open_dataset("C:/Users/amich/SURE/Python/ERA5_EC_tprecip_HIND_1ML.nc", engine='netcdf4')
dsE = xr.open_dataset("C:/Users/amich/SURE/Python/ERA5_EC_tprecip_FORE_MLs.nc", engine='netcdf4')
 
# Convert to DataFrame
dfhMO = dshMO.to_dataframe().reset_index()
dfMO = dsMO.to_dataframe().reset_index()
 
dfhEU = dshEU.to_dataframe().reset_index()
dfEU = dsEU.to_dataframe().reset_index()
 
dfhEC = dshEC.to_dataframe().reset_index()
dfEC = dsEC.to_dataframe().reset_index()
 
dfhMF = dshMF.to_dataframe().reset_index()
dfMF = dsMF.to_dataframe().reset_index()
 
dfhCM = dshCM.to_dataframe().reset_index()
dfCM = dsCM.to_dataframe().reset_index()
 
dfhE = dshE.to_dataframe().reset_index()
dfE = dsE.to_dataframe().reset_index()
 
 
#Renaming Columns
dfhMO.rename(columns={'forecast_reference_time':'date','indexing_time':'date','valid_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat','tp':'tprate'}, inplace=True)
dfMO.rename(columns={'forecast_reference_time':'date','indexing_time':'date','valid_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat','tp':'tprate'}, inplace=True)
 
dfhEU.rename(columns={'forecast_reference_time':'date','indexing_time':'date','valid_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat','tp':'tprate'}, inplace=True)
dfEU.rename(columns={'forecast_reference_time':'date','indexing_time':'date','valid_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat','tp':'tprate'}, inplace=True)
 
dfhEC.rename(columns={'forecast_reference_time':'date','indexing_time':'date','valid_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat','tp':'tprate'}, inplace=True)
dfEC.rename(columns={'forecast_reference_time':'date','indexing_time':'date','valid_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat','tp':'tprate'}, inplace=True)
 
dfhMF.rename(columns={'forecast_reference_time':'date','indexing_time':'date','valid_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat','tp':'tprate'}, inplace=True)
dfMF.rename(columns={'forecast_reference_time':'date','indexing_time':'date','valid_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat','tp':'tprate'}, inplace=True)
 
dfhCM.rename(columns={'forecast_reference_time':'date','indexing_time':'date','valid_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat','tp':'tprate'}, inplace=True)
dfCM.rename(columns={'forecast_reference_time':'date','indexing_time':'date','valid_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat','tp':'tprate'}, inplace=True)
 
dfhE.rename(columns={'forecast_reference_time':'date','indexing_time':'date','valid_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat','tp':'tprate'}, inplace=True)
dfE.rename(columns={'forecast_reference_time':'date','indexing_time':'date','valid_time':'date','forecastMonth':'lead_month','longitude':'long','latitude':'lat','tp':'tprate'}, inplace=True)
 
 
#Convert to datetime
dfMO['date'] = pd.to_datetime(dfMO['date'])
dfhMO['date'] = pd.to_datetime(dfhMO['date'])
 
dfEU['date'] = pd.to_datetime(dfEU['date'])
dfhEU['date'] = pd.to_datetime(dfhEU['date'])
 
dfEC['date'] = pd.to_datetime(dfEC['date'])
dfhEC['date'] = pd.to_datetime(dfhEC['date'])
 
dfMF['date'] = pd.to_datetime(dfMF['date'])
dfhMF['date'] = pd.to_datetime(dfhMF['date'])
 
dfCM['date'] = pd.to_datetime(dfCM['date'])
dfhCM['date'] = pd.to_datetime(dfhCM['date'])
 
dfE['date'] = pd.to_datetime(dfE['date'])
dfhE['date'] = pd.to_datetime(dfhE['date'])
 
 
#Conversion from m to mm
dfMO['tprecip']=dfMO['tprate'].mul(2419200000)
dfhMO['tprecip']=dfhMO['tprate'].mul(2419200000)
 
dfEU['tprecip']=dfEU['tprate'].mul(2419200000)
dfhEU['tprecip']=dfhEU['tprate'].mul(2419200000)
 
dfEC['tprecip']=dfEC['tprate'].mul(2419200000)
dfhEC['tprecip']=dfhEC['tprate'].mul(2419200000)
 
dfMF['tprecip']=dfMF['tprate'].mul(2419200000)
dfhMF['tprecip']=dfhMO['tprate'].mul(2419200000)
 
dfCM['tprecip']=dfCM['tprate'].mul(2419200000)
dfhCM['tprecip']=dfhCM['tprate'].mul(2419200000)
 
dfE['tprecip']=dfE['tprate'].mul(1000)
dfhE['tprecip']=dfhE['tprate'].mul(1000)
 
 
#Find mean of chosen paramater by Date and Lead Month
f_mean_tp=dfMO.groupby(['date','lead_month'])['tprecip'].transform('mean')
dfMO['monthly_mean_tprecip'] = f_mean_tp
h_mean_tp=dfhMO.groupby(['date','lead_month'])['tprecip'].transform('mean')
dfhMO['monthly_mean_tprecip'] = h_mean_tp
 
f_mean_tp=dfEU.groupby(['date','lead_month'])['tprecip'].transform('mean')
dfEU['monthly_mean_tprecip'] = f_mean_tp
h_mean_tp=dfhEU.groupby(['date','lead_month'])['tprecip'].transform('mean')
dfhEU['monthly_mean_tprecip'] = h_mean_tp
 
f_mean_tp=dfEC.groupby(['date','lead_month'])['tprecip'].transform('mean')
dfEC['monthly_mean_tprecip'] = f_mean_tp
h_mean_tp=dfhEC.groupby(['date','lead_month'])['tprecip'].transform('mean')
dfhEC['monthly_mean_tprecip'] = h_mean_tp
 
f_mean_tp=dfMF.groupby(['date','lead_month'])['tprecip'].transform('mean')
dfMF['monthly_mean_tprecip'] = f_mean_tp
h_mean_tp=dfhMF.groupby(['date','lead_month'])['tprecip'].transform('mean')
dfhMF['monthly_mean_tprecip'] = h_mean_tp
 
f_mean_tp=dfCM.groupby(['date','lead_month'])['tprecip'].transform('mean')
dfCM['monthly_mean_tprecip'] = f_mean_tp
h_mean_tp=dfhCM.groupby(['date','lead_month'])['tprecip'].transform('mean')
dfhCM['monthly_mean_tprecip'] = h_mean_tp
 
f_mean_tp=dfE.groupby(['date'])['tprecip'].transform('mean')
dfE['monthly_mean_tprecip'] = f_mean_tp
h_mean_tp=dfhE.groupby(['date'])['tprecip'].transform('mean')
dfhE['monthly_mean_tprecip'] = h_mean_tp
 
 
#Find mean of each unique month in Climatology
dfMO['month'] = dfMO['date'].dt.month
dfhMO['month'] = dfhMO['date'].dt.month
h_uniq_mo_mean=dfhMO.groupby('month')['monthly_mean_tprecip'].transform('mean')
dfhMO['uniq_mo_mean']=h_uniq_mo_mean
 
dfEU['month'] = dfEU['date'].dt.month
dfhEU['month'] = dfhEU['date'].dt.month
h_uniq_mo_mean=dfhEU.groupby('month')['monthly_mean_tprecip'].transform('mean')
dfhEU['uniq_mo_mean']=h_uniq_mo_mean
 
dfEC['month'] = dfEC['date'].dt.month
dfhEC['month'] = dfhEC['date'].dt.month
h_uniq_mo_mean=dfhEC.groupby('month')['monthly_mean_tprecip'].transform('mean')
dfhEC['uniq_mo_mean']=h_uniq_mo_mean
 
dfMF['month'] = dfMF['date'].dt.month
dfhMF['month'] = dfhMF['date'].dt.month
h_uniq_mo_mean=dfhMF.groupby('month')['monthly_mean_tprecip'].transform('mean')
dfhMF['uniq_mo_mean']=h_uniq_mo_mean
 
dfCM['month'] = dfCM['date'].dt.month
dfhCM['month'] = dfhCM['date'].dt.month
h_uniq_mo_mean=dfhCM.groupby('month')['monthly_mean_tprecip'].transform('mean')
dfhCM['uniq_mo_mean']=h_uniq_mo_mean
 
dfE['month'] = dfE['date'].dt.month
dfhE['month'] = dfhE['date'].dt.month
h_uniq_mo_mean=dfhE.groupby('month')['monthly_mean_tprecip'].transform('mean')
dfhE['uniq_mo_mean']=h_uniq_mo_mean
 
 
#Climatology Monthly Means
month_meansMO=dfhMO[['month','uniq_mo_mean']].copy()
month_meansMO=month_meansMO.groupby('month').mean('uniq_mo_mean')
 
month_meansEU=dfhEU[['month','uniq_mo_mean']].copy()
month_meansEU=month_meansEU.groupby('month').mean('uniq_mo_mean')
 
month_meansEC=dfhEC[['month','uniq_mo_mean']].copy()
month_meansEC=month_meansEC.groupby('month').mean('uniq_mo_mean')
 
month_meansMF=dfhMF[['month','uniq_mo_mean']].copy()
month_meansMF=month_meansMF.groupby('month').mean('uniq_mo_mean')
 
month_meansCM=dfhCM[['month','uniq_mo_mean']].copy()
month_meansCM=month_meansCM.groupby('month').mean('uniq_mo_mean')
 
month_meansE=dfhE[['month','uniq_mo_mean']].copy()
month_meansE=month_meansE.groupby('month').mean('uniq_mo_mean')
 
 
#Take Climatology away from Forecast
dfMO.groupby('month')
dfMO=dfMO.merge(month_meansMO, on='month',how='left')
dfMO['anomaly']=dfMO['monthly_mean_tprecip']-dfMO['uniq_mo_mean']
 
dfEU.groupby('month')
dfEU=dfEU.merge(month_meansEU, on='month',how='left')
dfEU['anomaly']=dfEU['monthly_mean_tprecip']-dfEU['uniq_mo_mean']
 
dfEC.groupby('month')
dfEC=dfEC.merge(month_meansEC, on='month',how='left')
dfEC['anomaly']=dfEC['monthly_mean_tprecip']-dfEC['uniq_mo_mean']
 
dfMF.groupby('month')
dfMF=dfMF.merge(month_meansMF, on='month',how='left')
dfMF['anomaly']=dfMF['monthly_mean_tprecip']-dfMF['uniq_mo_mean']
 
dfCM.groupby('month')
dfCM=dfCM.merge(month_meansCM, on='month',how='left')
dfCM['anomaly']=dfCM['monthly_mean_tprecip']-dfCM['uniq_mo_mean']
 
dfE.groupby('month')
dfE=dfE.merge(month_meansE, on='month',how='left')
dfE['anomaly']=dfE['monthly_mean_tprecip']-dfE['uniq_mo_mean']
 
 
#%%
'''Percentage Anomaly'''
 
dfMO['%anomaly']=(dfMO['anomaly']/dfMO['uniq_mo_mean'])*100
 
dfEU['%anomaly']=(dfEU['anomaly']/dfEU['uniq_mo_mean'])*100
 
dfEC['%anomaly']=(dfEC['anomaly']/dfEC['uniq_mo_mean'])*100
 
dfMF['%anomaly']=(dfMF['anomaly']/dfMF['uniq_mo_mean'])*100
 
dfCM['%anomaly']=(dfCM['anomaly']/dfCM['uniq_mo_mean'])*100
 
dfE['%anomaly']=(dfE['anomaly']/dfE['uniq_mo_mean'])*100
 
 
#%%
'''Z-Scores Prep'''
 
MO = dfMO[['date','month','lead_month','anomaly']].copy()
MO = MO.groupby(['date','lead_month'], as_index=False).mean(numeric_only=True)
 
EU = dfEU[['date','month','lead_month','anomaly']].copy()
EU = EU.groupby(['date','lead_month'], as_index=False).mean(numeric_only=True)
 
EC = dfEC[['date','month','lead_month','anomaly']].copy()
EC = EC.groupby(['date','lead_month'], as_index=False).mean(numeric_only=True)
 
MF = dfMF[['date','month','lead_month','anomaly']].copy()
MF = MF.groupby(['date','lead_month'], as_index=False).mean(numeric_only=True)
 
CM = dfCM[['date','month','lead_month','anomaly']].copy()
CM = CM.groupby(['date','lead_month'], as_index=False).mean(numeric_only=True)
 
E = dfE[['date','month','anomaly']].copy()
E = E.groupby('date', as_index=False).mean(numeric_only=True)
 
 
'''Standardise/Z-Scores'''
 
MO['sd']=np.std(dfMO['tprecip'])
MO['z_score']=MO['anomaly']/MO['sd']
 
EU['sd']=np.std(dfEU['tprecip'])
EU['z_score']=EU['anomaly']/EU['sd']
 
EC['sd']=np.std(dfEC['tprecip'])
EC['z_score']=EC['anomaly']/EC['sd']
 
MF['sd']=np.std(dfMF['tprecip'])
MF['z_score']=MF['anomaly']/MF['sd']
 
CM['sd']=np.std(dfCM['tprecip'])
CM['z_score']=CM['anomaly']/CM['sd']
 
E['sd']=np.std(dfE['tprecip'])
E['z_score']=E['anomaly']/E['sd']
 
 
'''3 Month rolling Z score'''
 
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
 
 
tpzLM1=pd.concat([LM1MO,LM1EU,LM1EC,LM1MF,LM1CM])
tpzLM1['date'] = pd.to_datetime(tpzLM1['date']).dt.date
tpzLM1.reset_index(drop=True,inplace=True)
 
tpzLM2=pd.concat([LM2MO,LM2EU,LM2EC,LM2MF,LM2CM])
tpzLM2['date'] = pd.to_datetime(tpzLM2['date']).dt.date
tpzLM2.reset_index(drop=True,inplace=True)
 
tpzLM3=pd.concat([LM3MO,LM3EU,LM3EC,LM3MF,LM3CM])
tpzLM3['date'] = pd.to_datetime(tpzLM3['date']).dt.date
tpzLM3.reset_index(drop=True,inplace=True)
 
tpzLM4=pd.concat([LM4MO,LM4EU,LM4EC,LM4MF,LM4CM])
tpzLM4['date'] = pd.to_datetime(tpzLM4['date']).dt.date
tpzLM4.reset_index(drop=True,inplace=True)
 
tpzLM5=pd.concat([LM5MO,LM5EU,LM5EC,LM5MF,LM5CM])
tpzLM5['date'] = pd.to_datetime(tpzLM5['date']).dt.date
tpzLM5.reset_index(drop=True,inplace=True)
 
tpzLM6=pd.concat([LM6MO,LM6EU,LM6EC,LM6MF,LM6CM])
tpzLM6['date'] = pd.to_datetime(tpzLM6['date']).dt.date
tpzLM6.reset_index(drop=True,inplace=True)
 
 
TPZlms=pd.concat([ERA5df,tpzLM1,tpzLM2,tpzLM3,tpzLM4,tpzLM5,tpzLM6])
TPZlms['date'] = pd.to_datetime(TPZlms['date']).dt.date
TPZlms.reset_index(drop=True,inplace=True)
 
TPZlms['lead_month'] = pd.to_numeric(TPZlms['lead_month'], downcast='integer', errors='coerce')
 
TPZlms['date'] = pd.to_datetime(TPZlms['date'], errors='coerce')
TPZlms['date'] = TPZlms['date'].dt.to_period('M')
 
 
# Save to CSV
TPZlms.to_csv("SSTlms.csv", index=False)
 
 
#%%
 
'''Line plots'''
 
#x=ERA5df['date']
#y2=ERA5df['z_score']
 
 
fig1,ax1=plt.subplots(6,1,figsize=(15,30))
custom_ylim=(-3,3)
plt.setp(ax1,ylim=custom_ylim)
 
ax1[0].plot(LM1MO['date'][:],LM1MO['rolling_z'][:],alpha=1,marker='.',c='green',label='1 Month Lead Rolling %Anomaly Z-Score')
ax1[0].plot(LM1EU['date'][:],LM1EU['rolling_z'][:],alpha=1,marker='.',c='goldenrod',label='1 Month Lead Rolling %Anomaly Z-Score')
ax1[0].plot(LM1EC['date'][:],LM1EC['rolling_z'][:],alpha=1,marker='.',c='red',label='1 Month Lead Rolling %Anomaly Z-Score')
ax1[0].plot(LM1MF['date'][:],LM1MF['rolling_z'][:],alpha=1,marker='.',c='mediumblue',label='1 Month Lead Rolling %Anomaly Z-Score')
ax1[0].plot(LM1CM['date'][:],LM1CM['rolling_z'][:],alpha=1,marker='.',c='silver',label='1 Month Lead Rolling %Anomaly Z-Score')
ax1[0].set_title('1 Month Lead Time')
 
ax1[1].plot(LM2MO['date'][:],LM2MO['rolling_z'][:],alpha=1,marker='.',c='green',label='2 Month Lead Rolling %Anomaly Z-Score')
ax1[1].plot(LM2EU['date'][:],LM2EU['rolling_z'][:],alpha=1,marker='.',c='goldenrod',label='2 Month Lead Rolling %Anomaly Z-Score')
ax1[1].plot(LM2EC['date'][:],LM2EC['rolling_z'][:],alpha=1,marker='.',c='red',label='2 Month Lead Rolling %Anomaly Z-Score')
ax1[1].plot(LM2MF['date'][:],LM2MF['rolling_z'][:],alpha=1,marker='.',c='mediumblue',label='2 Month Lead Rolling %Anomaly Z-Score')
ax1[1].plot(LM2CM['date'][:],LM2CM['rolling_z'][:],alpha=1,marker='.',c='silver',label='2 Month Lead Rolling %Anomaly Z-Score')
ax1[1].set_title('2 Month Lead Time')
 
ax1[2].plot(LM3MO['date'][:],LM3MO['rolling_z'][:],alpha=1,marker='.',c='green',label='3 Month Lead Rolling %Anomaly Z-Score')
ax1[2].plot(LM3EU['date'][:],LM3EU['rolling_z'][:],alpha=1,marker='.',c='goldenrod',label='3 Month Lead Rolling %Anomaly Z-Score')
ax1[2].plot(LM3EC['date'][:],LM3EC['rolling_z'][:],alpha=1,marker='.',c='red',label='3 Month Lead Rolling %Anomaly Z-Score')
ax1[2].plot(LM3MF['date'][:],LM3MF['rolling_z'][:],alpha=1,marker='.',c='mediumblue',label='3 Month Lead Rolling %Anomaly Z-Score')
ax1[2].plot(LM3CM['date'][:],LM3CM['rolling_z'][:],alpha=1,marker='.',c='silver',label='3 Month Lead Rolling %Anomaly Z-Score')
ax1[2].set_title('3 Month Lead Time')
 
ax1[3].plot(LM4MO['date'][:],LM4MO['rolling_z'][:],alpha=1,marker='.',c='green',label='4 Month Lead Rolling %Anomaly Z-Score')
ax1[3].plot(LM4EU['date'][:],LM4EU['rolling_z'][:],alpha=1,marker='.',c='goldenrod',label='4 Month Lead Rolling %Anomaly Z-Score')
ax1[3].plot(LM4EC['date'][:],LM4EC['rolling_z'][:],alpha=1,marker='.',c='red',label='4 Month Lead Rolling %Anomaly Z-Score')
ax1[3].plot(LM4MF['date'][:],LM4MF['rolling_z'][:],alpha=1,marker='.',c='mediumblue',label='4 Month Lead Rolling %Anomaly Z-Score')
ax1[3].plot(LM4CM['date'][:],LM4CM['rolling_z'][:],alpha=1,marker='.',c='silver',label='4 Month Lead Rolling %Anomaly Z-Score')
ax1[3].set_title('4 Month Lead Time')
 
ax1[4].plot(LM5MO['date'][:],LM5MO['rolling_z'][:],alpha=1,marker='.',c='green',label='5 Month Lead Rolling %Anomaly Z-Score')
ax1[4].plot(LM5EU['date'][:],LM5EU['rolling_z'][:],alpha=1,marker='.',c='goldenrod',label='5 Month Lead Rolling %Anomaly Z-Score')
ax1[4].plot(LM5EC['date'][:],LM5EC['rolling_z'][:],alpha=1,marker='.',c='red',label='5 Month Lead Rolling %Anomaly Z-Score')
ax1[4].plot(LM5MF['date'][:],LM5MF['rolling_z'][:],alpha=1,marker='.',c='mediumblue',label='5 Month Lead Rolling %Anomaly Z-Score')
ax1[4].plot(LM5CM['date'][:],LM5CM['rolling_z'][:],alpha=1,marker='.',c='silver',label='5 Month Lead Rolling %Anomaly Z-Score')
ax1[4].set_title('5 Month Lead Time')
 
ax1[5].plot(LM6MO['date'][:],LM6MO['rolling_z'][:],alpha=1,marker='.',c='green',label='UKMetOffice')
ax1[5].plot(LM6EU['date'][:],LM6EU['rolling_z'][:],alpha=1,marker='.',c='goldenrod',label='ECMWF')
ax1[5].plot(LM6EC['date'][:],LM6EC['rolling_z'][:],alpha=1,marker='.',c='red',label='ECCC')
ax1[5].plot(LM6MF['date'][:],LM6MF['rolling_z'][:],alpha=1,marker='.',c='mediumblue',label='Meteo France')
ax1[5].plot(LM6CM['date'][:],LM6CM['rolling_z'][:],alpha=1,marker='.',c='silver',label='CMCC')
ax1[5].set_title('6 Month Lead Time')
 
 
 
#For Lead Months
for ax1 in ax1[0:6]:
	ax1.axhline(y=0, color='black', alpha=0.5, linestyle='--', linewidth=1)
	ax1.grid(alpha=0.5,which='both')
	ax1.xaxis.remove_overlapping_locs=False
    ax1.xaxis.set_major_locator(mdates.YearLocator())
    ax1.xaxis.set_minor_locator(mdates.MonthLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("\n\n%Y"))
    ax1.xaxis.set_minor_formatter(mdates.DateFormatter("%b"))
	ax1.tick_params('x',length=4, width=1, which='both')
    #ax1.yaxis.set_minor_locator(AutoMinorLocator())
	ax1.tick_params(axis='x', which="minor", rotation=90, labelsize=8)
	ax1.set_xlabel('Date')
	ax1.set_ylabel("Z-Score")
 
ax1.legend(loc=4)
plt.tight_layout()
plt.show()
 
 
#%%
'''Heatmaps'''
 
import seaborn as sns
import pandas as pd
 
 
#SSTlms["plot_date"] = SSTlms.apply(
	#lambda r: r["date"] - pd.DateOffset(months=r["lead_month"]),
	#axis=1)
#SSTlms['plot_date'] = pd.to_datetime(SSTlms['plot_date']).dt.date
 
 
 
heatmap_data = TPZlms.pivot(
	index=['lead_month', 'model'],
	columns="date",
	values="rolling_z"
).sort_index(ascending=False)
 
 
#plt.style.use("dark_background")
plt.figure(figsize=(40, 20))
 
 
sns.heatmap(
	heatmap_data,
	cmap='BrBG',  	# good for anomalies
	center=0,       	# zero-centered color scale
	annot=False,
	xticklabels=True,
	yticklabels=True,
	vmin=-2,
	vmax=2,
	cbar_kws={'label': 'Anomaly (°C)'},
)
 
 
sns.set_style("whitegrid")
plt.tick_params(left=True, bottom=True,)
 
cbar = plt.gca().collections[0].colorbar
cbar.ax.tick_params(labelsize=30)
cbar.set_label("3-month Rolling Z-Score", fontsize=30, weight="bold")
 
plt.xlabel('Date', fontsize=35, fontweight='bold')
plt.xticks(rotation=70, fontsize=30, horizontalalignment='center')
plt.ylabel('Month Leadtime - Model Centre', fontsize=35, fontweight='bold')
plt.yticks(fontsize=30)
 
#plt.title('Sea Surface Temperature Anomaly (5°N – 25°N, 60°W - 20°W)', fontsize=50, fontweight='bold')
 
 
#plt.tight_layout()
plt.show()


