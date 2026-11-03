import random
import string
import time

CHARSET = string.ascii_lowercase + string.ascii_uppercase + " ,.!?1234567890"

Used = set()

def read_address(full_address):
    address, page_length = full_address.split("(")
    page_length = int(page_length.rstrip(")"))
    address = int(address)

    random.seed(address)
    page = "".join(random.choice(CHARSET) for _ in range(page_length))

    print("\n--- Page Content ---")
    print(page)
    print("--------------------")

def search_library(query, page_length):
    attempts = 0
    start_time = time.time()
    
    print(f"Searching for '{query}' in pages of {page_length} characters...")
    print("This might take a while (or forever). Press Ctrl+C to give up.")
    
    try:
        while True:
            attempts += 1
            
            # Generate a random "address" (book/page)
            address = random.randint(1, 1000000000)
            while True:
                if address in Used:
                   address = random.randint(1, 1000000000)
                else:
                    Used.add(address)
                    break
            random.seed(address)
            
            # Generate the page content
            page = "".join(random.choice(CHARSET) for _ in range(page_length))
            

            
            # Search the page
            if query in page:
                elapsed = time.time() - start_time
                print(f"\nFOUND IT!")
                print(f"Address: {address}({page_length})")
                print(f"Attempts: {attempts:,}")
                print(f"Time: {elapsed:.2f} seconds")
                print("--- Page Content ---")
                print(page)
                print("--------------------")
                return
                
            # Optional: Print progress every 10,000 attempts
            if attempts % 10000 == 0:
                print(f"Searched {attempts:,} pages...", end="\r")
            if attempts >= 1000000000:
                raise ValueError("Unable to find in 1,000,000,000 tries! Please narrow your search!")
                
    except KeyboardInterrupt:
        print(f"\nSearch aborted after {attempts:,} attempts.")

        

def main():
    while True:
        try:
            length = int(input("Enter max character limit for the page: "))
            if length <= 0:
                print("Length must be greater than 0.")
                continue
                
            # FIX: Added missing closing parentheses
            go = int(input("What operation? Search for keyword(1) or Address search(2): "))
            
            if go == 1 or go == 2:
                break # Valid inputs break the setup loop
            else:
                print("Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            
    # Route operations cleanly based on choice
    if go == 2:
        # FIX: Added missing closing parenthesis
        full_address = input("What FULL address? ")
        read_address(full_address)
        return # End execution after reading the address

    # Only run this if go == 1
    query = input("Enter text to search for: ")
    
    if len(query) > length:
        print("Error: Query is longer than the page length!")
        return
        
    try:
        search_library(query, length)
    except ValueError as e:
        print(f"\n{e}")

if __name__ == "__main__":
    main()
