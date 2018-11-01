import tkinter as tk
from PIL import Image, ImageTk

"""
Imports:
    tkinter as tk
    PIL

Contains:
    embed_image
"""

class PIL: # Wrapper for inability to just import PIL
    Image = Image
    ImageTk = ImageTk

def embed_image(tk_frame, image_path):
    """
    Embeds the image located at image_path
    ... into tk_frame using PIL and a tk.Label

    The tk.Label is packed, with bd=0

    Returns:
        {
            'Image': <PIL.Image> instance,
            'PhotoImage': <PIL.ImageTk.PhotoImage> instance,
            'Label': <tk.Label> instance,
        }
    """

    pil_image = PIL.Image.open(image_path)
    tk_image = PIL.ImageTk.PhotoImage(pil_image)

    label = tk.Label(tk_frame, image=tk_image, bd=0)
    label.pack()

    data = \
    {
        'Image': pil_image,
        'PhotoImage': tk_image,
        'Label': label,
    }

    return data
