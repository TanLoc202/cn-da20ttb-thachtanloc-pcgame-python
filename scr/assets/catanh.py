from PIL import Image

#--------------------------------------------------------
# Mở ảnh ĐẦU VÀO
img = Image.open("SRC/assets/image/background.png")
img1 = img.crop((0, 0, 160, 160))  # cắt lấy phần góc trên bên trái 256x256
img1.save('SRC/assets/image/ưall1.png')
#--------------------------------------------------------


#--------------------------------------------------------
# 📌 Tạo ảnh nền mới để ghép tile
canvas = Image.new("RGBA", (64, 64), (0, 0, 0, 0))  # ảnh rỗng 256x256


