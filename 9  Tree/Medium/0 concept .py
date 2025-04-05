from queue import Queue

# Create a queue
q = Queue()

# Enqueue elements
q.put("Customer 1")
q.put("Customer 2")
q.put("Customer 3")

# Display the queue size
print("Initial queue size:", q.qsize())

# Dequeue elements
print("\nServing:", q.get())
print("Queue size after serving one customer:", q.qsize())

print("\nServing:", q.get())
print("Queue size after serving another customer:", q.qsize())

# Add a new customer
q.put("Customer 4")
print("\nNew customer joins. Current queue size:", q.qsize())

# Serve the remaining customers
while not q.empty():
    print("Serving:", q.get())

# Final queue size
print("Queue size after all customers are served:", q.qsize())