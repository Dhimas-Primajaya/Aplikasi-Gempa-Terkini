"""
Aplikasi Gempa Terkini
MODULARISASI DENGAN FUNCTION
"""

#Cara pertama (kurang recommend)

# from gempaterkini import ekstraksi_data, tampilkan_data
#
# if __name__ == '__main__':
#     print("Aplikasi Utama:")
#     result = ekstraksi_data()
#     tampilkan_data(result)

#Cara Kedua (recommended)

import gempaterkini

if __name__ == "__main__":
    print("Aplikasi Gempa Terkini")
    result = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data(result)