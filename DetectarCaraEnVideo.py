import cv2
import time
import numpy as np
import matplotlib.pyplot as plt

captura = cv2.VideoCapture('video.mp4')
cascada_cara = cv2.CascadeClassifier('XML/haarcascade_frontalface_default.xml')

def detectar_cara(imagen):
    imagen1 = imagen.copy()
    rectangulos = cascada_cara.detectMultiScale(imagen1)
    for (x,y,w,h) in rectangulos:
        cv2.rectangle(imagen1,(x,y),(x+w,y+h),(255,0,0),10)
    return imagen1

if captura.isOpened() == False:
    print('Error al abrir el fichero de video')
    
while captura.isOpened():
    
    resultado, video = captura.read()
    #time.sleep(0.0001)
    video = detectar_cara(video)
    if resultado == True:
        
        cv2.imshow('Detectar Cara en Video', video)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
            
captura.release()
cv2.destroyAllWindows()