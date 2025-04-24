# import library
import qrcode
import qrcode.constants
# Set variable of QR code
qr_code = qrcode.QRCode(version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_H,
                        box_size=12,
                        border=2)

# Add path to which link
qr_code.add_data("https://github.com/Ubaid883/QR_code_Generator")
qr_code.make(fit=True)

# Change background color and other aspect
image = qr_code.make_image(fill_color='black', back_color='white')

# save QR Code into image
image.save("github_repo_qrcode.png")