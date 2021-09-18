from os import write
from pickle import POP
from google.protobuf.symbol_database import Default
import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import pandas as pd
import streamlit.components.v1 as components
import math
import altair as alt
import plotly.express as px
import plotly.graph_objects as go


    
def main():
    st.title('FRAGMENTACION DE ROCAS')
    #st.write('En minas subterráneas, el principio básico es proveer la suficiente cantidad de aire fresco a los frentes de trabajo y remover los contaminantes generados como el polvo respirable, productos de combustión del diesel, gases de la mina y el exceso de calor. Por lo que realizar el calculo correcto de esta cantidad es fundamental, en esta oportunidad nos vamos a basar en las leyes de Perú. ')
    st.markdown("<div style='text-align: justify'>La fragmentación de rocas por voladura comprende a la acción de un explosivo y a la consecuente respuesta de la masa de roca circundante, involucrando factores de tiempo, energía termodinámica, ondas de presión, mecánica de rocas y otros, en un rápido y complejo mecanismo de interacción.</div>", unsafe_allow_html=True)
    st.write("")
    st.markdown("<div style='text-align: justify'>Una adecuada fragmentación es importante para facilitar la remoción y transporte del material volado y está en relación directa con el uso al que se destinará este material, lo que calificará a la “mejor” fragmentación. Así, en la explotación de minerales se busca preferentemente fragmentación menuda, que facilita los procesos posteriores de conminución en las plantas metalúrgicas, mientras que en la de rocas algunas veces se requiere que sea en grandes bloques, como los que se emplean para la construcción de ataguías o rompeolas. El desplazamiento y la forma de acumulación del material volado se proyecta de la manera más conveniente para el paleo o acarreo, de acuerdo al tipo y dimensiones de las palas y vehículos disponibles.</div>", unsafe_allow_html=True)
    st.write("")
    st.markdown('## MACIZO ROCOSO')
    col1, col2 = st.columns([2, 2])
    with col2.expander("FORMULA", expanded=False):
        image5 = Image.open('imagenes/j5.jpg')
        st.image(image5)
        image6 = Image.open('imagenes/j6.jpg')
        st.image(image6)
        image7 = Image.open('imagenes/j7.jpg')
        st.image(image7)
        image8 = Image.open('imagenes/j8.jpg')
        st.image(image8)
        pass
    with col1.expander("INPUTS", expanded=False):
        indice_volabilidad_A=st.number_input('Indice de Volabilidad A',value=7)
        altura_banco=st.number_input('Altura de Banco H',value=8)
        burden_B=st.number_input('Burden B',value=6.1)
        espaciamiento_E=st.number_input('Espaciamiento S',value=6.6)    
        volumen_roca_VO=altura_banco*burden_B*espaciamiento_E
        densidad_explosivo=st.number_input('Densidad Explosivo g/cm3',value=1.24)
        diametro=st.number_input('Diámetro m',value=0.149)
        reologia=st.number_input('Reologia Y',value=1.05)
        sobreperforacion=st.number_input('Sobreperforacion m',value=0.8)
        taco=st.number_input('Taco m',value=3.3)
        longitud_carga=altura_banco+sobreperforacion-taco
        carga_explosivo_taladro=reologia*longitud_carga*(math.pi*diametro*diametro/4)*densidad_explosivo*1000
        volumen_explosivo_vf=carga_explosivo_taladro/(densidad_explosivo*1000)
        rws=st.number_input('RWS',value=1.4)
        potencia_explosivo_RWS=rws*100
        grado_alteracion=st.number_input('Grado de Alteracion a1',value=0.8)
        vod=st.number_input('VOD',value=5400)
        presion_detonacion=densidad_explosivo*((vod/1000)*(vod/1000))/4
        ratio_VOD_W_util_gurney=0.2+0.37*densidad_explosivo
        densidad_cj=(4*densidad_explosivo)/3
        ratio_presicion_b_relife=ratio_VOD_W_util_gurney*presion_detonacion/densidad_cj
        ka=1/math.sqrt(ratio_presicion_b_relife)
        esponjamiento=st.number_input('Esponjamiento e',value=(16/100))
        potensia_tensional=(densidad_explosivo*vod*rws*ratio_presicion_b_relife/ratio_VOD_W_util_gurney)/1000
        potencia_empuje=(densidad_explosivo*vod*rws*ratio_VOD_W_util_gurney/ratio_presicion_b_relife)/1000
        sobretamaño=40
        tamaño_promedio=ka*grado_alteracion*indice_volabilidad_A*pow((volumen_roca_VO/carga_explosivo_taladro),0.8)*pow(carga_explosivo_taladro,(1/6))*pow((115/potencia_explosivo_RWS),0.633)
        desviacion=st.number_input('Desviacion W',value=0.1)
        longitud_taladro=altura_banco+sobreperforacion
        diametro_taladro=diametro*1000
        carga_columna=st.number_input('Carga de Columna CL',value=6)
        longitud_carga=st.number_input('Longitud de Carga Lc',value=5.5)
        malla_trabada_ps=1.1
        electronico=1.15
        indice_uniformidad=electronico*(2.2-(14*burden_B/diametro_taladro))*(1-(desviacion/burden_B))*pow(((1+(espaciamiento_E/burden_B))/2),0.5)*(longitud_carga/altura_banco)*malla_trabada_ps
    tamaño_carcteristico=tamaño_promedio/(pow((0.693),(1/indice_uniformidad)))
    lista_tamaños=np.arange(1,101,0.05)
    #lista_tamaños=np.arange(5,105,5)
    lista_pulgadas=lista_tamaños/2.54
    pasantes=[]
    for i in lista_tamaños:
        pasante=1-math.exp((-(i/tamaño_carcteristico)**indice_uniformidad))
        pasantes.append(pasante)
    source = pd.DataFrame({
        'TAMAÑO_DE_FRAGMENTO_(Pulgadas)': lista_pulgadas,
        'PASANTE_(%)': pasantes,'TAMAÑO_DE_FRAGMENTO_(cm)':lista_tamaños
        })

    fig2 = px.line(source, x='TAMAÑO_DE_FRAGMENTO_(Pulgadas)', y='PASANTE_(%)')
    fig2.update_layout(title_text="CURVA GRANULOMÉTRICA")
    fig2.update_xaxes(range=[0, 15])
    st.plotly_chart(fig2, use_container_width=True)
    valores_para_buscar=source['PASANTE_(%)'].values
    valor=st.number_input('VALOR BUSCADO DE PASANTE Px',value=0.5)
    buscado=valores_para_buscar.flat[np.abs(valores_para_buscar-valor).argmin()]
    df_mask=source['PASANTE_(%)']==buscado
    df = source[df_mask]

    st.write(df)
    st.markdown('## RESUMEN')
    resumen = pd.DataFrame({
        'TAMAÑO PROMEDIO (X50)': tamaño_promedio,
        'Indice de Volabilidad (A)': indice_volabilidad_A,
        'Volumen de Roca (Vo)':volumen_roca_VO,
        'Carga de Explosivo por Taladro (Qe)':carga_explosivo_taladro,
        'Volumen de Explosivo (Vf)':volumen_explosivo_vf,
        'Potencia del Explosivo (RWS)':potencia_explosivo_RWS,
        'Grado de Alteracion':grado_alteracion,
        "Ratio VOD W Util (b1)":ratio_VOD_W_util_gurney,
        "Ratio Presicion B Relief (c)":ratio_presicion_b_relife,
        "Reologia (Y)":reologia,
        "Esponjamiento (e)": esponjamiento,
        "Potencia Tensional (wT)":potensia_tensional,
        "Potencia Empuje (wE)":potencia_empuje,
        "SOBRE TAMAÑO":sobretamaño,
        "INDICE DE UNIFORMIDAD (n)":indice_uniformidad,
        "Burden (B)":burden_B,
        "Espaciamiento (E)":espaciamiento_E,
        "Desviacion (W)":desviacion,
        "Longitud Taladro (L)":longitud_taladro,
        "Altura de Banco (H)":altura_banco,
        "Diametro Taladro (D)":diametro_taladro,
        "Carga de Columna (CL)":carga_columna,
        "Longitud de Carga (Lc)":longitud_carga,
        "TAMAÑO CARACTERÍSTICO (Xc)":tamaño_carcteristico,
        "Tamaño promedio (X50)":tamaño_promedio,
        "Indice de Uniformidad (n)":indice_uniformidad
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
    st.plotly_chart(fig3, use_container_width=True)
