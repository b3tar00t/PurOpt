import requests
import threading
from queue import Queue
from colorama import Fore, init
import pyfiglet
import time

# Initialize colorama for Windows compatibility
init(autoreset=True)

# Function to display the title using the custom ASCII art
def display_title():
    ascii_art = """
██████╗ ██╗   ██╗██████╗  ██████╗ ██████╗ ████████╗
██╔══██╗██║   ██║██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
██████╔╝██║   ██║██████╔╝██║   ██║██████╔╝   ██║   
██╔═══╝ ██║   ██║██╔══██╗██║   ██║██╔═══╝    ██║   
██║     ╚██████╔╝██║  ██║╚██████╔╝██║        ██║   
╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝        ╚═╝   
    """
    print(Fore.CYAN + ascii_art)
    print(Fore.GREEN + "PurOpt - A powerful HTTP method checker and purger tool.")
    print(Fore.YELLOW + "Creator: b3tar00t")

def read_urls_from_file(file_path):
    """Reads a list of URLs from the specified file."""
    try:
        with open(file_path, 'r') as file:
            urls = [line.strip() for line in file.readlines() if line.strip()]
        return urls
    except FileNotFoundError:
        print(Fore.RED + f"Error: The file '{file_path}' was not found.")
        return []
    except Exception as e:
        print(Fore.RED + f"An error occurred while reading the file: {e}")
        return []

def send_options_request(url, timeout):
    """Sends an OPTIONS request to the specified URL and returns the allowed methods and cache status."""
    try:
        # Sending OPTIONS request
        response = requests.options(url, timeout=timeout)
        
        # Check for successful response
        if response.status_code == 200:
            # Get allowed methods from response headers
            allowed_methods = response.headers.get('allow', '')
            
            # If no allowed methods are found, default to GET and POST
            if not allowed_methods:
                allowed_methods = 'GET, POST'
            
            # Check x-cache and x-cache-hits headers for cache information
            x_cache = response.headers.get('x-cache', 'MISS')
            x_cache_hits = int(response.headers.get('x-cache-hits', 0))

            # Return allowed methods and whether cache hit count is greater than 1 with HIT status
            if x_cache == 'HIT' and x_cache_hits > 1:
                return allowed_methods, True  # Cache hit and valid for Purge logic
            else:
                return allowed_methods, False  # Not valid for Purge logic
        
        # Handle the case where response status is not 200
        else:
            error_message = f"Error: Received status code {response.status_code} for {url}"
            # Return formatted error message and False for cache status
            return f"{Fore.RED}{error_message}{Fore.RESET}"
    
    except requests.Timeout:
        # Return timeout error with yellow color
        return f"{Fore.YELLOW}Error: Request to {url} timed out (took longer than {timeout} seconds).{Fore.RESET}"
    
    except requests.RequestException as e:
        # Handle general request exception with red color
        return f"{Fore.RED}Error: Failed to send OPTIONS request to {url}. Reason: {e}{Fore.RESET}"





def send_purge_request(url, timeout):
    """Sends a PURGE request to the specified URL and returns the result."""
    try:
        response = requests.request("PURGE", url, timeout=timeout)
        if response.status_code == 405:
            return f"{Fore.RED}PURGE Method: Not Allowed (405 Method Not Allowed)"
        elif response.status_code == 200:
            return f"{Fore.GREEN}PURGE Method: Allowed (Cache Purged)"
        else:
            return f"{Fore.RED}Error: Received status code {response.status_code} for PURGE at {url}"
    except requests.Timeout:
        return f"{Fore.YELLOW}Error: Request to {url} timed out for PURGE (took longer than {timeout} seconds)."
    except requests.RequestException as e:
        return f"{Fore.RED}Error: Failed to send PURGE request to {url}. Reason: {e}"

def worker(queue, timeout, test_purge, results):
    """Worker thread to process URLs."""
    while not queue.empty():
        url = queue.get()
        result_str = f"\n{Fore.CYAN}Processing: {url}\n"
        
        # Send OPTIONS request and collect the result
        options_result = send_options_request(url, timeout)
        result_str += f"OPTIONS Result: {Fore.GREEN}{options_result}{Fore.RESET}\n"

        # Always attempt to send the PURGE request, regardless of the OPTIONS result
        if test_purge:
            purge_result = send_purge_request(url, timeout)
            result_str += f"{Fore.CYAN}PURGE Result: {purge_result}{Fore.RESET}\n"
        
        # Add the result for this URL to the shared results list
        results.append(result_str)
        
        queue.task_done()


def display_results(results):
    """Displays the results in an elegant and attractive manner."""
    print("\n" + "="*60)
    print(Fore.GREEN + "Final Results for URLs")
    print("="*60)
    for result in results:
        print(result)
        print("-" * 60)

def main():
    # Display tool title and information
    display_title()

    print(Fore.CYAN + "="*60)
    print(Fore.CYAN + "Welcome to the HTTP OPTIONS & PURGE Header Checker Tool!")
    print(Fore.CYAN + "This tool will send an OPTIONS request to each URL and display the allowed HTTP methods.")
    print(Fore.CYAN + "Additionally, it will check for the PURGE method if requested.\n")
    print(Fore.CYAN + "="*60)

    # Ask user for URL input or file path using numeric options
    print(Fore.MAGENTA + "Please choose an option:")
    print("1. Enter a single URL")
    print("2. Provide a file containing URLs")
    url_choice = input("Enter 1 or 2: ").strip()

    if url_choice == "1":
        url = input(Fore.MAGENTA + "Please enter the URL: ").strip()
        urls = [url]
    elif url_choice == "2":
        file_path = input(Fore.MAGENTA + "Please enter the path to the file containing URLs: ").strip()
        urls = read_urls_from_file(file_path)
    else:
        print(Fore.RED + "Invalid choice. Exiting.")
        return
    
    if not urls:
        print(Fore.RED + "No URLs to process. Exiting.")
        return

    # Get timeout and threads, with default values if not provided
    timeout = input(Fore.MAGENTA + "Enter custom timeout in seconds (default is 10): ").strip()
    timeout = int(timeout) if timeout else 10
    num_threads = input(Fore.MAGENTA + "Enter the number of threads (default is 5): ").strip()
    num_threads = int(num_threads) if num_threads else 5
    test_purge = input(Fore.MAGENTA + "Do you want to test for the PURGE method? (y/n): ").strip().lower() == "y"
    
    print(f"\n{Fore.CYAN}Sending OPTIONS requests to {len(urls)} URLs... Please wait.\n")
    
    # Queue for threads
    queue = Queue()
    for url in urls:
        queue.put(url)
    
    # List to store results
    results = []

    # Create worker threads
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=worker, args=(queue, timeout, test_purge, results))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Display the results for all URLs
    display_results(results)

    print(Fore.GREEN + "\nTool execution completed!")

if __name__ == "__main__":
    main()
