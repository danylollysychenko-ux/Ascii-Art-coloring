from colors import Colors

red = Colors.BG_BRIGHT_RED + "  " + Colors.RESET
white = Colors.BG_BRIGHT_WHITE + "  " + Colors.RESET
black = Colors.BG_BLACK + "  " + Colors.RESET
blue = Colors.BG_BRIGHT_BLUE + "  " + Colors.RESET
yellow = Colors.BG_BRIGHT_YELLOW + " " + Colors.RESET
green = Colors.BG_BRIGHT_GREEN + " " + Colors.RESET
brown = Colors.BG_BRIGHT_BROWN + " " + Colors.RESET

mario = [
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

for i in mario:
    print("".join(i))