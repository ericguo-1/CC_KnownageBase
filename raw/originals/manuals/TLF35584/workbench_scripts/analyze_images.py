import os
from PIL import Image

chapter_dir = r"D:\GG\Doc_Dlod\UserMannual\TLF35584\div\05_Wake_Function"

print("第5章图片分析:")
print("=" * 50)

# 查找所有Picture_1图片
picture_1_files = []
for file in os.listdir(chapter_dir):
    if file.startswith("_page_") and file.endswith("_Picture_1.jpeg"):
        picture_1_files.append(file)

picture_1_files.sort()

print(f"找到 {len(picture_1_files)} 个Picture_1图片:")
print()

for img_file in picture_1_files:
    img_path = os.path.join(chapter_dir, img_file)
    
    # 获取图片信息
    try:
        with Image.open(img_path) as img:
            width, height = img.size
            mode = img.mode
            size_kb = os.path.getsize(img_path) / 1024
            
            print(f"文件: {img_file}")
            print(f"  尺寸: {width}x{height}")
            print(f"  模式: {mode}")
            print(f"  大小: {size_kb:.2f} KB")
            print(f"  位置: 第{img_file.split('_')[1]}页")
            
            # 简单分析: 如果图片很小且是正方形,可能是图标
            if width == height and width < 100:
                print(f"  判断: 可能是图标 (小正方形)")
            elif width < 200 and height < 200:
                print(f"  判断: 可能是图标 (小尺寸)")
            else:
                print(f"  判断: 可能是内容图片")
            print()
            
    except Exception as e:
        print(f"无法分析 {img_file}: {e}")
        print()

print("=" * 50)
print("分析完成!")