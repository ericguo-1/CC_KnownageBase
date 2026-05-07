import os
import glob
import fitz  # PyMuPDF

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
        doc = fitz.open(pdf_file)
        
        # 创建新PDF
        new_doc = fitz.open()
        
        # 定义页眉区域 (通常在顶部,高度约80-100像素)
        # 根据PDF页面大小调整,这里假设页眉在前10%的高度
        header_height_ratio = 0.1  # 页面高度的10%
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            
            # 获取页面尺寸
            rect = page.rect
            page_height = rect.height
            page_width = rect.width
            
            # 计算页眉区域 (顶部10%)
            header_height = page_height * header_height_ratio
            
            # 定义要保留的区域 (去掉页眉)
            crop_rect = fitz.Rect(
                rect.x0,                      # 左边界
                rect.y0 + header_height,      # 上边界 (去掉页眉)
                rect.x1,                      # 右边界
                rect.y1                       # 下边界
            )
            
            # 创建新页面 (去掉页眉)
            new_page = new_doc.new_page(
                width=page_width,
                height=page_height - header_height
            )
            
            # 将内容(去掉页眉)绘制到新页面
            new_page.show_pdf_page(
                page,
                fitz.Rect(0, -header_height, page_width, page_height)
            )
        
        # 保存处理后的PDF
        backup_file = pdf_file.replace('.pdf', '_backup.pdf')
        os.rename(pdf_file, backup_file)
        
        new_doc.save(pdf_file)
        new_doc.close()
        doc.close()
        
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