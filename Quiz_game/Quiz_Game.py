from tkinter import *
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import subprocess

def start_video():
    window.destroy()
    subprocess.Popen(['python', 'Quiz_Game2.py'])


def update():
    ret, frame = vid.read()

    if ret:
        # Calculate the aspect ratio of the video frame
        aspect_ratio = frame.shape[1] / frame.shape[0]

        # Resize the frame to fit the canvas while maintaining the aspect ratio
        if aspect_ratio > 1:
            new_width = canvas_width
            new_height = int(canvas_width / aspect_ratio)
        else:
            new_width = int(canvas_height * aspect_ratio)
            new_height = canvas_height

        resized_frame = cv2.resize(frame, (new_width, new_height))
        photo = ImageTk.PhotoImage(image=Image.fromarray(resized_frame))
        canvas.create_image(0, 0, image=photo, anchor=tk.NW)
        canvas.photo = photo  # Save a reference to the image to avoid garbage collection

    # Schedule the next frame update after a delay (in milliseconds)
    window.after(15, update)

# Create the main window
window = tk.Tk()
window.title("Tkinter and OpenCV")
window.geometry("900x500+300+200")  # Set window size and position
window.configure(bg="black")  # Set window background color to black
window.resizable(False, False)  # Make the window non-resizable

# Open video source
video_source = "image/intro_.mp4"
vid = cv2.VideoCapture(video_source)
if not vid.isOpened():
    raise ValueError("Unable to open video source", video_source)

# Set the canvas size to the desired dimensions
canvas_width = 880
canvas_height = 470
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="black")
canvas.grid(row=0, column=0, padx=10, pady=10)

# Load and resize the "Next" button image to fit the button size
next_button = Image.open("image/next1.png")
next_button = next_button.resize((300, 70), Image.LANCZOS)  # Use Resampling.LANCZOS
next_button = ImageTk.PhotoImage(next_button)


# Create a "Next" button and place it in the corner of the video
btn_next = tk.Button(window, image=next_button, width=300, height=70, command=start_video, bg="green")
btn_next.image = next_button  # Save a reference to the image to avoid garbage collection
btn_next.place(relx=0.99, rely=0.95, anchor=tk.SE)

# Start the video playback
update()

# Start the Tkinter main loop
window.mainloop()

# Release the video source when the window is closed
vid.release()
cv2.destroyAllWindows()
