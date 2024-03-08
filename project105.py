import cv2
import os

path ='/Users/asmamohammed/Desktop/PYTHON/c104-105/105Images'

images = []

for folder in os.listdir(path):
    name, ext = os.path.splitext(folder)
    
    if ext in['.gif','.png','.jpg', 'jpeg','.jfif']:
        file_name = path+"/"+folder
        print(file_name)
        print()
        images.append(file_name)
        
count = len(images)
frame = cv2.imread(images[0])

height,width,channel = frame.shape
size = (width,height)

print(size)

friends = cv2.VideoWriter('project105.mp4',cv2.VideoWriter_fourcc(*'DIVX'),2,size)

for i in range(0,count-1):
    frame = cv2.imread(images[i])
    friends.write(frame)
    
friends.release()
print("done")