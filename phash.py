from PIL import Image
import imagehash

def perceptual_hash(image_path):
    image = Image.open(image_path)
    grayscale_image = image.convert('L')
    hash_value = imagehash.phash(grayscale_image)
    return str(hash_value)

def average_hash(image_path):
    image = Image.open(image_path)
    grayscale_image = image.convert('L')
    hash_value = imagehash.phash(grayscale_image)
    return str(hash_value)

def wavelet_hash(image_path):
    image = Image.open(image_path)
    grayscale_image = image.convert('L')
    hash_value = imagehash.whash(grayscale_image)
    return str(hash_value)

def difference_hash(image_path):
    image = Image.open(image_path)
    grayscale_image = image.convert('L')
    hash_value = imagehash.dhash(grayscale_image)
    return str(hash_value)


image_path = 'img/lung1.jpeg'
image_path_copy='img/lung1 copy.jpeg'
hash_value_1 = perceptual_hash(image_path)
hash_value_2 = wavelet_hash(image_path)
hash_value_3 = difference_hash(image_path)
hash_value_4 = average_hash(image_path)
hash_value_11 = perceptual_hash(image_path_copy)
hash_value_22 = wavelet_hash(image_path_copy)
hash_value_33 = difference_hash(image_path_copy)
hash_value_44 = average_hash(image_path_copy)

print("Perceptual hash of 1:", hash_value_1)
print("Perceptual hash of 2:", hash_value_2)
print("Perceptual hash of 3:", hash_value_3)
print("Perceptual hash of 4:", hash_value_4)
print("Perceptual hash of 11:", hash_value_11)
print("Perceptual hash of 22:", hash_value_22)
print("Perceptual hash of 33:", hash_value_33)
print("Perceptual hash of 44:", hash_value_44)
