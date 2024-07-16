from tkinter import *
from tkinter import filedialog, messagebox

from PIL import Image, ImageTk, ImageDraw, ImageFont


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark Application")

        self.canvas = Canvas(root, width=600, height=400, bg='gray')
        self.canvas.pack()

        self.upload_button = Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.water_mark_label = Label(root, text="Water mark text: ")
        self.water_mark_label.pack()

        self.entry = Entry(root)
        self.entry.pack()

        self.apply_watermark = Button(root, text="Apply watermark", command=self.apply_watermark)

        self.apply_watermark.pack()

        self.save_button = Button(root, text="Save Image", command=self.save_button)
        self.save_button.pack()

        self.image = None
        self.image_path = ""

    def upload_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            self.image = Image.open(self.image_path)
            self.display_image(self.image)

    def display_image(self, image):
        img = image.resize((600, 400), Image.LANCZOS)
        self.tk_img = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=NW, image=self.tk_img)

    def apply_watermark(self):
        if self.image:
            watermark_text = self.entry.get()
            if watermark_text:
                watermark_image = self.image.copy()
                draw = ImageDraw.Draw(watermark_image)

                font = ImageFont.truetype("arial.ttf", 40)

                # Get the size of the text
                width, height = watermark_image.size

                bbox = draw.textbbox((0, 0), text=watermark_text, font=font)
                text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

                # Calculate the position of the text
                x = width - text_width - 10
                y = height - text_height - 10

                # Draw the text
                draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))
                self.display_image(watermark_image)
                self.watermarked_image = watermark_image

            else:
                messagebox.showerror("Error", "Please write watermark text.")
        else:
            messagebox.showerror("Error","Please upload the Image first.")



    def save_button(self):
        if hasattr(self, 'watermarked_image'):
            save_file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"),
                                                                                              ("All files", "*.*")])
            if save_file_path:
                self.watermarked_image.save(save_file_path)
                messagebox.showinfo("Success", "Image saved successfully")

        else:
            messagebox.showerror("Error", "Please apply a watermark first.")


if __name__ == "__main__":
    root = Tk()
    app = WatermarkApp(root)
    root.mainloop()
