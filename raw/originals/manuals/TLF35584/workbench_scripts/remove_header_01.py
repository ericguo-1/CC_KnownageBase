import os
from pypdf import PdfReader, PdfWriter

pdf_file = r"D:\GG\Doc_Dlod\UserMannual\TLF35584\div\01_Overview.pdf"
backup_file = pdf_file.replace('.pdf', '_temp_backup.pdf')

print(f"处理文件: {os.path.basename(pdf_file)}")
print("=" * 50)

# 先备份
if os.path.exists(backup_file):
    os.remove(backup_file)
os.rename(pdf_file, backup_file)

try:
    reader = PdfReader(backup_file)
    writer = PdfWriter()
    
    print(f"原始PDF: {len(reader.pages)} 页")
    
    # 分析第一页,确定页眉高度
    first_page = reader.pages[0]
    page_width = float(first_page.mediabox.width)
    page_height = float(first_page.mediabox.height)
    
    print(f"页面尺寸: {page_width} x {page_height} points")
    print(f"尝试删除页眉 (顶部15%)")
    
    # 尝试不同的页眉删除比例
    header_ratios = [0.15, 0.12, 0.10, 0.08]
    
    for ratio in header_ratios:
        header_height = page_height * ratio
        
        print(f"\n尝试比例 {ratio*100:.0f}% (删除 {header_height:.1f} points):")
        
        writer = PdfWriter()
        
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            
            # 裁剪掉顶部页眉
            page.mediabox.lower_left = (0, header_height)
            page.mediabox.upper_right = (page_width, page_height)
            page.cropbox.lower_left = (0, header_height)
            page.cropbox.upper_right = (page_width, page_height)
            
            writer.add_page(page)
        
        # 保存测试文件
        test_file = pdf_file.replace('.pdf', f'_test_{ratio}.pdf')
        with open(test_file, 'wb') as f:
            writer.write(f)
        
        print(f"  已生成测试文件: {os.path.basename(test_file)}")
    
    # 使用最保守的比例(8%)作为最终结果
    final_ratio = 0.08
    header_height = page_height * final_ratio
    
    writer = PdfWriter()
    
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        
        # 最终裁剪
        page.mediabox.lower_left = (0, header_height)
        page.mediabox.upper_right = (page_width, page_height)
        page.cropbox.lower_left = (0, header_height)
        page.cropbox.upper_right = (page_width, page_height)
        
        writer.add_page(page)
    
    # 保存最终结果
    with open(pdf_file, 'wb') as f:
        writer.write(f)
    
    print(f"\n最终结果: 使用 {final_ratio*100:.0f}% 页眉删除比例")
    print(f"已保存到: {os.path.basename(pdf_file)}")
    print(f"原始备份: {os.path.basename(backup_file)}")
    
except Exception as e:
    print(f"处理失败: {e}")
    # 恢复原始文件
    if os.path.exists(backup_file):
        os.rename(backup_file, pdf_file)

print("=" * 50)
print("处理完成!")