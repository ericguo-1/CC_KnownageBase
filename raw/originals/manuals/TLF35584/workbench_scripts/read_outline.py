import PyPDF2

pdf_path = r"D:\GG\Doc_Dlod\UserMannual\TLF35584\infineon-tlf35584-datasheet-en.pdf"
pdf = PyPDF2.PdfReader(pdf_path)

print(f"总页数: {len(pdf.pages)}")
print("\n目录结构:")

try:
    outline = pdf.outline
    if outline:
        print(f"大纲项数: {len(outline)}")
        for i, item in enumerate(outline[:25]):  # 显示前25个
            try:
                page_num = pdf.get_destination_page_number(item) + 1
                print(f"{i+1}. {item.title} - 页码: {page_num}")
            except:
                print(f"{i+1}. {item.title} - 页码: 未知")
    else:
        print("无目录结构")
except Exception as e:
    print(f"读取目录错误: {e}")