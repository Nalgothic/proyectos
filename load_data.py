import streamlit as st
import pandas as pd

@st.cache_data
def load_data(uploaded_file):
    return pd.read_csv(uploaded_file)

def filter_data(df, Role=None, country=None, CNAE=None, industry=None):
    if Role is not None:
        df = df[df['Role'] == Role]
    if country is not None:
        df = df[df['country'] == country]
    if CNAE is not None:
        df = df[df['CNAE'] == CNAE]
    if industry is not None:
        df = df[df['industry'] == industry]
    return df

def main():
    st.title("Sistema de Filtrado de Datos CSV")
    uploaded_file = st.file_uploader("Sube tu archivo CSV", type='csv')
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        st.write("Datos cargados con éxito:")
        st.dataframe(df)
        
        st.write("Columnas en el DataFrame:", df.columns.tolist())
        
        # Opcionalmente, muestra los valores únicos para cada criterio
        st.write("Valores únicos en 'Role':", df['Role'].unique())
        st.write("Valores únicos en 'country':", df['country'].unique())
        st.write("Valores únicos en 'CNAE':", df['CNAE'].unique())
        st.write("Valores únicos en 'industry':", df['industry'].unique())
        
        # Permite al usuario seleccionar valores para filtrar
        Role = st.selectbox('Selecciona Rol (o deja en blanco para todos)', [None] + list(df['Role'].unique()))
        country = st.selectbox('Selecciona país (o deja en blanco para todos)', [None] + list(df['country'].unique()))
        CNAE = st.selectbox('Selecciona CNAE (o deja en blanco para todos)', [None] + list(df['CNAE'].unique()))
        industry = st.selectbox('Selecciona Industria (o deja en blanco para todos)', [None] + list(df['industry'].unique()))
        
        st.write(f"Filtrando por: Rol={Role}, País={country}, CNAE={CNAE}, Industria={industry}")
        
        df_filtered = filter_data(df, Role, country, CNAE, industry)
        
        st.write("Datos Filtrados:")
        st.dataframe(df_filtered)
        
        if 'count' not in st.session_state:
            st.session_state['count'] = 0
        
        def download_callback():
            st.session_state['count'] += 1
        
        csv = df_filtered.to_csv(index=False).encode('utf-8')
        st.download_button(label="Descargar datos filtrados como CSV", data=csv, 
                           file_name='datos_filtrados.csv', mime='text/csv',
                           on_click=download_callback)
        
        st.write(f"El archivo ha sido descargado {st.session_state['count']} veces.")

if __name__ == "__main__":
    main()
