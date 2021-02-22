import numpy as np
import cv2

size = 255

#чорный злева
horizontal_gradient1 = np.zeros((size,size))

for i in range(size):
    for j in range(size):
         horizontal_gradient1[i][j] =  j 

print(horizontal_gradient1,'\n')
cv2.imwrite('C:/digitalprocessing/numpy/horizontal_grad1.jpg', horizontal_gradient1)


#чорный зправа
horizontal_gradient2 = np.zeros((size,size))

for i in range(size):
    for j in range(size):
         horizontal_gradient2[i][j] = size - j
        
print(horizontal_gradient2,'\n')
cv2.imwrite('C:/digitalprocessing/numpy/horizontal_grad2.jpg', horizontal_gradient2)


#чорний зверху
vertical_gradient1 = np.zeros((size,size))

for i in range(size):
    for j in range(size):
         vertical_gradient1[i][j] = 0 + i + 1
        
print(vertical_gradient1,'\n')
cv2.imwrite('C:/digitalprocessing/numpy/vertical_gradient1.jpg', vertical_gradient1)


#чорний знизу
vertical_gradient2 = np.zeros((size,size))

for i in range(size):
    for j in range(size):
         vertical_gradient2[i][j] = size - i
        
print(vertical_gradient2,'\n')
cv2.imwrite('C:/digitalprocessing/numpy/vertical_gradient2.jpg', vertical_gradient2)
