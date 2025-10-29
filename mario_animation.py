from colors import Colors
import os
import time

red = Colors.BG_BRIGHT_RED + "  " + Colors.RESET
white = Colors.BG_BRIGHT_WHITE + "  " + Colors.RESET
black = Colors.BG_BLACK + "  " + Colors.RESET
blue = Colors.BG_BRIGHT_BLUE + "  " + Colors.RESET
yellow = Colors.BG_BRIGHT_YELLOW + " " + Colors.RESET
green = Colors.BG_BRIGHT_GREEN + " " + Colors.RESET
brown = Colors.BG_BRIGHT_BROWN + " " + Colors.RESET

def clear_screen():
    if os.name == 'nt':
        os.system("cls")

mario1 = [
    [(white * 4),white,white, red, red, red, red, red, red, (white * 8)],
    [(white * 4),red, red, red, red, red, red, red, red, red, red, red, red, red, (white * 8)],
    [(white * 4), white, white, green, green, green, green, green, green, green, yellow, yellow, yellow, yellow, green, green, green, yellow, yellow, yellow, white * 8],
    [(white * 4), green, green, green, green, yellow, yellow, yellow, green, green, yellow, yellow, yellow, yellow, yellow, yellow, green, green, green, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, (white * 8)],
    [(white * 4), green, green, green, green, yellow, yellow, yellow, green, green, green, green, yellow, yellow, yellow, yellow, yellow, yellow, yellow, green, green, green, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, (white * 8)],
    [(white * 4),green, green, green, green, green, green, green, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, green, green, green, green, green, green, green, green, green, green, green, (white * 8)],
    [(white * 4), white, white, white, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, (white * 8)],
    [(white * 4), white, white, green, green, green, green, green, red, green , green, green, red, green , green , green , green, green ,green, green, (white * 8)],
    [(white * 4), green, green, green, green, green, green , green, green, green, red, green, green,green, red, green, green, green, green, green, green, green, green, green, green, (white * 8)],
    [(white * 2), (green * 13), red, green, green,green, red, (green * 13), (white * 8)],
    [(white * 2), (yellow * 8), (green * 2), (red), (yellow * 2), (red * 2), yellow, yellow, (red * 1), (green * 5), (yellow * 6), (white * 8)],
    [(white * 2), (yellow * 10), (red * 6), (yellow * 11), (white * 8)],
    [(white * 2), (yellow * 8), (red * 10), (yellow * 5), (white * 8)],
    [(white * 6), (red * 3), (white * 2), (red * 5), (white * 8)],
    [(white * 4), (brown * 7), (white * 6), (brown * 8), (white * 8)],
    [(white * 2), (brown * 11), (white * 6), (brown * 11), (white * 8)]
]

mario2 = [
    [(white * 20), (yellow * 9),],
    [(white * 10), (red * 7), (white * 3), (yellow * 9)],
    [(white * 9), (red * 12), (yellow * 7)],
    [(white * 9), (green * 8), (yellow * 5), (green * 3), (yellow * 3), (white), (red * 5)],
    [(white * 7), (green * 4), (yellow * 2), (green * 3), (yellow * 8), (green * 3), (yellow * 5), (red * 5)],
    [(white * 7), (green * 4), (yellow * 2), (green * 6), (yellow * 8), (green * 3), (yellow * 8), (red * 2)],
    [(white * 7), (green * 6), (yellow * 11), (green * 14), (white * 2)],
    [(white * 10), (yellow * 19), (green * 4), (white * 3)],
    [(white * 4), (green * 14), (red * 2), (green * 6), (red * 2), (green * 3), (white * 5)],
    [(white * 2), (green * 21), (red * 2), (green * 6), (red * 2), (white * 3), (green * 4)],
    [(yellow * 8), (green * 17), (red * 7), (white * 3), (green * 4)],
    [(yellow * 11), (white * 2), (red * 2), (green * 4), (red * 3), (yellow * 3), (red * 2), (yellow * 3),(red * 2), (green * 6)],
    [(white * 2), (yellow * 3), (white * 2), (green * 4), (red * 14), (green * 6)],
    [(white * 4), (green * 9), (red * 13), (green * 6)],
    [(white * 2), (green * 11), (red * 10), (white * 7)],
    [(white * 2), (green * 3), (white * 4), (red * 6), (white * 11)]
]

def main():
    for i in range(200):
        for i in mario1:
            print("".join(i))
        time.sleep(0.3)
        clear_screen()

        for j in mario2:
            print("".join(j))
        time.sleep(0.3)
        clear_screen()
    

if __name__ == "__main__":
    main()