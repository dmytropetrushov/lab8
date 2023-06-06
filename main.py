import tkinter as tk
from nltk.corpus import wordnet as wn

# Create the main application window
root = tk.Tk()
root.title("NLTK Word Tasks")
root.geometry("400x300")

# Create a frame to contain the tasks
tasks_frame = tk.Frame(root, padx=20, pady=20)
tasks_frame.pack()
# Task 1: Get all synsets for the word "dish"
def task1():
    synsets = wn.synsets("dish")
    result_text = '\n'.join([str(synset) for synset in synsets])
    show_result("Task 1", result_text)

# Task 2: Get a definition and example using the lemma of the third noun synset
# and the first verb synset of the word "dish"
# Task 2: Get a definition and example using the lemma of the third noun synset
# and the first verb synset of the word "dish"
def task2():
    noun_synsets = wn.synsets("dish", pos=wn.NOUN)
    verb_synsets = wn.synsets("dish", pos=wn.VERB)
    if len(noun_synsets) > 2 and len(verb_synsets) > 0:
        noun_lemma = noun_synsets[2].lemmas()[0]
        verb_lemma = verb_synsets[0].lemmas()[0]
        noun_synset = noun_lemma.synset()
        verb_synset = verb_lemma.synset()
        result_text = f"Definition: {noun_synset.definition()}\nExample: {verb_synset.examples()[0]}"
        show_result("Task 2", result_text)
    else:
        show_result("Task 2", "Insufficient synsets found")


# Task 3: Get all names, definitions, and examples of uses of the noun "dish" synsets
def task3():
    noun_synsets = wn.synsets("dish", pos=wn.NOUN)
    result_text = ""
    for synset in noun_synsets:
        result_text += f"Name: {synset.name()}\nDefinition: {synset.definition()}\n"
        if synset.examples():
            result_text += f"Example: {synset.examples()[0]}\n"
        result_text += "\n"
    show_result("Task 3", result_text)

# Task 4: Get all names, definitions, and examples of verb synsets "dish"
def task4():
    verb_synsets = wn.synsets("dish", pos=wn.VERB)
    result_text = ""
    for synset in verb_synsets:
        result_text += f"Name: {synset.name()}\nDefinition: {synset.definition()}\n"
        if synset.examples():
            result_text += f"Example: {synset.examples()[0]}\n"
        result_text += "\n"
    show_result("Task 4", result_text)

# Task 5: Get the lemma and the name of this lemma of any synset of the word "dish"
def task5():
    synsets = wn.synsets("dish")
    if len(synsets) > 0:
        lemma = synsets[0].lemmas()[0]
        result_text = f"Lemma: {lemma}\nLemma name: {lemma.name()}"
        show_result("Task 5", result_text)
    else:
        show_result("Task 5", "No synsets found")

# Helper function to display the result in a new window
def show_result(task_name, result_text):
    result_window = tk.Toplevel(root)
    result_window.title(task_name)
    result_label = tk.Label(result_window, text=result_text)
    result_label.pack()

# Create buttons for each task
task1_button = tk.Button(root, text="Task 1", command=task1)
task2_button = tk.Button(root, text="Task 2", command=task2)
task3_button = tk.Button(root, text="Task 3", command=task3)
task4_button = tk.Button(root, text="Task 4", command=task4)
task5_button = tk.Button(root, text="Task 5", command=task5)

# Position the buttons in the main window
task1_button.pack()
task2_button.pack()
task3_button.pack()
task4_button.pack()
task5_button.pack()

# Start the main GUI event loop
root.mainloop()
