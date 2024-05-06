import sys
import select

# Function to process the scanned barcode
def process_barcode(barcode):
    # Print the scanned barcode
    print(f"Scanned barcode: {barcode.strip()}")
    # Add your logic here, such as sending the barcode value to Google Keep

# Continuous loop to read input
try:
    barcode = ""
    while True:
        # Check if there's data available to read from stdin
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            # Read input from stdin
            char = sys.stdin.read(1)
            
            # Append the character to the barcode string
            barcode += char
            
            # Check if the character is a newline (indicating the end of the barcode)
            if char == '\n':
                # Process the scanned barcode
                process_barcode(barcode)
                
                # Reset the barcode string for the next scan
                barcode = ""
except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit(0)
