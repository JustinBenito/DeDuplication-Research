import cv2

def orb_sim(img1, img2):
  orb = cv2.ORB_create()

  kp_a, desc_a = orb.detectAndCompute(img1, None)
  kp_b, desc_b = orb.detectAndCompute(img2, None)

  bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    
  matches = bf.match(desc_a, desc_b)
  similar_regions = [i for i in matches if i.distance < 50]  
  if len(matches) == 0:
    return 0
  return len(similar_regions) / len(matches)


img1 = cv2.imread('img/lung1.jpeg', 0)  
img2 = cv2.imread('img/lung1 copy.jpeg', 0) 

orb_similarity = orb_sim(img1, img2)  
print("Similarity using ORB is: ", orb_similarity)
