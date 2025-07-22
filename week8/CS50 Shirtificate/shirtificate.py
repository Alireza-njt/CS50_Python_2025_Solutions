# Alireza Nejati (alirezanejatiz27@gmail.com)
# Tuesday , July 22 , 2025

from fpdf import FPDF

name = input("Name: ").strip()
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=False, margin=0)
pdf.set_font("Helvetica", "B", 50)
pdf.cell(0, 50, txt="CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.image("shirtificate.png", x=5, y=80, w=200)
pdf.set_font("Helvetica", "B", size=30)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 180, align="C", txt=f"{name} took CS50")
pdf.output("shirtificate.pdf")
