import qrcode

def main():
    song = "https://www.youtube.com/watch?v=9GOd64-1nlg&list=RDUqdK3pLrwUg&index=3"
    qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
    qr.add_data('Some.data')

    qr.add_data(song)
    qr.make(fit=True)


    img = qr.make_image(fill_color="red", back_color="white")
    img.save("my-qrcode.png")



if __name__=="__main__":
    main()
