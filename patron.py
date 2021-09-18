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
    
    st.title('PARÁMETROS DE DISEÑO DE VOLADURAS EN BANCOS')
    #st.write('En minas subterráneas, el principio básico es proveer la suficiente cantidad de aire fresco a los frentes de trabajo y remover los contaminantes generados como el polvo respirable, productos de combustión del diesel, gases de la mina y el exceso de calor. Por lo que realizar el calculo correcto de esta cantidad es fundamental, en esta oportunidad nos vamos a basar en las leyes de Perú. ')
    st.markdown("<div style='text-align: justify'>También denominados parámetros de la voladura, son datos empleados en el cálculo y diseño de disparos. Unos son invariables, como los correspondientes a las CARACTERÍSTICAs físicas de la roca: densidad, dureza, grado de fisuramiento, coeficientes de resistencia a deformación y rotura, etc; y otros son variables, es decir que podemos modificarlos a voluntad, de acuerdo a las necesidades reales del trabajo y condiciones del terreno. Estos parámetros controlables se pueden agrupar en:</div>", unsafe_allow_html=True)
    st.write("")
    st.markdown("<div style='text-align: justify'>a. Geométricos: altura, ancho y largo del banco, talud, cara libre. </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify'>b. De perforación: diámetro y longitud del taladro, malla. </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify'>c. De carga: densidad, columna explosiva, longitud de taco, características físico-químicas del explosivo.  </div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify'>d. De tiempo: tiempos de retardo entre taladros, secuencia de salidas de los disparos.  </div>", unsafe_allow_html=True)
    st.write("")
    st.markdown("<div style='text-align: justify'>A continuación, se describen las formulas para hallar los parámetros iniciales de diseño, los cuales deben de ser ajustados según la mina donde se esté trabajando.</div>", unsafe_allow_html=True)
    st.markdown('## PATRON DE VOLADURA')
    col1, col2 = st.columns([2, 2])
    
    with col2.expander("FORMULAS", expanded=False):
        image_patron1 = Image.open('imagenes/j3.jpg')
        st.image(image_patron1)
        image_patron2 = Image.open('imagenes/j2.jpg')
        st.image(image_patron2)
    diametro_pulgada=col1.number_input('Diámetro pulg',value=6.75)
    densidad_explosivo=col1.number_input('Densidad Explosivo',value=1.2)
    potencia_explosivo=col1.number_input('Potencia Explosivo',value=1.2)
    diametro_milimetro=diametro_pulgada*2.54/100
    col1a, col2a = st.columns([1, 3])

    Kb=25*math.sqrt(densidad_explosivo*potencia_explosivo/0.8*1)

    Ks=1.15

    Kj=0.3

    Kt=0.7

    

    burden_m=Kb*diametro_milimetro

    espaciamiento=burden_m*Ks

    sobreperforacion=burden_m*Kj

    taco=burden_m*Kt



    resumen = pd.DataFrame({
        'Diámetro (mm)': diametro_milimetro,
        'KB': Kb,
        'KS':Ks,
        'Kj':Kj,
        'Kt':Kt,
        'Burden (m)':burden_m,
        'Espaciamiento (m)':espaciamiento,
        "Sobreperforacion (m)":sobreperforacion,
        "Taco (m)":taco
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
    fig3['layout'].update(height=1000,width=1600)
    col2.plotly_chart(fig3, use_container_width=True)




    
