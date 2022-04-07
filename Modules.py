# using pyfiglet module to print asci art
import pyfiglet
from termcolor import colored

def print_art(msg, color_input):
  
  asci_art = pyfiglet.figlet_format(msg)
  final = colored(asci_art, color=color_input,attrs=['blink']) 
  print(final)
  
msg =input("enter a message to print in asci art")
color_input =input("enter a color")
print_art(msg, color_input)
















