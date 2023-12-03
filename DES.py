# Plaintext to try during the discussion "123456ABCD132536"

from Arrays import keyp, shift_table, key_comp
from Functions import hex2bin, permute, shift_left, bin2hex, encrypt

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap, QFont


class DESApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set up the background image
        background_image = QLabel(self)
        pixmap = QPixmap('cryptography.png') 
        background_image.setPixmap(pixmap)
        background_image.setGeometry(0, 0, pixmap.width(), pixmap.height())

        # Create widgets for user interaction
        font = QFont()
        font.setPointSize(16)

        plain_text_input = QLineEdit(self)
        plain_text_input.setPlaceholderText("Enter Plain Text")
        plain_text_input.setFont(font)

        encrypt_button = QPushButton("Encrypt", self)
        encrypt_button.setFont(font)
        encrypt_button.clicked.connect(self.encryptText)

        decrypt_button = QPushButton("Decrypt", self)
        decrypt_button.setFont(font)
        decrypt_button.clicked.connect(self.decryptText)

        cipher_text_label = QLabel(self)
        cipher_text_label.setFont(font)
        plain_text_output = QLabel(self)
        plain_text_output.setFont(font)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(plain_text_input, 2)
        layout.addWidget(encrypt_button, 1)
        layout.addWidget(decrypt_button, 1)
        layout.addWidget(cipher_text_label, 2)
        layout.addWidget(plain_text_output, 2)

        self.setLayout(layout)

        self.setGeometry(300, 300, pixmap.width(), pixmap.height())
        self.setWindowTitle('DES Encryption/Decryption App')
        self.show()

        # Store necessary elements as class attributes
        self.cipher_text_label = cipher_text_label
        self.plain_text_input = plain_text_input
        self.plain_text_output = plain_text_output

    def encryptText(self):
        pt = self.plain_text_input.text()
        key = "AABB09182736CCDD"

        key = hex2bin(key)
        key = permute(key, keyp, 56)
        left = key[0:28]
        right = key[28:56]

        rkb = []
        rk = []

        for i in range(0, 16):
            left = shift_left(left, shift_table[i])
            right = shift_left(right, shift_table[i])
            combine_str = left + right
            round_key = permute(combine_str, key_comp, 48)
            rkb.append(round_key)
            rk.append(bin2hex(round_key))

        cipher_text = bin2hex(encrypt(pt, rkb, rk))
        self.cipher_text_label.setText(f"Cipher Text: {cipher_text}")

    def decryptText(self):
        cipher_text = self.cipher_text_label.text().replace("Cipher Text: ", "")
        key = "AABB09182736CCDD"

        key = hex2bin(key)
        key = permute(key, keyp, 56)
        left = key[0:28]
        right = key[28:56]

        rkb = []
        rk = []

        for i in range(0, 16):
            left = shift_left(left, shift_table[i])
            right = shift_left(right, shift_table[i])
            combine_str = left + right
            round_key = permute(combine_str, key_comp, 48)
            rkb.append(round_key)
            rk.append(bin2hex(round_key))

        decrypted_text = bin2hex(encrypt(cipher_text, rkb[::-1], rk[::-1]))
        self.plain_text_output.setText(f"Decrypted Text: {decrypted_text}")


if __name__ == '__main__':
    app = QApplication([])
    des_app = DESApp()
    app.exec_()

