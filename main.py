import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import threading
from pathlib import Path
import platform

class GeometryDashSongSwapper:
    def __init__(self):
        self.setup_window()
        self.setup_ui()
        self.setup_drag_drop()
        
    def setup_window(self):
        self.root = ctk.CTk()
        self.root.title("Geometry Dash Song Swapper")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        # Set theme
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        
    def setup_ui(self):
        # Main container
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="Geometry Dash Song Swapper",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.title_label.pack(pady=(0, 20))
        
        # Instructions
        self.instructions_label = ctk.CTkLabel(
            self.main_frame,
            text="Drag and drop .mp3 files below to swap songs in Geometry Dash",
            font=ctk.CTkFont(size=14)
        )
        self.instructions_label.pack(pady=(0, 10))
        
        # Drop zone frame
        self.drop_frame = ctk.CTkFrame(self.main_frame, height=150, corner_radius=10)
        self.drop_frame.pack(fill="both", expand=True, pady=(0, 20))
        self.drop_frame.pack_propagate(False)
        
        # Drop zone label
        self.drop_label = ctk.CTkLabel(
            self.drop_frame,
            text="Drag .mp3 files here",
            font=ctk.CTkFont(size=16),
            text_color="gray"
        )
        self.drop_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # File list
        self.file_list_frame = ctk.CTkFrame(self.main_frame)
        self.file_list_frame.pack(fill="both", expand=True, pady=(0, 20))
        
        self.file_list_label = ctk.CTkLabel(
            self.file_list_frame,
            text="Dropped files:",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.file_list_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        # Scrollable frame for file list
        self.scrollable_frame = ctk.CTkScrollableFrame(self.file_list_frame)
        self.scrollable_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        # Song ID input
        self.id_frame = ctk.CTkFrame(self.main_frame)
        self.id_frame.pack(fill="x", pady=(0, 20))
        
        self.id_label = ctk.CTkLabel(
            self.id_frame,
            text="Song ID:",
            font=ctk.CTkFont(size=14)
        )
        self.id_label.pack(side="left", padx=(10, 5), pady=10)
        
        self.id_entry = ctk.CTkEntry(
            self.id_frame,
            placeholder_text="Enter song ID",
            width=150
        )
        self.id_entry.pack(side="left", padx=(0, 10), pady=10)
        
        # Swap button
        self.swap_button = ctk.CTkButton(
            self.id_frame,
            text="Swap Song",
            command=self.swap_song,
            width=120,
            height=35
        )
        self.swap_button.pack(side="left", padx=(0, 10), pady=10)
        
        # Clear button
        self.clear_button = ctk.CTkButton(
            self.id_frame,
            text="Clear",
            command=self.clear_files,
            width=80,
            height=35
        )
        self.clear_button.pack(side="left", padx=(0, 10), pady=10)
        
        # Status label
        self.status_label = ctk.CTkLabel(
            self.main_frame,
            text="Ready",
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        self.status_label.pack(pady=(0, 10))
        
        # Store dropped files
        self.dropped_files = []
        
    def setup_drag_drop(self):
        # Bind drag and drop events
        self.drop_frame.bind("<Enter>", self.on_drag_enter)
        self.drop_frame.bind("<Leave>", self.on_drag_leave)
        self.drop_frame.bind("<Button-1>", self.on_drop_click)
        
    def on_drag_enter(self, event):
        self.drop_frame.configure(fg_color="#3498db")
        self.drop_label.configure(text_color="white")
        
    def on_drag_leave(self, event):
        self.drop_frame.configure(fg_color="transparent")
        self.drop_label.configure(text_color="gray")
        
    def on_drop_click(self, event):
        # Open file dialog when clicking the drop zone
        from tkinter import filedialog
        files = filedialog.askopenfilenames(
            title="Select .mp3 files",
            filetypes=[("MP3 files", "*.mp3"), ("All files", "*.*")]
        )
        if files:
            self.add_files(files)
            
    def on_file_drop(self, event):
        # Handle dropped files
        try:
            if hasattr(event, 'data'):
                files = [event.data]
            else:
                files = self.root.tk.splitlist(event.data)
            self.add_files(files)
        except:
            # Fallback to file dialog if drag and drop fails
            pass
        
    def add_files(self, files):
        valid_files = []
        
        for file_path in files:
            if file_path.lower().endswith('.mp3'):
                valid_files.append(file_path)
                self.add_file_to_list(file_path)
            else:
                self.status_label.configure(text=f"Skipped non-mp3 file: {os.path.basename(file_path)}", text_color="orange")
        
        self.dropped_files.extend(valid_files)
        
        if len(valid_files) > 0:
            self.status_label.configure(text=f"Added {len(valid_files)} .mp3 file(s)", text_color="green")
        else:
            self.status_label.configure(text="No valid .mp3 files found", text_color="red")
            
    def add_file_to_list(self, file_path):
        # Create a frame for each file
        file_frame = ctk.CTkFrame(self.scrollable_frame)
        file_frame.pack(fill="x", pady=2)
        
        # File name label
        file_name = os.path.basename(file_path)
        file_label = ctk.CTkLabel(
            file_frame,
            text=file_name,
            font=ctk.CTkFont(size=12)
        )
        file_label.pack(side="left", padx=10, pady=5)
        
        # Remove button
        remove_button = ctk.CTkButton(
            file_frame,
            text="×",
            width=30,
            height=25,
            command=lambda fp=file_path: self.remove_file(fp)
        )
        remove_button.pack(side="right", padx=10, pady=5)
        
    def remove_file(self, file_path):
        if file_path in self.dropped_files:
            self.dropped_files.remove(file_path)
        
        # Refresh the file list
        self.refresh_file_list()
        
    def refresh_file_list(self):
        # Clear the scrollable frame
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        # Re-add remaining files
        for file_path in self.dropped_files:
            self.add_file_to_list(file_path)
            
    def clear_files(self):
        self.dropped_files.clear()
        self.refresh_file_list()
        self.status_label.configure(text="Files cleared", text_color="gray")
        
    def swap_song(self):
        if not self.dropped_files:
            messagebox.showwarning("No Files", "Please drag and drop .mp3 files first.")
            return
            
        song_id = self.id_entry.get().strip()
        if not song_id:
            messagebox.showwarning("No Song ID", "Please enter a song ID.")
            return
            
        if not song_id.isdigit():
            messagebox.showwarning("Invalid ID", "Song ID must be a number.")
            return
            
        # Start the swap operation in a separate thread
        threading.Thread(target=self.perform_swap, args=(song_id,), daemon=True).start()
        
    def perform_swap(self, song_id):
        try:
            # Get Geometry Dash directory
            gd_dir = self.get_geometry_dash_directory()
            if not gd_dir:
                self.root.after(0, lambda: messagebox.showerror("Error", "Geometry Dash directory not found."))
                return
                
            # Create songs directory if it doesn't exist
            songs_dir = gd_dir / "songs"
            songs_dir.mkdir(exist_ok=True)
            
            # Copy the first file with the specified ID
            source_file = self.dropped_files[0]
            target_file = songs_dir / f"{song_id}.mp3"
            
            self.root.after(0, lambda: self.status_label.configure(text="Copying file...", text_color="blue"))
            
            # Copy the file
            shutil.copy2(source_file, target_file)
            
            self.root.after(0, lambda: self.status_label.configure(text=f"Song swapped successfully! ID: {song_id}", text_color="green"))
            self.root.after(0, lambda: messagebox.showinfo("Success", f"Song copied to:\n{target_file}"))
            
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            self.root.after(0, lambda: self.status_label.configure(text=error_msg, text_color="red"))
            self.root.after(0, lambda: messagebox.showerror("Error", error_msg))
            
    def get_geometry_dash_directory(self):
        # Get the appropriate local app data directory based on platform
        if platform.system() == "Windows":
            local_app_data = os.environ.get('LOCALAPPDATA', os.path.expanduser('~\\AppData\\Local'))
            gd_dir = Path(local_app_data) / "GeometryDash"
        elif platform.system() == "Darwin":  # macOS
            home = Path.home()
            gd_dir = home / "Library" / "Application Support" / "GeometryDash"
        else:  # Linux and other Unix-like systems
            home = Path.home()
            gd_dir = home / ".local" / "share" / "GeometryDash"
            
        return gd_dir if gd_dir.exists() else None

if __name__ == "__main__":
    app = GeometryDashSongSwapper()
    app.root.mainloop()