import os
import sys
import time
from colorama import Fore
fs = {
  '/mnt' : {
    '/mnt/root' : {
      "secret" : "этот код бессмысленный"    
    },
    '/mnt/boot' : {
      "bios" : {}
    }
  }
}
secret = "этот код бессмысленный"
ascii = """
  █████████           █████       ██████████
 ███░░░░░███         ░░███       ░███░░░░░░█
░███    ░░░   ██████  ░███       ░███     ░ 
░░█████████  ███░░███ ░███       ░█████████ 
 ░░░░░░░░███░███████  ░███       ░░░░░░░░███
 ███    ░███░███░░░   ░███      █ ███   ░███
░░█████████ ░░██████  ███████████░░████████ 
 ░░░░░░░░░   ░░░░░░  ░░░░░░░░░░░  ░░░░░░░░  
      
the free kernel made by a joke          """

def bios_boot():
  components = ["cpu, ram"]
  print("[  01]  booting")
  time.sleep(0.5)
  for comp in components:
    print(f"{comp:.<30}", end="", flush=True)
    time.sleep(0.2)
  os.system("clear")
  print(ascii)
bios_boot()
def command():
  cmd = input("root@sel5-> ")
  if cmd == "listf":
    print ("secret  ascii")
  elif cmd == "cat secret":
    print(secret)
  elif cmd == "pwd":
    print ("/mnt/root")
  elif cmd == "exit":
    sys.exit(0)
  elif cmd == "rm -rf /":
    print ("removing /")
    time.sleep(1)
    print("sucsessfully removed /")
    time.sleep(3)
    sys.exit(0)
  elif cmd == "cat ascii":
    print (ascii)
  elif cmd == "clear":
    os.system("clear")
  elif cmd == "help":
    print ("the commands are:listf, cat, rm -rf /, clear, pwd, exit ")
  elif cmd == "selfetch":
    selfetch()
  else:
    print ("E:command not found")
def selfetch():
  print (Fore.GREEN + """
      root@sel5       
 _____     __    ___ 
|   __|___|  |  |  _|
|__   | -_|  |__|_  |
|_____|___|_____|___|
                     """ + Fore.RESET)
  print ("""OS:SeL5
hostn:sel5
user:root
term:/dev/tty
""")
while True:
  command()
