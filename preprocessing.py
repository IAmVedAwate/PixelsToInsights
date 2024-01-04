
def preprocessor(img_path, file_name):
    import improver as im
    import cv2
    from matplotlib import pyplot as plt 
    
    image_file = img_path
    img = cv2.imread(image_file)

    inverted_image = cv2.bitwise_not(img)
    cv2.imwrite("temp/inverted.png",inverted_image)

    def grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray_image = grayscale(img)

    thresh, im_bw = cv2.threshold(gray_image, 69, 240, cv2.THRESH_BINARY)

    def noise_removal(image):
        import numpy as np 
        kernel = np.ones((1,1), np.uint8)
        image = cv2.dilate(image, kernel, iterations=1)
        kernel = np.ones((1,1), np.uint8)
        image = cv2.erode(image, kernel, iterations=1)
        image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        image = cv2.medianBlur(image, 1)
        return (image)

    no_noise = noise_removal(im_bw)
    inverted_image2 = cv2.bitwise_not(no_noise)
    cv2.imwrite(file_name,inverted_image2)
    file_name2 = file_name.replace("inverted", "crop").replace("temp3","temp2")
    
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