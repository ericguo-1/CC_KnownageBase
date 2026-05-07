import PyPDF2

pdf_path = r"D:\GG\Doc_Dlod\UserMannual\TLF35584\infineon-tlf35584-datasheet-en.pdf"
pdf = PyPDF2.PdfReader(pdf_path)

print(f"总页数: {len(pdf.pages)}")
print("\n目录结构:")

def extract_outline(outline, level=0, prefix=""):
    items = []
    for item in outline:
        # 处理不同类型的目录项
        if isinstance(item, list):
            # 递归处理子目录
            items.extend(extract_outline(item, level+1, prefix))
        else:
            try:
                title = item.title
                page_num = pdf.get_destination_page_number(item) + 1
                indent = "  " * level
                print(f"{indent}{prefix}{len(items)+1}. {title} - 页码: {page_num}")
                items.append({
                    'title': title,
                    'page': page_num,
                    'level': level
                })
            except Exception as e:
                print(f"{indent}处理目录项错误: {e}")
                continue
    return items

try:
    outline = pdf.outline
    if outline:
        items = extract_outline(outline)
        print(f"\n总共提取了 {len(items)} 个章节")
    else:
        print("无目录结构")
except Exception as e:
    print(f"读取目录错误: {e}")