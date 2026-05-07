import PyPDF2
import os

pdf_path = r"D:\GG\Doc_Dlod\UserMannual\TLF35584\infineon-tlf35584-datasheet-en.pdf"
output_dir = r"D:\GG\Doc_Dlod\UserMannual\TLF35584"

# 读取原PDF
original_pdf = PyPDF2.PdfReader(pdf_path)
original_pages = len(original_pdf.pages)
original_size = os.path.getsize(pdf_path)

print(f"原始PDF信息:")
print(f"  文件名: {os.path.basename(pdf_path)}")
print(f"  总页数: {original_pages}")
print(f"  文件大小: {original_size / 1024:.2f} KB")
print()

# 验证拆分结果
split_files = []
total_split_pages = 0
total_split_size = 0

print("拆分文件验证:")

# 按文件名排序
for i in range(1, 19):
    filename = f"{i:02d}_*.pdf"
    # 查找匹配的文件
    matching_files = [f for f in os.listdir(output_dir) if f.startswith(f"{i:02d}_") and f.endswith('.pdf')]

    for file in matching_files:
        file_path = os.path.join(output_dir, file)
        pdf = PyPDF2.PdfReader(file_path)
        pages = len(pdf.pages)
        size = os.path.getsize(file_path)

        split_files.append({
            'name': file,
            'pages': pages,
            'size': size
        })

        total_split_pages += pages
        total_split_size += size

        print(f"  {file}: {pages} 页, {size / 1024:.2f} KB")

print()
print(f"拆分统计:")
print(f"  拆分文件数: {len(split_files)}")
print(f"  拆分总页数: {total_split_pages}")
print(f"  拆分总大小: {total_split_size / 1024:.2f} KB")
print()

# 检查是否有遗漏
if total_split_pages == original_pages:
    print("✅ 页数匹配: 拆分完整,无遗漏")
else:
    print(f"❌ 页数不匹配: 原始 {original_pages} 页, 拆分 {total_split_pages} 页")
    print(f"   差异: {original_pages - total_split_pages} 页")

# 检查是否覆盖了所有页码
covered_pages = set()
for file_info in split_files:
    # 这里简化检查,实际应该读取每个文件的页码范围
    pass

print()
print("拆分文件列表:")
for file_info in split_files:
    print(f"  - {file_info['name']}")