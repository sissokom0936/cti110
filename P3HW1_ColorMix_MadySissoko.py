# CTI-110
# P3HW1 - Color Mixer
# Mady Sissoko
# March 8, 2020
#
color1 = input("Please enter a color between red, blue and yellow:")
color2 = input("Please enter another different color between red, blue and yellow:")

if color1 == "red" and color2 == "yellow" or color1 == "yellow"  and color2 == "red":
    print("Orange")
elif color1 == "blue" and color2 == "yellow" or color1 == "yellow" and color2 == "blue":
    print("Green")
elif color1 == "blue" and color2 == "red" or color1 == "red" and color2 == "blue":
    print("Purple")
else:
    print("Error")
