from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QSpinBox, QPushButton, QTextEdit
import sys

class KasirApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tugas 3")
        self.setGeometry(100, 100, 400, 450)
        
        # Data produk dan harga
        self.produk_harga = {
            "Bimoli (Rp. 20,000)": 20000,
            "Gula Pasir (Rp. 15,000)": 15000,
            "Beras (Rp. 50,000)": 50000
        }
        
        # Label Nama
        self.label_nama = QLabel("Nama: Muhammad Ridho Fahru Rozy", self)
        self.label_nama.setGeometry(10, 10, 380, 20)
        
        # Label NIM
        self.label_nim = QLabel("NIM: F1D022076", self)
        self.label_nim.setGeometry(10, 30, 200, 20)
        
        # Label Pilih Produk
        self.label_produk = QLabel("Product:", self)
        self.label_produk.setGeometry(10, 60, 100, 20)
        
        # ComboBox Produk
        self.combo_produk = QComboBox(self)
        self.combo_produk.setGeometry(120, 60, 200, 20)
        for produk in self.produk_harga.keys():
            self.combo_produk.addItem(produk)
        
        # Label Jumlah
        self.label_jumlah = QLabel("Quantity:", self)
        self.label_jumlah.setGeometry(10, 90, 100, 20)
        
        # SpinBox Jumlah
        self.spin_jumlah = QSpinBox(self)
        self.spin_jumlah.setGeometry(120, 90, 50, 20)
        self.spin_jumlah.setMinimum(1)
        
        # Label Diskon
        self.label_diskon = QLabel("Discount:", self)
        self.label_diskon.setGeometry(10, 120, 100, 20)
        
        # ComboBox Diskon
        self.combo_diskon = QComboBox(self)
        self.combo_diskon.setGeometry(120, 120, 80, 20)
        self.combo_diskon.addItems(["0%", "10%", "15%", "20%"])
        
        # Tombol Tambah
        self.btn_tambah = QPushButton("Tambah", self)
        self.btn_tambah.setGeometry(10, 160, 100, 30)
        
        # Tombol Reset
        self.btn_reset = QPushButton("Hapus", self)
        self.btn_reset.setGeometry(120, 160, 100, 30)
        
        # Event handlers
        self.btn_tambah.clicked.connect(self.tambah_ke_keranjang)
        self.btn_reset.clicked.connect(self.reset_keranjang)
        
        # Label Keranjang Belanja
        self.label_keranjang = QLabel("", self)
        self.label_keranjang.setGeometry(10, 200, 200, 20)
        
        # Text Area Keranjang
        self.text_keranjang = QTextEdit(self)
        self.text_keranjang.setReadOnly(True)
        self.text_keranjang.setGeometry(10, 220, 380, 150)
        
        # Label Total
        self.label_total = QLabel("Total: Rp. 0", self)
        self.label_total.setGeometry(10, 380, 200, 20)
        
        # Variabel total harga
        self.total_harga = 0
    
    def tambah_ke_keranjang(self):
        produk = self.combo_produk.currentText()
        jumlah = self.spin_jumlah.value()
        diskon_persen = int(self.combo_diskon.currentText().replace('%', ''))
        harga_satuan = self.produk_harga.get(produk, 0)
        harga_total = harga_satuan * jumlah
        diskon = harga_total * (diskon_persen / 100)
        harga_setelah_diskon = harga_total - diskon
        
        self.total_harga += harga_setelah_diskon
        self.text_keranjang.append(f"{produk} - {jumlah}x Rp. {harga_satuan:,} (disc {diskon_persen}%)")
        self.label_total.setText(f"Total: Rp. {self.total_harga:,.0f}")
    
    def reset_keranjang(self):
        self.text_keranjang.clear()
        self.total_harga = 0
        self.label_total.setText("Total: Rp. 0")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KasirApp()
    window.show()
    sys.exit(app.exec_())
