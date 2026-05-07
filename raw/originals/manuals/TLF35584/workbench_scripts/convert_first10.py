import os
import subprocess

pdf_dir = r"D:\GG\Doc_Dlod\UserMannual\TLF35584\div"
marker_exe = r"C:\Users\79006\AppData\Local\Programs\Python\Python311\Scripts\marker_single.exe"

# 只转换前10个章节,跳过第5章
pdf_files = [
    "01_Overview.pdf",           # 第1章
    "02_Block_Diagram.pdf",      # 第2章  
    "03_Pin_Configuration.pdf",  # 第3章
    "04_General_Product_Characteristics.pdf",  # 第4章
    # "05_Wake_Function.pdf",     # 第5章 - 已转换,跳过
    "06_Enable_Function.pdf",    # 第6章
    "07_Reset_Function.pdf",     # 第7章
    "08_Under_Voltage_Lock_Out.pdf",  # 第8章
    "09_Overvoltage_Protection.pdf",  # 第9章
    "10_Overcurrent_Protection.pdf"   # 第10章
]

print("开始转换前10个章节(跳过第5章)...\n")

converted_count = 0
failed_count = 0
skipped_count = 0

for i, pdf_file in enumerate(pdf_files):
    pdf_path = os.path.join(pdf_dir, pdf_file)
    
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
        print(f"[SKIP] 跳过已转换: {pdf_file}")
        skipped_count += 1
        continue
    
    print(f"[PROCESSING] 正在转换 [{i+1}/{len(pdf_files)}]: {pdf_file}")
    
    try:
        # 执行Marker转换
        result = subprocess.run(
            [marker_exe, pdf_path, "--output_dir", pdf_dir],
            capture_output=True,
            text=True,
            timeout=180  # 3分钟超时
        )
        
        if result.returncode == 0:
            print(f"[SUCCESS] 转换成功: {pdf_file}")
            converted_count += 1
        else:
            print(f"[FAILED] 转换失败: {pdf_file}")
            print(f"   错误: {result.stderr[:200]}")
            failed_count += 1
            
    except subprocess.TimeoutExpired:
        print(f"[TIMEOUT] 转换超时: {pdf_file}")
        failed_count += 1
    except Exception as e:
        print(f"[ERROR] 转换异常: {pdf_file} - {str(e)[:100]}")
        failed_count += 1

print(f"\n转换完成!")
print(f"✅ 成功: {converted_count} 个文件")
print(f"⏭️  跳过: {skipped_count} 个文件(已存在)")
print(f"❌ 失败: {failed_count} 个文件")