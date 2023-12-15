import qrcode

def generar_codigo_qr(datos):
    if datos:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(datos)
        qr.make(fit=True)

        imagen_qr = qr.make_image(fill_color="black", back_color="white")

        imagen_qr.save("codigo_qr_temporal.png")
        print("Código QR generado y guardado como 'codigo_qr_temporal.png'")

datos = input("Ingresa los datos para el código QR: ")

generar_codigo_qr(datos)
