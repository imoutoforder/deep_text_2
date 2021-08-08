import easyocr
import cv2
import matplotlib.pyplot as plt

reader = easyocr.Reader(['fa'], recog_network = 'our_model_300000')
img = cv2.imread('/home/yousef/Desktop/mehdiBagheri.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img.shape)
result = reader.readtext(img)
print(result)


for (bbox, text, prob) in result: 
  # unpack the bounding box
  print(prob)
  (tl, tr, br, bl) = bbox
  tl = (int(tl[0]), int(tl[1]))
  tr = (int(tr[0]), int(tr[1]))
  br = (int(br[0]), int(br[1]))
  bl = (int(bl[0]), int(bl[1]))
  cv2.rectangle(img, tl, br, (0, 255, 0), 2)
  cv2.putText(img, text, (tl[0], tl[1] - 10),
    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
cv2.imwrite("./after.jpg", img)


