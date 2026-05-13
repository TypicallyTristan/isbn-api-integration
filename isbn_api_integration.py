## Imports
import logging
import requests




## Initialize logging
logging.basicConfig(
    filename='intergration_errors.log',
    level=logging.ERROR,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True
)



## Function to get book title from ISBN
def getIsbnTitle(isbn):
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&jscmd=details&format=json"
    response = requests.get(url)
    searchKey = f"ISBN:{isbn}"

    ## Check if connection was made succesfully
    try:
        if response.status_code == 200:
            # Check if data is empty and log if it is
            if not response.json():
                print(f"Error: No record found for ISBN '{isbn}'")
                logging.error(f"{searchKey}: Failed to Lookup - Empty Payload Recieved")
                return

        
            # If data as value access information
            isbn_record = response.json().get(searchKey, {})
            details = isbn_record.get('details', {})
            title = details.get('title', 'Title not found')
            print("Connection: Success")
            print(f"Book Found: {title}")

        else:
            print(f"Connection Failed. Status:", response.status_code)
    except requests.exceptions.RequestException as e:
        print(f"Connection Error: {str(e)}")
        logging.error(f"{searchKey}: Connection Error: {str(e)}")

def main():
    isbnInput = input("Please enter ISBN: ").strip()
    getIsbnTitle(isbnInput)

main()