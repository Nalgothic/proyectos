import pandas as pd

convertir=pd.read_excel('ALL_LEADS.xlsx')
convertir.to_csv('ALL_LEADS_CSV.csv', index=None, header=True)

def leo_CSV():
    
    data=pd.read_csv('ALL_LEADS_CSV.csv')
    
    return data