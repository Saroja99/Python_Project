import datetime
import time
import pygame
import tkinter as tk
from threading import Thread

# Initialize pygame mixer
pygame.mixer.init()

# Function to play the alarm sound
def play_alarm_sound():
    alarm_sound_path = r"C:\Users\anush\OneDrive\Desktop\python gamming\AlarmApp\test.mp3"
    print(f"Attempting to load sound file from: {alarm_sound_path}")
    
    try:
        pygame.mixer.music.load(alarm_sound_path)
        pygame.mixer.music.play()
        print("Alarm sound is playing.")
    except pygame.error as e:
        print(f"Pygame error: {e}")

# Function to start the alarm thread
def Threading():
    t1 = Thread(target=alarm)
    t1.start()

# Function to check the alarm time
def alarm():
    while True:
        # Set alarm time
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        # Wait for one second
        time.sleep(1)

        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {current_time}, Alarm time: {set_alarm_time}")

        # Check if current time matches the alarm time
        if current_time == set_alarm_time:
            print("Time to Wake up")
            # Playing sound
            play_alarm_sound()
            break

# Create Tkinter window
root = tk.Tk()
root.geometry("400x200")

# Create and configure widgets
tk.Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
tk.Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

frame = tk.Frame(root)
frame.pack()

hour = tk.StringVar(root)
hours = [f'{i:02}' for i in range(24)]
hour.set(hours[0])

hrs = tk.OptionMenu(frame, hour, *hours)
hrs.pack(side=tk.LEFT)

minute = tk.StringVar(root)
minutes = [f'{i:02}' for i in range(60)]
minute.set(minutes[0])

mins = tk.OptionMenu(frame, minute, *minutes)
mins.pack(side=tk.LEFT)

second = tk.StringVar(root)
seconds = [f'{i:02}' for i in range(60)]
second.set(seconds[0])

secs = tk.OptionMenu(frame, second, *seconds)
secs.pack(side=tk.LEFT)

tk.Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
