# Fungsi untuk mengonversi teks menjadi representasi biner
def text_to_binary(text):
    binary_result = ''.join(format(ord(char), '08b') for char in text)
    return binary_result

# Fungsi untuk mengonversi representasi biner ke teks
def binary_to_text(binary_str):
    text = ''.join(chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8))
    return text

# Fungsi untuk melakukan enkripsi dengan XOR antara teks dan kunci
def encrypt(plaintext, key):
    if len(plaintext) != len(key):
        raise ValueError("Panjang plainteks dan kunci harus sama")

    # Mengonversi plainteks dan kunci ke representasi biner
    plaintext_binary = text_to_binary(plaintext)
    key_binary = text_to_binary(key)

    # Melakukan XOR antara setiap bit plainteks dan kunci
    encrypted_binary = ''.join(str(int(plain_bit) ^ int(key_bit)) for plain_bit, key_bit in zip(plaintext_binary, key_binary))
    
    # Mengonversi hasil enkripsi dari biner ke teks
    encrypted_text = binary_to_text(encrypted_binary)

    return encrypted_text

# Fungsi untuk melakukan dekripsi dengan XOR antara teks terenkripsi dan kunci
def decrypt(encrypted_text, key):
    if len(encrypted_text) != len(key):
        raise ValueError("Panjang teks terenkripsi dan kunci harus sama")

    # Mengonversi teks terenkripsi dan kunci ke representasi biner
    encrypted_binary = text_to_binary(encrypted_text)
    key_binary = text_to_binary(key)

    # Melakukan XOR antara setiap bit teks terenkripsi dan kunci
    decrypted_binary = ''.join(str(int(encrypted_bit) ^ int(key_bit)) for encrypted_bit, key_bit in zip(encrypted_binary, key_binary))
    
    # Mengonversi hasil dekripsi dari biner ke teks
    decrypted_text = binary_to_text(decrypted_binary)

    return decrypted_text

# Contoh penggunaan
plaintext = "RUSDI"
key = "CRUSH"
encrypted_text = encrypt(plaintext, key)
decrypted_text = decrypt(encrypted_text, key)

# Menampilkan hasil enkripsi dan dekripsi
print(f"Plainteks: {plaintext}")
print(f"Kunci: {key}")
print(f"Hasil Enkripsi: {encrypted_text}")
print(f"Hasil Dekripsi: {decrypted_text}")
