# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 20:31:10 2025

@author: nisan
"""

class Market:
    def __init__(self):
        self.filename = "product.txt"
        try:
            # Eğer dosya açılamazsa oluştur
            with open(self.filename, "r") as file:
                pass
        except FileNotFoundError:
            with open(self.filename, "w") as file:
                pass

    def __del__(self):
        print("Market sınıfı yıkıldı ve işlemler tamamlandı.")

    def list_products(self):
        """Tüm ürünleri listeler."""
        try:
            with open(self.filename, "r") as file:
                products = file.readlines()
        except FileNotFoundError:
            print("Dosya bulunamadı, lütfen yeniden deneyin.")
            return

        if not products:
            print("Ürün bulunmamaktadır.")
            return

        print("\n*** Ürün Listesi ***")
        for index, product in enumerate(products, start=1):
            name, category, price, stock = product.strip().split(",")
            print(f"{index}) Ad: {name}, Kategori: {category}, Fiyat: {price} TL, Stok: {stock}")

    def add_product(self):
        """Yeni bir ürün ekler."""
        name = input("Ürün Adı: ")
        category = input("Kategori: ")
        price = input("Fiyat: ")
        stock = input("Stok Miktarı: ")

        try:
            with open(self.filename, "a") as file:
                file.write(f"{name},{category},{price},{stock}\n")
            print("Ürün başarıyla eklendi.")
        except Exception as e:
            print(f"Ürün eklenirken bir hata oluştu: {e}")

    def delete_product(self):
        """Bir ürünü siler."""
        self.list_products()
        product_number = int(input("Silmek istediğiniz ürün numarasını girin: "))

        try:
            with open(self.filename, "r") as file:
                products = file.readlines()

            if 1 <= product_number <= len(products):
                deleted_product = products.pop(product_number - 1)
                with open(self.filename, "w") as file:
                    file.writelines(products)
                print(f"{deleted_product.strip()} silindi.")
            else:
                print("Geçersiz ürün numarası.")
        except FileNotFoundError:
            print("Dosya bulunamadı, işlem yapılamadı.")
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

# Menü fonksiyonu
def menu():
    market = Market()

    while True:
        print("\n*** MENÜ ***")
        print("1) Ürünleri Listele")
        print("2) Ürün Ekle")
        print("3) Ürün Sil")
        print("4) Çıkış")

        choice = input("Seçiminizi yapın (1-4): ")

        if choice == "1":
            market.list_products()
        elif choice == "2":
            market.add_product()
        elif choice == "3":
            market.delete_product()
        elif choice == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

# Program çalıştırma
if __name__ == "__main__":
    menu()
