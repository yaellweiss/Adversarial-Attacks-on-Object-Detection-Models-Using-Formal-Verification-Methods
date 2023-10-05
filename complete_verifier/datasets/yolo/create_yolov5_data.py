import os
import numpy as np
import cv2
import yaml

def get_class_names(file_path):
    with open(file_path, 'r') as f:
        class_names = yaml.load(f, Loader=yaml.FullLoader)
    return class_names['names']

def get_image_and_annotation_paths(data_dir):
    img_dir = os.path.join(data_dir, 'images')
    ann_dir = os.path.join(data_dir, 'annotations')
    img_paths = [os.path.join(img_dir, f) for f in os.listdir(img_dir) if f.endswith('.jpg')]
    ann_paths = [os.path.join(ann_dir, f) for f in os.listdir(ann_dir) if f.endswith('.txt')]
    return img_paths, ann_paths

def parse_annotation_file(ann_path):
    with open(ann_path, 'r') as f:
        lines = f.readlines()
    boxes = []
    class_ids = []
    for line in lines:
        parts = line.strip().split(' ')
        class_id = int(parts[0])
        x, y, w, h = map(float, parts[1:])
        x_min = int((x - w/2) * 416)
        y_min = int((y - h/2) * 416)
        x_max = int((x + w/2) * 416)
        y_max = int((y + h/2) * 416)
        boxes.append([x_min, y_min, x_max, y_max])
        class_ids.append(class_id)
    return boxes, class_ids

def create_yolov5_data(data_dir, anchors):
    img_paths, ann_paths = get_image_and_annotation_paths(data_dir)
    class_names = get_class_names(os.path.join(data_dir, 'coco128.yaml'))
    num_classes = len(class_names)
    yolo_boxes = []
    class_ids = []
    confidences = []
    for i in range(len(img_paths)):
        img_path = img_paths[i]
        ann_path = ann_paths[i]
        boxes, cids = parse_annotation_file(ann_path)
        img = cv2.imread(img_path)
        h, w, _ = img.shape
        targets = []
        for j, box in enumerate(boxes):
            x_min, y_min, x_max, y_max = box
            xc, yc = (x_min + x_max) / 2, (y_min + y_max) / 2
            bw, bh = x_max - x_min, y_max - y_min
            for k, anchor in enumerate(anchors):
                aw, ah = anchor
                if bw / aw < 4 and bh / ah < 4:
                    tx = xc / w
                    ty = yc / h
                    tw = bw / aw
                    th = bh / ah
                    target = [tx, ty, tw, th, 1, cids[j]]
                    targets.append(target)
                    break
        targets = np.array(targets)
        if targets.shape[0] > 0:
            yolo_boxes.append(targets[:, :-1].flatten())
            class_ids.append(targets[:, -1])
            confidences.append(np.ones(targets.shape[0]))
    np.save('X_yolo.npy', np.array(yolo_boxes))
    np.save('y_yolo.npy', np.array([np.array(class_ids), np.array(confidences)]))
