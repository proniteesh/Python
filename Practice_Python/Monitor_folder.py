import time
import os
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
import getpass
import tkinter as tk
from tkinter import filedialog, messagebox

class Watcher:
    def __init__(self, directory_to_watch, duration):
        self.DIRECTORY_TO_WATCH = directory_to_watch
        self.observer = Observer()
        self.duration = duration

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        print(f"Started monitoring {self.DIRECTORY_TO_WATCH} for {self.duration} seconds.")
        try:
            time.sleep(self.duration)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.stop()
        self.observer.join()
        event_handler.save_to_excel()

class Handler(FileSystemEventHandler):
    def __init__(self):
        self.log_entries = []

    def process(self, event):
        username = getpass.getuser()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        event_type = event.event_type
        file_path = event.src_path
        self.log_entries.append([timestamp, username, event_type, file_path])
        print(f"Event: {event_type} - Path: {file_path} - User: {username} - Time: {timestamp}")

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)

    def on_deleted(self, event):
        self.process(event)

    def save_to_excel(self):
        df = pd.DataFrame(self.log_entries, columns=['Timestamp', 'Username', 'Event Type', 'File Path'])
        output_path = 'file_changes_log.xlsx'
        df.to_excel(output_path, index=False)
        print(f"Log saved to {output_path}")
        messagebox.showinfo("Info", f"Log saved to {output_path}")

def start_monitoring(folder_path, duration):
    if not folder_path:
        messagebox.showerror("Error", "Please select a folder to monitor")
        return
    if not duration.isdigit() or int(duration) <= 0:
        messagebox.showerror("Error", "Please enter a valid duration in seconds")
        return
    monitor_duration = int(duration)
    w = Watcher(folder_path, monitor_duration)
    w.run()

def select_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

if __name__ == '__main__':
    # Set up the GUI
    root = tk.Tk()
    root.title("Folder Monitor")

    tk.Label(root, text="Folder to monitor:").grid(row=0, column=0, padx=10, pady=10)
    folder_entry = tk.Entry(root, width=50)
    folder_entry.grid(row=0, column=1, padx=10, pady=10)
    tk.Button(root, text="Browse", command=select_folder).grid(row=0, column=2, padx=10, pady=10)

    tk.Label(root, text="Duration (seconds):").grid(row=1, column=0, padx=10, pady=10)
    duration_entry = tk.Entry(root, width=50)
    duration_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(root, text="Start Monitoring", command=lambda: start_monitoring(folder_entry.get(), duration_entry.get())).grid(row=2, column=0, columnspan=3, pady=20)

    root.mainloop()
