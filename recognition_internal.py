import tkinter
import face_recognition
import cv2
import numpy as np

master = tkinter.Tk()
master.title("Face Recognition")


def run():
    video_capture = cv2.VideoCapture(0)

    while True:
        # video_capture.open(0)
        ret, frame = video_capture.read()
        # print(video_capture.isOpened())

        # print(ret)
        # print(frame)
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()


b = tkinter.Button(master, text="Start", command=run)
b.pack()
master.mainloop()
