from PIL import Image, ImageDraw, ImageFont
import textwrap

# Load the image
image_template_path = '../images/lean_canvas_template.png'  # Update to the path of your Lean Canvas image
image_template = Image.open(image_template_path)
draw = ImageDraw.Draw(image_template)

# Choose a font and size
font_path = '../fonts/Montserrat-Black.otf'  # Update to the path of a font file
font_size = 14
font = ImageFont.truetype(font_path, font_size)

# Define the coordinates for each box on the Lean Canvas (left, top, right, bottom)
horiz_top_y1 = 40
horiz_bottom_y1 = 340
horiz_top_y2 = 400
horiz_bottom_y2 = 700
horiz_top_y3 = 760
horiz_bottom_y3 = 1000
vert_left_x1 = 14
vert_right_x1 = 260
vert_left_x2 = 290
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
""" * 2
# Define the text content for each box
box_texts = {
    "Problem": f"Describe the problem {filler_text}...",
    "Solution": f"Describe the solution {filler_text}...",
    "Unique Value Proposition": "Describe the Unique Value Proposition...",
    # "Unfair Advantage": "Describe the Unfair Advantage...",
    # "Channels": "Describe the Unfair Advantage...",
    # "Customer Segments": "Describe the Customer Segments...",
    # "Cost Structure": "Describe the Cost Structure...",
    # "Revenue Streams": "Describe the Revenue Streams...",
}

# Function to wrap and position text within a box
def draw_text_in_box(draw, text, box, font):
    x1, y1, x2, y2 = box
    box_width = x2 - x1

    # Estimate characters per line based on average character width at the given font size
    average_char_width = draw.textlength('x', font=font)
    est_chars_per_line = max(1, int(box_width / average_char_width))  # Ensure at least 1 character per line

    # Wrap the text according to estimated characters per line
    lines = textwrap.wrap(text, width=est_chars_per_line)

    y_offset = y1
    for line in lines:
        # Get text dimensions for height
        text_height = draw.textbbox((0, 0), line, font=font)[3]

        # Check if there's enough vertical space left to draw the text
        if y_offset + text_height <= y2:
            # Left align text by using x1 as the x_offset
            draw.text((x1, y_offset), line, fill=(0, 0, 0), font=font)
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
