from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont, ImageText


name=input("Name: ")
shirt=Image.open("shirtificate.png")
font = ImageFont.load("arial.pill")

text = ImageText.Text("Hello world", font)
text.embed_color()
text.stroke(2, "#0f0")

print(text.get_length())  # 154.0
print(text.get_bbox())  # (-2, 3, 156, 22)

im = Image.new("RGB", text.get_bbox()[2:])
d = ImageDraw.Draw(im)
d.text((0, 0), text, "#f00")

pdf=FPDF(oreintation="P", unti="mm", format="A4")

