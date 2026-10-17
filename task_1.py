from queue import Queue

queue = Queue()

def generate_request(task):
    request = f"Request - {task}"
    print(f"Generated: {request}")
    queue.put(request)

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Processing: {request}")
    else:
        print("No requests to process.")

def main():
    generate_request("Task 1")
    generate_request("Task 2")
    process_request()
    process_request()
    process_request()

if __name__ == "__main__":
    main()