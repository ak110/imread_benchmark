import numpy as np
from pathlib import Path

from imread_benchmark import (imread_opencv, imread_pillow,
                              imread_imageio, imread_skimage,
                              imread_tf, imread_lycon, imread_jpeg4py,
                              imread_torchvision)

BASE_DIR = Path(__file__).parent
image_paths = list(path for path in (BASE_DIR / 'で～た').glob('*')
                   if path.suffix != ".gif")


def test_imread():
    functions = [
        imread_opencv,
        imread_pillow,
        imread_imageio,
        imread_skimage,
        imread_tf,
        imread_lycon,
        imread_torchvision
        # imread_jpeg4py
    ]
    for image_path in image_paths:
        for f in functions:
            img = f(image_path)
            assert img is not None and \
                   img.shape == (1280, 1920, 3) and \
                   img.dtype == np.float32, \
                f'Load error: {f.__name__}("{x}") -> {img if img is None else img.shape}"'


if __name__ == '__main__':
    test_imread()
