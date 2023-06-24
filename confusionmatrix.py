import os
from PIL import Image
import imagehash


image_directory = "./images_dataset"

phash_times = []
whash_times = []
average_hash_times = []
dhash_times = []

# List to store the hash values for each image
phash_hashes = []
whash_hashes = []
average_hashes = []
dhash_hashes = []

#algo duplicates
phash_duplicates= []


image_hash_map = {}
duplicate_copy_counter = 0

# Iterate over the images
# def p_hashes():
#     for filename in os.listdir(image_directory):
#         if filename.endswith(".jpg") or filename.endswith(".png"):
#             image_path = os.path.join(image_directory, filename)
#             image = Image.open(image_path)

#             # Calculate the hash value for the current image
#             hash_value = str(imagehash.phash(image))

#             # Store the image name and hash value in the dictionary
#             image_hash_map[filename] = hash_value
    
#     for image_name, hash_value in image_hash_map.items():
#         if list(image_hash_map.values()).count(hash_value) > 1:
#             if 'Copy' in image_name:
#                 duplicate_copy_counter += 1



def confusionmatrix(hashfunc):
    true_positive=0
    true_negative=0
    false_positive=0
    false_negative=0
    for filename in os.listdir(image_directory):
         if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(image_directory, filename)
            image = Image.open(image_path)
            hash_value = str(hashfunc(image))
            image_hash_map[filename] = hash_value

    for image_name, hash_value in image_hash_map.items():
        if list(image_hash_map.values()).count(hash_value) > 1:
            if 'Copy' in image_name:
                true_negative += 1
        if list(image_hash_map.values()).count(hash_value) == 1:
            if 'Copy' in image_name:
                false_negative += 1
        if list(image_hash_map.values()).count(hash_value) > 1:
            if 'Copy' not in image_name:
                false_positive += 1
        if list(image_hash_map.values()).count(hash_value) == 1:
            if 'Copy' not in image_name:
                true_positive += 1

    print('For', str(hashfunc)[9:16])
    print('true_positive', true_positive)
    print('true_negative', true_negative)
    print('false_positive', false_positive)
    print('false_negative', false_negative)
    error=(false_positive+false_negative)/(true_positive+true_negative+false_positive+false_negative)
    accuracy=(true_positive+true_negative)/(true_positive+true_negative+false_positive+false_negative)
    print('error', error*100,"%")
    print('accuracy', accuracy*100,"%")


confusionmatrix(imagehash.phash)
confusionmatrix(imagehash.whash)
confusionmatrix(imagehash.average_hash)
confusionmatrix(imagehash.dhash)
# print(image_hash_map)

                   









# def measure_execution_time(func, image):
#     start_time = time.time()
#     hash_value = func(image)
#     end_time = time.time()
#     execution_time = end_time - start_time
#     return hash_value, execution_time

# def confusionmatrix_phash(img):
#     phash_hash, phash_time = measure_execution_time(imagehash.phash, img)
#     phash_hashes.append(phash_hash)
#     phash_times.append(phash_time)
    




# Function to find duplicate hashes and add them to the list


# def find_duplicate_hashes(hash_list):
#     duplicates = []
#     for i, hash_value in enumerate(hash_list):
#         if hash_value in hash_list[i+1:]:
#             if hash_value not in duplicates:
#                 duplicates.append(hash_value)
#     return duplicates

# for filename in os.listdir(image_directory):
#     if filename.endswith(".jpg") or filename.endswith(".png"):
#         image_path = os.path.join(image_directory, filename)
#         image = Image.open(image_path)

#         confusionmatrix_phash(image)