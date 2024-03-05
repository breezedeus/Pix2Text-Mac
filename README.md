# 一个基于LaTex-OCR的识别数学公式的macOS菜单栏应用程序

### 注意该应用程序仅适用于macOS

### 效果图

- 应用在启动台的效果图
  ![app_style.png](assets%2Fapp_style.png)
- 菜单栏应用的效果图
  ![menu_bar_style.png](assets%2Fmenu_bar_style.png)

### 如何安装

- 克隆库

```angular2html
git clone https://github.com/horennel/LaTex-OCR_for_macOS.git
```

- 安装依赖环境

```angular2html
pip3 install -r requirements.txt
```

- 打包应用程序

```angular2html
python3 setup.py py2app -A
```

- 在生成的dist文件夹中可以看到应用程序`MyLatexOCR.app`，将其移动到`应用程序文件夹`即可

### 如何使用

- 启动程序
    - 启动应用`MyLatexOCR`，可以看到应用程序的菜单栏图标
    - 点击菜单栏图标的`On / Off`按钮，确保`Start OCR`按钮常亮
- 截图
    - 使用任意截图软件，例如`Snipaste`，截图并复制到剪切板
- 识别
    - 点击`Start OCR`按钮，识别成功后，会收到通知栏的通知（tip：如果不想接受通知可以在系统设置里关闭通知）
    - 收到通知后，即可粘贴Latex公式到任意地方

### 感谢开源图标作者

- [ELÍAS的个人主页](https://eliasruiz.com/)

### 如何二次开发

- [macOS菜单栏应用开发：rumps文档](https://rumps.readthedocs.org)
- [macOS应用程序构建：py2app文档](https://py2app.readthedocs.io)

### 感谢以下开源作者

- [latex公式识别：LaTex-OCR](https://github.com/lukas-blecher/LaTeX-OCR)
- [复制和粘贴剪贴板：pyperclip](https://github.com/asweigart/pyperclip)
- [macOS菜单栏应用程序：rumps](https://github.com/jaredks/rumps)
- [macOS应用程序构建：py2app](https://github.com/ronaldoussoren/py2app)
- [图像处理：pillow](https://github.com/python-pillow/Pillow)