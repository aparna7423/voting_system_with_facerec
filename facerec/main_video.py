from platform import python_branch
import cv2
import numpy
from simple_facerec import SimpleFacerec
import pandas as pd
# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("D://facerec//images//")
#print(sfr.known_face_encodings)
# Load Camera
VoterId = 0
VoterId = int(input('enter voterid:'))
print("VoterId is",VoterId)
print("VoterId is verified Successfully")
print("proceed for face authentication")
if VoterId:
    doc = pd.read_csv("voting_doc.csv")
    lst = list(doc['VoterName'])
    arr =''
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
            
        print(face_names)
        if len(face_names):
            if face_names[0] not in arr:
                arr = face_names[0]
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
    if arr not in lst:
        doc = doc.append({'VoterId':VoterId,'VoterName':arr},ignore_index=True)
    else:
        print("Fraud Detected!!")
    doc.to_csv("voting_doc.csv")

