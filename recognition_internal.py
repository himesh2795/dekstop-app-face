import tkinter

master = tkinter.Tk()
master.title("Face Recognition")


def run():
    import face_recognition
    import cv2
    import numpy as np

    # video_capture = cv2.VideoCapture(0)


b = tkinter.Button(master, text="Start", command=run)
b.pack()
master.mainloop()
