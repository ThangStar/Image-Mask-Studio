from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from .qt.build.preview_image_ui import Ui_PreviewDialog

class PreviewDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PreviewDialog()
        self.ui.setupUi(self)
        
        # Setup connections
        self.ui.btnClose.clicked.connect(self.reject)
        self.ui.btnSave.clicked.connect(self.accept)
        
        # Set window modality
        self.setWindowModality(Qt.ApplicationModal)
        
        # Set preview label properties
        self.ui.previewLabel.setMinimumSize(500, 400)
        self.ui.previewLabel.setScaledContents(True)

    def set_preview_image(self, pixmap):
        if pixmap and not pixmap.isNull():
            # Get the preview label size
            label_size = self.ui.previewLabel.size()
            
            # Scale the image to fit the preview label while maintaining aspect ratio
            scaled_pixmap = pixmap.scaled(
                label_size.width(),
                label_size.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.ui.previewLabel.setPixmap(scaled_pixmap)
        
    def get_save_settings(self):
        return {
            'format': self.ui.formatComboBox.currentText(),
            'quality': self.ui.qualitySpinBox.value()
        }