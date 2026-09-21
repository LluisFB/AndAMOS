# -*- coding: utf-8 -*-
# Alan Parson's code
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

