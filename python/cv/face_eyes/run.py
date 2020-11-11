import cv2 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 
cap = cv2.VideoCapture(0) 

while 1: 
    ret, img = cap.read() 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 

    offset_x = 0
    offset_y = -30

    for (x,y,w,h) in faces: 
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = img[y:y+h, x:x+w] 
        eyes = eye_cascade.detectMultiScale(roi_gray) 
        for (ex,ey,ew,eh) in eyes: 

            # Leer pixeles.
            for i in range(ew):
                for j in range(eh):
                    rgb = roi_color[ey+j, ex+i]

                    r = int(rgb[0])
                    g = int(rgb[1])
                    b = int(rgb[2])

                    cv2.circle(roi_color, (ex+i+offset_x, ey+j+offset_y), radius=0, color=(int(r), int(g), int(b)), thickness=-1)

            # Rectangulo
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2) 

    cv2.imshow('img',img) 
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break

cap.release() 
cv2.destroyAllWindows() 


