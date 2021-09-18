import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

def main():
    lgit = """<a href='https://github.com/CartagenaMinas/VentiST' target="_blank">Github</a>"""
    st.title('MODELOS Y FÓRMULAS PARA VOLADURA SUPERFICIAL')
    st.write("")
    st.write("")
    col1, col2 = st.columns([2, 2])
    #col1.write('Bienvenidos en esta app donde se podra calcular el requerimiento de aire necesario para Minería Subterránea.')
    #col1.write(f'\n  Si quieres quieres conocer el codigo de esta app escrito en python puedes visitarlo en el siguiente enlace de {lgit}.', unsafe_allow_html=True)
    #col1.write("Tambien puedes visitar nuestra pagina web IDL Mining donde subimos post sobre programacion orientado a la ingeniera de minas y nos dedicamos a la creacion de Modelos de Deep Learning.")
    col1.write("")
    col1.write("")
    col1.write("")
    col1.write("")
    col1.markdown("<div style='text-align: justify'>Esta app está enfocada a ser de guía para las personas que están estudiando perforación y voladura. Para este ejemplo vamos a aplicar diferentes formulas y modelos para calcular el patrón de voladura, campo de velocidad pico partícula, índice de volabilidad, calculo de taco optimo, está diseñado en Python para que los estudiantes se familiaricen con el lenguaje de programación.</div>", unsafe_allow_html=True)
    #col1.markdown("<div style='text-align: justify'>Si quieres quieres conocer el codigo de esta app escrito en python puedes visitarlo en el siguiente enlace <a style='color:black; font-size:110% ;' href='https://github.com/CartagenaMinas/clasificacion-rocas' target='_blank'><i class='fa fa-rocket'></i>GitHub</a> </div>", unsafe_allow_html=True)
    col1.write("")
    col1.markdown("<div style='text-align: justify'>Tambien puedes visitar nuestra pagina web IDL Mining donde subimos post sobre programacion orientado a la ingeniera de minas y nos dedicamos a la creacion de Modelos de Deep Learning.</div>", unsafe_allow_html=True)
    
    image = Image.open('imagenes/j20.jpg')
    col2.write("")
    col2.image(image, caption='MODELOS Y FÓRMULAS PARA VOLADURA SUPERFICIAL')
    st.write('### CREATED BY CRISTIAN CARTAGENA MATOS')
    components.html(
        """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <a style="color:black; font-size:110% ;" href="https://www.linkedin.com/in/cristiancartagenamatos/" target="_blank"><i class="fa fa-linkedin-square"></i>Linkedin</a>
        <a style="color:black; font-size:110% ;" href="https://github.com/CartagenaMinas" target="_blank"><i class="fa fa-github"></i>Github</a>
        <a style="color:black; font-size:110% ;" href="http://www.idlmining.com/" target="_blank"><i class="fa fa-rocket"></i>IDL Mining</a>
        """  , height=600)

