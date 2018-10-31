from PIL import Image
import os


class PixDB:

    def __init__(self, *, filename="db"):
        self.filename = filename
        self.filepath = filename + ".png"

    def _to_binary_array(self, text: str):
        return [format(ord(x), "b") for x in text]

    def write(self, text: str, *, bit_length=8):
        binary = self._to_binary_array(text)
        img_size = bit_length, len(binary)
        img = Image.new("L", img_size)
        for n, bit in enumerate(binary):
            bit_data = enumerate(bit)
            for i, b in bit_data:
                img.putpixel((i, n), 255 if b == "1" else 0)
            if len(bit) < bit_length:
                img.putpixel((len(bit), n), 125)
        img.save(self.filepath)

    def read(self):
        if not os.path.isfile(self.filepath):
            raise FileNotFoundError("Not a valid file.")
        img = Image.open(self.filepath)
        x, y = img.size
        decoded = b""
        for h in range(y):
            byte = ""
            for w in range(x):
                pixel = img.getpixel((w, h))
                if pixel == 255:
                    byte += "1"
                elif pixel == 0:
                    byte += "0"
                elif pixel == 125:
                    break
            n = int(byte, 2)
            decoded += n.to_bytes((n.bit_length() + 7) // 8, "big")
        return decoded
