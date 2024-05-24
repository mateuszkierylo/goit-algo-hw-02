import queue

# Create a queue for requests
request_queue = queue.Queue()

# A global variable to keep track of request IDs
request_id = 0

# Function to generate new requests and add them to the queue
def generate_request():
    global request_id
    request_id += 1
    request = f"Request-{request_id}"
    request_queue.put(request)
    print(f"Generated: {request}")

# Function to process requests from the queue
def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Processing: {request}")
        print(f"Completed: {request}")
    else:
        print("The queue is empty")

# Main loop for the program
def main_loop():
    try:
        while True:
            generate_request()
            process_request()
    except KeyboardInterrupt:
        print("Program terminated by user.")

if __name__ == "__main__":
    main_loop()
    