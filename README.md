# 各種ライブラリの画像読み込み速度比較

各種ライブラリで画像を読み込む速度を比較するコード。

- cv2.imread
- PIL.Image.open
- imageio.imread
- skimage.io.imread
- [tf.io.decode_image](https://www.tensorflow.org/api_docs/python/tf/io/decode_image)
- [lycon.load](https://github.com/ethereon/lycon)
- [torchvision.io.read_image](https://pytorch.org/docs/stable/torchvision/io.html#image)

(後ろ二つはバックエンドがPillowとかだったりするけど一応。)

インターフェースは以下に統一して計測。

- 入力: pathlib.Path
- 出力: float32のndarray。shapeは`(height, width, RGB)`。値は[0, 255]。エラー時はNone。

## 環境情報
GoogleColabratoryに依存します、その他のライブラリversionは以下のrequirements.txtを参照しております。
- [wakamezake/imread_benchmark/blob/master/requirements.txt](https://github.com/wakamezake/imread_benchmark/blob/master/requirements.txt)

実験に使用したコードやデータは以下になります。
- [wakamezake/imread_benchmark/blob/master/Load_image_benchmark.ipynb](https://github.com/wakamezake/imread_benchmark/blob/master/Load_image_benchmark.ipynb)
- [wakamezake/imread_benchmark/blob/master/imread_benchmark.py](https://github.com/wakamezake/imread_benchmark/blob/master/imread_benchmark.py)
- [wakamezake/imread_benchmark/tree/master/%E3%81%A7%EF%BD%9E%E3%81%9F](https://github.com/wakamezake/imread_benchmark/tree/master/%E3%81%A7%EF%BD%9E%E3%81%9F)

## 実行結果例

環境によって結構変わるのであくまでも例。(しかも結構ぶれる。。)

### Linuxで普通のPillowな環境

```txt
================================ img.jpg ================================
imread_opencv  : 23.0[sec] (mean: 0.0767)[sec]
imread_pillow  : 21.9[sec] (mean: 0.0730)[sec]
imread_imageio : 24.1[sec] (mean: 0.0804)[sec]
imread_skimage : 23.1[sec] (mean: 0.0768)[sec]
imread_tf      : 12.6[sec] (mean: 0.0420)[sec]
imread_lycon   : 13.0[sec] (mean: 0.0432)[sec]
imread_torchvision: 13.2[sec] (mean: 0.0442)[sec]
================================ img.png ================================
imread_opencv  : 24.4[sec] (mean: 0.0815)[sec]
imread_pillow  : 21.1[sec] (mean: 0.0703)[sec]
imread_imageio : 22.3[sec] (mean: 0.0744)[sec]
imread_skimage : 22.0[sec] (mean: 0.0732)[sec]
imread_tf      : 22.5[sec] (mean: 0.0749)[sec]
imread_lycon   : 19.8[sec] (mean: 0.0662)[sec]
imread_torchvision: 21.0[sec] (mean: 0.0699)[sec]
```

- **JPEGでTensorflowが最速**
- **PNGについてはlyconが最速**

### Linuxで[Pillow-SIMD](https://github.com/uploadcare/pillow-simd)な環境

```txt
================================ img.jpg ================================
imread_opencv  : 22.3[sec] (mean: 0.0745)[sec]
imread_pillow  : 15.7[sec] (mean: 0.0524)[sec]
imread_imageio : 16.7[sec] (mean: 0.0556)[sec]
imread_skimage : 17.9[sec] (mean: 0.0598)[sec]
imread_tf      : 12.4[sec] (mean: 0.0413)[sec]
imread_lycon   : 13.0[sec] (mean: 0.0432)[sec]
imread_torchvision: 14.0[sec] (mean: 0.0468)[sec]
================================ img.png ================================
imread_opencv  : 24.9[sec] (mean: 0.0831)[sec]
imread_pillow  : 21.1[sec] (mean: 0.0703)[sec]
imread_imageio : 22.0[sec] (mean: 0.0734)[sec]
imread_skimage : 22.2[sec] (mean: 0.0740)[sec]
imread_tf      : 23.4[sec] (mean: 0.0781)[sec]
imread_lycon   : 19.8[sec] (mean: 0.0660)[sec]
imread_torchvision: 21.7[sec] (mean: 0.0722)[sec]
```

- `Pillow-SIMD`導入してもJPEGではTensorflowが最速
- 同様にPNGについてはlyconが最速