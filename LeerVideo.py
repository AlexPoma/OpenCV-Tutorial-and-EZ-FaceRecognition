import cv2
import time

captura = cv2.VideoCapture('video.mp4')

if captura.isOpened() == False:
    print('Error al abrir el fichero de video')
    
while captura.isOpened():
    
    resultado, video = captura.read()
    time.sleep(0.03)
    if resultado == True:
        
        cv2.imshow('Mi video', video)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
            
captura.release()
cv2.destroyAllWindows()