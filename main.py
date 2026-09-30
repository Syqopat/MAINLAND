import sys
import json
from mintosec import convert_minutes_to_seconds

def main():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
    except Exception:
        config = {"default_format": "sec"}
    
    print("MAINLAND Utility Toolkit")
    print("1. Minute to Second Converter")
    print("2. Exit")
    choice = input("Select option: ")
    if choice == "1":
        val = input("Enter minutes (e.g. 230 for 2m30s): ")
        if val.isdigit():
            res = convert_minutes_to_seconds(int(val))
            print(f"Result: {res} seconds")
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
