# import module
import qrcode
import image


qr = qrcode.QRCode(

    version = 15,  # 15 means the version of qr code, high the number bigger the code image and complicated picture
    box_size = 10,  # size of the box where qr code will display
    border = 5  # it is the white part of image
)

# making of qr code for my resume website
# data = "https://mayur-valsangkar-resume.netlify.app/"

data = input("Enter data to get its qr code")

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", back_color = "white")
img.save("qrcode.png")



