from PIL import Image, ImageDraw, ImageFont
import textwrap

# Load the image
image_template_path = '../images/lean_canvas_template.png'  # Update to the path of your Lean Canvas image
image_template = Image.open(image_template_path)
draw = ImageDraw.Draw(image_template)

# Choose a font and size
font_path = '../fonts/Montserrat-Black.otf'  # Update to the path of a font file
font_size = 12
font = ImageFont.truetype(font_path, font_size)

# Define the coordinates for each box on the Lean Canvas (left, top, right, bottom)
horiz_top_y1 = 40
horiz_bottom_y1 = 340
horiz_top_y2 = 400
horiz_bottom_y2 = 700
horiz_top_y3 = 760
horiz_bottom_y3 = 1000
vert_left_x1 = 4
vert_right_x1 = 260
vert_left_x2 = 280
vert_right_x2 = 540
vert_left_x3 = 570
vert_right_x3 = 810
vert_left_x4 = 710
vert_right_x4 = 1100
vert_left_x5 = 850
vert_right_x5 = 1380

box_coords = {
    "Problem": (vert_left_x1, horiz_top_y1, vert_right_x1, horiz_bottom_y2),
    "Solution": (vert_left_x2, horiz_top_y1, vert_right_x2, horiz_bottom_y1),
    "Key Metrics": (vert_left_x2, horiz_top_y2, vert_right_x2, horiz_bottom_y2),
    "Unique Value Proposition": (vert_left_x3, horiz_top_y1, vert_right_x3, horiz_bottom_y2),
    # "Unfair Advantage": (vert_left_x4, horiz_top_y1, vert_right_x4, horiz_bottom_y1),
    # "Channels": (vert_left_x2, horiz_top_y1, vert_right_x2, horiz_bottom_y1),
    # "Customer Segments": (vert_left_x2, horiz_top_y1, vert_right_x2, horiz_bottom_y1),
    # "Cost Structure": (vert_left_x2, horiz_top_y1, vert_right_x2, horiz_bottom_y1),
    # "Revenue Streams": (vert_left_x2, horiz_top_y1, vert_right_x2, horiz_bottom_y1),
}

filler_text = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type 
specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in 
the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
and more recently with desktop publishing software like Aldus PageMaker including 
versions of Lorem Ipsum.
"""
# Define the text content for each box
box_texts = {
    "Problem": "Describe the problem bro bro bro ...",
    "Solution": "Describe the solution \nbro bro bro ...",
    "Unique Value Proposition": "Describe the Unique Value Proposition...",
    # "Unfair Advantage": "Describe the Unfair Advantage...",
    # "Channels": "Describe the Unfair Advantage...",
    # "Customer Segments": "Describe the Customer Segments...",
    # "Cost Structure": "Describe the Cost Structure...",
    # "Revenue Streams": "Describe the Revenue Streams...",
}

# Function to wrap and position text within a box
def draw_text_in_box(draw, text, box, font):
    print(len(text))
    x1, y1, x2, y2 = box
    box_width = x2 - x1
    box_height = y2 - y1

    # Estimate characters per line based on average character width at the given font size
    average_char_width = draw.textlength('x', font=font)
    est_chars_per_line = max(1, int(box_width / average_char_width))  # Ensure at least 1 character per line

    # Wrap the text according to estimated characters per line
    lines = textwrap.wrap(text, width=est_chars_per_line)

    y_offset = y1
    for line in lines:
        # Get text dimensions using textlength and getsize
        text_width = draw.textlength(line, font=font)
        print(text_width)
        # text_height = font.getsize(line)[1]  # Use font.getsize for height
        text_height = font.getbbox(line)[3]
        print(text_height)

        # Check if there's enough vertical space left to draw the text
        if y_offset + text_height <= y2:
            x_offset = x1 + (box_width - text_width) // 2  # Center text horizontally
            draw.text((x_offset, y_offset), line, fill=(0, 0, 0), font=font)
            y_offset += text_height
        else:
            # Stop if the text exceeds the box height
            break



# Iterate over each box and draw the text
for box_name, text in box_texts.items():
    draw_text_in_box(draw, text, box_coords[box_name], font)

# Save or display the updated canvas image
updated_canvas_path = '../images/drawn_lean_canvas.png'
image_template.save(updated_canvas_path)
image_template.show()


# Coordinates: (17, 41)
# Coordinates: (265, 44)
# Coordinates: (26, 691)
# Coordinates: (262, 695)
# Coordinates: (295, 51)
# Coordinates: (545, 49)
# Coordinates: (299, 336)
# Coordinates: (537, 338)
# Coordinates: (298, 403)
# Coordinates: (535, 401)
# Coordinates: (299, 695)
# Coordinates: (537, 694)
# Coordinates: (574, 47)
# Coordinates: (820, 51)
# Coordinates: (575, 696)
# Coordinates: (817, 701)
# Coordinates: (848, 46)
# Coordinates: (1098, 46)
# Coordinates: (850, 339)
# Coordinates: (1098, 338)
# Coordinates: (848, 404)
# Coordinates: (1101, 407)
# Coordinates: (851, 695)
# Coordinates: (1098, 699)
# Coordinates: (1124, 41)
# Coordinates: (1376, 47)
# Coordinates: (1130, 694)
# Coordinates: (1378, 699)
# Coordinates: (20, 761)
# Coordinates: (682, 762)
# Coordinates: (26, 988)
# Coordinates: (680, 996)
# Coordinates: (715, 759)
# Coordinates: (1374, 754)
# Coordinates: (714, 994)
# Coordinates: (1375, 995)