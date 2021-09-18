from os import write
from google.protobuf.symbol_database import Default
import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import pandas as pd
import streamlit.components.v1 as components
import math
import plotly.graph_objects as go


    
def main():
    st.title('INDICE DE VOLABILIDAD')
    #st.write('En minas subterráneas, el principio básico es proveer la suficiente cantidad de aire fresco a los frentes de trabajo y remover los contaminantes generados como el polvo respirable, productos de combustión del diesel, gases de la mina y el exceso de calor. Por lo que realizar el calculo correcto de esta cantidad es fundamental, en esta oportunidad nos vamos a basar en las leyes de Perú. ')
    col1c, col2c = st.columns([3, 1])
    col1c.markdown("<div style='text-align: justify'>Describe la naturaleza y la geología de la roca, el índice de volabilidad o “BI” (blastability index) que se obtiene como suma de los valores representativos de cuatro parámetros. Este índice debe de ser corregido según la mina en que se esté trabajando, acondicionándolo con factores para hacerlo más representativo de la roca a volar, si quieres más información visita el siguiente <a style='color:black; font-size:110% ;' href='https://www.smctesting.com/documents/mine-to-mill/The%20kuz%20ram%20fragmentation%20model%2020%20years%20on.pdf' target='_blank'><i class='fa fa-rocket'></i>enlace.</a> </div>", unsafe_allow_html=True)
    image2 = Image.open('imagenes\ja.jpg')
    col2c.image(image2, caption='INDICE DE VOLABILIDAD')
    st.write("")
    st.markdown('### INPUTS')
    col1, col2 = st.columns([2, 2])
    densidad_roca_mineral=col1.number_input('Densidad de Roca Mineral (SG)',value=2.58)
    resostencia_compresion_simple_mineral=col1.number_input('Resistencia a Compresion Simple Mineral (MPa)',value=200)
    direccion_cara_libre_mineral=col1.number_input('Direccion de la cara libre Mineral (deg)',value=299)
    modulo_de_elasticidad_mineral=0.12*resostencia_compresion_simple_mineral
    macizo_rocoso={"MINERAL":[densidad_roca_mineral,resostencia_compresion_simple_mineral,modulo_de_elasticidad_mineral,direccion_cara_libre_mineral]
               }
    df_maciza_rocoso=pd.DataFrame(macizo_rocoso)
    df_maciza_rocoso.index=["DENSIDAD DE ROCA","MODULO DE ELASTICIDAD","RESISTENCIA A COMPRESION SIMPLE","DIRECCION DE LA CARA LIBRE"]
    col2.write(df_maciza_rocoso)
    with col2.expander("FORMULAS PARA EL CALCULO", expanded=False):
        image = Image.open('imagenes\young.jpg')
        st.write("**Para el calculo se utilizo el modelo 3 (E=0.12*UCS)**")
        st.image(image, caption='MODELOS PARA EL CÁLCULO DEL MÓDULO DE YOUNG')
        image3 = Image.open('imagenes\jfactores.jpg')
        st.image(image3, caption='Factores')
        
    col1a, col2a = st.columns([2, 2])
    espaciamiento_s1=col1.number_input('Espaciamiento',value=0.13)
    buzamiento_s1=col1.number_input('Buzamiento',value=34)
    direccion_buzamiento_s1=col1.number_input('Direccion de buzamiento',value=295)
    tamaño_de_bloque_insitu_s1=col1.number_input('Tamaño de bloque in-situ',value=0.2)
    rmd=10+(10*(tamaño_de_bloque_insitu_s1))
    jps=0
    if (espaciamiento_s1<0.1):
        jps=10
    elif (0.1<=espaciamiento_s1<0.5):
        jps=20
    else:
        jps=50
    jpa=0
    if (buzamiento_s1<10):
        jpa=10
    elif (abs(direccion_buzamiento_s1-direccion_cara_libre_mineral)<30):
        jpa=20
    elif (60<abs(direccion_buzamiento_s1-direccion_cara_libre_mineral)):
        jpa=30
    else:
        jpa=40
    rdi=(25*(densidad_roca_mineral)-50)
    hf=0
    if (modulo_de_elasticidad_mineral<=50):
        hf=(modulo_de_elasticidad_mineral/3)
    else:
        hf=(resostencia_compresion_simple_mineral)/5
    indice_volabilidad=0.06*(rmd+jps+jpa+rdi+hf) 
    
    col1b, col2b = st.columns([2, 2])

    resumen = pd.DataFrame({
        'INDICE DE VOLABILIDAD': indice_volabilidad
        }, index=[0])

    tabla_plotly=resumen.T
    tabla_plotly['index'] = tabla_plotly.index
    tabla_plotly.columns = ['CARACTERÍSTICA','VALOR']
    tabla_plotly = tabla_plotly[['CARACTERÍSTICA','VALOR']]
    tabla_plotly['CARACTERÍSTICA'] = tabla_plotly['CARACTERÍSTICA'].apply(lambda x: '{:.2f}'.format(x))
    fig3 = go.Figure(data=[go.Table(
    header=dict(values=list(tabla_plotly.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[tabla_plotly.VALOR,tabla_plotly.CARACTERÍSTICA],
               fill_color='lavender',
               align='left'))
])
    fig3['layout'].update(height=500,width=200)
    col2.plotly_chart(fig3, use_container_width=True)
