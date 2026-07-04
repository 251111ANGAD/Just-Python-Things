import os

def create_folders():

    folders = [
        "recordings",
        "snapshots",
        "logs"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)