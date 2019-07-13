'''
 * @author Muhammad Faheem Khan
 * @email faheem5948@gmail.com
 * @create date 2019-07-13 01:44:37
 * @modify date 2019-07-13 01:44:37
 * @desc This program configures smtp settings for open-edx 
 '''

import os
import sys
import json

conf_dir  = "/opt/bitnami/apps/edx/conf/" # directory containing all the config files

def checkRootStatus():
	# make change in /opt/ directory and see if its allowed or not
	if os.getuid() == 0:
		return True
	else:
		return False

def loadFile(fname):
	fname = conf_dir + fname
	if os.path.exists(fname):
		with open(fname, "r") as f:
			return json.load(f)
	else:
		print("File does not exists at " + fname)
		sys.exit(1)

def dumpFile(fname, content):
	fname = conf_dir + fname
	with open(fname, "r+") as f:
		json.dump(content, f)

def applyEnvChanges(domain, email_host, email_port, email_use_tls, env_fname, env):
	env["EMAIL_HOST"] = email_host
	env["EMAIL_PORT"] = email_port
	env["EMAIL_USE_TLS"] = email_use_tls
	dumpFile(env_fname, env)
	
def applyAuthChanges(domain, email_host_username, email_host_password, auth_fname, auth):
	# "EMAIL_HOST_PASSWORD": "",
	# "EMAIL_HOST_USER": "",
	auth["EMAIL_HOST_USER"] = email_host_username
	auth["EMAIL_HOST_PASSWORD"] = email_host_password
	dumpFile(auth_fname, auth)

def main():
	# Definign Variables for function level root scope
	domain = None
	email_host = None
	email_port = None
	email_use_tls = None
	email_host_password = None
	email_host_password = None
	# the script is running as Root/Superuser
	if checkRootStatus():
		# Printing the about script string
		print("This programs helps configure SMTP with open-edx")
		
		# Ask the user if they want to change the default file path
		while True:
			print("Default configuration file path: " + conf_dir)
			changeDirPath = input("Do you want to change the default configuration file path?(Y/N) \n: ").lower()
			if changeDirPath == "y":
				conf_dir = input(": ")
			elif changeDirPath == "n":
				break
			else:
				print("Invalid Input. Enter 'Y' for yes OR 'N' for no")
		
		# Asking the user necssary password
		while True:
			# env.json
			# "EMAIL_HOST": "smtp.google.com",
			# "EMAIL_PORT": 587,
			# "EMAIL_USE_TLS": true,
			domain = input("domain (ie. example.com) \n: ")
			email_host = input("SMTP Server url (ie. smtp.google.com)\n: ")
			email_port = input("SMTP Server port (ie. 587) \n: ")
			email_use_tls = input("enable tls (true/false) \n: ").lower()
			# auth.json
			# "EMAIL_HOST_PASSWORD": "",
			# "EMAIL_HOST_USER": "",
			email_host_password = input("SMTP Server password \n: ")
			email_host_username = input("SMTP Server user \n: ")

			# if the user made a mistake and wants to reneter all the information again
			userInput = input("Do you want re-enter the above inputs? Enter everything above again. (Y/N) \n: ")
			# if the user made does not wants to make enter the above information again
			if userInput.lower() == "n":
				break
			# if the user made a mistake and wants to reneter all the information again
			else:
				pass

		# loading all files
		# env files
		lms_env = loadFile("lms.env.json")
		cms_env = loadFile("cms.env.json")

		# Applying the changes and saving the content to files
		applyEnvChanges(domain, email_host, email_port, email_use_tls, "lms.env.json", lms_env)
		applyEnvChanges(domain, email_host, email_port, email_use_tls, "cms.env.json", cms_env)
	
		# auth files
		lms_auth = loadFile("lms.auth.json")
		cms_auth = loadFile("cms.auth.json")

		# Applying the changes and saving the content to files
		applyAuthChanges(domain, email_host_username, email_host_password, "lms.auth.json", lms_auth)
		applyAuthChanges(domain, email_host_username, email_host_password, "cms.auth.json", cms_auth)

	# Break if the script is not running as Root/Superuser
	else:
		print("Please run this script as SUDO/ROOT")
		sys.exit(1)
		
main()
