def convert_minutes_to_seconds(raw_val: int) -> int:
    calc1 = raw_val // 100
    num2 = calc1 * 40
    return raw_val - num2

def run_cli():
    while True:
        print("Welcome to min to sec!\nType minute with no dots like (2.30m = 230)")
        raw_input_str = input("NUMBER : ")
        if not raw_input_str.isdigit():
            print("Invalid number format!")
            continue
        num1 = int(raw_input_str)
        result = convert_minutes_to_seconds(num1)
        print("\nSeconds:", result)

        sel = input("Do you want to exit? (y/n): ").lower()
        if sel == "y":
            break

if __name__ == "__main__":
    run_cli()
