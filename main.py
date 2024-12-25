import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
import cv2
import numpy as np
from tkinter import colorchooser
from tkinter import END
from tkinter import messagebox
from tkinter import simpledialog

class ImageProcessor:
    def __init__(self):
        self.window = ttk.Window(themename="litera")
        self.window.title("Xử lý Ảnh")
        
        # Thêm các biến khởi tạo cho lưới
        self.grid_visible = False
        self.grid_cells = []
        
        # Thêm dòng này ở đầu __init__
        style = ttk.Style()
        
        # Đặt kích thước cửa sổ bằng 80% màn hình và căn giữa
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Tạo frame chứa các nút với style mới
        button_frame = ttk.Frame(self.window, padding=10)
        button_frame.pack(fill=X, padx=20, pady=10)
        
        # Frame cho các nút chính
        main_buttons = ttk.Frame(button_frame)
        main_buttons.pack(fill=X)
        
        buttons_container = ttk.Frame(main_buttons)
        buttons_container.pack(anchor=CENTER, expand=True)
        
        # Cập nhật các nút với style của ttkbootstrap
        self.btn_choose = ttk.Button(
            buttons_container, 
            text="Chọn Ảnh",
            command=self.choose_image,
            bootstyle="primary",
            width=15
        )
        self.btn_choose.pack(side=LEFT, padx=5)
        
        self.btn_process = ttk.Button(
            buttons_container,
            text="Xử lý",
            command=self.process_image,
            bootstyle="success",
            width=15
        )
        self.btn_process.pack(side=LEFT, padx=5)
        
        self.btn_save = ttk.Button(
            buttons_container,
            text="Lưu Ảnh", 
            command=self.save_image,
            bootstyle="info",
            width=15
        )
        self.btn_save.pack(side=LEFT, padx=5)

        # Thêm nút tạo ô vuông vào buttons_container
        self.btn_create_box = ttk.Button(
            buttons_container,
            text="Tạo Ô Vuông",
            command=self.create_selection_box,
            bootstyle="warning",
            width=15
        )
        self.btn_create_box.pack(side=LEFT, padx=5)

        # Thêm nút Clone vào buttons_container
        self.btn_clone = ttk.Button(
            buttons_container,
            text="Nhân Bản",
            command=self.clone_boxes,
            bootstyle="secondary",
            width=15
        )
        self.btn_clone.pack(side=LEFT, padx=5)

        # Thêm nút Hiện Lưới vào đầu buttons_container
        self.btn_grid = ttk.Button(
            buttons_container,
            text="Hiện Lưới",
            command=self.toggle_grid,
            bootstyle="primary-outline",
            width=15
        )
        self.btn_grid.pack(side=LEFT, padx=5)

        # Cập nhật canvas frame với style mới
        self.canvas_frame = ttk.Frame(self.window, bootstyle="secondary")
        self.canvas_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
        
        # Canvas với màu nền mới
        self.canvas = tk.Canvas(self.canvas_frame, bg='#ffffff')
        
        # Thanh cuộn với style ttkbootstrap
        self.scrollbar_y = ttk.Scrollbar(
            self.canvas_frame,
            orient=VERTICAL,
            command=self.canvas.yview,
            bootstyle="round"
        )
        self.scrollbar_x = ttk.Scrollbar(
            self.canvas_frame,
            orient=HORIZONTAL,
            command=self.canvas.xview,
            bootstyle="round"
        )

        # Thanh cuộn với style mới
        style.configure("Custom.Vertical.TScrollbar", arrowsize=16)
        style.configure("Custom.Horizontal.TScrollbar", arrowsize=16)
        
        self.scrollbar_y.pack(side=RIGHT, fill=Y)
        
        self.scrollbar_x.pack(side=BOTTOM, fill=X)
        
        self.canvas.configure(xscrollcommand=self.scrollbar_x.set, 
                             yscrollcommand=self.scrollbar_y.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        
        # Thêm các biến offset cho ảnh
        self.image_offset_x = 0
        self.image_offset_y = 0
        
        # Biến để lưu trữ ảnh và tỷ lệ zoom
        self.image = None
        self.photo = None
        self.zoom_factor = 1.0
        
        # Bind sự kiện chuột để zoom
        self.canvas.bind("<MouseWheel>", self.mouse_wheel)
        
        # Thêm biến để theo dõi vùng được chọn
        self.start_x = None
        self.start_y = None
        self.rect_id = None
        self.selection = None
        
        # Bind các sự kiện chuột để vẽ khung chọn
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        
        # Thêm biến để theo dõi trạng thái kéo
        self.drag_start = None
        self.is_panning = False
        
        # Bind cc sự kiện mới
        self.canvas.bind("<Control-MouseWheel>", self.mouse_wheel)  # Zoom với Ctrl
        self.canvas.bind("<space>", self.start_pan_mode)  # Bắt đầu chế độ pan
        self.canvas.bind("<KeyRelease-space>", self.end_pan_mode)  # Kết thúc chế độ pan
        self.canvas.bind("<B1-Motion>", self.on_drag)  # Xử lý kéo
        self.canvas.focus_set()  # Cho phép canvas nhận input từ bàn phím
        
        # Tạo frame properties có thể toggle
        self.properties_frame = ttk.Frame(self.window)
        self.properties_visible = False  # Đặt trạng thái mặc định là ẩn
        
        # Nút toggle
        self.toggle_btn = ttk.Button(
            self.window,
            text="⚙",  # Unicode icon cho settings
            command=self.toggle_properties,
            bootstyle="secondary",
            width=3
        )
        self.toggle_btn.place(relx=0.97, rely=0.02)  # Đặt ở góc phải trên
        
        # Tiêu đề Properties
        ttk.Label(
            self.properties_frame,
            text="Properties",
            font=('Helvetica', 14, 'bold'),
            bootstyle="inverse-primary"
        ).pack(anchor=W, pady=(0, 10), fill=X)
        
        # Frame cho các thuộc tính với style mới
        props_frame = ttk.Frame(self.properties_frame)
        props_frame.pack(fill=X)
        
        # Font properties với style mới
        font_frame = ttk.Labelframe(
            props_frame,
            text="Font",
            padding=10,
            bootstyle="primary"
        )
        font_frame.pack(fill=X, pady=5)
        
        # Cập nhật các entry và label với style ttkbootstrap
        ttk.Label(font_frame, text="Family:", bootstyle="inverse").pack(anchor=W)
        self.font_family = ttk.Entry(
            font_frame,
            bootstyle="primary"
        )
        self.font_family.insert(0, "Roboto-Bold")
        self.font_family.pack(fill=X, pady=(0, 5))
        
        ttk.Label(font_frame, text="Size (px):", bootstyle="inverse").pack(anchor=W)
        self.font_size = ttk.Entry(
            font_frame,
            bootstyle="primary"
        )
        self.font_size.insert(0, "24")
        self.font_size.pack(fill=X, pady=(0, 5))
        
        color_container = ttk.Frame(font_frame)
        color_container.pack(fill=X)
        
        ttk.Label(color_container, text="Color:", bootstyle="inverse").pack(side=LEFT)
        
        # Frame chứa ô màu và nút
        color_input_frame = ttk.Frame(color_container)
        color_input_frame.pack(side=LEFT, fill=X, expand=True)
        
        self.font_color = ttk.Entry(
            color_input_frame,
            bootstyle="primary"
        )
        self.font_color.insert(0, "#272727")
        self.font_color.pack(side=LEFT, fill=X, expand=True)
        
        # Chỉ giữ lại nút color picker
        self.color_btn = ttk.Button(
            color_input_frame,
            text="🎨",
            command=self.pick_color,
            width=3,
            bootstyle="secondary-outline"
        )
        self.color_btn.pack(side=LEFT, padx=(5, 0))
        
        # Text properties với style mới
        text_frame = ttk.Labelframe(
            props_frame,
            text="Text",
            padding=10,
            bootstyle="primary"
        )
        text_frame.pack(fill=X, pady=5)
        
        ttk.Label(text_frame, text="Content:", bootstyle="inverse").pack(anchor=W)
        self.text_content = ttk.Entry(
            text_frame,
            bootstyle="primary"
        )
        self.text_content.insert(0, "10")
        self.text_content.pack(fill=X)
        
        # Thêm nút Apply
        self.apply_btn = ttk.Button(
            text_frame,
            text="Apply All",
            command=self.apply_to_all,
            bootstyle="primary-outline",
            width=10
        )
        self.apply_btn.pack(pady=(5,0))
        
        # Thêm biến để lưu trữ các vị trí của s 10
        self.number_positions = []
        
        # Thêm đường dẫn font vào properties
        self.font_path = "assets/fonts/Roboto-Bold.ttf"  # Đặt file font của bạn vào thư mục fonts
        
        # Thêm các biến mới để theo dõi trạng thái của ô vuông
        self.box_dragging = False
        self.box_resizing = False
        self.resize_handle = None
        self.default_box_size = 100  # Kích thước mặc định của ô vuông
        self.box_list = []  # Thêm dòng này

        # Bind các sự kiện mới
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.canvas.bind("<Motion>", self.on_motion)
        
        # Thêm các biến mặc định cho lưới
        self.grid_cols = 3
        self.grid_rows = 5
        self.cell_width = 180
        self.cell_height = 45
        self.horizontal_gap = 8
        self.vertical_gap = 60.5
    
    def mouse_wheel(self, event):
        if event.state & 0x4:  # Kiểm tra phím Ctrl
            # Xử lý zoom
            if event.delta > 0:
                self.zoom_in()
            else:
                self.zoom_out()
        else:
            # Cuộn dọc khi không nhấn Ctrl
            self.canvas.yview_scroll(-1 * (event.delta // 120), "units")
    
    def zoom_in(self):
        self.zoom_factor *= 1.1
        self.update_image()
    
    def zoom_out(self):
        self.zoom_factor *= 0.9
        self.update_image()
    
    def update_image(self):
        if self.image is not None:
            # Lưu trữ thông tin về lưới hiện tại
            grid_info = None
            if self.grid_visible:
                grid_info = [(self.canvas.coords(cell['id']), self.canvas.itemcget(cell['id'], 'outline'))
                            for cell in self.grid_cells]
            
            # Chuyển đổi ảnh OpenCV sang PIL Image
            img = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            
            # Tính kích thước mới dựa trên zoom_factor
            new_width = int(img.width * self.zoom_factor)
            new_height = int(img.height * self.zoom_factor)
            
            # Resize ảnh
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Chuyển đổi sang PhotoImage
            self.photo = ImageTk.PhotoImage(img)
            
            # Cập nhật canvas và căn giữa ảnh
            self.canvas.delete("all")
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            
            # Cập nhật offset
            self.image_offset_x = max(0, (canvas_width - new_width) // 2)
            self.image_offset_y = max(0, (canvas_height - new_height) // 2)
            
            # Vẽ ảnh với offset mới
            self.canvas.create_image(
                self.image_offset_x,
                self.image_offset_y,
                image=self.photo,
                anchor="nw"
            )
            
            # Khôi phục lưới nếu đang hiển thị
            if grid_info:
                self.grid_cells.clear()
                for coords, outline in grid_info:
                    cell = self.canvas.create_rectangle(
                        coords[0], coords[1], coords[2], coords[3],
                        outline=outline,
                        width=2,
                        tags='grid_cell'
                    )
                    self.grid_cells.append({
                        'id': cell,
                        'coords': coords
                    })
            
            # Cập nhật vùng scroll
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def choose_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff")]
        )
        if file_path:
            self.image = cv2.imread(file_path)
            self.zoom_factor = 1.0
            self.update_image()
    
    def on_press(self, event):
        """Xử lý khi nhấn chuột"""
        if self.is_panning:
            return

        canvas_x = self.canvas.canvasx(event.x)
        canvas_y = self.canvas.canvasy(event.y)

        # Kiểm tra xem có đang bấm vào handle không
        items = self.canvas.find_closest(canvas_x, canvas_y)
        if items and 'handle' in self.canvas.gettags(items[0]):
            self.box_resizing = True
            self.rect_id = None
            for rect, handle in self.box_list:
                if handle == items[0]:
                    self.rect_id = rect
                    break
            return

        # Kiểm tra xem có đang bấm vào ô vuông không
        items = self.canvas.find_overlapping(canvas_x-2, canvas_y-2, canvas_x+2, canvas_y+2)
        for item in items:
            if 'box' in self.canvas.gettags(item):
                self.box_dragging = True
                self.drag_start = (canvas_x, canvas_y)
                self.rect_id = item
                return
    
    def on_drag(self, event):
        """Xử lý khi kéo chuột"""
        if self.is_panning:
            # Xử lý pan mode
            self.canvas.scan_dragto(event.x, event.y, gain=1)
            return

        canvas_x = self.canvas.canvasx(event.x)
        canvas_y = self.canvas.canvasy(event.y)

        if self.box_dragging and self.rect_id:
            # Di chuyển ô vuông
            dx = canvas_x - self.drag_start[0]
            dy = canvas_y - self.drag_start[1]
            self.canvas.move(self.rect_id, dx, dy)
            self.canvas.move(self.resize_handle, dx, dy)
            self.drag_start = (canvas_x, canvas_y)
            self.update_selection()
            
            # Kiểm tra xem ô vuông có nằm trong vùng ảnh không
            box_coords = self.canvas.coords(self.rect_id)
            image_bounds = (
                self.image_offset_x,
                self.image_offset_y,
                self.image_offset_x + self.image.shape[1] * self.zoom_factor,
                self.image_offset_y + self.image.shape[0] * self.zoom_factor
            )
            
            # Nếu ô vuông nằm hoàn toàn trong vùng ảnh
            if (box_coords[0] >= image_bounds[0] and 
                box_coords[1] >= image_bounds[1] and 
                box_coords[2] <= image_bounds[2] and 
                box_coords[3] <= image_bounds[3]):
                # Highlight ô vuông bằng màu xanh
                self.canvas.itemconfig(self.rect_id, outline='green')
            else:
                # Đổi lỗi màu đỏ nếu ở ngoài
                self.canvas.itemconfig(self.rect_id, outline='red')

        elif self.box_resizing and self.rect_id:
            # Thay đổi kích thước ô vuông
            bbox = self.canvas.coords(self.rect_id)
            self.canvas.coords(self.rect_id, bbox[0], bbox[1], canvas_x, canvas_y)
            self.canvas.coords(self.resize_handle,
                             canvas_x - 5, canvas_y - 5,
                             canvas_x + 5, canvas_y + 5)
            self.update_selection()
    
    def update_selection(self):
        """Cập nhật selection dựa trên vị trí hiện tại của ô vuông"""
        if self.rect_id:
            bbox = self.canvas.coords(self.rect_id)
            self.selection = (
                int((bbox[0] - self.image_offset_x) / self.zoom_factor),
                int((bbox[1] - self.image_offset_y) / self.zoom_factor),
                int((bbox[2] - self.image_offset_x) / self.zoom_factor),
                int((bbox[3] - self.image_offset_y) / self.zoom_factor)
            )
    
    def on_release(self, event):
        """Xử lý khi thả chuột"""
        if self.rect_id and self.box_dragging:
            # Kiểm tra xem ô vuông có nằm trong vùng ảnh không
            box_coords = self.canvas.coords(self.rect_id)
            image_bounds = (
                self.image_offset_x,
                self.image_offset_y,
                self.image_offset_x + self.image.shape[1] * self.zoom_factor,
                self.image_offset_y + self.image.shape[0] * self.zoom_factor
            )
            
            # Nếu ô vuông nằm hoàn toàn trong vùng ảnh
            if (box_coords[0] >= image_bounds[0] and 
                box_coords[1] >= image_bounds[1] and 
                box_coords[2] <= image_bounds[2] and 
                box_coords[3] <= image_bounds[3]):
                # Chỉ cập nhật selection mà không xử lý
                self.update_selection()
                # Đổi màu thành xanh để chỉ báo vị trí hợp lệ
                self.canvas.itemconfig(self.rect_id, outline='green')
        
        self.box_dragging = False
        self.box_resizing = False

    def process_image(self, save_position=True):
        if self.image is None or self.selection is None:
            return
        
        # Hiển thị dialog nhập số
        text = simpledialog.askstring("Nhập số", "Vui lòng nhập số:")
        if text is None:  # Người dùng bấm Cancel
            return
        
        # Cập nhật text_content
        self.text_content.delete(0, END)
        self.text_content.insert(0, text)
        
        # Highlight vùng được chọn
        x1, y1, x2, y2 = self.selection
        highlight = self.canvas.create_rectangle(
            x1 * self.zoom_factor + self.image_offset_x,
            y1 * self.zoom_factor + self.image_offset_y,
            x2 * self.zoom_factor + self.image_offset_x,
            y2 * self.zoom_factor + self.image_offset_y,
            outline='cyan',
            width=2
        )
        self.window.update()
        self.window.after(1000, lambda: self.canvas.delete(highlight))
        
        width = x2 - x1
        height = y2 - y1
        
        cv2.rectangle(self.image, (x1, y1), (x2, y2), (255,255,255), -1)
        
        font_size = int(self.font_size.get())
        color = tuple(int(self.font_color.get().lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        
        try:
            # Tạo ảnh tạm với kích thước vùng được chọn
            temp_img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
            draw = ImageDraw.Draw(temp_img)
            
            # Xử lý text đơn giản hơn
            x_offset = 0
            # Tính tổng chiều rộng của text
            font = ImageFont.truetype(self.font_path, font_size)
            total_width = draw.textbbox((0, 0), text, font=font)[2]
            x_offset = (width - total_width) // 2
            
            # Tính chiều cao của text
            text_height = draw.textbbox((0, 0), text, font=font)[3]
            y_pos = (height - text_height) // 2
            
            # Vẽ toàn bộ text một lần
            draw.text((x_offset, y_pos), text, font=font, fill=color[::-1] + (255,))
            
            # Chuyển đổi sang numpy array
            temp_array = np.array(temp_img)
            b, g, r, a = cv2.split(temp_array)
            temp_bgr = cv2.merge([b, g, r])
            mask = a / 255.0
            
            # Đặt text lên ảnh gốc
            roi = self.image[y1:y2, x1:x2]
            for c in range(3):
                roi[:, :, c] = roi[:, :, c] * (1 - mask) + temp_bgr[:, :, c] * mask
            
            self.image[y1:y2, x1:x2] = roi
            
        except Exception as e:
            print(f"Lỗi khi xử lý font: {e}")
            # Fallback về phương thức cũ nếu có lỗi
            
        if save_position:
            self.number_positions.append(self.selection)
        self.selection = None
        if self.rect_id:
            self.canvas.delete(self.rect_id)
            
        self.update_image()
    
    def start_pan_mode(self, event):
        self.is_panning = True
        self.canvas.config(cursor="hand2")

    def end_pan_mode(self, event):
        self.is_panning = False
        self.canvas.config(cursor="")
        self.drag_start = None

    def save_image(self):
        if self.image is None:
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            cv2.imwrite(file_path, self.image)
    
    def toggle_properties(self):
        """Toggle hiển thị/ẩn properties panel"""
        if self.properties_visible:
            self.properties_frame.place_forget()
            self.properties_visible = False
        else:
            self.properties_frame.place(
                relx=0.75,
                rely=0,
                relwidth=0.25,
                relheight=1
            )
            self.properties_visible = True
    
    def run(self):
        self.window.mainloop()
    
    def apply_to_all(self):
        """Áp dụng text mới cho tất cả các số đã thêm"""
        if not self.number_positions or self.image is None:
            return
            
        # Lưu selection hiện tại
        current_selection = self.selection
        positions = self.number_positions.copy()
        
        # Xử lý từng vị trí
        for pos in positions:
            self.selection = pos
            self.process_image(save_position=False)  # Sẽ hiển thị dialog cho mỗi ô
            
        # Khôi phục selection
        self.selection = current_selection
        
        # Cập nhật hiển thị
        self.update_image()
    
    def pick_color(self):
        """Mở color picker dialog"""
        color = colorchooser.askcolor(self.font_color.get())
        if color[1]:  # Nếu người dùng không bấm Cancel
            self.font_color.delete(0, END)
            self.font_color.insert(0, color[1])
    
    def create_selection_box(self):
        """Tạo một ô chữ nhật mới ở giữa canvas"""
        if self.image is None:
            return

        # Lấy kích thước từ ô trước đó nếu có
        if self.number_positions:  # Kiểm tra xem có vị trí đã xử lý nào không
            last_box = self.number_positions[-1]  # Lấy vị trí cuối cùng
            width = last_box[2] - last_box[0]  # Lấy width thực tế
            height = last_box[3] - last_box[1]  # Lấy height thực tế
            # Nhân với zoom_factor sau khi có kích thước thực
            scaled_width = width * self.zoom_factor
            scaled_height = height * self.zoom_factor
        else:
            scaled_width = self.default_box_size * self.zoom_factor
            scaled_height = self.default_box_size * self.zoom_factor

        # Xóa ô cũ nếu có
        if self.rect_id:
            self.canvas.delete(self.rect_id)
            self.canvas.delete(self.resize_handle)
            self.box_list = []  # Reset danh sách

        # Tính toán vị trí giữa canvas
        center_x = self.image_offset_x + (self.image.shape[1] * self.zoom_factor) / 2
        center_y = self.image_offset_y + (self.image.shape[0] * self.zoom_factor) / 2

        # Tạo ô chữ nhật mới
        x1 = center_x - scaled_width/2
        y1 = center_y - scaled_height/2
        x2 = center_x + scaled_width/2
        y2 = center_y + scaled_height/2

        self.rect_id = self.canvas.create_rectangle(
            x1, y1, x2, y2,
            outline='red',
            width=2,
            tags=('box', 'draggable')
        )

        # Tạo handle để resize
        self.create_resize_handle(x2, y2)

        # Cập nhật selection
        self.selection = (
            int((x1 - self.image_offset_x) / self.zoom_factor),
            int((y1 - self.image_offset_y) / self.zoom_factor),
            int((x2 - self.image_offset_x) / self.zoom_factor),
            int((y2 - self.image_offset_y) / self.zoom_factor)
        )
        
        # Thêm ô vào danh sách
        self.box_list.append((self.rect_id, self.resize_handle))
    
    def create_resize_handle(self, x, y):
        """Tạo handle để resize ở góc phải dưới"""
        size = 10
        if self.resize_handle:
            self.canvas.delete(self.resize_handle)
        self.resize_handle = self.canvas.create_rectangle(
            x - size/2, y - size/2,
            x + size/2, y + size/2,
            fill='red',
            tags=('handle', 'draggable')
        )

    def on_motion(self, event):
        """X lý khi di chuyển chut"""
        if self.rect_id:
            canvas_x = self.canvas.canvasx(event.x)
            canvas_y = self.canvas.canvasy(event.y)
            
            # Kiểm tra xem chuột có gần handle không
            handle_bbox = self.canvas.bbox(self.resize_handle)
            if handle_bbox:
                if (abs(canvas_x - handle_bbox[0]) < 10 and 
                    abs(canvas_y - handle_bbox[1]) < 10):
                    self.canvas.config(cursor="sizing")
                    return
            
            # Kiểm tra xem chuột có nằm trên ô vuông không
            items = self.canvas.find_overlapping(canvas_x-2, canvas_y-2, canvas_x+2, canvas_y+2)
            for item in items:
                if 'box' in self.canvas.gettags(item):
                    self.canvas.config(cursor="fleur")  # Con trỏ di chuyển
                    return
            
            self.canvas.config(cursor="")  # Con trỏ mặc định

    def clone_boxes(self):
        """Nhân bản ô vuông hiện tại"""
        if not self.rect_id:
            messagebox.showwarning("Cảnh báo", "Vui lòng tạo ô vuông trước!")
            return
        
        try:
            # Sửa dòng này: thay ttk.askstring bằng simpledialog.askstring
            num_copies = simpledialog.askstring("Nhân bản", "Nhập số lượng cần nhân bản:")
            if num_copies is None:  # Người dùng bấm Cancel
                return
            
            num_copies = int(num_copies)
            if num_copies <= 0:
                raise ValueError
            
            # Lấy kích thước và v trí của ô vuông gốc
            bbox = self.canvas.coords(self.rect_id)
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]
            
            # Clone các ô vuông mới
            for i in range(num_copies):
                # Tạo vị trí mới, dịch xuống dưới một chút
                x1 = bbox[0] + (i + 1) * 20
                y1 = bbox[1] + (i + 1) * 20
                x2 = x1 + width
                y2 = y1 + height
                
                # Tạo ô vuông mới
                new_rect = self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    outline='red',
                    width=2,
                    tags=('box', 'draggable')
                )
                
                # Tạo handle mới
                new_handle = self.canvas.create_rectangle(
                    x2 - 5, y2 - 5,
                    x2 + 5, y2 + 5,
                    fill='red',
                    tags=('handle', 'draggable')
                )
                
                # Lưu vào danh sách
                self.box_list.append((new_rect, new_handle))
                
                # Tạo selection mới
                new_selection = (
                    int((x1 - self.image_offset_x) / self.zoom_factor),
                    int((y1 - self.image_offset_y) / self.zoom_factor),
                    int((x2 - self.image_offset_x) / self.zoom_factor),
                    int((y2 - self.image_offset_y) / self.zoom_factor))
                
                self.number_positions.append(new_selection)
                
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số dương hợp lệ!")

    def toggle_grid(self):
        """Bật/tắt hiển thị lưới"""
        if self.image is None:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn ảnh trước!")
            return

        if not self.grid_visible:
            # Tạo dialog để nhập thông số
            dialog = ttk.Toplevel(self.window)
            dialog.title("Thông số lưới")
            
            # Đặt kích thước lớn hơn cho dialog
            dialog_width = 500
            dialog_height = 700
            
            # Lấy kích thước màn hình
            screen_width = self.window.winfo_screenwidth()
            screen_height = self.window.winfo_screenheight()
            
            # Tính toán vị trí để dialog nằm giữa màn hình
            x = (screen_width - dialog_width) // 2
            y = (screen_height - dialog_height) // 2
            
            # Đặt kích thước và vị trí cho dialog
            dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")
            
            # Tạo frame chính với padding
            main_frame = ttk.Frame(dialog, padding="20")
            main_frame.pack(fill='both', expand=True)
            
            # Tạo các biến để lưu giá trị
            cols_var = tk.StringVar(value="3")
            rows_var = tk.StringVar(value="10")
            width_var = tk.StringVar(value="175")
            height_var = tk.StringVar(value="40")
            h_gap_var = tk.StringVar(value="18")
            v_gap_var = tk.StringVar(value="60.5")
            
            # Tạo các label và entry với font size lớn hơn và padding
            style = ttk.Style()
            style.configure("Large.TLabel", font=("Helvetica", 12))
            style.configure("Large.TEntry", font=("Helvetica", 12))
            
            # Tạo các label và entry
            ttk.Label(main_frame, text="Số cột:", style="Large.TLabel").pack(pady=10)
            cols_entry = ttk.Entry(main_frame, textvariable=cols_var, width=30)
            cols_entry.pack(pady=5)
            
            ttk.Label(main_frame, text="Số hàng:", style="Large.TLabel").pack(pady=10)
            rows_entry = ttk.Entry(main_frame, textvariable=rows_var, width=30)
            rows_entry.pack(pady=5)
            
            ttk.Label(main_frame, text="Chiều rộng mỗi cột (px):", style="Large.TLabel").pack(pady=10)
            width_entry = ttk.Entry(main_frame, textvariable=width_var, width=30)
            width_entry.pack(pady=5)
            
            ttk.Label(main_frame, text="Chiều cao mỗi cột (px):", style="Large.TLabel").pack(pady=10)
            height_entry = ttk.Entry(main_frame, textvariable=height_var, width=30)
            height_entry.pack(pady=5)
            
            ttk.Label(main_frame, text="Khoảng cách ngang (px):", style="Large.TLabel").pack(pady=10)
            h_gap_entry = ttk.Entry(main_frame, textvariable=h_gap_var, width=30)
            h_gap_entry.pack(pady=5)
            
            ttk.Label(main_frame, text="Khoảng cách dọc (px):", style="Large.TLabel").pack(pady=10)
            v_gap_entry = ttk.Entry(main_frame, textvariable=v_gap_var, width=30)
            v_gap_entry.pack(pady=5)
            
            def apply_settings():
                try:
                    # Lưu các giá trị vào biến instance
                    self.grid_cols = int(cols_var.get())
                    self.grid_rows = int(rows_var.get())
                    self.cell_width = int(width_var.get())
                    self.cell_height = int(height_var.get())
                    self.horizontal_gap = int(h_gap_var.get())
                    self.vertical_gap = float(v_gap_var.get())
                    
                    dialog.destroy()
                    self.grid_visible = True
                    self.show_grid()
                    self.btn_grid.configure(text="Ẩn Lưới")
                    
                except ValueError:
                    messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")
            
            # Nút Apply lớn hơn
            ttk.Button(
                main_frame,
                text="Áp dụng",
                command=apply_settings,
                bootstyle="primary",
                width=20
            ).pack(pady=30)
            
            # Đặt dialog ở giữa cửa sổ chính
            dialog.transient(self.window)
            dialog.grab_set()
            
        else:
            self.grid_visible = False
            self.hide_grid()
            self.btn_grid.configure(text="Hiện Lưới")

    def show_grid(self):
        """Hiển thị lưới"""
        # Xóa lưới cũ nếu có
        self.hide_grid()
        
        # Sử dụng các thông số đã được cấu hình
        cell_width = self.cell_width * self.zoom_factor
        cell_height = self.cell_height * self.zoom_factor
        horizontal_gap = self.horizontal_gap * self.zoom_factor
        vertical_gap = self.vertical_gap * self.zoom_factor
        
        # Tính toán chiều cao tổng của lưới
        total_height = self.grid_rows * (cell_height + vertical_gap) - vertical_gap
        
        # Vẽ lưới với số cột và hàng đã cấu hình
        for row in range(self.grid_rows):
            for col in range(self.grid_cols):
                x1 = self.image_offset_x + col * (cell_width + horizontal_gap)
                y1 = self.image_offset_y + row * (cell_height + vertical_gap)
                x2 = x1 + cell_width
                y2 = y1 + cell_height
                
                cell = self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    outline='red',
                    width=2,
                    tags='grid_cell'
                )
                
                self.grid_cells.append({
                    'id': cell,
                    'row': row,
                    'col': col,
                    'coords': (x1, y1, x2, y2)
                })
                
                # Thêm đường line dọc màu xanh đi qua tâm của mỗi ô
                if row == 0:  # Chỉ vẽ line ở hàng đầu tiên
                    # Tính toán tâm điểm của ô
                    center_x = x1 + cell_width/2
                    
                    self.canvas.create_line(
                        center_x, self.image_offset_y, 
                        center_x, self.image_offset_y + total_height,
                        fill='blue',
                        width=1,
                        tags=('grid_line', 'grid_cell')
                    )
        
        # Bind các sự kiện cho canvas
        self.canvas.bind('<ButtonPress-1>', self.on_grid_press)
        self.canvas.bind('<B1-Motion>', self.on_grid_drag)
        self.canvas.bind('<ButtonRelease-1>', self.on_grid_release)

    def hide_grid(self):
        """Ẩn lưới"""
        self.canvas.delete('grid_cell')
        self.canvas.delete('grid_line')  # Thêm xóa các đường line
        self.grid_cells.clear()

    def on_grid_press(self, event):
        """Xử lý khi nhấn chuột"""
        if not self.grid_visible:
            return
        
        # Lấy tọa độ click
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        
        # Kiểm tra xem có click vào ô lưới không
        items = self.canvas.find_overlapping(x-2, y-2, x+2, y+2)
        for item in items:
            if 'grid_cell' in self.canvas.gettags(item):
                self.grid_drag_start = (x, y)
                return

    def on_grid_drag(self, event):
        """Xử lý khi kéo lưới"""
        if not self.grid_visible or self.grid_drag_start is None:
            return
        
        # Tính khoảng cách di chuyển
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        dx = x - self.grid_drag_start[0]
        dy = y - self.grid_drag_start[1]
        
        # Di chuyển tất cả các ô lưới
        self.canvas.move('grid_cell', dx, dy)
        
        # Cập nhật tọa độ cho tất cả các ô
        for cell in self.grid_cells:
            x1, y1, x2, y2 = cell['coords']
            cell['coords'] = (x1 + dx, y1 + dy, x2 + dx, y2 + dy)
        
        # Cập nhật vị trí bắt đầu
        self.grid_drag_start = (x, y)

    def on_grid_release(self, event):
        """Xử lý khi thả chuột"""
        if not self.grid_visible or self.grid_drag_start is None:
            return
        
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        dx = abs(x - self.grid_drag_start[0])
        dy = abs(y - self.grid_drag_start[1])
        
        if dx < 5 and dy < 5:
            items = self.canvas.find_overlapping(x-2, y-2, x+2, y+2)
            for item in items:
                if 'grid_cell' in self.canvas.gettags(item):
                    # Lưu vị trí hiện tại của tất cả các ô lưới và đường line
                    current_grid_positions = []
                    current_line_positions = []
                    
                    for cell in self.grid_cells:
                        coords = self.canvas.coords(cell['id'])
                        current_grid_positions.append(coords)
                    
                    # Lưu vị trí của các đường line
                    for line in self.canvas.find_withtag('grid_line'):
                        coords = self.canvas.coords(line)
                        current_line_positions.append(coords)
                    
                    # Hiển thị dialog nhập số
                    text = simpledialog.askstring("Nhập số", "Vui lòng nhập số:")
                    if text is not None:
                        for cell in self.grid_cells:
                            if cell['id'] == item:
                                # Highlight ô được chọn
                                self.canvas.itemconfig(item, outline='cyan', width=2)
                                
                                # Lấy tọa độ hiện tại của ô
                                current_coords = self.canvas.coords(item)
                                selection = (
                                    int((current_coords[0] - self.image_offset_x) / self.zoom_factor),
                                    int((current_coords[1] - self.image_offset_y) / self.zoom_factor),
                                    int((current_coords[2] - self.image_offset_x) / self.zoom_factor),
                                    int((current_coords[3] - self.image_offset_y) / self.zoom_factor))
                                
                                # Vẽ hình chữ nhật trắng
                                cv2.rectangle(
                                    self.image,
                                    (selection[0], selection[1]),
                                    (selection[2], selection[3]),
                                    (255, 255, 255),
                                    -1
                                )
                                
                                # Chuẩn bị để vẽ text
                                font_size = int(self.font_size.get())
                                color = tuple(int(self.font_color.get().lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
                                
                                # Tạo ảnh tạm với kích thước vùng được chọn
                                width = selection[2] - selection[0]
                                height = selection[3] - selection[1]
                                temp_img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
                                draw = ImageDraw.Draw(temp_img)
                                
                                # Xử lý text
                                font = ImageFont.truetype(self.font_path, font_size)
                                total_width = draw.textbbox((0, 0), text, font=font)[2]
                                text_height = draw.textbbox((0, 0), text, font=font)[3]
                                
                                x_offset = (width - total_width) // 2
                                y_pos = (height - text_height) // 2
                                
                                # Vẽ text
                                draw.text((x_offset, y_pos), text, font=font, fill=color[::-1] + (255,))
                                
                                # Chuyển đổi và áp dụng lên ảnh gốc
                                temp_array = np.array(temp_img)
                                b, g, r, a = cv2.split(temp_array)
                                temp_bgr = cv2.merge([b, g, r])
                                mask = a / 255.0
                                
                                roi = self.image[selection[1]:selection[3], selection[0]:selection[2]]
                                for c in range(3):
                                    roi[:, :, c] = roi[:, :, c] * (1 - mask) + temp_bgr[:, :, c] * mask
                                
                                self.image[selection[1]:selection[3], selection[0]:selection[2]] = roi
                                
                                # Cập nhật hiển thị
                                self.update_image()
                                
                                # Khôi phục lưới
                                self.show_grid()
                                
                                # Khôi phục vị trí cho từng ô
                                for i, cell in enumerate(self.grid_cells):
                                    if i < len(current_grid_positions):
                                        self.canvas.coords(cell['id'], *current_grid_positions[i])
                                
                                # Khôi phục vị trí cho các đường line
                                lines = self.canvas.find_withtag('grid_line')
                                for i, line in enumerate(lines):
                                    if i < len(current_line_positions):
                                        self.canvas.coords(line, *current_line_positions[i])
                                
                                # Reset highlight sau 500ms
                                self.canvas.after(500, lambda: self.canvas.itemconfig(item, outline='red', width=2))
                                break
        
        self.grid_drag_start = None

if __name__ == "__main__":
    app = ImageProcessor()
    app.run()
