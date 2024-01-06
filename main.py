import tkinter as tk
import requests
from tkinter import messagebox

def delete_repos():
    username = username_entry.get()
    token = token_entry.get()
    headers = {'Authorization': f'token {token}'}
    repos = repo_entry.get().split(',')
    for repo in repos:
            repo_name = repo
            delete_url = f'https://api.github.com/repos/{username}/{repo_name}'
            delete_response = requests.delete(delete_url, headers=headers)
            if delete_response.status_code == 204:
                messagebox.showinfo('Success','Repositories deleted successfully.')
                print(f'Repository {repo_name} deleted successfully.')
            else:
                messagebox.showerror('Error', f'{delete_response.reason}')
                print(f'Failed to delete repository {repo_name}. Status code: {delete_response.reason}')

window = tk.Tk()
window.title('Bulk Delete GitHub Repositories Tool')

window_width = 800
window_height = 300
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f'{window_width}x{window_height}+{x}+{y}')

repo_label = tk.Label(window, text='Repository(s) Name:')
repo_label.pack()
repo_entry = tk.Entry(window)
repo_entry.pack()

username_label = tk.Label(window, text='GitHub Username:')
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

token_label = tk.Label(window, text='Personal Access Token:')
token_label.pack()
token_entry = tk.Entry(window, show='*')
token_entry.pack()

delete_button = tk.Button(window, text='Delete Repositories',command=delete_repos)
delete_button.pack()


window.mainloop()