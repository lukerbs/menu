import cv2
import time
import screeninfo

def showImage(filename):
     screen_id = 0
     screen = screeninfo.get_monitors()[screen_id]
     W, H = screen.width, screen.height

     raw_img = cv2.imread(filename)

     height, width, depth = raw_img.shape

     scaleWidth = float(W)/float(width)
     scaleHeight = float(H)/float(height)

     if scaleHeight > scaleWidth:
          imgScale = scaleWidth
     else:
          imgScale = scaleHeight

     newX, newY = raw_img.shape[1]*imgScale, raw_img.shape[0]*imgScale

     resized_img = cv2.resize(raw_img, (int(newX),int(newY)))

     window_name = 'projector'
     cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
     cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

     cv2.imshow(window_name, resized_img)
     time.sleep(1) 
     cv2.waitKey(1) 
     cv2.destroyAllWindows()

files = ['imgs/1.png', 'imgs/2.png', 'imgs/3.png', 'imgs/4.png']

for i in range(5):
     for j in range(len(files)):
          showImage(files[j])