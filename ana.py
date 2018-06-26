import json
import os
import cv2

label_categories_file = "D:\\magus\\database\\PIC_2018_train-val\\categories_list\\label_categories.json"
relation_categories_file = "D:\\magus\\database\\PIC_2018_train-val\\categories_list\\relation_categories.json"
relations_train_file="D:\\magus\\database\\PIC_2018_train-val\\relation\\relations_train.json"
relations_val_file="D:\\magus\\database\\PIC_2018_train-val\\relation\\relations_val.json"
image_dir="D:\\magus\\database\\PIC_2018_train-val\\image\\train"
semantic_dir="D:\\magus\\database\\PIC_2018_train-val\\segmentation\\train\\semantic"
instance_dir="D:\\magus\\database\\PIC_2018_train-val\\segmentation\\train\\instance"

def getImageFile(path):
    filenames=[]
    for filename in os.listdir(path):  # listdir的参数是文件夹的路径
        filenames.append(filename)
    return filenames

def resolveJson(path):
    images=None
    with open(path) as f:
        for line in f:
            images=json.loads(line)
    return images

# imagefiles = getImageFile(image_dir)
# relation_catetories = sorted(resolveJson(relation_categories_file),key=lambda relation: relation['id'])
# label_categories = sorted(resolveJson(label_categories_file),key=lambda label:label['id'])
# images = resolveJson(relations_train_file)
# others = []
# for image in images:
#     for relation in image['relations']:
#         if(relation['relation'] == 30): #other
#             other = dict()
#             other['image_name'] = imagefiles[image['image_id']]
#             other['image_id'] = image['image_id']
#             other['subject'] = relation['subject']
#             other['object'] = relation['object']
#             other['relation'] = relation['relation']
#             others.append(other)
# with open('others_image.json', 'w', encoding='utf-8') as f:
#     json.dump(others, f)

others_images = sorted(resolveJson("others_image.json"),key=lambda image: image['image_id'])
for others_image in others_images:
    semantic_image = cv2.imread(semantic_dir+"\\"+others_image['image_name'],cv2.IMREAD_GRAYSCALE)
    instance_image = cv2.imread(instance_dir+"\\"+others_image['image_name'],cv2.IMREAD_GRAYSCALE)

    break
