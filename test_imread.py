import unittest
import numpy as np
from pathlib import Path

from imread_benchmark import (
    imread_opencv,
    imread_pillow,
    imread_imageio,
    imread_skimage,
    imread_tf,
    imread_torchvision,
)

BASE_DIR = Path(__file__).parent
IMG_DIR_NAME = "images"
IMG_PATH = BASE_DIR / IMG_DIR_NAME
image_paths = list(path for path in IMG_PATH.glob("*") if path.suffix != ".gif")


class TestImread(unittest.TestCase):
    def test_imread(self):
        functions = [
            imread_opencv,
            imread_pillow,
            imread_imageio,
            imread_skimage,
            imread_tf,
            imread_torchvision,
        ]
        for image_path in image_paths:
            for f in functions:
                img = f(image_path)
                self.assertIsNotNone(
                    img,
                    f'Load error: {f.__name__}("{image_path}") -> {img if img is None else img.shape}"',
                )
                self.assertEqual(img.shape, (1280, 1920, 3))
                self.assertEqual(img.dtype, np.float32)


if __name__ == "__main__":
    unittest.main()
