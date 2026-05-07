import os
import glob
from pypdf import PdfReader, PdfWriter, Transformation, PageObject

pdf_dir = r"D:\GG\Doc_Dlod\UserMannual\TLF35584\div"

print("开始删除PDF页眉区域...")
print("=" * 60)

# 获取所有PDF文件
pdf_files = []
for i in range(1, 19):  # 1-18章
    pattern = os.path.join(pdf_dir, f"{i:02d}_*.pdf")
    matching_files = glob.glob(pattern)
    for pdf_file in sorted(matching_files):
        if os.path.isfile(pdf_file):
            pdf_files.append(pdf_file)

pdf_files.sort()

processed_count = 0
failed_count = 0

for pdf_file in pdf_files:
    pdf_name = os.path.basename(pdf_file)
    print(f"[PROCESSING] 处理: {pdf_name}")
    
    try:
        # 打开原始PDF
        reader = PdfReader(pdf_file)
        writer = PdfWriter()
        
        # 定义页眉删除比例 (删除顶部10%)
        header_ratio = 0.1
        
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            
            # 获取页面尺寸
            page_width = float(page.mediabox.width)
            page_height = float(page.mediabox.height)
            
            # 计算页眉高度
            header_height = page_height * header_ratio
            
            # 创建裁剪区域 (去掉顶部页眉)
            # 保留的矩形: 从页眉下方开始到页面底部
            x0 = 0
            y0 = header_height
            x1 = page_width
            y1 = page_height
            
            # 裁剪页面
            page.mediabox.lower_left = (x0, y0)
            page.mediabox.upper_right = (x1, y1)
            page.cropbox.lower_left = (x0, y0)
            page.cropbox.upper_right = (x1, y1)
            
            # 添加到新PDF
            writer.add_page(page)
        
        # 保存处理后的PDF
        backup_file = pdf_file.replace('.pdf', '_backup.pdf')
        os.rename(pdf_file, backup_file)
        
        with open(pdf_file, 'wb') as output_file:
            writer.write(output_file)
        
        print(f"  [SUCCESS] 已删除页眉,备份: {os.path.basename(backup_file)}")
        processed_count += 1
        
    except Exception as e:
        print(f"  [FAILED] 处理失败: {e}")
        failed_count += 1

print("=" * 60)
print(f"处理完成!")
print(f"成功: {processed_count} 个文件")
print(f"失败: {failed_count} 个文件")
print(f"原始文件已备份为 *_backup.pdf")