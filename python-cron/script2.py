# script.py
import requests
import random
import string

def call_api_and_save_result():
    api_url = "https://jsonplaceholder.typicode.com/todos/2"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        filename = f"/tmp/{generate_random_string()}.txt"
        with open(filename, 'w') as file:
            file.write(str(data))
        print(f"API response saved to: {filename}")
    else:
        print(f"Failed to call API. Status code: {response.status_code}")

def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

if __name__ == "__main__":
    call_api_and_save_result()