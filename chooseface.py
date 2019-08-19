import cv2
import os,sys
import json

imgpath = sys.argv[1]
with open(imgpath+"alignments.json","r") as load_f:
    imgdict = json.load(load_f)

newdict = {}

for key in imgdict:
    newdict[key] = []
    for face in imgdict[key]:
        img = cv2.imread(imgpath+key)
        shape = img.shape
        f = 1000.0/max(shape[0],shape[1])
        cv2.rectangle(img,(face["x"],face["y"]),(face["x"]+face["w"],face["y"]+face["h"]),(255,0,0),3)
        
        for point in face["landmarksXY"]:
            cv2.circle(img,(point[0],point[1]),1,(0,255,0),-1)

        img = cv2.resize(img,(0,0),fx=f,fy=f)
        cv2.imshow(key,img)
        k = cv2.waitKey(0)
        if k==27:   #按下esc退出
            os._exit(0)
        elif k==ord("y"):   #按y保存，按其它键丢弃
            newdict[key].append(face)
        cv2.destroyAllWindows()

with open(imgpath+"newalignments.json","w") as f:
    json.dump(newdict,f)
    print("写入json成功")