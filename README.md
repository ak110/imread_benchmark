# 各種ライブラリの画像読み込み速度比較

各種ライブラリで画像を読み込む速度を比較するコード。

- cv2.imread
- PIL.Image.open
- imageio.imread
- skimage.io.imread

(後ろ二つはバックエンドがPillowとかだったりするけど一応。)

インターフェースは以下に統一して計測。

- 入力: pathlib.Path
- 出力: float32のndarray。shapeは`(height, width, RGB)`。値は[0, 255]。エラー時はNone。

## 実行結果例

環境によって結構変わるのであくまでも例。(しかも結構ぶれる。。)

### Linuxで普通のPillowな環境

```txt
================================ img.gif ================================
imread_opencv  : 16.9
imread_pillow  :  8.4
imread_imageio : 43.0
imread_skimage : 10.6
================================ img.jpg ================================
imread_opencv  : 17.9
imread_pillow  : 31.0
imread_imageio : 31.3
imread_skimage : 31.1
================================ img.png ================================
imread_opencv  : 36.7
imread_pillow  : 22.4
imread_imageio : 22.0
imread_skimage : 23.1
```

個人的に一番よく使うJPEGでOpenCVがだいぶ速かった。が…

### Linuxで[Pillow-SIMD](https://github.com/uploadcare/pillow-simd)な環境

```txt
================================ img.gif ================================
imread_opencv  : 17.6
imread_pillow  :  8.9
imread_imageio : 43.7
imread_skimage : 10.5
================================ img.jpg ================================
imread_opencv  : 18.4
imread_pillow  : 11.2
imread_imageio : 11.5
imread_skimage : 11.5
================================ img.png ================================
imread_opencv  : 36.3
imread_pillow  : 23.9
imread_imageio : 22.7
imread_skimage : 22.3
```

`Pillow-SIMD`にしてみたらもうこれでいいじゃんという感じ。
