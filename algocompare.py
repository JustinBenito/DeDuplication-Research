import os
import time
from PIL import Image
import imagehash

# Function to calculate execution time


def measure_execution_time(func, image):
    start_time = time.time()
    hash_value = func(image)
    end_time = time.time()
    execution_time = end_time - start_time
    return hash_value, execution_time


# Directory containing your images
image_directory = "./images_dataset"

# List to store the execution times for each algorithm
phash_times = []
whash_times = []
average_hash_times = []
dhash_times = []

# List to store the hash values for each image
phash_hashes = []
whash_hashes = []
average_hashes = []
dhash_hashes = []

# Counter for images with 'Copy' in their file name
copy_counter = 0

# Iterate over the images
for filename in os.listdir(image_directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(image_directory, filename)
        image = Image.open(image_path)

        # Measure execution time and calculate the hash for the current image using phash
        phash_hash, phash_time = measure_execution_time(imagehash.phash, image)
        phash_hashes.append(phash_hash)
        phash_times.append(phash_time)

        # Measure execution time and calculate the hash for the current image using whash
        whash_hash, whash_time = measure_execution_time(imagehash.whash, image)
        whash_hashes.append(whash_hash)
        whash_times.append(whash_time)

        # Measure execution time and calculate the hash for the current image using average_hash
        average_hash, average_hash_time = measure_execution_time(
            imagehash.average_hash, image)
        average_hashes.append(average_hash)
        average_hash_times.append(average_hash_time)

        # Measure execution time and calculate the hash for the current image using dhash
        dhash_hash, dhash_time = measure_execution_time(imagehash.dhash, image)
        dhash_hashes.append(dhash_hash)
        dhash_times.append(dhash_time)

        # Check if the file name contains 'Copy'
        if 'Copy' in filename:
            copy_counter += 1

# List to store duplicate hashes
duplicate_hashes = []

# Function to find duplicate hashes and add them to the list


def find_duplicate_hashes(hash_list):
    duplicates = []
    for i, hash_value in enumerate(hash_list):
        if hash_value in hash_list[i+1:]:
            if hash_value not in duplicates:
                duplicates.append(hash_value)
    return duplicates


# Find duplicate hashes for each hash type
phash_duplicates = find_duplicate_hashes(phash_hashes)
whash_duplicates = find_duplicate_hashes(whash_hashes)
average_duplicates = find_duplicate_hashes(average_hashes)
dhash_duplicates = find_duplicate_hashes(dhash_hashes)

# Calculate the accuracy for each hash type
phash_accuracy = len(phash_duplicates)
whash_accuracy = len(whash_duplicates)
average_accuracy = len(average_duplicates)
dhash_accuracy = len(dhash_duplicates)

# Calculate the average execution times for each algorithm
phash_avg_time = sum(phash_times) / len(phash_times)
whash_avg_time = sum(whash_times) / len(whash_times)
average_hash_avg_time = sum(average_hash_times) / len(average_hash_times)
dhash_avg_time = sum(dhash_times) / len(dhash_times)

# Print the average execution times for each algorithm
print("Average execution time for phash:", phash_avg_time)
print("Average execution time for whash:", whash_avg_time)
print("Average execution time for average_hash:", average_hash_avg_time)
print("Average execution time for dhash:", dhash_avg_time)

# Print the accuracy for each hash type
print("Accuracy for phash:", phash_accuracy)
print("Accuracy for whash:", whash_accuracy)
print("Accuracy for average_hash:", average_accuracy)
print("Accuracy for dhash:", dhash_accuracy)

# Print the number of images with 'Copy' in their file name
print("Number of images actually duplicated", copy_counter)
