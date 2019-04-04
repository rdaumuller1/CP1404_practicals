HEX_COLOURS = {"blue1": "#0000ff", "CadetBlue": "#5f9ea0", "coral": "#ff7f50", "DarkSalmon": "#e9967a",
               "firebrick": "#b22222", "gold1": "#ffd700", "green1": "#00ff00", "LightBlue": "#add8e6",
               "magenta": "#ff00ff", "orange1": "#ffa500"}

colour = input("Enter colour name: ")
while colour != "":
    if colour in HEX_COLOURS:
        print(colour, "is", HEX_COLOURS[colour])
    else:
        print("Invalid colour name")
    state = input("Enter colour name: ")
exit()
