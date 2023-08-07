from PIL import Image, ImageDraw, ImageFont

# Create a blank label with a background color
label_width = 300
label_height = 150
background_color = (200, 200, 200)
label = Image.new("RGB", (label_width, label_height), background_color)

# Load the logo image
logo = Image.open("icon.png")  # Replace with the path to your logo image

# Resize the logo image to fit within the label width
max_logo_width = label_width - 40  # Adjust margin
logo.thumbnail((max_logo_width, label_height))

# Paste the logo onto the label
logo_x = (label_width - logo.width) // 2
logo_y = (label_height - logo.height) // 2
label.paste(logo, (logo_x, logo_y))

# Create a drawing object
draw = ImageDraw.Draw(label)

# Prepare your data
data = "ksjhfkjdhfkjhs"

# Define font and size for the data
font = ImageFont.truetype("arial.ttf", 16)  # Replace with your font path

# Calculate the position to center the data text horizontally
data_width, data_height = draw.textsize(data, font=font)
data_x = (label_width - data_width) // 2
data_y = logo_y + logo.height + 10  # Position below the logo

# Draw the data text on the label
draw.text((data_x, data_y), data, fill=(0, 0, 0), font=font)

# Save or display the label image
label.save("output_label.png")  # Save the label image
label.show()  # Display the label image
