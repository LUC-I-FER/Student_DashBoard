import os
import time as t
import sqlite3
import sys
from database_manage import utils as utl
from frontend.main_1 import place_login_component
import tkinter as tk

def start_app():
    # utl.insert_data_in_user("23104B0028", "Manvith", "Mogaveera", "ExTC", "Manvith");
    place_login_component()
    print("start app was triggered....")

def change_settings():
    data = utl.fetch_user_data("23104B0028")
    print(data)
    print("Change settings....")

if __name__ == "__main__":
    if "--change-settings" in sys.argv:
        change_settings()
    elif "--start-app" in sys.argv:
        start_app()
    else:
        print("Please read the manual")