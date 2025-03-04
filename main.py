from art import text2art
import colorama

def select_font():
    fonts = ["block", "banner", "standard", "avatar", "3d_diagonal"]
    print("Choose a font for your ASCII art:")
    for i, font in enumerate(fonts, start=1):
        print(f"{i}. {font}")

    while True:
        choice = input("Enter the number of your font choice: ")
        if choice.isdigit() and 0 < int(choice) <= len(fonts):
            return fonts[int(choice) - 1]
        else:
            print("Invalid choice. Please enter a valid number.")

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def select_color():
    colors = {
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
        "magenta": "35",
        "cyan": "36",
        "white": "37"
    }
    
    print("Choose a color:")
    for color in colors:
        print(color)
    
    while True:
        color_choice = input("Enter the name of the chosen color (leave empty for no specific color): ").lower()
        if color_choice in colors or not color_choice:
            return colors.get(color_choice, "")
        else:
            print("Invalid color. Please enter a valid color name.")

def main():
    colorama.init()

    while True:
        s = input("Write something: ")
        if not s.strip():
            print("Please enter a word or a sentence.")
            continue

        font_choice = select_font()
        color_code = select_color()
        ascii_art = text2art(s, font=font_choice)
        colored_ascii_art = color_text(ascii_art, color_code) if color_code else ascii_art
        print(colored_ascii_art)

        while True:
            continue_choice = input("Do you want to continue? (yes/no): ").lower()
            if continue_choice in ["yes", "no"]:
                break
            else:
                print("Invalid response. Please answer 'yes' or 'no'.")

        if continue_choice == "no":
            break

if __name__ == "__main__":
    main()
