# -*- coding: utf-8 -*-
# Alan Parson's code
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


