import tkinter as tk
from tkinter import messagebox

# ---------------- RULE BASE ---------------- #

rules = [
    (["fever", "cough"], "flu"),
    (["fever", "rash"], "measles"),
    (["headache", "fever"], "viral infection"),
    (["flu", "body_pain"], "severe flu"),
    (["cough", "chest_pain"], "bronchitis")
]

# ---------------- FORWARD CHAINING ENGINE ---------------- #

def forward_chaining(facts):

    inferred = set(facts)
    log = []
    added = True

    while added:
        added = False

        for condition, result in rules:
            if all(c in inferred for c in condition) and result not in inferred:

                inferred.add(result)
                log.append(f"Rule Applied: IF {condition} THEN {result}")
                added = True

    return inferred, log


# ---------------- RUN EXPERT SYSTEM ---------------- #

def run_system():

    selected = []

    for symptom, var in symptom_vars.items():
        if var.get():
            selected.append(symptom)

    if not selected:
        messagebox.showwarning("Warning", "Select at least one symptom")
        return

    results, reasoning = forward_chaining(selected)

    result_box.delete("1.0", tk.END)

    result_box.insert(tk.END, "Selected Symptoms:\n")
    result_box.insert(tk.END, str(selected) + "\n\n")

    result_box.insert(tk.END, "Inference Steps:\n")
    for step in reasoning:
        result_box.insert(tk.END, step + "\n")

    result_box.insert(tk.END, "\nFinal Knowledge Base:\n")
    result_box.insert(tk.END, str(results))


# ---------------- UI DESIGN ---------------- #

root = tk.Tk()
root.title("Rule Based Expert System")
root.geometry("600x550")
root.configure(bg="#1e1e2f")

title = tk.Label(
    root,
    text="AI Rule Based Expert System",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#1e1e2f"
)
title.pack(pady=15)


frame = tk.Frame(root, bg="#2c2c3c", padx=20, pady=20)
frame.pack(pady=10)


symptoms = [
    "fever",
    "cough",
    "rash",
    "headache",
    "body_pain",
    "chest_pain"
]

symptom_vars = {}

tk.Label(
    frame,
    text="Select Symptoms",
    font=("Arial", 14, "bold"),
    bg="#2c2c3c",
    fg="white"
).pack()


for s in symptoms:
    var = tk.BooleanVar()
    symptom_vars[s] = var

    cb = tk.Checkbutton(
        frame,
        text=s,
        variable=var,
        font=("Arial", 11),
        bg="#2c2c3c",
        fg="white",
        selectcolor="#444"
    )

    cb.pack(anchor="w")


run_btn = tk.Button(
    root,
    text="Run Expert System",
    font=("Arial", 12, "bold"),
    bg="#00adb5",
    fg="white",
    command=run_system
)

run_btn.pack(pady=10)


result_box = tk.Text(
    root,
    height=15,
    width=65,
    bg="#111",
    fg="#00ff9f",
    font=("Consolas", 10)
)

result_box.pack(pady=10)


root.mainloop()