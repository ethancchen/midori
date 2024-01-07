from PIL import Image, ImageDraw, ImageFont
from pathlib import PurePath as pp
import textwrap
import os
import streamlit as st



def draw(): 
    # get the current working directory
    # current_working_directory = os.getcwd()
    # # print output to the console
    # # st.write(current_working_directory)
    # print(current_working_directory)

    # Load the image
    # image_template_path = './images/lean_canvas_template.png'  # Update to the path of your Lean Canvas image
    image_template_path = pp('images/lean_canvas_template.png')

    image_template = Image.open(image_template_path.as_posix())
    draw = ImageDraw.Draw(image_template)

    # Choose a font and size
    # font_path = 'fonts/Montserrat-Black.otf'  # Update to the path of a font file
    font_path = pp('fonts/Montserrat-Black.otf')

    font_size = 18
    font = ImageFont.truetype(font_path.as_posix(), font_size)

    # Define the coordinates for each box on the Lean Canvas (left, top, right, bottom)
    small_box_height = 300
    small_box_width = 245
    large_box_width = 670
    box_height_dist1 = 360

    horiz_top_y1 = 40
    horiz_top_y2 = horiz_top_y1 + box_height_dist1
    horiz_bottom_y2 = 700
    horiz_top_y3 = 760
    horiz_bottom_y3 = 1000
    vert_left_x1 = 15
    vert_left_x2 = 290
    vert_left_x3 = 570
    vert_left_x4 = 710
    vert_left_x5 = 850
    vert_left_x6 = 1130

    box_coords = {
        "Problem": (vert_left_x1, horiz_top_y1, vert_left_x1 + small_box_width, horiz_bottom_y2),
        "Solution": (vert_left_x2, horiz_top_y1, vert_left_x2 + small_box_width, horiz_top_y1 + small_box_height),
        "Key Metrics": (vert_left_x2, horiz_top_y2, vert_left_x2 + small_box_width, horiz_bottom_y2),
        "Unique Value Proposition": (vert_left_x3, horiz_top_y1, vert_left_x3 + small_box_width, horiz_bottom_y2),
        "Unfair Advantage": (vert_left_x5, horiz_top_y1, vert_left_x5 + small_box_width, horiz_top_y1 + small_box_height),
        "Channels": (vert_left_x5, horiz_top_y2, vert_left_x5 + small_box_width, horiz_bottom_y2),
        "Customer Segments": (vert_left_x6, horiz_top_y1, vert_left_x6 + small_box_width, horiz_bottom_y2),
        "Cost Structure": (vert_left_x1, horiz_top_y3, vert_left_x1 + large_box_width, horiz_bottom_y3),
        "Revenue Streams": (vert_left_x4, horiz_top_y3, vert_left_x6 + small_box_width, horiz_bottom_y3),
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
        "Problem": f"Describe the problem ... {filler_text}",
        "Solution": f"Describe the solution ... {filler_text}",
        "Key Metrics": f"Describe the key metrics ... {filler_text}",
        "Unique Value Proposition": f"Describe the unique value proposition ... {filler_text}",
        "Unfair Advantage": f"Describe the unfair advantage ... {filler_text}",
        "Channels": f"Describe the channels ... {filler_text}",
        "Customer Segments": f"Describe the Customer Segments ... {filler_text}",
        "Cost Structure": f"Describe the Cost Structure ... {filler_text}",
        "Revenue Streams": f"Describe the Revenue Streams ... {filler_text}",
    }

    # Function to wrap and position text within a box
    def draw_text_in_box(draw, text, box, font, line_spacing = 4):
        x1, y1, x2, y2 = box
        box_width = x2 - x1

        # Split the text into words
        words = text.split()
        lines = []
        current_line = ''

        # Determine the height of a single line of text
        single_line_height = font.getbbox('Ay')[3]  # Use characters like 'Ay' that have both ascenders and descenders

        # Accumulate lines of text, breaking at words
        for word in words:
            # Add a space if not the first word in a line
            test_line = current_line + (' ' if current_line else '') + word
            test_line_width = draw.textlength(test_line, font=font)
            # If the word fits, continue the line
            if test_line_width <= box_width:
                current_line = test_line
            else:
                # If the word doesn't fit, start a new line
                lines.append(current_line)
                current_line = word
        # Add the last line
        lines.append(current_line)

        # Draw the text line by line
        y_offset = y1
        for line in lines:
            if y_offset + single_line_height <= y2:
                # Left-align text by setting the x-coordinate to x1
                draw.text((x1, y_offset), line, fill=(0, 0, 0), font=font)
                y_offset += single_line_height + line_spacing  # Move down by the height of a line plus spacing
            else:
                break  # Stop if there is no vertical space for more lines


    # Iterate over each box and draw the text
    for box_name, text in box_texts.items():
        draw_text_in_box(draw, text, box_coords[box_name], font)

    # Save or display the updated canvas image
    updated_canvas_path = 'images/drawn_lean_canvas.png'
    # image_template.save(updated_canvas_path)
    # image_template.show()

    return image_template



img = draw()