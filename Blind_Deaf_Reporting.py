import pyttsx3
import tkinter as tk
from tkinter import scrolledtext

# Initialize the Speech Engine
engine = pyttsx3.init()

class HR:
    def __init__(self, name):
        self.name = name

    def respond(self, user, message):
        response = f"Dear {user.name}, we have received your complaint: '{message}'. We are working on it."
        return response


class User:
    def __init__(self, name, is_blind, is_deaf):
        self.name = name
        self.is_blind = is_blind
        self.is_deaf = is_deaf

    def send_message(self, hr, message):
        if self.is_blind:
            engine.say(message)
            engine.runAndWait()
        response = hr.respond(self, message)
        if self.is_deaf:
            print(response)
        if self.is_blind:
            engine.say(response)
            engine.runAndWait()


# Create a user and an HR representative
hr = HR("John")
user = User("Alice", is_blind=True, is_deaf=False)

# User sends a message
user.send_message(hr, "My delivery was delayed.")
