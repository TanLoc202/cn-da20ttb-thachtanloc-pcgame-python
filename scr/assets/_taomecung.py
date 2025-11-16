import random
import numpy as np

# Đặt kích thước
HEIGHT = 51
WIDTH = 51

# 1. Bắt đầu với một ma trận toàn tường (số 1)
maze = np.ones((HEIGHT, WIDTH), dtype=int)

# Dùng một stack (ngăn xếp) để lưu đường đi cho việc "lùi lại"
stack = []

# 2. Chọn ô bắt đầu (0, 0)
start_x, start_y = 1, 1
maze[start_y, start_x] = 0
stack.append((start_x, start_y))

while stack:
    # Lấy ô hiện tại (ô trên cùng của stack)
    cx, cy = stack[-1]
    
    # 3. Tìm các hàng xóm (cách 2 ô) chưa được thăm
    neighbors = []
    # (dx, dy) là hướng di chuyển
    for (dx, dy) in [(0, -2), (0, 2), (-2, 0), (2, 0)]:
        nx, ny = cx + dx, cy + dy
        
        # Kiểm tra xem hàng xóm có nằm trong biên không
        if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
            # Và kiểm tra xem nó có phải là tường (1) không
            if maze[ny, nx] == 1:
                neighbors.append((nx, ny))

    if neighbors:
        # 4. Chọn ngẫu nhiên một hàng xóm
        nx, ny = random.choice(neighbors)
        
        # Tính toán vị trí của "tường" nằm giữa ô hiện tại và hàng xóm
        wall_x, wall_y = (cx + nx) // 2, (cy + ny) // 2
        
        # Đào tường
        maze[wall_y, wall_x] = 0
        # Đào ô hàng xóm
        maze[ny, nx] = 0
        
        # Đẩy ô hàng xóm vào stack để tiếp tục từ đó
        stack.append((nx, ny))
    else:
        # 5. Nếu bị kẹt (không còn hàng xóm), "lùi lại"
        stack.pop()

print(maze.tolist())  # In ra mê cung dưới dạng danh sách để dễ đọc hơn