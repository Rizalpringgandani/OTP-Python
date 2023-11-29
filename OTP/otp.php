<?php
// Fungsi untuk melakukan enkripsi XOR pada teks dengan kunci
function encrypt($plaintext, $key) {
    $encryptedText = '';
    $keyLength = strlen($key);

    // Loop melalui setiap karakter dalam plaintext
    for ($i = 0; $i < strlen($plaintext); $i++) {
        $char = $plaintext[$i];
        $keyChar = $key[$i % $keyLength]; // Mendapatkan karakter kunci yang sesuai dengan indeks saat ini
        $encryptedChar = chr(ord($char) ^ ord($keyChar)); // Melakukan operasi XOR pada representasi ASCII karakter
        $encryptedText .= $encryptedChar; // Menambahkan karakter terenkripsi ke hasil akhir
    }

    return $encryptedText;
}

// Fungsi untuk melakukan dekripsi XOR pada teks terenkripsi dengan kunci
function decrypt($encryptedText, $key) {
    $decryptedText = '';
    $keyLength = strlen($key);

    // Loop melalui setiap karakter dalam teks terenkripsi
    for ($i = 0; $i < strlen($encryptedText); $i++) {
        $char = $encryptedText[$i];
        $keyChar = $key[$i % $keyLength]; // Mendapatkan karakter kunci yang sesuai dengan indeks saat ini
        $decryptedChar = chr(ord($char) ^ ord($keyChar)); // Melakukan operasi XOR pada representasi ASCII karakter
        $decryptedText .= $decryptedChar; // Menambahkan karakter terdekripsi ke hasil akhir
    }

    return $decryptedText;
}

// Contoh penggunaan
$plaintext = "RUSDI";
$key = "CRUSH";
$encryptedText = encrypt($plaintext, $key);

// Menampilkan hasil enkripsi
echo "Plainteks: $plaintext\n";
echo "Kunci: $key\n";
echo "Hasil Enkripsi: $encryptedText\n";

// Melakukan dekripsi pada teks terenkripsi
$decryptedText = decrypt($encryptedText, $key);
echo "Teks Terenkripsi: $encryptedText\n";
echo "Kunci: $key\n";
echo "Hasil Dekripsi: $decryptedText\n";
?>
