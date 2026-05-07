import PyPDF2
import re

pdf_path = r"D:\GG\Doc_Dlod\UserMannual\TLF35584\infineon-tlf35584-datasheet-en.pdf"
output_dir = r"D:\GG\Doc_Dlod\UserMannual\TLF35584"

# 定义18个主要章节
chapters = [
    (1, "Overview", 6),
    (2, "Block_Diagram", 7),
    (3, "Pin_Configuration", 8),
    (4, "General_Product_Characteristics", 19),
    (5, "Wake_Function", 26),
    (6, "Enable_Function", 30),
    (7, "Reset_Function", 34),
    (8, "Under_Voltage_Lock_Out", 38),
    (9, "Overvoltage_Protection", 42),
    (10, "Overcurrent_Protection", 53),
    (11, "State_Machine", 58),
    (12, "Safe_State_Control_Function", 148),
    (13, "SPI_Serial_Peripheral_Interface", 162),
    (14, "Interrupt_Generation", 219),
    (15, "Window_Watchdog_And_Functional_Watchdog", 222),
    (16, "Application_Information", 239),
    (17, "Package_Outlines", 241),
    (18, "Revision_History", 243)
]

pdf = PyPDF2.PdfReader(pdf_path)
total_pages = len(pdf.pages)

print(f"总页数: {total_pages}")
print(f"将拆分为 {len(chapters)} 个章节")

# 拆分PDF
for i, (num, title, start_page) in enumerate(chapters):
    # 计算结束页码 (下一个章节的起始页-1, 或最后一页)
    if i < len(chapters) - 1:
        end_page = chapters[i + 1][2] - 1
    else:
        end_page = total_pages - 1

    # 确保页码范围有效
    if start_page > end_page:
        print(f"警告: 章节 {num} ({title}) 的起始页 {start_page} 大于结束页 {end_page}")
        continue

    # 创建新的PDF
    writer = PyPDF2.PdfWriter()
    for page_num in range(start_page - 1, end_page):
        writer.add_page(pdf.pages[page_num])

    # 保存文件
    output_filename = f"{num:02d}_{title}.pdf"
    output_path = f"{output_dir}\\{output_filename}"

    with open(output_path, 'wb') as output_file:
        writer.write(output_file)

    print(f"已生成: {output_filename} (页码 {start_page}-{end_page}, 共 {end_page - start_page + 1} 页)")

print("\n拆分完成!")