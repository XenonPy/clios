# 0.1.0
import time
import requests
from .colors import *
from .colors import colorprint as print
from .prompt import prompt
from .data import generate_sample_data

class Assistant:
    def __init__(self, wolframApiKey=""):
        if wolframApiKey != "":
            self.isWolframEnabled = True
            self.wolframApiKey = wolframApiKey
    def start(self):
        while True:
            print(red, " > Clios Assistant v0.1.0", bold)
            appChoice = prompt("""
            What would you like to do?
                   Do Math (math)
                   Ask AI (ask)
                   Random Trivia (trivia)
                   Generate Data (data)
            """)
            if appChoice == "data":
                datapath = prompt("Please enter the path where the data should be created: ")
                datanumdirs = prompt("How many directories should be made inside of there? ")
                datafiles_per_dir = prompt("How many files per directory? ")
                datafile_size_mb = prompt("How big should each file be (in MB)? ")
                datamax_workers = prompt("How many workers should create the files? ")
                generate_sample_data(
                    directory=datapath, 
                    num_dirs=int(datanumdirs),                      
                    files_per_dir=int(datafiles_per_dir),      
                    file_size_mb=int(datafile_size_mb),  
                    max_workers=int(datamax_workers)
                )
            elif appChoice == "ask":
                question = prompt("What would you like to know? ")
                res = requests.get(f"http://api.wolframalpha.com/v1/result?appid={self.wolframApiKey}&i={question}")
                print(white, "\n")
                print(white, res.text)
                
            elif appChoice == "trivia":
                pass
            else:
                pass

