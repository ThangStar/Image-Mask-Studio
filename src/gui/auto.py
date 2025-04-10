from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox, QInputDialog, QApplication
from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QDesktopServices, QGuiApplication, QImage, QPixmap, QPainter, QPen, QColor, QFont, QFontDatabase, QScreen
from .qt.build.main_ui import Ui_Form
import os
from .preview_image import PreviewDialog

class HomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.imageLabel.setMinimumSize(600, 800)
        self.ui.imageLabel.setScaledContents(True)
        self.ui.imageLabel.setAlignment(Qt.AlignCenter)
        # Set fixed window size and center
        # screen_width = chiều rộng của màn hình
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        window_width = int(screen_width * 0.5)
        window_height = int(screen_height * 0.9)
        self.setFixedSize(window_width, window_height)

        self.center_window()
        self.font_size = 24
        self.setup_ui()
        self.setup_connections()
        self.setup_keyboard_shortcuts()  # Add this line
        self.show_grid = True
        self.dark_mode = False
        self.hide_grid = False
        
        # Load default image
        default_image_path = "default.jpg"
           # Lấy kích thước của ảnh
    
        self.current_image = QImage(default_image_path) if os.path.exists(default_image_path) else None
        
        # Grid default parameters
        self.grid_cols = 3
        self.grid_rows = 5
        self.cell_width = 170
        self.cell_height = 40
        self.horizontal_gap = 22
        self.vertical_gap = 60.5
        self.grid_offset_x = -1  # Changed initial X offset
        self.grid_offset_y = -100   # Changed initial Y offset
        self.grid_cells = {}  # Store cell values
        self.initialize_grid_cells()  # Initialize cell numbers
        self.selected_cells = {}  # Track all modified cells with their positions
        self.update_image_display()  # Add this line to show the default image

    def initialize_grid_cells(self):
        # Initialize empty grid cells (no default numbers)
        pass

    # def draw_grid(self, painter, label_rect):
    #     total_cells = self.grid_rows * self.grid_cols
    #     for i in range(total_cells):
    #         self.grid_cells[i] = i

    def setup_ui(self):
        # Apply initial bootstrap-like styling
        self.setStyleSheet(self.get_light_theme())
        
        # Set image label properties
        self.ui.imageLabel.setMinimumSize(600, 800)
        self.ui.imageLabel.setScaledContents(True)
        self.ui.imageLabel.setAlignment(Qt.AlignCenter)
        
        # Add custom font
        self.grid_font = QFont("Roboto")
        base_path = os.path.dirname(__file__)
        font_path = os.path.join(base_path, "..", "..", "assets", "fonts", "Roboto-Bold.ttf")
        font_id = QFontDatabase.addApplicationFont(font_path)
        print(font_path)
        print(font_id)
        if font_id != -1:
            self.grid_font = QFont(QFontDatabase.applicationFontFamilies(font_id)[0])
        self.grid_font.setPixelSize(self.font_size)
        self.grid_font.setBold(True)

    def setup_connections(self):
        self.ui.btnOpen.clicked.connect(self.open_image)
        self.ui.btnSave.clicked.connect(self.save_image)
        self.ui.btnGrid.clicked.connect(self.toggle_grid)
        self.ui.btnTheme.clicked.connect(self.toggle_theme)
        self.ui.btnRotate.clicked.connect(self.rotate_image)
        self.ui.btnFlip.clicked.connect(self.flip_image)
        self.ui.btnCrop.clicked.connect(self.crop_image)
        self.ui.btnFilter.clicked.connect(self.apply_filters)

    def get_light_theme(self):
        return """
            QWidget {
                background-color: #ffffff;
                color: #212529;
            }
            QPushButton {
                background-color: #0d6efd;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #0b5ed7;
            }
            QLabel {
                background-color: #f8f9fa;
            }
        """

    def get_dark_theme(self):
        return """
            QWidget {
                background-color: #212529;
                color: #f8f9fa;
            }
            QPushButton {
                background-color: #0d6efd;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #0b5ed7;
            }
            QLabel {
                background-color: #343a40;
            }
        """

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.setStyleSheet(self.get_dark_theme() if self.dark_mode else self.get_light_theme())

    def open_image(self):
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Image", downloads_path, "Image Files (*.png *.jpg *.jpeg *.bmp)"
        )
        if file_name:
            self.current_image = QImage(file_name)
            image_width = self.current_image.width()
            image_height = self.current_image.height()
            self.ui.imageLabel.setFixedSize(image_width, image_height)
            self.update_image_display()

    def save_image(self):
        
        if not self.current_image:
            QMessageBox.warning(self, "Warning", "No image to save!")
            return
        self.hide_grid = True
        print(self.hide_grid)
        self.update_image_display()
       


        # Get the current displayed image from the label
        current_pixmap = self.ui.imageLabel.pixmap()
        print(current_pixmap.size())
        print(current_pixmap.size())

        if current_pixmap and not current_pixmap.isNull():
            # Create and show preview dialog
            preview_dialog = PreviewDialog(self)

            
            # Get the actual image without scaling
            preview_pixmap = QPixmap.fromImage(self.current_image)

           
            if self.show_grid:
                # If grid is shown, use the current display pixmap instead
                preview_pixmap = current_pixmap
                
            preview_dialog.set_preview_image(preview_pixmap)
            
            if preview_dialog.exec():
                # User clicked Save
                settings = preview_dialog.get_save_settings()
                
                file_name, _ = QFileDialog.getSaveFileName(
                    self,
                    "Save Image",
                    "",
                    f"All Supported Formats (*.{settings['format'].lower()});;PNG (*.png);;JPEG (*.jpg *.jpeg);;BMP (*.bmp)"
                )
                
                if file_name:
                    # Save with selected format and quality
                    save_format = settings['format'].lower()
                    quality = settings['quality']
                    preview_pixmap.save(file_name, save_format, quality)
        self.hide_grid = False
        self.update_image_display()

    def toggle_grid(self):
        self.show_grid = not self.show_grid
        self.update_image_display()

    def mousePressEvent(self, event):
        if self.show_grid and self.ui.imageLabel.geometry().contains(event.pos()):
            pos = self.ui.imageLabel.mapFrom(self, event.pos())
            self.handle_grid_click(pos.x(), pos.y())

    def handle_grid_click(self, x, y):
        # Calculate starting position to center the grid
        label_rect = self.ui.imageLabel.rect()
        total_width = (self.cell_width * self.grid_cols) + (self.horizontal_gap * (self.grid_cols - 1))
        total_height = (self.cell_height * self.grid_rows) + (self.vertical_gap * (self.grid_rows - 1))
        # Add grid offsets to the starting position
        start_x = (label_rect.width() - total_width) // 2 + self.grid_offset_x
        start_y = (label_rect.height() - total_height) // 2 + self.grid_offset_y

        for row in range(self.grid_rows):
            for col in range(self.grid_cols):
                cell_x = start_x + col * (self.cell_width + self.horizontal_gap)
                cell_y = start_y + row * (self.cell_height + self.vertical_gap)
                cell_rect = QRect(cell_x, cell_y, self.cell_width, self.cell_height)
                
                if cell_rect.contains(x, y):
                    cell_index = row * self.grid_cols + col
                    value, ok = QInputDialog.getText(
                        self, 
                        "Enter Value", 
                        "Enter any value for this cell:",
                        text=str(self.grid_cells.get(cell_index, ""))
                    )
                    if ok:
                        self.grid_cells[cell_index] = value
                        self.selected_cells[cell_index] = cell_rect
                        self.update_image_display()
                    break

    def setup_keyboard_shortcuts(self):
        self.setFocusPolicy(Qt.StrongFocus)  # Enable keyboard focus

    def move_grid(self, direction, state):
        if not self.show_grid:
            return

        # Smaller step if Shift is pressed (state & 1)
        step = 1 if state & 1 else 5

        if direction == 'left':
            self.grid_offset_x -= step
        elif direction == 'right':
            self.grid_offset_x += step
        elif direction == 'up':
            self.grid_offset_y -= step
        elif direction == 'down':
            self.grid_offset_y += step

        self.update_image_display()

    def keyPressEvent(self, event):
        if not self.show_grid:
            return

        # Get shift state
        state = 1 if event.modifiers() & Qt.ShiftModifier else 0

        if event.key() == Qt.Key_Left:
            self.move_grid('left', state)
        elif event.key() == Qt.Key_Right:
            self.move_grid('right', state)
        elif event.key() == Qt.Key_Up:
            self.move_grid('up', state)
        elif event.key() == Qt.Key_Down:
            self.move_grid('down', state)
        # Grid cell size adjustments
        elif event.key() == Qt.Key_D:
            if state:
                self.cell_width = max(10, self.cell_width - 5)  # Decrease width (min 10)
            else:
                self.cell_width += 5  # Increase width
        elif event.key() == Qt.Key_A:
            if state:
                self.horizontal_gap = max(0, self.horizontal_gap - 1)  # Decrease gap (min 0)
            else:
                self.horizontal_gap += 1  # Increase gap
        elif event.key() == Qt.Key_W:
            if state:
                self.cell_height = max(10, self.cell_height - 5)  # Decrease height (min 10)
            else:
                self.cell_height += 5  # Increase height
        elif event.key() == Qt.Key_S:
            if state:
                self.vertical_gap = max(0, self.vertical_gap - 1)  # Decrease gap (min 0)
            else:
                self.vertical_gap += 1  # Increase gap
        else:
            return

        self.update_image_display()

    def draw_grid(self, painter, label_rect):
        painter.save()
        pen = QPen(QColor("#FF0000"))
        pen.setWidth(1)
        painter.setPen(pen)

        # Draw rectangles and backgrounds with normal opacity
        total_width = (self.cell_width * self.grid_cols) + (self.horizontal_gap * (self.grid_cols - 1))
        total_height = (self.cell_height * self.grid_rows) + (self.vertical_gap * (self.grid_rows - 1))
        start_x = (label_rect.width() - total_width) // 2 + self.grid_offset_x
        start_y = (label_rect.height() - total_height) // 2 + self.grid_offset_y

        for row in range(self.grid_rows):
            for col in range(self.grid_cols):
                x = start_x + col * (self.cell_width + self.horizontal_gap)
                y = start_y + row * (self.cell_height + self.vertical_gap)
                
                cell_rect = QRect(x, y, self.cell_width, self.cell_height)
                if not self.hide_grid:
                    painter.drawRect(cell_rect)

                cell_index = row * self.grid_cols + col
                
                if cell_index in self.selected_cells:
                    # Draw solid white background
                    text_rect = QRect(x + 2, y + 2, self.cell_width - 4, self.cell_height - 4)
                    painter.fillRect(text_rect, QColor("white"))
                    
                    # Draw text with reduced quality
                    painter.save()
                    painter.setFont(self.grid_font)
                    painter.setRenderHint(QPainter.TextAntialiasing, False)  # Disable text anti-aliasing
                    painter.setRenderHint(QPainter.SmoothPixmapTransform, False)  # Disable smooth transform
                    text_color = QColor(0, 0, 0, 245)
                    painter.setPen(text_color)
                    painter.drawText(cell_rect, Qt.AlignCenter, str(self.grid_cells.get(cell_index, "")))


    def draw_grid_info(self, painter, label_rect):
        # Grid position info
        grid_info = f"""Grid Position | X: {self.grid_offset_x} | Y: {self.grid_offset_y}"""
        self.ui.lblGridInfo.setText(grid_info)
        
        # Object parameters info
        object_info = f"""Cell Width: {self.cell_width}px
Horizontal Gap: {self.horizontal_gap}px
Cell Height: {self.cell_height}px
Vertical Gap: {self.vertical_gap}px"""
        self.ui.lblObjectParams.setText(object_info)

    def update_image_display(self):
        if not self.current_image or self.current_image.isNull():
            return
            
        label_rect = self.ui.imageLabel.rect()
        pixmap = QPixmap(label_rect.size())
        pixmap.fill(Qt.transparent)
        
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw image if exists
        scaled_image = self.current_image.scaled(
            label_rect.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        painter.drawImage(
            (label_rect.width() - scaled_image.width()) // 2,
            (label_rect.height() - scaled_image.height()) // 2,
            scaled_image
        )

        # Draw grid if enabled
        if self.show_grid:
            self.draw_grid(painter, label_rect)
            self.draw_grid_info(painter, label_rect)  # Add grid info display

        painter.end()
        self.ui.imageLabel.setPixmap(pixmap)

    def rotate_image(self):
        # Implementation for image rotation
        pass

    def flip_image(self):
        # Implementation for image flipping
        pass

    def crop_image(self):
        # Implementation for image cropping
        pass

    def apply_filters(self):
        pass

    def center_window(self):
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)