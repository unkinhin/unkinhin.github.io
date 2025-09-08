from PIL import Image, ImageDraw

def floyd_steinberg_dithering(image, dot_size, levels):
    width, height = image.size
    new_width = 750
    new_height = int((height/width) * new_width)
    process = image.resize((new_width,new_height))
    pixels = process.load()

    # Create a new blank image with the same size as the input image
    dot_image = Image.new('L', (new_width * dot_size, new_height * dot_size), 255)

    # Create a new ImageDraw object for drawing circles
    draw = ImageDraw.Draw(dot_image)

    # Define the circle radius as half the dot size
    radius = dot_size // 2

    for y in range(new_height - 1):
        for x in range(1, new_width - 1):
            old_pixel = pixels[x, y]
            new_pixel = int(round(old_pixel / 255 * (levels - 1)) * (255 / (levels - 1)))

            # Set the dot color based on the quantized pixel value
            dot_color = int(new_pixel) + 50

            # Draw a circle at the current pixel position
            x_pos = x * dot_size + dot_size // 2
            y_pos = y * dot_size + dot_size // 2
            draw.ellipse((x_pos - radius, y_pos - radius, x_pos + radius, y_pos + radius), fill=dot_color)

            quant_error = old_pixel - new_pixel

            # Distribute the error to neighboring pixels
            if x + 1 < new_width:
                pixels[x + 1, y] += int(quant_error * 7 / 16)
            if x - 1 >= 0 and y + 1 < new_height:
                pixels[x - 1, y + 1] += int(quant_error * 3 / 16)
            if y + 1 < new_height:
                pixels[x, y + 1] += int(quant_error * 5 / 16)
            if x + 1 < new_width and y + 1 < new_height:
                pixels[x + 1, y + 1] += int(quant_error * 1 / 16)

    return dot_image

# Load the input image and convert to grayscale
input_image = Image.open("Poster.jpg").convert("L")

# Apply halftone with the desired parameters
output_image = floyd_steinberg_dithering(input_image, dot_size=10, levels=10)

# Display the output image
output_image.show()