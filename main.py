"""
Aplikasi Gempa Terkini
MODULARISASI DENGAN FUNCTION
"""

import gempaterupdate

if __name__ == "__main__":
    print("Aplikasi Gempa Terkini")
    result = gempaterupdate.ekstraksi_data()
    gempaterupdate.tampilkan_data(result)