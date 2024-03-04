from pix2tex.cli import LatexOCR
from PIL import ImageGrab
import pyperclip
import rumps


class LatexOrc(rumps.App):
    def __init__(self, name):
        super(LatexOrc, self).__init__(name=name, icon='./icons/menubar_ogo.png', quit_button="Quit")
        self.ocr_model = LatexOCR()

    @rumps.clicked("Start OCR")
    def prefs(self, _):
        image = ImageGrab.grabclipboard()
        latex_string = self.ocr_model(image)
        pyperclip.copy(latex_string)
        rumps.notification("Success!", latex_string, latex_string)

    @rumps.notifications
    def notification_center(self, info):
        pass

    @rumps.clicked("On / Off")
    def onoff(self, _):
        print_button = self.menu['Start OCR']
        if print_button.callback is None:
            print_button.set_callback(self.prefs)
        else:
            print_button.set_callback(None)


if __name__ == "__main__":
    LatexOrc(name='').run()
