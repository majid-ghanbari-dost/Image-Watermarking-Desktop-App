from tkinter import Tk, filedialog, Entry, Button
from PIL import Image, ImageDraw, ImageFont

# Create the main window
root = Tk()
root.title("Image Watermarking App")

# Function to open the image file
def open_image():
    global image_path
    image_path = filedialog.askopenfilename(title="Select Image")
    image_path_entry.delete(0, END)
    image_path_entry.insert(0, image_path)

# Function to add watermark and save image
def add_watermark():
    if image_path:
        # Open image using Pillow
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)

        # Get watermark text and font from UI
        watermark_text = watermark_text_entry.get()
        if not watermark_text:
            print("Please enter watermark text!")
            return

        try:
            watermark_font = ImageFont.truetype(font_path.get(), int(font_size_entry.get()))
        except FileNotFoundError:
            print("Font file not found!")
            return
        except ValueError:
            print("Invalid font size!")
            return

        # Get image and watermark text dimensions
        image_width, image_height = image.size
        watermark_width, watermark_height = draw.textsize(watermark_text, font=watermark_font)

        # Calculate watermark position (adjust for different positions)
        watermark_x = int(watermark_x_entry.get())
        watermark_y = int(watermark_y_entry.get())

        # Set watermark transparency (0-255)
        try:
            opacity = int(opacity_entry.get())
            if opacity < 0 or opacity > 255:
                raise ValueError
        except ValueError:
            print("Invalid opacity!")
            return

        # Draw watermark text on the image with transparency
        draw.text((watermark_x, watermark_y), watermark_text, font=watermark_font, fill=(255, 255, 255, opacity))

        # Save the watermarked image
        save_path = save_path_entry.get()
        if not save_path:
            save_path = "watermarked_image.jpg"

        try:
            image.save(save_path)
            print("Image watermarked and saved to:", save_path)
        except Exception as e:
            print("Error saving image:", e)

    else:
        print("Please select an image first!")

# Labels and entry fields for watermark settings
watermark_text_label = Label(root, text="Watermark Text:")
watermark_text_label.pack()
watermark_text_entry = Entry(root)
watermark_text_entry.pack()

font_path_label = Label(root, text="Font Path:")
font_path_label.pack()
font_path = Entry(root)
font_path.pack()

font_size_label = Label(root, text="Font Size:")
font_size_label.pack()
font_size_entry = Entry(root)
font_size_entry.pack()

watermark_x_label = Label(root, text="Watermark X:")
watermark_x_label.pack()
watermark_x_entry = Entry(root)
watermark_x_entry.pack()

watermark_y_label = Label(root, text="Watermark Y:")
watermark_y_label.pack()
watermark_y_entry = Entry(root)
watermark_y_entry.pack()

opacity_label = Label(root, text="Opacity (0-255):")
opacity_label.pack()
opacity_entry = Entry(root)
opacity_entry.pack()

save_path_label = Label(root, text="Save Path:")
save_path_label.
*
