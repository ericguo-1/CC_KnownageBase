import os
import glob
import shutil

base_dir = r"D:\GG\Doc_Dlod\UserMannual\TLF35584\div"

print("合并第11章分段转换结果...")
print("=" * 60)

# 查找所有分段目录
part_dirs = []
for i in range(1, 10):
    part_dir = os.path.join(base_dir, f"11_State_Machine_part{i}")
    if os.path.exists(part_dir):
        part_dirs.append(part_dir)

print(f"找到 {len(part_dirs)} 个分段目录:")
for i, part_dir in enumerate(part_dirs, 1):
    print(f"  {i}. {os.path.basename(part_dir)}")

# 创建合并后的目录
merged_dir = os.path.join(base_dir, "11_State_Machine")
if os.path.exists(merged_dir):
    shutil.rmtree(merged_dir)
os.makedirs(merged_dir)

print(f"\n创建合并目录: {os.path.basename(merged_dir)}")

# 合并MD文件
print("\n合并Markdown文件...")
merged_md = []
for part_dir in part_dirs:
    md_file = os.path.join(part_dir, f"{os.path.basename(part_dir)}.md")
    if os.path.exists(md_file):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            merged_md.append(content)
            print(f"  [MERGED] {os.path.basename(md_file)}")

# 保存合并后的MD文件
merged_md_file = os.path.join(merged_dir, "11_State_Machine.md")
with open(merged_md_file, 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(merged_md))

print(f"\n[SAVED] 合并后的MD文件: {os.path.basename(merged_md_file)}")

# 复制所有图片文件
print("\n复制图片文件...")
image_count = 0
for part_dir in part_dirs:
    # 复制JPEG文件
    jpeg_files = glob.glob(os.path.join(part_dir, "*.jpeg"))
    for jpeg_file in jpeg_files:
        dest_file = os.path.join(merged_dir, os.path.basename(jpeg_file))
        if not os.path.exists(dest_file):
            shutil.copy2(jpeg_file, dest_file)
            image_count += 1
    
    # 复制PNG文件
    png_files = glob.glob(os.path.join(part_dir, "*.png"))
    for png_file in png_files:
        dest_file = os.path.join(merged_dir, os.path.basename(png_file))
        if not os.path.exists(dest_file):
            shutil.copy2(png_file, dest_file)
            image_count += 1

print(f"  [COPIED] {image_count} 个图片文件")

# 复制JSON文件
print("\n复制JSON文件...")
json_count = 0
for part_dir in part_dirs:
    json_files = glob.glob(os.path.join(part_dir, "*.json"))
    for json_file in json_files:
        dest_file = os.path.join(merged_dir, os.path.basename(json_file))
        if not os.path.exists(dest_file):
            shutil.copy2(json_file, dest_file)
            json_count += 1

print(f"  [COPIED] {json_count} 个JSON文件")

print("\n" + "=" * 60)
print("合并完成!")
print(f"合并目录: {merged_dir}")
print(f"MD文件: 1个")
print(f"图片文件: {image_count}个")
print(f"JSON文件: {json_count}个")