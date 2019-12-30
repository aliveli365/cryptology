import base64


def encode(en):
    message_bytes = girdi.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print(base64_message)

def decode(de):
    message_bytes = girdi.encode('ascii')
    base64_message = message_bytes.decode('ascii')
    print(base64_message)



while True:
    girdi = input("ENCODE(e) OR DECODE(d):")

    if girdi == "e" :
        en = input("Data to base64:")
        encode(en)

    elif girdi == "d" :
        de = input("base64 to hash:")
        decode(de)

    else:
        print("yanlış girdi..")
