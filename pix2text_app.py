import yaml
from PIL import ImageGrab
import pyperclip
import rumps
from pix2text import Pix2Text

SUCCESS_NT_FORM = {
    'title': 'Success!',
    'subtitle': 'Success! Copied to clipboard.',
    'message': '',
}

ERROR_NT_FORM = {
    'title': 'Fail!',
    'subtitle': 'Error! You didn\'t copy the screenshot.',
    'message': '',
}

CONFIG = yaml.safe_load(open('./config.yaml', 'r', encoding='utf-8'))


class Pix2TextApplication(rumps.App):
    def __init__(self, name):
        super(Pix2TextApplication, self).__init__(
            name=name, icon='./icons/p2t-logo.png', quit_button="Quit"
        )
        self.p2t = Pix2Text(
            **CONFIG['pix2text'],
            # text_config=dict(
            #     det_model_name='ch_PP-OCRv3_det',
            #     rec_model_backend='onnx',
            #     rec_model_name='doc-densenet_lite_666-gru_large',
            # ),
            # analyzer_config=dict(
            #     model_name='mfd',
            #     model_type='yolov7',
            #     model_fp='/Users/king/.cnstd/1.2/analysis/mfd-yolov7-epoch224-20230613.pt',
            # ),
            # formula_config=dict(
            #     model_name='mfr-pro',
            #     model_backend='onnx',
            #     # model_dir=formula_dir / 'mfr-pro-onnx',  # 注：修改成你的模型文件所存储的路径
            # ),
        )

    @rumps.clicked("Mixed OCR")
    def recognize_mixed(self, _):
        # Identify mixed image
        image = ImageGrab.grabclipboard()
        try:
            only_text = self.p2t.recognize(
                image, resized_shape=608, return_text=True
            )  # 也可以使用 `p2t(img_fp, resized_shape=608)` 获得相同的结果
            SUCCESS_NT_FORM['message'] = only_text
            pyperclip.copy(only_text)
            rumps.notification(**SUCCESS_NT_FORM)
        except Exception as e:
            ERROR_NT_FORM['message'] += str(e)
            rumps.notification(**ERROR_NT_FORM)

    @rumps.clicked("Formula OCR")
    def recognize_formula(self, _):
        # Only recognize formula
        image = ImageGrab.grabclipboard()
        try:
            formula_str = self.p2t.recognize_formula(image)
            pyperclip.copy(f'$$\n{formula_str}\n$$')
            SUCCESS_NT_FORM['message'] = formula_str
            rumps.notification(**SUCCESS_NT_FORM)
        except Exception as e:
            ERROR_NT_FORM['message'] += str(e)
            rumps.notification(**ERROR_NT_FORM)

    @rumps.clicked("Text OCR")
    def recognize_text(self, _):
        # Only recognize formula
        image = ImageGrab.grabclipboard()
        try:
            text_str = self.p2t.recognize_text(image)
            pyperclip.copy(text_str)
            SUCCESS_NT_FORM['message'] = text_str
            rumps.notification(**SUCCESS_NT_FORM)
        except Exception as e:
            ERROR_NT_FORM['message'] += str(e)
            rumps.notification(**ERROR_NT_FORM)

    @rumps.notifications
    def notification_center(self, info):
        pass

    @rumps.clicked("On / Off")
    def onoff(self, _):
        mixed_ocr_button = self.menu['Mixed OCR']
        if mixed_ocr_button.callback is None:
            mixed_ocr_button.set_callback(self.recognize_mixed)
        else:
            mixed_ocr_button.set_callback(None)
        formula_ocr_button = self.menu['Formula OCR']
        if formula_ocr_button.callback is None:
            formula_ocr_button.set_callback(self.recognize_formula)
        else:
            formula_ocr_button.set_callback(None)
        formula_ocr_button = self.menu['Text OCR']
        if formula_ocr_button.callback is None:
            formula_ocr_button.set_callback(self.recognize_text)
        else:
            formula_ocr_button.set_callback(None)


if __name__ == "__main__":
    Pix2TextApplication(name='').run()
