import os
import glob
import pypdf

pdf_dir = r"D:\GG\Doc_Dlod\UserMannual\TLF35584\div"

print("页眉删除效果验证:")
print("=" * 70)

# 获取所有处理后的PDF文件
pdf_files = []
for i in range(1, 19):  # 1-18章
    pattern = os.path.join(pdf_dir, f"{i:02d}_*.pdf")
    matching_files = glob.glob(pattern)
    for pdf_file in sorted(matching_files):
        if os.path.isfile(pdf_file) and '_backup' not in pdf_file and '_test' not in pdf_file:
            pdf_files.append(pdf_file)

pdf_files.sort()

total_pic1_removed = 0
total_chapters = 0

for pdf_file in pdf_files:
    pdf_name = os.path.basename(pdf_file)
    
    try:
        reader = pypdf.PdfReader(pdf_file)
        page_count = len(reader.pages)
        
        # 检查对应的转换目录
        base_name = pdf_file.replace('.pdf', '')
        if os.path.exists(os.path.join(pdf_dir, base_name)):
            md_dir = os.path.join(pdf_dir, base_name)
            jpeg_files = glob.glob(os.path.join(md_dir, "*.jpeg"))
            png_files = glob.glob(os.path.join(md_dir, "*.png"))
            
            # 统计Picture_1图片
            pic1_files = [f for f in jpeg_files if 'Picture_1' in f]
            
            if pic1_files:
                print(f"{pdf_name:45} 页数: {page_count:2}  Picture_1: {len(pic1_files):2}个  状态: [X]仍有图标")
            else:
                print(f"{pdf_name:45} 页数: {page_count:2}  Picture_1: 0个  状态: [OK]图标已删除")
                total_pic1_removed += 1
            
            total_chapters += 1
            
    except Exception as e:
        print(f"{pdf_name:45} [ERROR] 验证失败: {e}")

print("=" * 70)
print(f"验证统计:")
print(f"  检查章节: {total_chapters} 个")
print(f"  图标已删除: {total_pic1_removed} 个")
if total_chapters > 0:
    print(f"  删除成功率: {total_pic1_removed/total_chapters*100:.1f}%")

# 统计所有中间文件
test_files = glob.glob(os.path.join(pdf_dir, "*_test_*.pdf"))
temp_backup_files = glob.glob(os.path.join(pdf_dir, "*_temp_backup.pdf"))
original_backup_files = glob.glob(os.path.join(pdf_dir, "*_backup.pdf"))

print(f"\n中间文件统计:")
print(f"  测试文件 (*_test_*.pdf): {len(test_files)} 个")
print(f"  临时备份 (*_temp_backup.pdf): {len(temp_backup_files)} 个")
print(f"  原始备份 (*_backup.pdf): {len(original_backup_files)} 个")
print(f"  中间文件总计: {len(test_files) + len(temp_backup_files)} 个")