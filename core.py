# -*- coding: utf-8 -*-
# @Time : 20-6-9 下午3:06
# @Author : zhuying
# @Company : Minivision
# @File : test.py
# @Software : PyCharm

import os
import cv2
import numpy as np
import argparse
import warnings
import time
import uuid
import winsound

from src.anti_spoof_predict import AntiSpoofPredict
from src.generate_patches import CropImage
from src.utility import parse_model_name
warnings.filterwarnings('ignore')


SAMPLE_IMAGE_PATH = "./images/sample/"


# 因为安卓端APK获取的视频流宽高比为3:4,为了与之一致，所以将宽高比限制为3:4
def check_image(image):
    height, width, channel = image.shape
    if width/height != 3/4:
        print("Image is not appropriate!!!\nHeight/Width should be 4/3.")
        return False
    else:
        return True


def test(image_name,model_dir, device_id):
    model_test = AntiSpoofPredict(device_id)
    image_cropper = CropImage()
    cap = cv2.VideoCapture(0) # 0 represents the default camera
    while True:
        ret, image = cap.read()
        path="static/notregistered/"+str(uuid.uuid4())+".png"
        cv2.imwrite(path,image)
        if not ret:
            break
        height, width, _ = image.shape
        aspect_ratio = width / height
        if aspect_ratio != 4 / 3:
            new_height = int(width * 3 / 4)
            image = cv2.resize(image, (width, new_height))
        # result = check_image(image)
        # if result is False:
            # continue
        image_bbox = model_test.get_bbox(image)
        prediction = np.zeros((1, 3)) 
        test_speed = 0
        # sum the prediction from single model's result
        for model_name in os.listdir(model_dir):
            h_input, w_input, model_type, scale = parse_model_name(model_name)
            param = {
                "org_img": image,
                "bbox": image_bbox,
                "scale": scale,
                "out_w": w_input,
                "out_h": h_input,
                "crop": True,
            }
            if scale is None:
                param["crop"] = False
            img = image_cropper.crop(**param)
            start = time.time()
            prediction += model_test.predict(img, os.path.join(model_dir, model_name))
            test_speed += time.time()-start
        # draw result of prediction
        label = np.argmax(prediction)
        value = prediction[0][label]/2
        if label == 1:
            print("Frame is Real Face. Score: {:.2f}.".format(value))
            result_text = "RealFace Score: {:.2f}".format(value)
            color = (255, 0, 0)
            output={"status":"real","path":path}
            return output
        else:
            print("Frame is Fake Face. Score: {:.2f}.".format(value))
            result_text = "FakeFace Score: {:.2f}".format(value)
            color = (0, 0, 255)
            freq=500
            dur=100
            winsound.Beep(freq,dur)
            output={"status":"fake","path":path}
            return output

        print("Prediction cost {:.2f} s".format(test_speed))
        cv2.rectangle(
            image,
            (image_bbox[0], image_bbox[1]),
            (image_bbox[0] + image_bbox[2], image_bbox[1] + image_bbox[3]),
            color, 2)
        cv2.putText(
            image,
            result_text,
            (image_bbox[0], image_bbox[1] - 5),
            cv2.FONT_HERSHEY_COMPLEX, 0.5*image.shape[0]/1024, color)
        cv2.imshow("video", image)
        if cv2.waitKey(1) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


def startChecking():
    desc = "test"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument(
        "--device_id",
        type=int,
        default=0,
        help="which gpu id, [0/1/2/3]")
    parser.add_argument(
        "--model_dir",
        type=str,
        default="./resources/anti_spoof_models",
        help="model_lib used to test")
    parser.add_argument(
        "--image_name",
        type=str,
        default="image_F1.jpg",
        help="image used to test")
    args = parser.parse_args()
    print(args.device_id)
    out=test(args.image_name, args.model_dir, args.device_id)
    return out




# startChecking()





