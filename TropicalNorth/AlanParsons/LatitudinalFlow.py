# -*- coding: utf-8 -*-
# Alan Parson's code
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

