# script.py
import os
import random
import string

def generate_random_file():
    filename = '/tmp/' + ''.join(random.choices(string.ascii_lowercase, k=8)) + '.txt'
    with open(filename, 'w') as file:
        file.write("This is a random file content.")
    print(f"Generated file: {filename}")

if __name__ == "__main__":
    generate_random_file()