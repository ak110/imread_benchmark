# 各種ライブラリの画像読み込み速度比較

各種ライブラリで画像を読み込む速度を比較するコード。

- cv2.imread
- PIL.Image.open
- imageio.imread
- skimage.io.imread
- [tf.io.decode_image](https://www.tensorflow.org/api_docs/python/tf/io/decode_image)
- [lycon.load](https://github.com/ethereon/lycon)

(後ろ二つはバックエンドがPillowとかだったりするけど一応。)

インターフェースは以下に統一して計測。

- 入力: pathlib.Path
- 出力: float32のndarray。shapeは`(height, width, RGB)`。値は[0, 255]。エラー時はNone。

## 実行結果例

環境によって結構変わるのであくまでも例。(しかも結構ぶれる。。)

### Linuxで普通のPillowな環境

```txt
================================ img.jpg ================================
imread_opencv  : 19.9[sec] (mean: 0.0664)[sec]
imread_pillow  : 18.4[sec] (mean: 0.0613)[sec]
imread_imageio : 18.9[sec] (mean: 0.0631)[sec]
imread_skimage : 18.9[sec] (mean: 0.0629)[sec]
imread_tf      :  9.6[sec] (mean: 0.0321)[sec]
imread_lycon   : 10.8[sec] (mean: 0.0358)[sec]
================================ img.png ================================
imread_opencv  : 21.8[sec] (mean: 0.0726)[sec]
imread_pillow  : 17.5[sec] (mean: 0.0583)[sec]
imread_imageio : 18.1[sec] (mean: 0.0603)[sec]
imread_skimage : 18.1[sec] (mean: 0.0602)[sec]
imread_tf      : 18.8[sec] (mean: 0.0628)[sec]
imread_lycon   : 17.1[sec] (mean: 0.0571)[sec]
```

- **JPEGでTensorflowが最速**
- **PNGについてはlyconが最速**

### Linuxで[Pillow-SIMD](https://github.com/uploadcare/pillow-simd)な環境

```txt
================================ img.jpg ================================
imread_opencv  : 20.0[sec] (mean: 0.0666)[sec]
imread_pillow  : 12.2[sec] (mean: 0.0408)[sec]
imread_imageio : 12.7[sec] (mean: 0.0424)[sec]
imread_skimage : 12.8[sec] (mean: 0.0426)[sec]
imread_tf      :  9.6[sec] (mean: 0.0319)[sec]
imread_lycon   : 10.9[sec] (mean: 0.0364)[sec]
================================ img.png ================================
imread_opencv  : 21.6[sec] (mean: 0.0719)[sec]
imread_pillow  : 17.6[sec] (mean: 0.0586)[sec]
imread_imageio : 18.0[sec] (mean: 0.0601)[sec]
imread_skimage : 18.0[sec] (mean: 0.0601)[sec]
imread_tf      : 19.1[sec] (mean: 0.0635)[sec]
imread_lycon   : 17.3[sec] (mean: 0.0577)[sec]
```

- `Pillow-SIMD`導入してもJPEGではTensorflowが最速
- 同様にPNGについてはlyconが最速