# Author: Muhammad Faheem Khan
# Date: 9 July 2019
# Filename: settings_wrapper.py
# Dependencies: settings_wrapper_config.json
# DescriptionL This program aims help edit open edx configurations files lms.env.json, cms.env.json

import sys
import json

def print_options():
    '''
    This function prints all the menu options
    '''
    print("Configuration Wrapper for Open edx")
    print("Version: 1.0.0")
    print("1 - LMS Settings")
    print("2 - CMS Settings")
    print("3 - Default Settings")
    print("4 - Exit")

def loadSettings(fname):
    print("Attepmting to load %s" % fname)
    with open(fname, "r") as f:
        default_settings = json.load(f)
        print("Settings successfully loaded")
        return default_settings

def writeSettings(fname, settings):
    print("Attempting to save (Overwrite) %s" % fname)
    with open(fname, "w") as f:
        json.dump(settings, f)
        print("File successfull saved")

def previewSettings(settings, fname):
    print("Preview of %s" % fname)
    print(json.dumps(settings, indent=4, sort_keys=True))

def editManagementSettings(fname):
    settings = loadSettings(fname)
    previewSettings(settings, fname)
    print("Elements: %d" % len(settings))
    print("Editing Rules")
    print("To Skip Editing Option: +")
    for index, element in enumerate(settings, start=0):
        print(element + ": " + str(settings[element]))
        userInput = input(": ")
        if userInput != "":
            settings[element] = userInput
        else: pass
    previewSettings(settings, fname)
    writeSettings(fname, sorted(settings))
    
    
def menu():
    # loading settings from the default settings file
    settings_file = "settings_wrapper_config.json"
    default_settings = loadSettings(settings_file)
    print_options() # printing menu options
    option = input(": ")

    if option == "1":
        print("LMS Settings")
        editManagementSettings(default_settings["defaults"]["lms_config"])
        menu()

    elif option == "2":
        print("CMS Settings")
        editManagementSettings(default_settings["defaults"]["cms_config"])
        menu()
    
    elif option == "3":
        previewSettings(default_settings, settings_file)
        menu()
    
    elif option == "4":
        print("Exiting")
        sys.exit(0)
    
    else:
        print("Invalid option")
        print("Please Choose a number corresponding to the option")
        print("\n")
        menu()
    
menu()