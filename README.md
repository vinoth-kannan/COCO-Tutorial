# COCO-Tutorial

The **COCO (Common Objects in Context)** dataset is a large-scale image recognition dataset for object detection, segmentation, and captioning tasks. It contains over 330,000 images, each annotated with 80 object categories and 5 captions describing the scene. The COCO dataset is widely used in computer vision research and has been used to train and evaluate many state-of-the-art object detection and segmentation models.

The dataset has two main parts: the **images** and their **annotations**.

The images are organized into a hierarchy of directories, with the top-level directory containing subdirectories for the train, validation, and test sets.
The annotations are provided in JSON format, with each file corresponding to a single image.
Each annotation in the dataset includes the following information:

Image file name
Image size (width and height)
List of objects with the following information: Object class (e.g., "person," "car"); Bounding box coordinates (x, y, width, height); Segmentation mask (polygon or RLE format); Keypoints and their positions (if available)
Five captions describing the scene
The COCO dataset also provides additional information, such as image super categories, license, and coco-stuff (pixel-wise annotations for stuff classes in addition to 80 object classes).

MS COCO offers various types of annotations,

**Object detection **with bounding box coordinates and full segmentation masks for 80 different objects
**Stuff image segmentation** with pixel maps displaying 91 amorphous background areas
**Panoptic segmentation **identifies items in images based on 80 "things" and 91 "stuff" categories
Dense pose with over 39,000 photos featuring over 56,000 tagged persons with a mapping between pixels and a template 3D model and natural language descriptions for each image
Keypoint annotations for over 250,000 persons annotated with key points such as the right eye, nose, and left hip
