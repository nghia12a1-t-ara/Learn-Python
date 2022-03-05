import os, smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "nguyenvannghia2914@gmail.com"
receiver_email = "nghianvfx10608@funix.edu.vn"

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(sender_email, "nghia12a1")
