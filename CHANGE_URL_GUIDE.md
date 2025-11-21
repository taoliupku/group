# 修改网站URL指南

## 目标
将网站URL从 `https://yeyusu.github.io/taoliugroup-pku.github.io/` 改为 `https://taoliugroup-pku.github.io/`

## 原因说明

GitHub Pages的URL规则：
- 如果仓库名是 `username.github.io`，URL就是 `https://username.github.io/`
- 如果仓库名是其他名称，URL就是 `https://username.github.io/repository-name/`

当前情况：
- 仓库：`YeyuSu/taoliugroup-pku.github.io`
- URL：`https://yeyusu.github.io/taoliugroup-pku.github.io/`

要实现 `https://taoliugroup-pku.github.io/`，需要：
- 创建一个GitHub组织（Organization）名为 `taoliugroup-pku`
- 在该组织下创建名为 `taoliugroup-pku.github.io` 的仓库

---

## 解决方案：创建GitHub组织

### 步骤1：创建GitHub组织

1. **访问GitHub组织创建页面**：
   - 打开 https://github.com/organizations/new
   - 或点击GitHub右上角头像 → "Your organizations" → "New organization"

2. **填写组织信息**：
   - **Organization name（组织名称）**：`taoliugroup-pku` ⚠️ **必须完全匹配**
   - **Contact email**：填写您的邮箱
   - 选择 **Free** 计划（免费）

3. **完成创建**：
   - 点击 "Create organization"
   - 完成验证步骤

### 步骤2：在新组织下创建仓库

1. **创建新仓库**：
   - 在组织页面点击 "New repository"
   - 或访问：https://github.com/organizations/taoliugroup-pku/repositories/new

2. **设置仓库信息**：
   - **Repository name**：`taoliugroup-pku.github.io` ⚠️ **必须完全匹配**
   - **Description**：`LiuLab Research Group Website`
   - 选择 **Public**（公开）
   - **不要**勾选 "Add a README file"
   - **不要**勾选 "Add .gitignore"
   - **不要**勾选 "Choose a license"
   - 点击 "Create repository"

### 步骤3：推送代码到新仓库

在本地执行以下命令：

```bash
# 1. 添加新仓库为远程地址
git remote add new-origin https://github.com/taoliugroup-pku/taoliugroup-pku.github.io.git

# 2. 推送到新仓库
git push new-origin main

# 3. 验证推送成功
git remote -v
```

### 步骤4：启用GitHub Pages

1. **访问新仓库**：
   - https://github.com/taoliugroup-pku/taoliugroup-pku.github.io

2. **启用Pages**：
   - 点击 "Settings" → "Pages"
   - Source：选择 "Deploy from a branch"
   - Branch：选择 "main"
   - Folder：选择 "/ (root)"
   - 点击 "Save"

3. **等待部署**：
   - 通常需要2-5分钟
   - 可以在 "Actions" 标签查看部署状态

### 步骤5：验证新URL

等待几分钟后，访问：
- **新URL**：https://taoliugroup-pku.github.io/
- 应该能看到您的网站了！

### 步骤6（可选）：删除旧仓库

如果新URL工作正常，可以：
1. 访问旧仓库：https://github.com/YeyuSu/taoliugroup-pku.github.io
2. Settings → 最底部 → "Delete this repository"
3. 输入仓库名确认删除

---

## 替代方案：使用自定义域名

如果您有自己的域名（如 `liulab.com`），也可以：

1. **购买域名**（如果还没有）
2. **配置DNS**：
   - 添加A记录指向GitHub Pages的IP
   - 或添加CNAME记录指向 `taoliugroup-pku.github.io`
3. **在GitHub设置自定义域名**：
   - 仓库 Settings → Pages → Custom domain
   - 输入您的域名并保存

---

## 注意事项

⚠️ **重要提示**：
- 组织名称 `taoliugroup-pku` 必须完全匹配（区分大小写）
- 仓库名称 `taoliugroup-pku.github.io` 必须完全匹配
- 创建组织后，URL会自动变为 `https://taoliugroup-pku.github.io/`
- 旧URL `https://yeyusu.github.io/taoliugroup-pku.github.io/` 在新仓库创建后可能失效

---

## 快速命令参考

```bash
# 进入项目目录
cd "C:\Users\18103\BaiduSyncdisk\liulab_web\Web of Liu Lab\LiuLab_Simplified"

# 添加新远程仓库
git remote add new-origin https://github.com/taoliugroup-pku/taoliugroup-pku.github.io.git

# 推送到新仓库
git push new-origin main

# 如果需要，更新默认远程仓库
git remote set-url origin https://github.com/taoliugroup-pku/taoliugroup-pku.github.io.git
```

---

**需要帮助？** 如果在创建组织或仓库时遇到问题，请告诉我！

