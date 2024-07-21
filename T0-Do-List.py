import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x400")
        self.tasks = []
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="To-Do List", font=("Arial", 20))
        self.title_label.pack(pady=10)

        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, width=60, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.edit_button = tk.Button(self.root, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(pady=5)

        self.search_entry = tk.Entry(self.root, width=50)
        self.search_entry.pack(pady=5)
        self.search_button = tk.Button(self.root, text="Search", command=self.search_task)
        self.search_button.pack(pady=5)

        self.view_button = tk.Button(self.root, text="View All Tasks", command=self.view_all_tasks)
        self.view_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_index]
            self.tasks[selected_index] = f"✔️ {task}"
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "No task selected.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "No task selected.")

    def edit_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            new_task = self.task_entry.get().strip()
            if new_task:
                self.tasks[selected_index] = new_task
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a new task.")
        except IndexError:
            messagebox.showwarning("Warning", "No task selected.")

    def search_task(self):
        search_term = self.search_entry.get().strip().lower()
        if search_term:
            found_tasks = [task for task in self.tasks if search_term in task.lower()]
            self.update_task_listbox(found_tasks)
        else:
            self.update_task_listbox()
        self.search_entry.delete(0, tk.END)

    def view_all_tasks(self):
        self.update_task_listbox()

    def update_task_listbox(self, tasks_to_display=None):
        self.task_listbox.delete(0, tk.END)
        tasks_to_display = tasks_to_display or self.tasks
        for task in tasks_to_display:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
