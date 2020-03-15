import requests
import cv2
import numpy as np

captura = cv2.VideoCapture("http://192.168.1.34:8080/shot.jpg")

url = "http://192.168.1.34:8080/shot.jpg"

ancho = int(captura.get(cv2.CAP_PROP_FRAME_WIDTH))
alto = int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT))

codigo = cv2.VideoWriter_fourcc(*'mp4v')
grabador = cv2.VideoWriter('video.mp4',codigo,20,(ancho,alto))

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content),dtype = np.uint8)
    img = cv2.imdecode(img_arr,-1)

    cv2.imshow("AndroidCam",img)
    if cv2.waitKey(1) == 27:
        break
    grabador.write(img) 
    
#cerrar las ventanas
captura.release()
cv2.destroyAllWindows()