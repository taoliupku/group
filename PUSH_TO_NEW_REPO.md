# 推送到新仓库指南

## 目标仓库
- **账号**：`taoliupku`
- **仓库**：`group`
- **仓库地址**：https://github.com/taoliupku/group

## 方法1：使用命令行（如果网络正常）

在项目目录下执行：

```bash
cd "C:\Users\18103\BaiduSyncdisk\liulab_web\Web of Liu Lab\LiuLab_Simplified"

# 添加新远程仓库（如果还没添加）
git remote add taoliupku https://github.com/taoliupku/group.git

# 推送到新仓库
git push taoliupku main
```

## 方法2：使用GitHub Desktop（推荐，最可靠）

1. **下载安装GitHub Desktop**：
   - 访问：https://desktop.github.com/
   - 下载并安装

2. **添加仓库**：
   - 打开GitHub Desktop
   - 使用 `taoliupku` 账号登录
   - File → Add Local Repository
   - 选择：`C:\Users\18103\BaiduSyncdisk\liulab_web\Web of Liu Lab\LiuLab_Simplified`

3. **推送代码**：
   - 在GitHub Desktop中，点击 "Publish repository"
   - 选择推送到 `taoliupku/group`
   - 或如果已连接，直接点击 "Push origin"

## 方法3：手动上传文件

1. **访问仓库**：
   - https://github.com/taoliupku/group

2. **上传文件**：
   - 点击 "uploading an existing file"
   - 将 `LiuLab_Simplified` 文件夹中的所有文件拖拽上传
   - 添加提交信息："Initial commit: LiuLab website"
   - 点击 "Commit changes"

## 方法4：使用SSH方式（如果配置了SSH密钥）

```bash
# 添加SSH远程地址
git remote add taoliupku-ssh git@github.com:taoliupku/group.git

# 推送
git push taoliupku-ssh main
```

## 推送完成后启用GitHub Pages

1. **访问仓库**：
   - https://github.com/taoliupku/group

2. **启用Pages**：
   - Settings → Pages
   - Source: "Deploy from a branch"
   - Branch: "main"
   - Folder: "/ (root)"
   - 点击 "Save"

3. **访问网站**：
   - URL：`https://taoliupku.github.io/group/`
   - 等待2-5分钟部署完成

## 注意事项

⚠️ **URL说明**：
- 由于仓库名是 `group`（不是 `taoliupku.github.io`）
- 网站URL会是：`https://taoliupku.github.io/group/`
- 如果要使用 `https://taoliupku.github.io/`，需要将仓库重命名为 `taoliupku.github.io`

## 重命名仓库（可选）

如果想使用 `https://taoliupku.github.io/`：

1. 访问：https://github.com/taoliupku/group/settings
2. 滚动到底部，找到 "Repository name"
3. 改为：`taoliupku.github.io`
4. 点击 "Rename"
5. 重新启用Pages，URL会变成 `https://taoliupku.github.io/`

---

**推荐**：使用方法2（GitHub Desktop），最可靠且不容易出错。

