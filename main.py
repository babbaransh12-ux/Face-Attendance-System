import os.path
import datetime
import pickle

import tkinter as tk
import cv2
from PIL import Image, ImageTk
import face_recognition

class App:
    def __init__(self):
       self.main_window = tk.Tk()
       self.main.geometry("1200x520+350+100")

       self.login_button_main_window = util.get_button(slelf.main_window, 'login', 'green', self.login)
       self.login_button_main_window.place(x=750, y=100) 

       self.logout_button_main_window = util.get_button(self.main_window, 'logout', 'red', self.logout)   
       self.logout_button_main_window.place(x=750, y=200)  

       self.register_new_user_button_main_window = util.get_button(self.main_window, 'register new user', self.register_new_user, fg='black')
       self.register_new_user_button_main_window.place(x=750, y=300)

       self.webcame_label = util.get_img_label(self.main_window)
       self.webcam_label.place(x=10, y=0, width=700, height=500)

       self.add_webcam(self.webcam_label)

       self.db_dir = "./db"
       if not os.path.exists(self.db_dir):
        os.mkdir(self.db_dir)

        self.log_path = "./Log.txt"

        def add_webcam(self, Label):
            if 'cap' not in self.__dict__:
                self.cap = cv2.VideoCapture(2)
        
            self._label = Label
            self.process_webcam()

        def process_webcam(self):
            ret, frame = self.cap.read()

            self.most_recent_capture_arr = frame
            img_ = cv2.cvtColor(self.most_recetn_capture_arr, cv2.COLOR_BGR2RGB)
            self.most_recent_capture_pil = Image.fromarray(img_)
            imgtk = ImageTk.PhotoIMage(image=self.most_recent_capture_pil)
            self._label.imgtk = imgtk
            self._label.configure(image=imgtk)

            self.label.after(20, self.process_webcam)
            

        def login(Self):

            label = test(
                image=self.most_recent_capture_arr,
                
            )
