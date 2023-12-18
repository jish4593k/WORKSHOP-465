import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from torchvision import transforms
from scipy.stats import mode
import torch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class ImageToPDFConverter:
  

    def select_file(self):
        self.file_names = filedialog.askopenfilenames(initialdir="/", title="Select File")
        self.display_images()

    def display_images(self):
        self.canvas.delete("all")
        for file_name in self.file_names:
            image = Image.open(file_name)
            image.thumbnail((250, 250))
            photo_image = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo_image)
            self.canvas.photo = photo_image

    def image_to_pdf(self):
        if not self.file_names:
            return

        image = Image.open(self.file_names[0])
        tensor_image = transforms.ToTensor()(image)
        pdf_path = "file_image.pdf"

        with open(pdf_path, "wb") as f:
            f.write(self.tensor_to_pdf(tensor_image))

    def images_to_pdf(self):
        if not self.file_names:
            return

        pdf_path = "files_images.pdf"
        pdf_content = b""
        for file_name in self.file_names:
            image = Image.open(file_name)
            tensor_image = transforms.ToTensor()(image)
            pdf_content += self.tensor_to_pdf(tensor_image)

        with open(pdf_path, "wb") as f:
            f.write(pdf_content)

    def tensor_to_pdf(self, tensor_image):
      ue
        most_common_byte = mode(tensor_image.view(-1).numpy()).mode.item()
        tensor_image_mode = tensor_image.new_full(tensor_image.shape, most_common_byte)

s
        image_bytes = tensor_image_mode.numpy().tobytes()

        
        pdf_path = io.BytesIO()
        pdf_canvas = canvas.Canvas(pdf_path, pagesize=letter)
        pdf_canvas.drawInlineImage(image_bytes, 0, 0, letter[0], letter[1])
        pdf_canvas.save()

        return pdf_path.getvalue()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToPDFConverter(root)
    root.mainloop()
