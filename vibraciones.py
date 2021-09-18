import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()



#---------------------------------------------
def main():
    st.title('PREDICCIÓN DE VELOCIDAD DE PARTÍCULA – HOLMBERG & PERSSON (1994)')
    #st.write('En minas subterráneas, el principio básico es proveer la suficiente cantidad de aire fresco a los frentes de trabajo y remover los contaminantes generados como el polvo respirable, productos de combustión del diesel, gases de la mina y el exceso de calor. Por lo que realizar el calculo correcto de esta cantidad es fundamental, en esta oportunidad nos vamos a basar en las leyes de Perú. ')
    col1A, col2A = st.columns([3, 1])
    col1A.markdown("<div style='text-align: justify'>Muchos autores han realizado una integración de las ondas provenientes desde cada zona de la carga, tomando en consideración la diferencia de tiempos en que las ondas llegan al punto P. Sin embargo, la velocidad máxima de partícula, y en específico el punto máximo de estrés en la roca no ocurre cuando las primeras ondas producto de la tronadura arriban al punto P. Esto acontece cuando las ondas se propagan a través del macizo rocoso y se encuentran con una cara libre (vacío) que genera una onda de tensión reflejada. Por lo tanto, las diferencias de tiempo entre las llegadas de ondas son tan cortas que simplemente no se consideran como un problema para los cálculos. La velocidad de vibración V resultante de una unidad de carga W a una distancia R es dada por:</div>", unsafe_allow_html=True)
    image_patron15 = Image.open('imagenes\j15.jpg')
    col2A.image(image_patron15)
    
    st.write("")
    st.markdown('## VIBRACIONES')
    ############Taladro##########
    col1, col2 = st.columns([2, 2])
    with col2.expander("FORMULAS", expanded=False):
        image_patron11 = Image.open('imagenes\j11.jpg')
        st.image(image_patron11)
        image_patron12 = Image.open('imagenes\j12.jpg')
        st.image(image_patron12)
        image_patron13 = Image.open('imagenes\j13.jpg')
        st.image(image_patron13)
        image_patron14 = Image.open('imagenes\j14.jpg')
        st.image(image_patron14)
    with col1.expander("INPUTS", expanded=False):
        d=st.number_input('Diametro [mm]',value=200) #Diametro [mm]
        de=st.number_input('Densidad del Explosivo [g/cc]',value=1.1) #Densidad del Explosivo [g/cc]
        taco=st.number_input('Taco [m]',value=6) #Taco [m]
        lc=st.number_input('Longitud de Carga [m]',value=9) #Longitud de Carga [m]
        k=st.number_input('k',value=700)
        alpha=st.number_input('Alpha',value=0.7) #Parametro alpha
        ############Malla#########
        xmin=st.number_input('Valor minimo de X[m]',value=-10) #Valor minimo de X[m]
        xmax=st.number_input('Valor maximo de X[m]',value=10) #Valor maximo de X[m]
        ymin=st.number_input('Valor minimo de Y[m]',value=0)  #Valor minimo de Y[m]
        ymax=st.number_input('Valor maximo de Y[m]',value=20)  #Valor maximo de Y[m]
        paso=st.number_input('Paso del Dominio [m]',value=0.1)  #Paso del Dominio [m]

    u=[] #ticks
    listavpp=[]
    contador=0
    


    fig,ax=plt.subplots()

    ax.set_xlabel("Distancia X[m]",color="r")
    ax.set_ylabel("Distancia Y[m]",color="r")
    plt.gca().invert_yaxis()
    plt.title("Campo de Velocidades de Particula")

    

    #----------------Dominios---------------
    x=np.arange(xmin,xmax+paso,paso)
    y=np.arange(ymin,ymax+paso,paso)
    X,Y=np.meshgrid(x,y)
   
    #----------Parametros iniciales---------
    H=lc
    xc=10
    z1=taco
    z2=z1+H
    l=de*((d/1000)**2)*1000/4 
    yp=(z1+z2)/2
    print(yp)
    v = (k*((l/np.abs(X))**alpha)*(np.arctan((z2-Y)/np.abs(X))+np.arctan((Y-z1)/np.abs(X)))**alpha)/1000
    d=d/1000
    _v= (k*((l/np.abs(0.5*d))**alpha)*(np.arctan((z2-yp)/np.abs(0.5*d))+np.arctan((yp-z1)/np.abs(0.5*d)))**alpha)/1000

    


    if contador==0:
        u=[0.01*_v,0.05*_v,0.2*_v,0.5*_v,0.7*_v,0.9*_v,_v]
        cf=ax.contourf(X,Y,v,u,cmap="jet",alpha=0.6,extend="both")
        ax_bar=fig.add_axes([0.87,0.15,0.02,0.70],anchor="SW")
        cb=fig.colorbar(cf,cax=ax_bar,ticks=u)
        
    else:
        cf=ax.contourf(X,Y,v,u,cmap="jet",alpha=0.6,extend="both")
        ax_bar=fig.add_axes([0.87,0.15,0.02,0.70],anchor="SW")
        cb=fig.colorbar(cf,cax=ax_bar,ticks=u) 
    
    contador=contador+1

    ax.set_xlabel("Distancia X [m]",color="r")
    ax.set_ylabel("Distancia  Y [m]",color="r")
    ax.grid(True,color="lightgray")
    

    fig.subplots_adjust(bottom=0.12)
    fig.subplots_adjust(top=0.90)
    fig.subplots_adjust(left=0.13)
    fig.subplots_adjust(right=0.85)
    st.write(fig)




