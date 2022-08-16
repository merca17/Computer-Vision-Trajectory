# @autor: Juan Mercado
# date: 14-07-22
from pickle import FALSE
import xlsxwriter
import numpy as np
import imutils
import cv2

webcam = cv2.VideoCapture(1) # Selección de la camara

while True:
    cv2.namedWindow("espacio", 1) 
    cv2.resizeWindow("espacio", 480,480) # tamaño
    ret, espacio = webcam.read() # lectura
    if ret == FALSE:
        print("no se ha podido accedeer a la camara")
        break
    # para visualizar en blanco y negro:
    imagen_grayscale = cv2.cvtColor(espacio, cv2.COLOR_BGR2GRAY) #  
    thresh, imagen_blk_wht = cv2. threshold(imagen_grayscale, 140, 255, cv2.THRESH_BINARY)
    cv2.imshow('espacio',imagen_blk_wht)
    # teclas escape para salir y s para tomar fotografía    
    if cv2.waitKey(1)%256 == 27:
        print("se ha presionado la tecla escape")
        break
    elif cv2.waitKey(1) == ord('s'):
        screenshot = "foto.png" # se crea el objeto 
        cv2.imwrite(screenshot, espacio) # se imprime en el objeto el valor actual de la webcam
        print("imagen tomada")
        # numero de subdivisiones de la imagen:
        m = 30
        n_filas = m
        n_columnas = m
        # lectura de la imagen a procesar
        preimg = cv2.imread("foto.png") 
        imagen = preimg[0:480,0:480] # restricción de tamaño
        # acondicionamiento de la imagen
        imagen_grayscale = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(imagen_grayscale,(5,5),0) 
        thresh, imagen_blk_wht = cv2. threshold(blurred, 140, 255, cv2.THRESH_BINARY_INV)
        print(imagen_blk_wht)
        # a: ancho b:alto
        a = int(imagen_blk_wht.shape[0]) 
        b = int(imagen_blk_wht.shape[1]) 
        print(a, b)
        coordenadas = [] # lista de coordenadas
        scala = 10 # valor de escala de posición, depende de la altura de la camara
        # subdivisión de la imagen
        n = 0
        for i in range(0,n_filas):
            for j in range(0,n_columnas):
                roi = imagen_blk_wht[int(i*a/n_filas):int(i*a/n_filas+a/n_filas),int(j*b/n_columnas):int(j*b/n_columnas+b/n_columnas)] #subimagen
                cnts= cv2.findContours(roi.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #busqueda de contornos
                cnts = imutils.grab_contours(cnts) # se guarda el contorno
                for c in cnts:
                    M = cv2.moments(c) #momento de area
                    if M["m00"] != 0:
                        n=n+1
                        # centros del momento de area
                        cX = int(M["m10"]/M["m00"])  
                        cY = int(M["m01"]/M["m00"])
                        cv2.circle(imagen,(int( cY+j*b/n_columnas),int(cX+i*a/n_filas)),5,(0,0,255),-1) # se dibujan los puntos encontrados sobre la imagen
                        xy = [(cY+j*b/n_columnas)/scala,(cX+i*a/n_filas)/scala]
                        coordenadas.append(xy) # se guardan los datos en la lista
                        cv2.imshow('imagen',imagen) # se muestra la imagen con los puntos encontrados
        muestreo = "foto2.png"          # se guarda la imagen con los puntos 
        cv2.imwrite(muestreo, imagen)   # en foto2
        print(coordenadas) 
        # Ordenamiento de puntos
        sorted_coord = sorted({tuple(x): x for x in coordenadas}.values())        
        print(sorted_coord)
        sampled_coord = [] # lista de coordenadas muestreadas
        for m in range(1, len(sorted_coord),1): # muestreo con pasos de a 1 
            sampled_coord.append(sorted_coord[m]) 
        # sección de prueba
        with xlsxwriter.Workbook('test.xlsx') as workbook:
            worksheet = workbook.add_worksheet()

            for row_num, data in enumerate(sampled_coord):
                worksheet.write_row(row_num, 0, data)         
        break

webcam.release()
cv2.destroyAllWindows()