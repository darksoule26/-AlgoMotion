import google.generativeai as genai
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

# Configure your API key
genai.configure(api_key="ENTER_YOUT_API_KEY")

def analyze_code(code, output_text):
    """Analyzes C++ code and displays the result in the GUI."""
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    prompt = f"""
    Analyze the following C++ code and provide a detailed explanation of its functionality,
    including step-by-step execution, diagrams if applicable, and any potential errors.

    Code:
    ```cpp
    {code}
    ```

    Explanation:
    """
    try:
        response = model.generate_content(prompt)
        analysis = response.text
        output_text.delete(1.0, tk.END)  # Clear previous text
        output_text.insert(tk.END, analysis)

        if "Do you want me to attempt to debug and correct it?" in analysis:
            if messagebox.askyesno("Debug?", "Errors detected. Debug?"):
                debug_code(code, output_text)

    except Exception as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"An error occurred: {e}")

def debug_code(code, output_text):
    """Debugs the code and displays the result in the GUI."""
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    prompt = f"""
    Debug and correct the following C++ code. Provide the corrected code, a detailed explanation of the errors,
    and how they were fixed.

    Code:
    ```cpp
    {code}
    ```

    Corrected Code and Explanation:
    """
    try:
        response = model.generate_content(prompt)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, response.text)
    except Exception as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"An error occurred: {e}")

def on_analyze():
    """Handles the analyze button click."""
    code = code_input.get("1.0", tk.END).strip()
    if code:
        analyze_code(code, output_text)
    else:
        messagebox.showerror("Error", "Please enter C++ code.")

# ------------------ GUI Setup ------------------
root = tk.Tk()
root.title("C++ Code Analyzer")

# Set window dimensions and center it
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# Use ttk themed style for a modern look
style = ttk.Style(root)
style.theme_use("clam")
style.configure("TFrame", background="#2E2E2E")
style.configure("TLabel", background="#2E2E2E", foreground="white", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12), padding=6)

# Create the main frame with padding
main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.pack(fill=tk.BOTH, expand=True)

# ------------------ Input Section ------------------
input_frame = ttk.Frame(main_frame)
input_frame.pack(fill=tk.BOTH, expand=True, pady=10)

input_label = ttk.Label(input_frame, text="Enter C++ Code:")
input_label.pack(anchor=tk.W, padx=5, pady=5)

# Use scrolledtext with custom styling for code input
code_input = scrolledtext.ScrolledText(
    input_frame,
    wrap=tk.WORD,
    width=80,
    height=10,
    font=("Courier", 10),
    background="#1e1e1e",
    foreground="white",
    insertbackground="white"
)
code_input.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# ------------------ Analyze Button ------------------
analyze_button = ttk.Button(main_frame, text="Analyze Code", command=on_analyze)
analyze_button.pack(pady=10)

# ------------------ Output Section ------------------
output_frame = ttk.Frame(main_frame)
output_frame.pack(fill=tk.BOTH, expand=True, pady=10)

output_label = ttk.Label(output_frame, text="Analysis Output:")
output_label.pack(anchor=tk.W, padx=5, pady=5)

# Use scrolledtext with custom styling for output display
output_text = scrolledtext.ScrolledText(
    output_frame,
    wrap=tk.WORD,
    width=80,
    height=10,
    font=("Courier", 10),
    background="#1e1e1e",
    foreground="white",
    insertbackground="white"
)
output_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

root.mainloop()
