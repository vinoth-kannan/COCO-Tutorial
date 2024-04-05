from pycocotools.coco import COCO
import cv2


annotations_file = r"C:\Users\vinot\OneDrive\Documents\Intern_Projects\opencsv\image acquisition\shp1.v1i.coco\test\_annotations.coco.json"
coco = COCO(annotations_file)

categories = coco.loadCats(coco.getCatIds())
category_names = [category['name'] for category in categories]


def draw_boxes(image, ann_ids):
    for ann_id in ann_ids:
        ann = coco.loadAnns(ann_id)[0]
        bbox = ann['bbox']
        category_id = ann['category_id']
        category_name = category_names[category_id]

        x1 = int(bbox[0])
        y1 = int(bbox[1])
        x2 = int(bbox[0] + bbox[2])
        y2 = int(bbox[1] + bbox[3])

        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(image, category_name, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.imwrite(r"C:\Users\vinot\OneDrive\Documents\Intern_Projects\opencsv\image acquisition\Outputs\cocooutputs\\1.jpg",image)
    cv2.imshow('Annotated Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_filename = "2D-shape-_-pelmanism-game-202218_jpg.rf.674e201d0a10a8224ad1cdb402c80420.jpg"

image_info = None
for img in coco.dataset['images']:
    if img['file_name'] == image_filename:
        image_info = img
        break

if image_info:
    image_path = r"C:\Users\vinot\OneDrive\Documents\Intern_Projects\opencsv\image acquisition\shp1.v1i.coco\test\\" + image_filename
    image = cv2.imread(image_path)
    ann_ids = coco.getAnnIds(image_info['id'])
    draw_boxes(image, ann_ids)
else:
    print("Image not found in the dataset.")