

from PIL import Image, ImageDraw, ImageFont
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os




def create(certificate_path,text,output_filename):
    certificate = Image.open(certificate_path)
    draw = ImageDraw.Draw(certificate)
    text_color = (0, 0, 0)  # RGB value for black
    font_size = 40
    W, H = 2339,1655
    font = ImageFont.truetype('arial.ttf', font_size)
    w,h=font.getsize(text)
    draw.text(((W-w)/2,(H-h)/2), text, font=font, fill=text_color)
    certificate.save(output_filename)   
    




def send_image_email( receiver_email, image_path):
    # Create a multipart message container
    sender_email = 'envision.sitmng@gmail.com'
    sender_password = 'gspzbhhdmhppizjo'
    subject = 'Here is your certificate'
    
    
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the image to the email
    with open(image_path, 'rb') as f:
        image_data = f.read()

    image = MIMEImage(image_data, name='image.jpg')
    msg.attach(image)

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
        os.remove(image_path)
    except Exception as e:
        print("Failed to send email.")
        print(e)
        

# Usage example




if __name__ == '__main__':
    create('C:/Users/AIML/Desktop/Conference/supporting/cert_template.jpg',"Adarsh",'modified_certificate.png')
    sender_email = 'envision.sitmng@gmail.com'
    sender_password = 'gspzbhhdmhppizjo'
    receiver_email = 'adarshsavaligi@gmail.com'
    subject = 'Here is your certificate'
    image_path = 'C:/Users/AIML/Desktop/Conference/modified_certificate.png'
    send_image_email( receiver_email,  image_path)