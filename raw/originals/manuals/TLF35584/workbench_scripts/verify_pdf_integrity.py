import os
import glob
from pypdf import PdfReader

pdf_dir = r"D:\GG\Doc_Dlod\UserMannual\TLF35584\div"

print("PDF文件完整性验证:")
print("=" * 70)

# 获取所有PDF文件(排除备份文件)
pdf_files = []
for i in range(1, 19):  # 1-18章
    pattern = os.path.join(pdf_dir, f"{i:02d}_*.pdf")
    matching_files = glob.glob(pattern)
    for pdf_file in sorted(matching_files):
        if os.path.isfile(pdf_file) and not pdf_file.endswith('_backup.pdf'):
            pdf_files.append(pdf_file)

pdf_files.sort()

all_valid = True
total_pages = 0
total_size = 0

for pdf_file in pdf_files:
    pdf_name = os.path.basename(pdf_file)
    file_size = os.path.getsize(pdf_file) / 1024  # KB
    
    try:
        reader = PdfReader(pdf_file)
        page_count = len(reader.pages)
        
        # 检查页面是否完整
        is_encrypted = reader.is_encrypted
        
        print(f"{pdf_name:45} 页数: {page_count:3}  大小: {file_size:7.1f}KB  加密: {'是' if is_encrypted else '否'}")
        
        if is_encrypted:
            print(f"  [WARNING] PDF文件已加密!")
            all_valid = False
        
        total_pages += page_count
        total_size += file_size
        
    except Exception as e:
        print(f"{pdf_name:45} [ERROR] 文件损坏: {e}")
        all_valid = False

print("=" * 70)
print(f"验证统计:")
print(f"  文件总数: {len(pdf_files)}")
print(f"  总页数: {total_pages}")
print(f"  总大小: {total_size / 1024:.2f} MB")
print(f"  文件状态: {'全部正常' if all_valid else '存在问题'}")

# 检查备份文件
backup_files = glob.glob(os.path.join(pdf_dir, "*_backup.pdf"))
print(f"  备份文件: {len(backup_files)} 个")

# 随机检查一个备份文件的完整性
if backup_files:
    import random
    sample_backup = random.choice(backup_files)
    try:
        backup_reader = PdfReader(sample_backup)
        backup_pages = len(backup_reader.pages)
        print(f"\n随机检查备份文件: {os.path.basename(sample_backup)}")
        print(f"  备份页数: {backup_pages}")
        print(f"  [OK] 备份文件完整")
    except Exception as e:
        print(f"  [ERROR] 备份文件检查失败: {e}")

print("\n验证完成!")