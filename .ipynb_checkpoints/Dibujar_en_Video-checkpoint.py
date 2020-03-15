import requests
import cv2
import numpy as np

captura = cv2.VideoCapture("http://192.168.1.34:8080/shot.jpg")

url = "http://192.168.1.34:8080/shot.jpg"

ancho = int(captura.get(cv2.CAP_PROP_FRAME_WIDTH))
alto = int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Esquina izquierda del Rectangulo
x = 300
y = 300

# Dimensiones del Rectangulo
w = ancho // 4
h = alto // 4

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content),dtype = np.uint8)
    img = cv2.imdecode(img_arr,-1)
    
    # Dibujamos el Rectangulo
    cv2.rectangle(img, (x, y), ((x+w),(y+h)), color = (255,0,0), thickness = 4)
    
    cv2.imshow("Nuestro Video con Rectangulo", img)
    if cv2.waitKey(1) == 27:
        break
captura.release()
cv2.destroyAllWindows()