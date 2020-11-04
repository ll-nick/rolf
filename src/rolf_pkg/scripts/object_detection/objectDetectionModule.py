import cv2
import os

classNames= []
fileLocation = os.path.dirname(__file__)
classFile = fileLocation + '/coco.names'

with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = fileLocation + '/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = fileLocation + '/frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

def getObjects(img, thres, nms, draw=True, objects=[]):
    classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nms)
    #print(classIds,bbox)
    if len(objects) == 0: objects = classNames
    objectInfo =[]
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            className = classNames[classId - 1]
            if className in objects:
                objectInfo.append([box, className])
                if (draw):
                    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                    cv2.putText(img,className.upper(),(box[0]+10,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    return img,objectInfo

if __name__ == "__main__":
    img = cv2.imread(fileLocation + '/test_images/office-desk.jpg', cv2.IMREAD_UNCHANGED)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    result,objectInfo = getObjects(img,0.5,0.2,objects=['keyboard'])
    #print(objectInfo)
    cv2.imshow("Output", result)
    cv2.waitKey(0)