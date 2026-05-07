import os
from pypdf import PdfReader, PdfWriter

pdf_file = r"D:\GG\Doc_Dlod\UserMannual\TLF35584\div\11_State_Machine.pdf"
output_dir = r"D:\GG\Doc_Dlod\UserMannual\TLF35584\div"

print("拆分第11章 State Machine (90页)...")
print("=" * 60)

reader = PdfReader(pdf_file)
total_pages = len(reader.pages)

print(f"总页数: {total_pages}")
print(f"拆分策略: 每次转换10页")

# 计算需要拆分的段数
pages_per_segment = 10
num_segments = (total_pages + pages_per_segment - 1) // pages_per_segment

print(f"拆分段数: {num_segments}段")
print()

segments = []

for i in range(num_segments):
    start_page = i * pages_per_segment
    end_page = min((i + 1) * pages_per_segment, total_pages)
    
    # 创建分段PDF
    writer = PdfWriter()
    
    for page_num in range(start_page, end_page):
        writer.add_page(reader.pages[page_num])
    
    # 保存分段PDF
    segment_file = os.path.join(output_dir, f"11_State_Machine_part{i+1}.pdf")
    
    with open(segment_file, 'wb') as f:
        writer.write(f)
    
    segments.append({
        'file': segment_file,
        'start': start_page + 1,  # 页码从1开始
        'end': end_page,
        'pages': end_page - start_page
    })
    
    print(f"[CREATED] 第{i+1}段: {os.path.basename(segment_file)}")
    print(f"         页码范围: {start_page + 1}-{end_page} ({end_page - start_page}页)")

print()
print("=" * 60)
print(f"拆分完成! 共创建 {num_segments} 个分段文件")
print()
print("分段文件列表:")
for i, seg in enumerate(segments, 1):
    print(f"  {i}. {os.path.basename(seg['file'])} - 页码{seg['start']}-{seg['end']}")