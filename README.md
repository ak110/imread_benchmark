# 各種ライブラリの画像読み込み速度比較

各種ライブラリで画像を読み込む速度を比較するコード。

- cv2.imread
- PIL.Image.open
- imageio.imread
- skimage.io.imread
- [tf.io.decode_image](https://www.tensorflow.org/api_docs/python/tf/io/decode_image)
- [torchvision.io.read_image](https://pytorch.org/docs/stable/torchvision/io.html#image)

インターフェースは以下に統一して計測。

- 入力: pathlib.Path
- 出力: float32のndarray。shapeは`(height, width, RGB)`。値は[0, 255]。エラー時はNone。

## 実行結果例

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

## ライブラリ毎の画像読み込み速度比較結果

最新の処理結果は[wakame1367/imread_benchmark/issues](https://github.com/wakame1367/imread_benchmark/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)に載せています。

また次の`GitHubActions`を`workflow on dispatch`で実行した結果がIssueに載せ
[GitHubActions workflow on dispatch](https://github.com/wakame1367/imread_benchmark/actions/workflows/benchmark.yml)
