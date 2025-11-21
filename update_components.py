#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量更新HTML文件，将Header和Footer替换为组件系统
"""

import os
import re
import glob

# 要处理的HTML文件列表
html_files = [
    "Publications.html",
    "News.html", 
    "Members.html",
    "Photos.html",
    "Photos-2017 Spring Travel.html",
    "Photos-2018 Spring Travel.html",
    "Photos-2019 Spring Travel.html",
    "Photos-First Anniversary.html",
    "Photos-Liulab Members.html",
    "Photos-awards.html",
    "Photos-visitors.html"
]

# Header替换模式 - 匹配所有可能的Header结构
header_pattern = re.compile(
    r'<!-- Header -->.*?<!-- Header End -->',
    re.DOTALL
)
header_replacement = '''<!-- Header -->
<div id="header-container"></div>
<!-- Header End -->'''

# Footer替换模式 - 匹配所有可能的Footer结构
footer_pattern = re.compile(
    r'<!-- Footer -->.*?<!-- Footer End -->.*?(<script src="js/common\.js"></script>)',
    re.DOTALL
)

def update_file(filepath):
    """更新单个HTML文件"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 替换Header
        content = header_pattern.sub(header_replacement, content)
        
        # 替换Footer（保持脚本引用）
        # 先替换Footer HTML部分
        footer_html_pattern = re.compile(
            r'(<!-- Footer -->\s*<div id="footer">.*?</div>\s*</div>\s*<!-- Footer End -->)',
            re.DOTALL
        )
        content = footer_html_pattern.sub(
            '<!-- Footer -->\n<div id="footer-container"></div>\n<!-- Footer End -->',
            content
        )
        
        # 确保components.js在common.js之前
        if 'components.js' not in content:
            content = content.replace(
                '<script src="js/common.js"></script>',
                '<script src="js/components.js"></script>\n<script src="js/common.js"></script>'
            )
        
        # 如果内容有变化，写回文件
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Updated: {filepath}")
            return True
        else:
            print(f"- No changes: {filepath}")
            return False
            
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return False

if __name__ == '__main__':
    updated_count = 0
    for filename in html_files:
        if os.path.exists(filename):
            if update_file(filename):
                updated_count += 1
        else:
            print(f"⚠ File not found: {filename}")
    
    print(f"\nCompleted: {updated_count} files updated")


