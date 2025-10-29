from colors import Colors

red = Colors.BG_BRIGHT_RED + "  " + Colors.RESET
white = Colors.BG_BRIGHT_WHITE + "  " + Colors.RESET
black = Colors.BG_BLACK + "  " + Colors.RESET
blue = Colors.BG_BRIGHT_BLUE + "  " + Colors.RESET
yellow = Colors.BG_BRIGHT_YELLOW + " " + Colors.RESET
green = Colors.BG_BRIGHT_GREEN + " " + Colors.RESET
brown = Colors.BG_BRIGHT_BROWN + " " + Colors.RESET

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


for i in mario2:
    print("".join(i))