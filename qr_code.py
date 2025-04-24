# import library
import qrcode
import qrcode.constants

qr_code = qrcode.QRCode(version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_H,
                        box_size=12,
                        border=2)

qr_code.add_data("repo")
qr_code.make(fit=True)
image = qr_code.make_image(fill_color='black',light="lightblue", back_color='white')
image.save("github_repo_qrcode.png")