from pix2text import Pix2Text, merge_line_texts
from PIL import ImageGrab
import pyperclip
import rumps

SUCCESS_NT_FORM = {
    'title': 'Success!',
    'subtitle': 'Success!Copied to clipboard.',
    'message': ''
}

ERROR_NT_FORM = {
    'title': 'Fail!',
    'subtitle': 'Error!You didn\'t copy the screenshot.',
    'message': ''
}


class LatexOrcApplication(rumps.App):
    def __init__(self, name):
        super(LatexOrcApplication, self).__init__(name=name, icon='./icons/menu_bar_logo.png', quit_button="Quit")
        self.p2t = Pix2Text(analyzer_config=dict(model_name='mfd'))

    @rumps.clicked("Formula OCR")
    def recognize_formula(self, _):
        # Only recognize formula
        image = ImageGrab.grabclipboard()
        try:
            formula_str = self.p2t.recognize_formula(image, resized_shape=608, save_analysis_res=None)
            pyperclip.copy(formula_str)
            rumps.notification(**SUCCESS_NT_FORM)
        except Exception as e:
            ERROR_NT_FORM['message'] += str(e)
            rumps.notification(**ERROR_NT_FORM)

    @rumps.clicked("Mixed OCR")
    def recognize_mixed(self, _):
        # Identify mixed image
        image = ImageGrab.grabclipboard()
        try:
            outs = self.p2t.recognize(image, resized_shape=608)  # 也可以使用 `p2t(img_fp, resized_shape=608)` 获得相同的结果
            only_text = merge_line_texts(outs, auto_line_break=True)
            pyperclip.copy(only_text)
            rumps.notification(**SUCCESS_NT_FORM)
        except Exception as e:
            ERROR_NT_FORM['message'] += str(e)
            rumps.notification(**ERROR_NT_FORM)

    @rumps.notifications
    def notification_center(self, info):
        pass

    @rumps.clicked("On / Off")
    def onoff(self, _):
        formula_ocr_button = self.menu['Formula OCR']
        if formula_ocr_button.callback is None:
            formula_ocr_button.set_callback(self.recognize_formula)
        else:
            formula_ocr_button.set_callback(None)
        mixed_ocr_button = self.menu['Mixed OCR']
        if mixed_ocr_button.callback is None:
            mixed_ocr_button.set_callback(self.recognize_mixed)
        else:
            mixed_ocr_button.set_callback(None)


if __name__ == "__main__":
    LatexOrcApplication(name='').run()
