import sys
import threading

# Function to process the scanned barcode
def process_barcode(barcode):
    # Print the scanned barcode
    print(f"Scanned barcode: {barcode.strip()}")
    # Add your logic here, such as sending the barcode value to Google Keep

# Continuous loop to read keyboard input
try:
    barcode = ""
    while True:
        # Read input from the keyboard
        char = sys.stdin.read(1)
        
        # Append the character to the barcode string
        barcode += char
        
        # Check if the character is a newline (indicating the end of the barcode)
        if char == '\n':
            # Create a thread to process the scanned barcode
            t = threading.Thread(target=process_barcode, args=(barcode,))
            t.start()
            
            # Reset the barcode string for the next scan
            barcode = ""
        else:
            # Set a timeout after receiving the first character
            threading.Timer(0.2, lambda: process_barcode(barcode)).start()
except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit(0)
