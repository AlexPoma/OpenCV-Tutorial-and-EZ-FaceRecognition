import requests
import cv2
import numpy as np
import matplotlib.pyplot as plt

cascada_cara = cv2.CascadeClassifier('XML/haarcascade_frontalface_default.xml')

def detectar_cara(imagen):
    imagen1 = imagen.copy()
    rectangulos = cascada_cara.detectMultiScale(imagen1)
    for (x,y,w,h) in rectangulos:
        cv2.rectangle(imagen1,(x,y),(x+w,y+h),(255,0,0),10)
    return imagen1

url = "http://192.168.1.34:8080/shot.jpg"

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content),dtype = np.uint8)
    img = cv2.imdecode(img_arr,-1)
    
    # Dibujamos el Rectangulo
    img = detectar_cara(img)
    
    cv2.imshow("Detectar Cara en Video", img)
    
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()