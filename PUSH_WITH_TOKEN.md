# 使用Personal Access Token推送代码

## 问题
当前git使用的是 `YeyuSu` 账号的凭据，需要切换到 `taoliupku` 账号。

## 解决方案：使用Personal Access Token (PAT)

### 步骤1：创建Personal Access Token

1. **登录GitHub账号 `taoliupku`**

2. **创建Token**：
   - 访问：https://github.com/settings/tokens
   - 或：GitHub右上角头像 → Settings → Developer settings → Personal access tokens → Tokens (classic)

3. **生成新Token**：
   - 点击 "Generate new token" → "Generate new token (classic)"
   - **Note（备注）**：填写 `LiuLab Website Push`
   - **Expiration（过期时间）**：选择合适的时间（如90天或No expiration）
   - **Select scopes（权限）**：勾选 `repo`（完整仓库权限）
   - 点击 "Generate token"

4. **复制Token**：
   - ⚠️ **重要**：立即复制Token，只显示一次！
   - 格式类似：`ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### 步骤2：使用Token推送

在命令行中执行：

```bash
cd "C:\Users\18103\BaiduSyncdisk\liulab_web\Web of Liu Lab\LiuLab_Simplified"

# 使用Token推送（将YOUR_TOKEN替换为实际的Token）
git push https://taoliupku:YOUR_TOKEN@github.com/taoliupku/group.git main
```

或者更新远程URL：

```bash
# 更新远程URL包含Token（将YOUR_TOKEN替换为实际的Token）
git remote set-url taoliupku https://taoliupku:YOUR_TOKEN@github.com/taoliupku/group.git

# 推送
git push taoliupku main
```

---

## 替代方案：使用GitHub Desktop

如果命令行有问题，使用GitHub Desktop更简单：

1. **下载安装**：https://desktop.github.com/
2. **登录账号**：使用 `taoliupku` 账号登录
3. **添加仓库**：File → Add Local Repository
4. **推送代码**：点击 "Publish repository" 或 "Push origin"

---

## 推送完成后

1. **启用GitHub Pages**：
   - 访问：https://github.com/taoliupku/group/settings/pages
   - Source: "Deploy from a branch" → "main" → "/ (root)"
   - 保存

2. **访问网站**：
   - URL：`https://taoliupku.github.io/group/`
   - 等待2-5分钟部署完成

---

## 安全提示

⚠️ **Token安全**：
- 不要将Token提交到代码仓库
- 不要分享Token给他人
- 如果Token泄露，立即在GitHub上撤销

