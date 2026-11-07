import os
import cv2
import numpy as np


def Calibration_label(label_dir, save_dir):
    os.makedirs(save_dir, exist_ok=True)
    ori_labels = os.listdir(label_dir)
    for id, name in enumerate(ori_labels):
        ori_label_path = os.path.join(label_dir, name)
        ori_label_img = cv2.imread(ori_label_path)
        label_img = np.where(ori_label_img > 50, 255, 0)
        save_path = os.path.join(save_dir, name)
        cv2.imwrite(save_path, label_img)


if __name__ == '__main__':
    path1 = './train/labels'
    path2 = './train/Calibration_label'
    Calibration_label(path1, path2)