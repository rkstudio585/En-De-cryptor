from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
from cryptography.fernet import Fernet
import pyfiglet

# Function to generate a key
def generate_key():
    return Fernet.generate_key()

# Function to encrypt a message
def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    return encrypted

# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_message).decode()
    return decrypted

# Setup rich console
console = Console()

# Display ASCII banner
banner = pyfiglet.figlet_format("En-De-cryptor")
console.print(Text.from_markup(banner, style="bold green"))

# Main menu
def main():
    console.print("–––––––––––––––––––––––––––––––––––––––––––", style="bold green")
    console.print(" Welcome to the Encryptor/Decryptor Tool!", style="bold cyan")
    console.print(" Author:                                                  RK!", style="bold green")
    console.print(" Product Of:                                 RK Studio!", style="bold green")
    console.print(" GitHub: https://github.com/rkstudio585", style="bold green")
    console.print(" Website:        https://rkstudio.com", style="bold green")
    console.print("–––––––––––––––––––––––––––––––––––––––––––", style="bold green")
    
    
    
    while True:
        console.print("\nChoose an option:")
        console.print("[1] Generate Key")
        console.print("[2] Encrypt Message")
        console.print("[3] Decrypt Message")
        console.print("[4] Exit")
        choice = Prompt.ask("Select an option", choices=["1", "2", "3", "4"])

        if choice == "1":
            key = generate_key()
            console.print(f"Generated Key: {key.decode()}", style="bold yellow")

        elif choice == "2":
            key = Prompt.ask("Enter your key (string)")
            message = Prompt.ask("Enter the message to encrypt")
            try:
                encrypted = encrypt_message(message, key.encode())
                console.print(f"Encrypted Message: {encrypted.decode()}", style="bold green")
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")

        elif choice == "3":
            key = Prompt.ask("Enter your key (string)")
            encrypted_message = Prompt.ask("Enter the message to decrypt")
            try:
                decrypted = decrypt_message(encrypted_message.encode(), key.encode())
                console.print(f"Decrypted Message: {decrypted}", style="bold green")
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")

        elif choice == "4":
            console.print("Exiting the tool. Goodbye!", style="bold cyan")
            console.print("A Product Of: RK Studio \nCode By: MD Riad Khan!", style="bold green")
            
            break

if __name__ == "__main__":
    main()
    
