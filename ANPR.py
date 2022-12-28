import cv2
from PIL import Image
import easyocr
import numpy as np
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import aiocv
import matplotlib.pyplot as plt
 
# creating list

# creating numpy array

 
# path=_file_.split("\\")

# path.append("haarcascades")
# path="\\".join(path)
im = Image.open(r"C:\\Users\\Aman Sagar\\Desktop\\WhatsApp Image 2022-09-04 at 11.36.01 AM.jpeg")
img = cv2.imread("C:\\Users\\Aman Sagar\\Desktop\\WhatsApp Image 2022-09-04 at 11.36.01 AM.jpeg")


n= cv2.CascadeClassifier('C:\\Users\\Aman Sagar\\Desktop\\plate.xml')

  
# Applying the face detection method on the grayscale image
faces_rect = n.detectMultiScale(img, 1.1, 4)
car = aiocv.NumberPlateDetector(img)
# Use findNumberPlate() Method To Detect Number Plate On Image/Video
car.findNumberPlate()



imgplot = plt.imshow(img)
plt.show()
# Iterating through rectangles of detected faces
for (x, y, w, h) in faces_rect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 100)
    left = x
    top = y
    right = x+w
    bottom = y+h

im1 = im.crop((left, top, right, bottom))
# im1.show()
imgplot = plt.imshow(im1)
plt.show()
sample_array = np.array(im1)
reader = easyocr.Reader(['en'],gpu=True)
# result = reader.readtext(cv2.imread(Cropped_loc))
result = reader.readtext(sample_array)
c=str(result[0][1])
print(c)

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\Aman Sagar\\Desktop\\creds1.json", scope)

client = gspread.authorize(creds)

sheet = client.open("hello_world").sheet1  # Open the spreadsheet

# data = sheet.get_all_records()

# data_df = pd.DataFrame.from_dict(str(result[0][1]))
sheet.update_cell(2,6,c)