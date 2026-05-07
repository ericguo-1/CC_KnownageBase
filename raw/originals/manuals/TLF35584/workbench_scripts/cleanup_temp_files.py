import os
import glob

pdf_dir = r"D:\GG\Doc_Dlod\UserMannual\TLF35584\div"

print("清理中间文件...")
print("=" * 60)

# 删除测试文件
test_files = glob.glob(os.path.join(pdf_dir, "*_test_*.pdf"))
for file in test_files:
    try:
        os.remove(file)
        print(f"[DELETED] 测试文件: {os.path.basename(file)}")
    except Exception as e:
        print(f"[ERROR] 删除失败: {os.path.basename(file)} - {e}")

# 删除临时备份文件
temp_backup_files = glob.glob(os.path.join(pdf_dir, "*_temp_backup.pdf"))
for file in temp_backup_files:
    try:
        os.remove(file)
        print(f"[DELETED] 临时备份: {os.path.basename(file)}")
    except Exception as e:
        print(f"[ERROR] 删除失败: {os.path.basename(file)} - {e}")

# 删除旧的转换目录(保留01_Overview作为参考)
print()
print("清理旧的转换目录...")
for i in range(2, 19):  # 2-18章
    pattern = os.path.join(pdf_dir, f"{i:02d}_*")
    matching_dirs = glob.glob(pattern)
    for dir_path in matching_dirs:
        if os.path.isdir(dir_path) and dir_path != os.path.join(pdf_dir, "01_Overview"):
            try:
                import shutil
                shutil.rmtree(dir_path)
                print(f"[DELETED] 旧转换目录: {os.path.basename(dir_path)}")
            except Exception as e:
                print(f"[ERROR] 删除失败: {os.path.basename(dir_path)} - {e}")

print("=" * 60)
print("中间文件清理完成!")
print("\n保留文件:")
print(f"  最终PDF文件: 18个")
print(f"  原始备份文件: 18个 (用于恢复)")
print(f"  01_Overview转换目录: 1个 (作为参考)")