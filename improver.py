def improver(file_name,file_name2):
    import cv2
    import math
    image = cv2.imread(file_name)
    # height, width, _ = image.shape
    base_image = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7,7),0)
    thresh = cv2.threshold(blur, 0, 255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    kernal = cv2.getStructuringElement(cv2.MORPH_RECT,(30,20))
    dilate = cv2.dilate(thresh, kernal, iterations=1)
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])
    i = 0
    x_value=[]
    x_values=[]

    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        x_value.append(x)
        x_values.append(x)

    x_values.sort()

    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        if w > 300 and y > 0 and x > 50:
            h = 950-100
            y = 50
            w = 1200
            roi = image[y:y+h, x:x+w]
            cv2.imwrite(file_name2,roi)
            cv2.rectangle(base_image,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imwrite("temp/roi.png",base_image)                                                                                     