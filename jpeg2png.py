import os
import glob
from PIL import Image
import argparse

def convert_jpeg_to_png(input_path, output_dir=None, quality=95):
    """
    将JPEG文件转换为PNG格式
    
    参数:
    input_path: 输入文件路径或目录路径
    output_dir: 输出目录（可选，默认为输入文件所在目录）
    quality: 输出质量（1-100，默认95）
    """
    # 检查输入路径是文件还是目录
    if os.path.isfile(input_path):
        files = [input_path]
    elif os.path.isdir(input_path):
        # 获取目录中所有的jpeg/jpg文件
        files = glob.glob(os.path.join(input_path, "*.jpeg")) + glob.glob(os.path.join(input_path, "*.jpg"))
    else:
        print(f"错误：路径 '{input_path}' 不存在")
        return
    
    if not files:
        print("没有找到JPEG文件")
        return
    
    # 创建输出目录（如果指定了）
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    converted_count = 0
    for jpeg_file in files:
        try:
            # 打开JPEG图像
            with Image.open(jpeg_file) as img:
                # 转换为RGB模式（确保兼容性）
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # 生成输出文件名
                base_name = os.path.splitext(os.path.basename(jpeg_file))[0]
                if output_dir:
                    output_file = os.path.join(output_dir, f"{base_name}.png")
                else:
                    output_file = os.path.join(os.path.dirname(jpeg_file), f"{base_name}.png")
                
                # 保存为PNG格式
                img.save(output_file, 'PNG', optimize=True, quality=quality)
                
                print(f"转换成功: {jpeg_file} -> {output_file}")
                converted_count += 1
                
        except Exception as e:
            print(f"转换失败 {jpeg_file}: {str(e)}")
    
    print(f"\n转换完成！成功转换 {converted_count} 个文件")

def main():
    parser = argparse.ArgumentParser(description="将JPEG文件转换为PNG格式")
    parser.add_argument("--input", help="输入文件路径或目录路径")
    parser.add_argument("-o", "--output", help="输出目录（可选）")
    parser.add_argument("-q", "--quality", type=int, default=95, 
                       help="输出质量 (1-100, 默认: 95)")
    
    args = parser.parse_args()
    
    # 检查PIL库是否安装
    try:
        from PIL import Image
    except ImportError:
        print("错误：需要安装Pillow库")
        print("请运行: pip install Pillow")
        return
    
    convert_jpeg_to_png(args.input, args.output, args.quality)

if __name__ == "__main__":
    main()
