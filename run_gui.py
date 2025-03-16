import os
import subprocess
import tkinter as tk
from tkinter import messagebox

# === Configuration ===
# Replace this with your GitHub repository URL.
GITHUB_REPO_URL = "https://github.com/Berako00/CustomTkinter.git"

# Destination folder: here we place it on the Desktop.
LOCAL_DIR = os.path.join(os.path.expanduser("~"), "Desktop", "repo")

# The main script in the repository that should be executed.
MAIN_SCRIPT = "complex_main.py"  # Adjust if your entry point is named differently.

# === Function Definitions ===
def clone_repo():
    """Clones the repository if it hasn't been cloned already."""
    if not os.path.exists(LOCAL_DIR):
        try:
            # Run git clone command
            subprocess.check_call(["git", "clone", GITHUB_REPO_URL, LOCAL_DIR])
            messagebox.showinfo("Success", "Repository cloned successfully.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Error cloning repository: {e}")
            return False
    return True

def run_repo():
    """Clones (if necessary) and then runs the repository's main script."""
    if clone_repo():
        # Build the full path to the main script.
        script_path = os.path.join(LOCAL_DIR, MAIN_SCRIPT)
        if os.path.exists(script_path):
            try:
                # Start the script in a new process. The 'cwd' parameter ensures the script runs in its repo folder.
                subprocess.Popen(["python", script_path], cwd=LOCAL_DIR)
            except Exception as e:
                messagebox.showerror("Error", f"Error running repository: {e}")
        else:
            messagebox.showerror("Error", f"Main script not found:\n{script_path}")

# === Create the Desktop App GUI ===
root = tk.Tk()
root.title("GitHub Repo Runner")
root.geometry("300x150")  # Set a reasonable window size

label = tk.Label(root, text="Click the button to run the GitHub repo:")
label.pack(pady=10)

run_button = tk.Button(root, text="Run Repository", command=run_repo)
run_button.pack(pady=10)

# Start the GUI event loop.
root.mainloop()

