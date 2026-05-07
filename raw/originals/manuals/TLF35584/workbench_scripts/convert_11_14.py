import os
import subprocess

pdf_dir = r"D:\GG\Doc_Dlod\UserMannual\TLF35584\div"
marker_exe = r"C:\Users\79006\AppData\Local\Programs\Python\Python311\Scripts\marker_single.exe"

# 转换11-14章节
pdf_files = [
    "11_State_Machine.pdf",
    "12_Safe_State_Control_Function.pdf", 
    "13_SPI_Serial_Peripheral_Interface.pdf",
    "14_Interrupt_Generation.pdf"
]

print("开始转换11-14章节...\n")

converted_count = 0
failed_count = 0

for i, pdf_file in enumerate(pdf_files):
    pdf_path = os.path.join(pdf_dir, pdf_file)
    chapter_num = i + 11
    
    # 检查文件是否存在
    if not os.path.exists(pdf_path):
        print(f"[ERROR] 文件不存在: {pdf_file}")
        failed_count += 1
        continue
    
    # 检查是否已经转换过
    base_name = pdf_file.replace('.pdf', '')
    output_dir = os.path.join(pdf_dir, base_name)
    md_file = os.path.join(output_dir, f"{base_name}.md")
    
    if os.path.exists(md_file):
        print(f"[SKIP] 第{chapter_num}章已转换: {pdf_file}")
        converted_count += 1
        continue
    
    print(f"[PROCESSING] 正在转换第{chapter_num}章: {pdf_file}")
    
    try:
        # 执行Marker转换
        result = subprocess.run(
            [marker_exe, pdf_path, "--output_dir", pdf_dir, "--disable_multiprocessing"],
            capture_output=True,
            text=True,
            timeout=600  # 10分钟超时
        )
        
        if result.returncode == 0:
            print(f"[SUCCESS] 第{chapter_num}章转换成功: {pdf_file}")
            converted_count += 1
        else:
            print(f"[FAILED] 第{chapter_num}章转换失败: {pdf_file}")
            print(f"   错误: {result.stderr[:300]}")
            failed_count += 1
            
    except subprocess.TimeoutExpired:
        print(f"[TIMEOUT] 第{chapter_num}章转换超时: {pdf_file}")
        failed_count += 1
    except Exception as e:
        print(f"[ERROR] 第{chapter_num}章转换异常: {pdf_file} - {str(e)[:200]}")
        failed_count += 1

print(f"\n转换完成!")
print(f"成功: {converted_count} 个文件")
print(f"失败: {failed_count} 个文件")