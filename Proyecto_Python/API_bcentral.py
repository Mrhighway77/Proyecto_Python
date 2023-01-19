import requests
import pandas as pd
url = "https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?user=123456789&pass=tuPassword&firstdate=2021-01-01&lastdate=2021-01-31&timeseries=F022.TPM.TIN.D001.NO.Z.D&function=GetSeries"
response = requests.get(url)
response = response.json()
response = response["Series"]["Obs"]                

df_data = pd.DataFrame(response)
df_data.head()