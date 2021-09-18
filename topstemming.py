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
    
    st.title('SCALED DEPTH OF BURIAL CALCULATION')
    #st.write('En minas subterráneas, el principio básico es proveer la suficiente cantidad de aire fresco a los frentes de trabajo y remover los contaminantes generados como el polvo respirable, productos de combustión del diesel, gases de la mina y el exceso de calor. Por lo que realizar el calculo correcto de esta cantidad es fundamental, en esta oportunidad nos vamos a basar en las leyes de Perú. ')
    col1a, col2a = st.columns([3, 1])
    col1a.markdown("<div style='text-align: justify'>Normalmente el taladro no se llena en su parte superior o collar, la que se rellena con material inerte que tiene la función de retener a los gases generados durante la detonación, sólo durante fracciones de segundo, suficientes para evitar que estos gases fuguen como un soplo por la boca del taladro y más bien trabajen en la fragmentación y desplazamiento de la roca en toda la longitud de la columna de carga explosiva.</div>", unsafe_allow_html=True)
    col1a.write("")
    #st.markdown("<div style='text-align: justify'>a. Geométricos: altura, ancho y largo del banco, talud, cara libre. </div>", unsafe_allow_html=True)
    #st.markdown("<div style='text-align: justify'>b. De perforación: diámetro y longitud del taladro, malla. </div>", unsafe_allow_html=True)
    #st.markdown("<div style='text-align: justify'>c. De carga: densidad, columna explosiva, longitud de taco, CARACTERÍSTICAs físico-químicas del explosivo.  </div>", unsafe_allow_html=True)
    #st.markdown("<div style='text-align: justify'>d. De tiempo: tiempos de retardo entre taladros, secuencia de salidas de los disparos.  </div>", unsafe_allow_html=True)
    col1a.markdown("<div style='text-align: justify'>Si no hay taco los gases se escaparán a la atmósfera arrastrando un alto porcentaje de energía, que debería actuar contra la roca. Si el taco es insuficiente, además de la fuga parcial de gases se producirá proyección de fragmentos, craterización y fuerte ruido por onda aérea. Si el taco es excesivo, la energía se concentrará en fragmentos al fondo del taladro, dejando gran cantidad de bloques o bolones en la parte superior, especialmente si el fisuramiento natural de la roca es muy espaciado, resultando una fragmentación irregular y poco esponjada y adicionalmente se generará fuerte vibración. Normalmente como relleno se emplean los detritos de la perforación que rodean al taladro, arcillas o piedra chancada fina y angulosa. En ocasiones en taladros inundados se deja el agua como taco cuando la columna de carga es baja (también en voladura subacuática). En la práctica su longitud usual es de 1/3 del largo total del taladro. Si se tiene en cuenta al burden y resistencia de la roca, el taco variará entre T = 0,7 B para material muy competente, como granito homogéneo, o en un radio de taco o burden que puede aproximarse a 1, es decir: T = B para material incompetente con fisuras y fracturas abiertas. En esta ocasión usaremos la formula de Rangos de distancia escalada.</div>", unsafe_allow_html=True)
    image_patron12 = Image.open('imagenes/KL8.jpg')
    col2a.image(image_patron12)
    st.markdown('## PATRON DE VOLADURA')
    col1, col2, col3 = st.columns([2, 2, 2])
    
    with col2.expander("FORMULAS", expanded=False):
        image_patron1 = Image.open('imagenes/K1.jpg')
        st.image(image_patron1)
        image_patron2 = Image.open('imagenes/K9.jpg')
        st.image(image_patron2)
    longitud_taladro=col1.number_input('Largo del Taladro (m)',value=10.0)
    diametro_taladro=col1.number_input('Diametro del Taladro (pulg)',value=5.98)
    taco=col1.number_input('Taco (m)',value=3.66)
    densidad=col1.number_input('Densidad (gr/cc)',value=1.25)
    burden = col1.number_input('Burden',value=10.0)
    espaciamiento = col1.number_input('Espaciamiento',value=10.0)
    dennsidad_roca = col1.number_input('Densidad Roca',value=2.54)

    carga_lineal=diametro_taladro*diametro_taladro*densidad*0.507
    peso=(longitud_taladro-taco)*carga_lineal
    w=diametro_taladro*(2.54/10)*carga_lineal
    D=taco+(0.5*2.54*(diametro_taladro/10))
    SD=D/(pow(w,(1/3)))
    factor_carga=peso/(burden*espaciamiento)
    factor_carga_ton=peso*1000/(burden*espaciamiento*dennsidad_roca*longitud_taladro)

    resumen = pd.DataFrame({
        'Carga Lineal (kg/m)': carga_lineal,
        'Peso del Explosivo': peso,
        'W':w,
        'D':D,
        'Factor de Carga (Kg/m3)':factor_carga,
        "Factor de Carga (g/Ton)":factor_carga_ton,
        'SDoB (m/kg^1/3)':SD
        
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
    fig3['layout'].update(height=450,width=300)
    col2.plotly_chart(fig3, use_container_width=True)
    espacios="--------------"
    col2.write(f"**{espacios}El SDoB =** {round(SD,2)} (m/kg^1/3)**{espacios}**")

    if (0<SD<=0.62):
        image_patron33 = Image.open('imagenes/K7.jpg')
        col3.image(image_patron33)
    elif (0.64<SD<=0.90):
        image_patron33 = Image.open('imagenes/K6.jpg')
        col3.image(image_patron33)
    elif (0.90<SD<=1.42):
        image_patron33 = Image.open('imagenes/K5.jpg')
        col3.image(image_patron33)
    elif (1.42<SD<=1.82):
        image_patron33 = Image.open('imagenes/K4.jpg')
        col3.image(image_patron33)
    elif (1.82<SD<=2.42):
        image_patron33 = Image.open('imagenes/K3.jpg')
        col3.image(image_patron33)
    else:
        image_patron33 = Image.open('imagenes/K2.jpg')
        col3.image(image_patron33)
