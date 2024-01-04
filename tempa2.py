# import pytesseract
import cv2
import math
image = cv2.imread("temp/test1.png")
height, width, _ = image.shape
base_image = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("temp/index2.png",gray)
blur = cv2.GaussianBlur(gray, (7,7),0)
cv2.imwrite("temp/index3.png",blur)
thresh = cv2.threshold(blur, 0, 255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
cv2.imwrite("temp/index4.png",thresh)
kernal = cv2.getStructuringElement(cv2.MORPH_RECT,(20,18))
cv2.imwrite("temp/index5.png",kernal)
dilate = cv2.dilate(thresh, kernal, iterations=1)
cv2.imwrite("temp/index6.png",dilate)
cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])
i = 0
x_value=[]
x_values=[]
y_value=[]
y_extra=[]
w_value=[]
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    x_value.append(x)
    x_values.append(x)
    y_value.append(y)
    y_extra.append(y)
    w_value.append(w)

x_values.sort()
y_value.sort()
w_value.sort()
print(x_values)
print(f"y: {y_value}")
print(f"w: {w_value}")
best = []

for k in x_values:
    if k > (x_values[math.ceil((len(x_values)/2))]-100) and k < (x_values[math.ceil((len(x_values)/2))]+300):
        best.append(k)

x_subtitute = min(best)
y_subtitute = y_value[1]
width_best = []

for j in range(len(x_values)):
    # print(f"{k} , {j}")
    if y_extra[j] < 200  and x_values[j] > (max(x_values)-350):
        width_best.append(x_values[j])

print(width_best)
# index_value=[]
# for b in best:
#     if b in x_value:
#         index_value.append(x_value.index(b))

# print(f"indexes:  {set(index_value)}")
# for c in cnts:
#     x,y,w,h = cv2.boundingRect(c)
    
#     if w > 120:
#         print(f"{c}:  {y},{h} ")
#         roi = image[y:y+h, x:x+h]
#         cv2.imwrite("temp/index7.png",roi)
#         cv2.rectangle(base_image,(x,y),(x+w,y+h),(0,255,0),2)
w = min(width_best)
x = x_subtitute
y = y_subtitute
h = height-y-80
roi = image[y:y+h, x:x+h]
cv2.imwrite("temp/index7.png",roi)
cv2.rectangle(base_image,(x,y),(w,y+h),(0,255,0),2)
cv2.imwrite("temp/index8.png",base_image)                                                                                     