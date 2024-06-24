#!/usr/bin/env python3
import sys
import platform
import logging
import timeit

from pathlib import Path

import PIL.Image
import cv2
import imageio
import jpeg4py
import numpy as np
import skimage
import skimage.color
import skimage.io
import tensorflow as tf
import torch
import torchvision

BASE_DIR = Path(__file__).parent
IMG_DIR_NAME = "images"
IMG_PATH = BASE_DIR / IMG_DIR_NAME
X1 = list(path for path in IMG_PATH.glob("*") if path.suffix != ".gif")

logging.basicConfig(level=logging.INFO)
Logger = logging.getLogger(__name__)

image_libs = [
    np,
    cv2,
    PIL.Image,
    imageio,
    skimage,
    tf,
    torch,
    torchvision,
]


def library_version():
    def get_version(obj):
        return getattr(obj, "__version__", "None")

    def get_name(obj):
        return getattr(obj, "__name__", "None")

    Logger.info("=" * 32, "OS info", "=" * 32)
    Logger.info(platform.platform())
    Logger.info("=" * 32, "Python version", "=" * 32)
    Logger.info(sys.version)
    Logger.info("=" * 32, "Libraries version", "=" * 32)
    for _obj in image_libs:
        Logger.info(f"{get_name(_obj)}: {get_version(_obj)}")


def _main():
    library_version()
    functions = [
        imread_opencv,
        imread_pillow,
        imread_imageio,
        imread_skimage,
        imread_tf,
        imread_torchvision
        # imread_jpeg4py
    ]

    # 速度計測
    loop = 300
    for i, x in enumerate(X1):
        Logger.info("=" * 32, x.name, "=" * 32)
        for f in functions:
            t = timeit.timeit("""f(x)""", number=loop, globals={"f": f, "x": x})
            Logger.info(f"{f.__name__:15s}: {t:4.1f}[sec] (mean:{t / loop: .4f})[sec]")


def imread_opencv(path: Path) -> np.ndarray:
    arr = np.fromfile(str(path), np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    if img is None and path.suffix.lower() in (".gif"):  # TODO
        video = cv2.VideoCapture(str(path))
        _, img = video.read()
    if img is None:
        return None
    return img[:, :, ::-1].astype(np.float32)


def imread_pillow(path: Path) -> np.ndarray:
    try:
        with PIL.Image.open(path) as img:
            if img.mode != "RGB":
                img = img.convert("RGB")
            return np.asarray(img, dtype=np.float32)
    except Exception as e:
        Logger.error(f"failed to open {path} with error: {e}")
        return None


def imread_imageio(path: Path) -> np.ndarray:
    try:
        img = imageio.imread(path)
        if len(img.shape) == 2:
            img = skimage.color.gray2rgb(img)
        elif img.shape[2] == 4:
            img = skimage.color.rgba2rgb(img)
    except BaseException as e:
        Logger.error(f"failed to open {path} with error: {e}")
        return None
    return img.astype(np.float32)


def imread_skimage(path: Path) -> np.ndarray:
    try:
        img = skimage.io.imread(path)
        if len(img.shape) == 2:
            img = skimage.color.gray2rgb(img)
        elif img.shape[2] == 4:
            img = skimage.color.rgba2rgb(img)
        return img.astype(np.float32)
    except BaseException as e:
        Logger.error(f"failed to open {path} with error: {e}")
        return None


def imread_tf(path: Path) -> np.ndarray:
    try:
        img = tf.io.read_file(str(path))
        img = tf.image.decode_image(img, channels=3)
    except BaseException as e:
        Logger.error(f"failed to open {path} with error: {e}")
        return None
    # https://www.tensorflow.org/api_docs/python/tf/io/decode_image
    # Note: decode_gif returns a 4-D array [num_frames, height, width, 3],
    if path.suffix == ".gif":
        return img.numpy()[0].astype(np.float32)
    else:
        return img.numpy().astype(np.float32)


def imread_torchvision(path):
    # https://pytorch.org/docs/stable/torchvision/io.html#image
    try:
        # Tensor
        tensor = torchvision.io.read_image(str(path))
        # to numpy ndarray
        img = tensor.to("cpu").detach().numpy().copy()
        # (3, h, w) to (w, h, 3)
        img = img.transpose(1, 2, 0)
        if img is None:
            return None
        return img.astype(np.float32)
    except BaseException as e:
        Logger.error(f"failed to open {path} with error: {e}")
        return None


if __name__ == "__main__":
    _main()
