import tkinter as tk

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if mode == "Encrypt":
                if char.islower():
                    result += chr((ord(char) - 97 + shift_amount) % 26 + 97)
                else:
                    result += chr((ord(char) - 65 + shift_amount) % 26 + 65)
            elif mode == "Decrypt":
                if char.islower():
                    result += chr((ord(char) - 97 - shift_amount) % 26 + 97)
                else:
                    result += chr((ord(char) - 65 - shift_amount) % 26 + 65)
        else:
            result += char
    return result

def handle_cipher():
    text = text_entry.get("1.0", "end-1c")
    shift = int(shift_entry.get())
    mode = mode_var.get()
    result = caesar_cipher(text, shift, mode)
    result_text.delete("1.0", "end")
    result_text.insert("1.0", result)


root = tk.Tk()
root.title("Caesar Cipher")


text_label = tk.Label(root, text="Enter Text:")
text_entry = tk.Text(root, height=5, width=50)
shift_label = tk.Label(root, text="Enter Shift Value:")
shift_entry = tk.Entry(root)
mode_label = tk.Label(root, text="Choose Mode:")
mode_var = tk.StringVar()
mode_var.set("Encrypt")
encrypt_radio = tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="Encrypt")
decrypt_radio = tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="Decrypt")
cipher_button = tk.Button(root, text="Cipher", command=handle_cipher)
result_label = tk.Label(root, text="Result:")
result_text = tk.Text(root, height=5, width=50)

text_label.grid(row=0, column=0, sticky="w")
text_entry.grid(row=0, column=1, columnspan=2)
shift_label.grid(row=1, column=0, sticky="w")
shift_entry.grid(row=1, column=1, sticky="w")
mode_label.grid(row=2, column=0, sticky="w")
encrypt_radio.grid(row=2, column=1, sticky="w")
decrypt_radio.grid(row=2, column=2, sticky="w")
cipher_button.grid(row=3, column=0, columnspan=3)
result_label.grid(row=4, column=0, sticky="w")
result_text.grid(row=4, column=1, columnspan=2)


root.mainloop()
