import os
import glob

div_dir = r"D:\GG\Doc_Dlod\UserMannual\TLF35584\div"

print("各章节Picture_1图标占比分析:")
print("=" * 70)

# 获取所有章节目录
chapters = []
for i in range(1, 15):  # 1-14章
    pattern = os.path.join(div_dir, f"{i:02d}_*")
    matching_dirs = glob.glob(pattern)
    for dir_path in sorted(matching_dirs):
        if os.path.isdir(dir_path):
            chapters.append(os.path.basename(dir_path))

chapters.sort()

total_pic1 = 0
total_images = 0

for chapter in chapters:
    chapter_path = os.path.join(div_dir, chapter)
    
    # 统计Picture_1图片
    pic1_files = glob.glob(os.path.join(chapter_path, "*Picture_1.jpeg"))
    # 统计所有图片
    all_images = glob.glob(os.path.join(chapter_path, "*.jpeg")) + glob.glob(os.path.join(chapter_path, "*.png"))
    
    pic1_count = len(pic1_files)
    total_count = len(all_images)
    
    if total_count > 0:
        ratio = (pic1_count / total_count) * 100
    else:
        ratio = 0
    
    total_pic1 += pic1_count
    total_images += total_count
    
    print(f"{chapter:40} Picture_1: {pic1_count:2}个  总图片: {total_count:2}个  占比: {ratio:5.1f}%")

print("=" * 70)
print(f"总计: {total_pic1}个Picture_1图标 / {total_images}个总图片 ({total_pic1/total_images*100:.1f}%)")

# 估算时间影响
print(f"\n时间影响分析:")
print(f"如果每个Picture_1图标处理时间约30秒:")
print(f"  浪费时间: {total_pic1 * 30} 秒 = {total_pic1 * 30 / 60:.1f} 分钟")
print(f"  对于244页PDF,可能有244个这样的图标!")
print(f"  预计浪费: {244 * 30 / 3600:.1f} 小时")