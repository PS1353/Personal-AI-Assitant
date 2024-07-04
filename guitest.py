import tkinter as tk
from tkinter import scrolledtext

# Define the main window
root = tk.Tk()
root.title("AI Assistant")

# Set window size
root.geometry("400x300")

# Create a label
label = tk.Label(root, text="Ask me anything:", font=("Arial", 14))
label.pack(pady=10)

# Create an entry widget for user input
entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=5)

# Create a text area to display responses
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, font=("Arial", 12))
text_area.pack(pady=10)

# Define the function to handle user input and generate response
def get_response():
    user_input = entry.get()
    # Placeholder for AI assistant response logic
    response = f"User Said: {user_input}"
    text_area.insert(tk.END, response + "\n")
    entry.delete(0, tk.END)

# Create a button to submit the input
button = tk.Button(root, text="Submit", command=get_response, font=("Arial", 12))
button.pack(pady=5)

# Run the main loop
root.mainloop()
