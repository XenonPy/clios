import os
import random
import string
import concurrent.futures

def generate_random_string(size):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def generate_file(file_path, file_size_mb):
    file_content = generate_random_string(file_size_mb * 1024 * 1024)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(file_content)

def generate_sample_data(directory, num_dirs=10, files_per_dir=50, file_size_mb=20, max_workers=4):
    if not os.path.exists(directory):
        os.makedirs(directory)

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for dir_num in range(num_dirs):
            subdirectory = os.path.join(directory, f"subdir_{dir_num}")
            os.makedirs(subdirectory, exist_ok=True)

            for file_num in range(files_per_dir):
                file_name = f"file_{file_num}.txt"
                file_path = os.path.join(subdirectory, file_name)
                futures.append(executor.submit(generate_file, file_path, file_size_mb))
        
        concurrent.futures.wait(futures)

    print("\nSample data generation complete!\n")
