# 各種ライブラリの画像読み込み速度比較

各種ライブラリで画像を読み込む速度を比較するコード。

- cv2.imread
- PIL.Image.open
- imageio.imread
- skimage.io.imread
- [tf.io.decode_image](https://www.tensorflow.org/api_docs/python/tf/io/decode_image)

(後ろ二つはバックエンドがPillowとかだったりするけど一応。)

インターフェースは以下に統一して計測。

- 入力: pathlib.Path
- 出力: float32のndarray。shapeは`(height, width, RGB)`。値は[0, 255]。エラー時はNone。

## 実行結果例

環境によって結構変わるのであくまでも例。(しかも結構ぶれる。。)

### Linuxで普通のPillowな環境

```txt
================================ img.gif ================================
imread_opencv  : 14.8[sec] (mean: 0.0493)[sec]
imread_pillow  : 11.0[sec] (mean: 0.0366)[sec]
imread_imageio : 62.4[sec] (mean: 0.2081)[sec]
imread_skimage : 61.0[sec] (mean: 0.2034)[sec]
imread_tf      : 12.7[sec] (mean: 0.0425)[sec]
================================ img.png ================================
imread_opencv  : 22.7[sec] (mean: 0.0755)[sec]
imread_pillow  : 18.5[sec] (mean: 0.0616)[sec]
imread_imageio : 18.9[sec] (mean: 0.0631)[sec]
imread_skimage : 18.9[sec] (mean: 0.0631)[sec]
imread_tf      : 19.4[sec] (mean: 0.0645)[sec]
================================ img.jpg ================================
imread_opencv  : 20.8[sec] (mean: 0.0693)[sec]
imread_pillow  : 19.1[sec] (mean: 0.0638)[sec]
imread_imageio : 19.6[sec] (mean: 0.0652)[sec]
imread_skimage : 19.7[sec] (mean: 0.0656)[sec]
imread_tf      : 10.3[sec] (mean: 0.0342)[sec]
```

- **JPEGでTensorflowが最速**

### Linuxで[Pillow-SIMD](https://github.com/uploadcare/pillow-simd)な環境

```txt
================================ img.gif ================================
imread_opencv  : 14.7[sec] (mean: 0.0489)[sec]
imread_pillow  : 11.5[sec] (mean: 0.0385)[sec]
imread_imageio : 60.3[sec] (mean: 0.2011)[sec]
imread_skimage : 59.5[sec] (mean: 0.1984)[sec]
imread_tf      : 12.8[sec] (mean: 0.0428)[sec]
================================ img.png ================================
imread_opencv  : 22.7[sec] (mean: 0.0757)[sec]
imread_pillow  : 18.4[sec] (mean: 0.0612)[sec]
imread_imageio : 18.6[sec] (mean: 0.0621)[sec]
imread_skimage : 18.6[sec] (mean: 0.0621)[sec]
imread_tf      : 19.4[sec] (mean: 0.0645)[sec]
================================ img.jpg ================================
imread_opencv  : 20.8[sec] (mean: 0.0695)[sec]
imread_pillow  : 12.9[sec] (mean: 0.0432)[sec]
imread_imageio : 13.2[sec] (mean: 0.0440)[sec]
imread_skimage : 13.2[sec] (mean: 0.0441)[sec]
imread_tf      : 10.4[sec] (mean: 0.0346)[sec]
```

- `Pillow-SIMD`導入してもJPEGではTensorflowが最速
