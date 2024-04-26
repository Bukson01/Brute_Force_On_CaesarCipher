import threading
import tkinter as tk
from tkinter import messagebox

class CaesarCipherHacker:
    def __init__(self):
        self.SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def brute_force_attack(self, message):
        """Perform a brute force attack to decrypt the message."""
        decrypted_messages = []
        for key in range(len(self.SYMBOLS)):
            decrypted_message = ''.join([self.SYMBOLS[(self.SYMBOLS.find(symbol) - key) % len(self.SYMBOLS)] if symbol in self.SYMBOLS else symbol for symbol in message])
            decrypted_messages.append((key, decrypted_message))
        return decrypted_messages

    def multi_threaded_brute_force_attack(self, message):
        """Perform a multi-threaded brute force attack to decrypt the message."""
        decrypted_messages = []
        threads = []
        for key in range(len(self.SYMBOLS)):
            thread = threading.Thread(target=self.decrypt_message, args=(key, message, decrypted_messages))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return decrypted_messages

    def decrypt_message(self, key, message, decrypted_messages):
        """Decrypt the message using a specific key."""
        decrypted_message = ''.join([self.SYMBOLS[(self.SYMBOLS.find(symbol) - key) % len(self.SYMBOLS)] if symbol in self.SYMBOLS else symbol for symbol in message])
        decrypted_messages.append((key, decrypted_message))

    def frequency_analysis(self, message):
        """Analyze the frequency of symbols in the message for optimized key search."""
        # Implement frequency analysis here
        pass

    def handle_error(self, error_message):
        """Handle errors by displaying an error message."""
        messagebox.showerror('Error', error_message)

    def run_gui(self):
        """Run the graphical user interface (GUI) for the Caesar Cipher Hacker."""
        self.root = tk.Tk()
        self.root.title('Caesar Cipher Hacker')

        tk.Label(self.root, text='Enter the encrypted message:').pack()
        self.message_entry = tk.Entry(self.root)
        self.message_entry.pack()

        tk.Button(self.root, text='Decrypt', command=self.decrypt).pack()

        self.decrypted_text_label = tk.Label(self.root, text='')
        self.decrypted_text_label.pack()

        self.root.mainloop()

    def decrypt(self):
        """Decrypt the message entered by the user."""
        message = self.message_entry.get()
        if not message:
            self.handle_error('Please enter an encrypted message.')
            return

        decrypted_messages = self.multi_threaded_brute_force_attack(message)
        self.display_decrypted_message(decrypted_messages)

    def display_decrypted_message(self, decrypted_messages):
        """Display the decrypted messages in the GUI."""
        self.decrypted_text_label.config(text='Decrypted Messages:\n')
        for key, decrypted_message in decrypted_messages:
            self.decrypted_text_label.config(text=self.decrypted_text_label['text'] + f'Key #{key}: {decrypted_message}\n')

if __name__ == '__main__':
    caesar_cipher_hacker = CaesarCipherHacker()
    caesar_cipher_hacker.run_gui()
