# -*- coding: utf-8 -*-
"""PrakAlgo8

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hD9UbV4ZpYXisa4mgpd9v8c145TqS-nx
"""

def karakter_ganjil(input_list):
    result = []
    for i in range(len(input_list)):
        if i % 2 == 1:
            result.append(input_list[i])
    return result
input_user = input("Masukkan sebuah kata: ")
input_list = list(input_user)
output = karakter_ganjil(input_list)
print("Karakter pada indeks ganjil:", ''.join(output))

start_value = int(input("Masukkan angka pertama: "))
end_value = int(input("Masukkan angka kedua: "))
total = 0
current_value = start_value
while current_value <= end_value:
    total += current_value
    current_value += 1
print(f"Jumlah range adalah: {total}")