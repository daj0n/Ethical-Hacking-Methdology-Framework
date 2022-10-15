#!/usr/bin/python3
from time import sleep

def spaces():
	print('\n')
spaces()
name = input("What's your name?\n")
print("""\n\nWelcome to the...

█▀▀ ▀█▀ █░█ █ █▀▀ ▄▀█ █░░   █░█ ▄▀█ █▀▀ █▄▀ █ █▄░█ █▀▀   █▀▀ █▀█ ▄▀█ █▀▄▀█ █▀▀ █░█░█ █▀█ █▀█ █▄▀
██▄ ░█░ █▀█ █ █▄▄ █▀█ █▄▄   █▀█ █▀█ █▄▄ █░█ █ █░▀█ █▄█   █▀░ █▀▄ █▀█ █░▀░█ ██▄ ▀▄▀▄▀ █▄█ █▀▄ █░█
""")

if __name__ == '__main__':
	delay = 1
	sleep(delay)
	print("[1] Reconnaissance\n[2] Scanning and Enumeration\n[3] Gaining Access\n[4] Maintaining Access\n[5] Clearing Tracks\n")

stage = input(f"Which stage number are you on, {name}?: ")
if stage == "1":
	print("\n[1] Human Reconnaissance\n[2] IP Reconnaissance\n[3] Corporation Reconnaissance")
	category = input("\nWhich category?: ")
	if category == "1":
		print("\n[1] Full Name\n[2] Username\n[3] Email Address\n[4] Phone Number")
		hr_category = input("\nWhich category?: ")
		if hr_category == "1":
			print("\nExample input: John-Doe\n(make sure to add a - as a space between the first and last name")
			delay = 2
			sleep(delay)
			hr_name = input ("\nWhat is their first and last name?\n")
			print(f"\nNavigate to this link:\nhttps://www.fastpeoplesearch.com/name/{hr_name}\nHappy Recon, {name} :)")
