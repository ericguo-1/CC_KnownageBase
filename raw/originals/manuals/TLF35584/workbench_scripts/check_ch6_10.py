import os
import glob

div_dir = r"D:\GG\Doc_Dlod\UserMannual\TLF35584\div"

print("第6章和第10章转换结果检查:")
print("=" * 50)

chapters = ["06_Enable_Function", "10_Overcurrent_Protection"]

for chapter_name in chapters:
    chapter_path = os.path.join(div_dir, chapter_name)
    
    if not os.path.exists(chapter_path):
        print(f"❌ {chapter_name}: 目录不存在")
        continue
    
    md_files = glob.glob(os.path.join(chapter_path, "*.md"))
    json_files = glob.glob(os.path.join(chapter_path, "*.json"))
    image_files = glob.glob(os.path.join(chapter_path, "*.jpeg")) + glob.glob(os.path.join(chapter_path, "*.png"))
    
    print(f"章节: {chapter_name}")
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
            
            # 显示前几行内容预览
            print(f"  内容预览:")
            preview_lines = content.split('\n')[:5]
            for line in preview_lines:
                if line.strip():
                    print(f"    {line[:80]}")
    
    print()

print("=" * 50)
print("检查完成!")