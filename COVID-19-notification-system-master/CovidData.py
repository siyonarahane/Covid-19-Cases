import requests
from bs4 import BeautifulSoup
import re
from PIL import Image, ImageDraw, ImageFont

url = "https://www.mohfw.gov.in/"  # Replace this with your URL
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")

# Example: Retrieving all elements with a specific class name
specific_class = "col-xs-8 site-stats-count"
elements_with_class = soup.find_all(class_=specific_class)
line = ""
for element in elements_with_class:
    line += (element.text)

ans = ""
i = -1
while (i < len(line) - 1):
    i += 1
    currChar = line[i]
    key = ""
    while (i < len(line) and currChar.isalpha()):
        currChar = line[i]
        ans += currChar
        i += 1
    if (currChar.isdigit()):
        ans += "-"

    while (i < len(line) and currChar.isdigit()):
        currChar = line[i]
        ans += currChar
        i += 1

key_value_pairs = re.findall(r'(\w+)\s*-\s*(\S+)', ans)
result_dict = {key: value for key, value in key_value_pairs}

states = ["Maharashtra", 'Delhi', "Goa"]

# Load the icon image
icon = Image.open("icon.png")  # Replace with the path to your icon image

# Create a blank image with a white background
image_width = 700
image_height = 275
background_color = (200, 200, 200)
image = Image.new("RGB", (image_width, image_height), background_color)

# Calculate the position to center the icon horizontally
icon_x = (image_width - icon.width) // 1
icon_y = 5  # Adjust this value to position the icon vertically

# Paste the icon onto the image
image.paste(icon, (icon_x, icon_y))

# Create a drawing object
draw = ImageDraw.Draw(image)

# Define text box dimensions
textbox_x = 15
textbox_y = 20
textbox_width = 10
textbox_height = 30

# Define font and size
font = ImageFont.truetype("arial.ttf", 20)  # Replace with your font path

# Fill the rectangle for the text box without outline
textbox_background_color = (200, 200, 200)
draw.rectangle([(textbox_x, textbox_y), (textbox_x + textbox_width, textbox_y + textbox_height)],
               fill=textbox_background_color)

# Print bold title
title = "Cases of COVID-19 India"
# Define font and size for the bold title
title_font_bold = ImageFont.truetype("arialbd.ttf", 30)  # Use the bold variant of the font (change the path accordingly)
title_x = textbox_x + 25
title_y = textbox_y + 10
draw.text((title_x, title_y), title, fill=(0, 0, 0), font=title_font_bold)

# Loop through dictionary items and print key-values inside the text box
x = textbox_x + 70
y = title_y + 45  # Adjust y-coordinate based on title position
for key, value in result_dict.items():
    text = f"{key}: {value}"
    draw.text((x, y), text, fill=(0, 0, 0), font=font)
    y += 40  # Adjust vertical spacing

    if key.upper() in states:
        state_text = f"State: {key}"
        draw.text((x, y), state_text, fill=(0, 0, 0), font=font)
        y += 45  # Adjust vertical spacing

# Save or display the modified image
image.save("output_image_with_text_box.jpg")  # Save the modified image
image.show()  # Display the modified image
