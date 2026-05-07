import os
import glob
from pypdf import PdfReader, PdfWriter

pdf_dir = r"D:\GG\Doc_Dlod\UserMannual\TLF35584\div"

print("开始删除其他PDF页眉区域 (跳过01_Overview)...")
print("=" * 60)

# 获取所有PDF文件(排除01_Overview和备份文件)
pdf_files = []
for i in range(2, 19):  # 2-18章
    pattern = os.path.join(pdf_dir, f"{i:02d}_*.pdf")
    matching_files = glob.glob(pattern)
    for pdf_file in sorted(matching_files):
        if os.path.isfile(pdf_file) and not '_backup' in pdf_file and '_test' not in pdf_file:
            pdf_files.append(pdf_file)

pdf_files.sort()

processed_count = 0
failed_count = 0

for pdf_file in pdf_files:
    pdf_name = os.path.basename(pdf_file)
    print(f"[PROCESSING] 处理: {pdf_name}")
    
    try:
        # 备份原始文件
        backup_file = pdf_file.replace('.pdf', '_temp_backup.pdf')
        if os.path.exists(backup_file):
            os.remove(backup_file)
        os.rename(pdf_file, backup_file)
        
        # 处理PDF
        reader = PdfReader(backup_file)
        writer = PdfWriter()
        
        # 使用8%的页眉删除比例
        header_ratio = 0.08
        
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            
            # 获取页面尺寸
            page_width = float(page.mediabox.width)
            page_height = float(page.mediabox.height)
            
            # 计算页眉高度
            header_height = page_height * header_ratio
            
            # 裁剪掉顶部页眉
            page.mediabox.lower_left = (0, header_height)
            page.mediabox.upper_right = (page_width, page_height)
            page.cropbox.lower_left = (0, header_height)
            page.cropbox.upper_right = (page_width, page_height)
            
            writer.add_page(page)
        
        # 保存处理后的PDF
        with open(pdf_file, 'wb') as f:
            writer.write(f)
        
        print(f"  [SUCCESS] 页眉已删除")
        processed_count += 1
        
    except Exception as e:
        print(f"  [FAILED] 处理失败: {e}")
        failed_count += 1
        # 恢复原始文件
        if os.path.exists(backup_file):
            os.rename(backup_file, pdf_file)

print("=" * 60)
print(f"处理完成!")
print(f"成功: {processed_count} 个文件")
print(f"失败: {failed_count} 个文件")