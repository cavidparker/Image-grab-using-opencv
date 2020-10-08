import numpy as np
import cv2
import pyscreenshot as ImageGrab

while(True):
    img = ImageGrab.grab(bbox=(107, 157, 841, 540))
    # img_np = np.array(img)
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    cv2.imshow("frame", frame)
    cv2.waitKey(1)
cv2.destroyAllWindows()