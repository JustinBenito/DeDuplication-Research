import os
from PIL import Image
import imagehash
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mlxtend.plotting import plot_confusion_matrix

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
def plot_confusion(hash,title):
        categories=[["True Positive","True Negative"],["False Positive","False Negative"]]
        fig, ax = plt.subplots()
        cax = ax.matshow(hash,cmap='cividis')  

        for i in range(hash.shape[0]):
            for j in range(hash.shape[1]):
                ax.text(j, i, f'{categories[i][j]}\n{hash[i, j]:.2f}%', ha='center', va='center', color='black')

        plt.xlabel('False')
        plt.ylabel('True')
        plt.title(title)

        plt.show()


def confusionmatrix(hashfunc):
    num_images = 0
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0
    
    confusion_matrix = np.zeros((2, 2))  # Initialize the confusion matrix
    
    for filename in os.listdir(image_directory):
        num_images += 1
        if filename.endswith(".jpeg") or filename.endswith(".png"):
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
    
    # Update the confusion matrix with calculated values
    confusion_matrix[0, 0] = true_positive / num_images * 100
    confusion_matrix[0, 1] = true_negative / num_images * 100
    confusion_matrix[1, 0] = false_positive / num_images * 100
    confusion_matrix[1, 1] = false_negative / num_images * 100
    
    error = (false_positive + false_negative) / num_images
    accuracy = (true_positive + true_negative) / num_images
    print('For', str(hashfunc)[9:16])
    print('true_positive %', (true_positive / num_images) * 100)
    print('true_negative %', (true_negative / num_images) * 100)
    print('false_positive %', (false_positive / num_images) * 100)
    print('false_negative %', (false_negative / num_images) * 100)
    print('error', error * 100, "%")
    print('accuracy', accuracy * 100, "%")
    plot_confusion(confusion_matrix,str(hashfunc)[9:16])


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