import cv2

# configurable parameters
source="Ritik.jpeg"
dest="newImage.jpeg"
scale=50
src = cv2.imread("Ritik.jpeg",cv2.IMREAD_UNCHANGED)
# cv2.imshow("title",image)
# cv2.waitKey(0)

new_width=int(src.shape[1]*scale/100)
new_height=int(src.shape[0]*scale/100)

output=cv2.resize(src,(new_width,new_height))

cv2.imwrite(dest,output)
