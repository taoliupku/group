# 网站更新Protocol

本文档说明如何更新LiuLab网站内容并推送到GitHub Pages。

## 准备工作

### 1. 确认工作环境
- 确保在 `LiuLab_Simplified` 目录下工作
- 确保已安装 Git
- 确保已配置 Git 用户信息（如未配置，运行以下命令）：
```bash
git config --global user.name "您的名字"
git config --global user.email "您的邮箱"
```

### 2. 检查Git状态
打开终端/命令行，进入项目目录：
```bash
cd "C:\Users\18103\BaiduSyncdisk\liulab_web\Web of Liu Lab\LiuLab_Simplified"
```

## 更新流程

### 步骤1：修改网站文件

根据您的需求修改相应的文件：

#### 常见修改场景：

**a) 添加新论文/更新Publications页面**
- 编辑文件：`Publications.html`
- 在 "After PKU" 或 "Before PKU" 部分添加新条目
- 如需添加图片，将图片放入 `images/` 文件夹

**b) 更新首页内容**
- 编辑文件：`index.html` 或 `LiuLab.html`
- 修改轮播图：更新 `images/` 文件夹中的图片
- 修改近期论文：在 "Recent Publications" 部分更新

**c) 更新成员信息**
- 编辑文件：`Members.html`
- 添加成员照片：放入 `images/` 文件夹，确保文件名与HTML中引用一致

**d) 添加/更新新闻**
- 编辑文件：`News.html`

**e) 更新照片页面**
- 编辑相应照片页面：`Photos.html`, `Photos-*.html`
- 添加新照片到 `images/` 或相应文件夹

**f) 修改研究内容**
- 编辑文件：`Research.html`

**g) 更新关于页面**
- 编辑文件：`About Liu.html`

### 步骤2：添加图片资源（如需要）

如果需要添加新图片：
1. 将图片文件复制到 `images/` 文件夹
2. 确保文件名与HTML中的引用路径一致（注意大小写和空格）
3. 建议使用 `.jpg`、`.jpeg`、`.png` 格式

### 步骤3：检查Git状态

查看哪些文件被修改：
```bash
git status
```

### 步骤4：添加修改的文件到暂存区

**添加所有修改的文件：**
```bash
git add .
```

**或仅添加特定文件：**
```bash
git add 文件名.html
git add images/图片名.jpg
```

### 步骤5：提交更改

提交时使用有意义的提交信息：
```bash
git commit -m "描述性信息，例如：Add 2025 publication / Update members page"
```

**推荐的提交信息格式：**
- `Add 2025 Nano Letters publication`
- `Update members page: add new member photos`
- `Fix image paths in Publications page`
- `Update homepage slider images`
- `Add news item for 2025`

### 步骤6：推送到GitHub

```bash
git push origin main
```

### 步骤7：等待GitHub Pages更新

- GitHub Pages 通常会在推送后 **2-5分钟** 自动更新
- 如果遇到问题，可以查看 GitHub 仓库的 Actions 标签页查看部署状态

### 步骤8：验证更新

访问网站验证更改是否生效：
- https://taoliugroup-pku.github.io/
- https://yeyusu.github.io/taoliugroup-pku.github.io/

如果看不到更新，尝试：
1. 清除浏览器缓存
2. 强制刷新（Ctrl+F5 或 Cmd+Shift+R）
3. 等待更长时间（最多10分钟）

## 常见问题排查

### 问题1：推送失败 - "Updates were rejected"

**原因：** 远程仓库有您本地没有的更改

**解决方案：**
```bash
git pull --rebase origin main
git push origin main
```

### 问题2：网络连接问题

**解决方案：**
1. 检查网络连接
2. 清除Git代理设置（如之前设置过）：
   ```bash
   git config --global --unset http.proxy
   git config --global --unset https.proxy
   ```
3. 稍后重试推送

### 问题3：图片不显示

**检查项：**
- 图片文件是否已放入 `images/` 文件夹
- HTML中的图片路径是否正确（相对路径 `images/文件名.jpg`）
- 文件名大小写是否完全匹配
- 文件名中的空格是否使用了URL编码（`%20`）或已替换为下划线

### 问题4：网站显示旧版本

**解决方案：**
1. 确认推送成功：检查 `git push` 命令是否成功执行
2. 等待更长时间（GitHub Pages可能需要更长时间部署）
3. 清除浏览器缓存并强制刷新
4. 检查GitHub仓库的Pages设置是否正常

## 完整更新示例

### 示例1：添加新论文

```bash
# 1. 修改Publications.html文件（添加新论文条目）

# 2. 将论文图片复制到images文件夹
# （假设图片名为：2025_newpaper.jpg）

# 3. 检查状态
git status

# 4. 添加文件
git add Publications.html
git add images/2025_newpaper.jpg

# 5. 提交
git commit -m "Add 2025 new publication"

# 6. 推送
git push origin main

# 7. 等待2-5分钟后访问网站验证
```

### 示例2：更新多个页面

```bash
# 1. 修改多个文件（Publications.html, Members.html, News.html）

# 2. 检查状态
git status

# 3. 添加所有修改
git add .

# 4. 提交
git commit -m "Update publications, members and news pages"

# 5. 推送
git push origin main
```

## 快速参考命令

```bash
# 进入项目目录
cd "C:\Users\18103\BaiduSyncdisk\liulab_web\Web of Liu Lab\LiuLab_Simplified"

# 查看修改状态
git status

# 添加所有修改
git add .

# 提交更改
git commit -m "您的提交信息"

# 推送到GitHub
git push origin main

# 如果需要先拉取远程更改
git pull --rebase origin main
```

## 注意事项

1. **备份重要文件**：修改前建议备份原始文件
2. **测试本地**：推送前可以在本地浏览器打开HTML文件测试
3. **提交信息**：使用清晰、描述性的提交信息，方便后续追踪
4. **图片大小**：大图片会影响加载速度，建议压缩后使用
5. **文件编码**：确保HTML文件使用UTF-8编码
6. **路径一致性**：所有图片路径使用相对路径 `images/文件名`

## 需要帮助？

如果遇到问题，可以：
1. 检查Git状态：`git status`
2. 查看Git日志：`git log --oneline -10`
3. 查看远程仓库：访问 https://github.com/YeyuSu/taoliugroup-pku.github.io

---

**最后更新：** 2025年1月


