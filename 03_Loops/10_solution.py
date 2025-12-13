import time

wait_time = 1
max_retries = 5
attempt = 0

while attempt < max_retries:
    print(f"Attempt {attempt + 1} of {max_retries}")
    time.sleep(wait_time)
    wait_time *= 2
    attempt += 1
    
