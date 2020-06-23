import cv2

face_class=cv2.CascadeClassifier('harcascades/haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(0)
if not cap.isOpened():
	print("Could not Open Camera")
	exit(1)

cap.set(cv2.cv2.CAP_PROP_FPS,60)


def detect_face():
	global cap,face_class
	print("Press Q to quit\nWait Loading Camera...")
	while True:
		ret,frame=cap.read()
		faces=face_class.detectMultiScale(frame,1.2,3)
		
		for x,y,w,h in faces:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
			cv2.imshow('Face Detection',frame)
		if cv2.waitKey(1) & 0xFF==ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()


detect_face()