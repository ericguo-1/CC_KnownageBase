import os
import glob

div_dir = r"D:\GG\Doc_Dlod\UserMannual\TLF35584\div"

print("转换结果检查:")
print("=" * 50)

# 查找所有转换后的目录
converted_dirs = []
for i in range(1, 11):  # 检查1-10章节
    pattern = os.path.join(div_dir, f"{i:02d}_*")
    matching_dirs = glob.glob(pattern)
    for dir_path in matching_dirs:
        if os.path.isdir(dir_path):
            converted_dirs.append(os.path.basename(dir_path))

converted_dirs.sort()

print(f"找到 {len(converted_dirs)} 个转换后的章节:")
print()

for chapter_dir in converted_dirs:
    chapter_path = os.path.join(div_dir, chapter_dir)
    md_files = glob.glob(os.path.join(chapter_path, "*.md"))
    json_files = glob.glob(os.path.join(chapter_path, "*.json"))
    image_files = glob.glob(os.path.join(chapter_path, "*.jpeg")) + glob.glob(os.path.join(chapter_path, "*.png"))

    print(f"章节: {chapter_dir}")
    print(f"  MD文件: {len(md_files)} 个")
    print(f"  JSON文件: {len(json_files)} 个")
    print(f"  图片文件: {len(image_files)} 个")

    # 检查MD文件内容
    if md_files:
        md_file = md_files[0]
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = len(content.split('\n'))
            chars = len(content)
            print(f"  MD内容: {lines} 行, {chars} 字符")

            # 检查是否包含重要内容
            has_title = '#' in content
            has_table = '|' in content
            has_image = '![](' in content

            print(f"  包含标题: {'是' if has_title else '否'}")
            print(f"  包含表格: {'是' if has_table else '否'}")
            print(f"  包含图片: {'是' if has_image else '否'}")

    print()

print("=" * 50)
print("检查完成!")