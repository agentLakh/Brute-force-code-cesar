import tkinter as tk
from tkinter import scrolledtext

def caesar_encrypt(plaintext, shift):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                shift_value = ord('A')
            else:
                shift_value = ord('a')
            ciphertext += chr((ord(char) - shift_value + shift) % 26 + shift_value)
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                shift_value = ord('A')
            else:
                shift_value = ord('a')
            plaintext += chr((ord(char) - shift_value - shift) % 26 + shift_value)
        else:
            plaintext += char
    return plaintext

def brute_force_caesar(ciphertext):
    decrypted_texts = []
    for shift in range(1, 26):
        plaintext = caesar_decrypt(ciphertext, shift)
        decrypted_texts.append((shift, plaintext))
    return decrypted_texts

def on_encrypt():
    plaintext = input_text.get("1.0", tk.END).strip()
    shift = int(shift_entry.get())
    ciphertext = caesar_encrypt(plaintext, shift)
    result_window.delete('1.0', tk.END)
    result_window.insert(tk.END, f"Texte chiffré avec un décalage de {shift} :\n\n{ciphertext}")

def on_decrypt():
    ciphertext = input_text.get("1.0", tk.END).strip()
    decrypted_texts = brute_force_caesar(ciphertext)
    result_window.delete('1.0', tk.END)
    for shift, plaintext in decrypted_texts:
        result_window.insert(tk.END, f"Décalage de {shift} : {plaintext}\n\n")

# Création de la fenêtre principale
window = tk.Tk()
window.title("Chiffrement et déchiffrement César")

# Zone de texte pour l'entrée du texte
input_text = scrolledtext.ScrolledText(window, width=40, height=10, wrap=tk.WORD)
input_text.grid(row=0, column=0, padx=10, pady=10)

# Entrée pour spécifier le décalage
shift_label = tk.Label(window, text="Décalage:")
shift_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

shift_entry = tk.Entry(window, width=10)
shift_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

# Bouton pour chiffrer le texte
encrypt_button = tk.Button(window, text="Chiffrer", command=on_encrypt)
encrypt_button.grid(row=2, column=0, padx=10, pady=5)

# Bouton pour déchiffrer par force brute
decrypt_button = tk.Button(window, text="Décrypter par force brute", command=on_decrypt)
decrypt_button.grid(row=2, column=1, padx=10, pady=5)

# Zone de texte pour afficher les résultats
result_window = scrolledtext.ScrolledText(window, width=60, height=20, wrap=tk.WORD)
result_window.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Lancement de la boucle principale
window.mainloop()
