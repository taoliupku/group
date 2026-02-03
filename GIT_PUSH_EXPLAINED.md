# Git 和 GitHub 推送底层逻辑详解

## 📚 核心概念

### 1. **本地仓库（Local Repository）**

```
你的电脑上的文件夹
├── .git/          ← Git的"大脑"，记录所有历史
├── index.html
├── About Liu.html
└── ...
```

**本地仓库**就是你的项目文件夹 + `.git` 隐藏文件夹。

- `.git` 文件夹存储了：
  - 所有文件的版本历史
  - 提交记录（commit）
  - 分支信息
  - **远程仓库地址**（在 `.git/config` 中）

### 2. **远程仓库（Remote Repository）**

**远程仓库**就是 GitHub 服务器上的一个"云文件夹"。

```
GitHub服务器
└── taoliupku/
    └── group/          ← 这就是远程仓库
        ├── .git/
        ├── index.html
        └── ...
```

### 3. **远程地址（Remote URL）**

本地仓库需要知道"把代码推送到哪里"，这个信息存储在**远程地址**中。

```bash
# 查看远程地址
git remote -v

# 输出示例：
origin  https://github.com/taoliupku/group.git  (fetch)
origin  https://github.com/taoliupku/group.git  (push)
```

**`origin`** 是远程仓库的**别名**（默认名称），指向实际的 GitHub 地址。

---

## 🔄 推送（Push）的完整流程

### 步骤1：本地提交（Commit）

```bash
# 1. 添加文件到暂存区
git add .

# 2. 创建提交（保存到本地.git文件夹）
git commit -m "更新网站"
```

**此时发生了什么？**
- 文件被保存到本地 `.git` 文件夹
- 创建了一个"快照"（commit）
- **代码还在你的电脑上，没有上传**

### 步骤2：推送到远程（Push）

```bash
git push origin main
```

**这个命令做了什么？**

1. **读取远程地址**：
   ```
   git 查看 .git/config 文件
   找到 origin = https://github.com/taoliupku/group.git
   ```

2. **建立网络连接**：
   ```
   你的电脑 → 互联网 → GitHub服务器
   ```

3. **身份验证**：
   ```
   GitHub问："你是谁？"
   你的电脑提供：
   - 用户名（从git配置或凭据管理器）
   - 密码/Token（从凭据管理器或手动输入）
   ```

4. **权限检查**：
   ```
   GitHub检查：
   - 这个账号（如taoliupku）是否有权限访问 taoliupku/group？
   - 如果有 → 继续
   - 如果没有 → 返回 403 错误
   ```

5. **传输数据**：
   ```
   你的电脑发送：
   - 新的提交（commit）
   - 新的文件内容
   - 分支信息
   
   GitHub接收并保存到服务器
   ```

6. **更新远程分支**：
   ```
   GitHub上的 main 分支被更新
   现在远程仓库和本地仓库同步了
   ```

---

## 🔐 权限认证机制

### 问题：GitHub 如何知道你是谁？

#### 方法1：HTTPS + 用户名密码（已废弃）

```bash
# 旧方式（GitHub已不支持密码）
git push https://username:password@github.com/user/repo.git
```

**为什么废弃？**
- 密码容易被窃取
- 不安全

#### 方法2：HTTPS + Personal Access Token (PAT)

```bash
# 新方式
git push https://username:token@github.com/user/repo.git
```

**Token 是什么？**
- 类似"临时密码"，但更安全
- 可以设置过期时间
- 可以设置权限范围（如只读、只写等）
- 可以随时撤销

#### 方法3：SSH 密钥

```bash
# 使用SSH地址
git push git@github.com:user/repo.git
```

**SSH 密钥是什么？**
- 一对密钥：私钥（在你电脑上）+ 公钥（在GitHub上）
- 不需要每次输入密码
- 更安全

#### 方法4：凭据管理器（Credential Manager）

**Windows 凭据管理器**会记住你的账号密码/Token：

```
Windows凭据管理器
└── git:https://github.com
    ├── 用户名: YeyuSu
    └── 密码: [已保存的Token]
```

**问题所在**：
- 如果你之前用 `YeyuSu` 账号推送过
- Windows 会记住这个账号
- 即使你改了远程地址，Git 还是会用 `YeyuSu` 的凭据
- 所以推送到 `taoliupku/group` 时会提示"没有权限"

---

## 🎯 你遇到的问题分析

### 问题1：为什么显示"没有权限"？

```
1. 本地仓库的远程地址：origin → https://github.com/taoliupku/group.git ✅
2. Windows凭据管理器保存的是：YeyuSu 的账号 ❌
3. Git尝试用 YeyuSu 推送到 taoliupku/group
4. GitHub检查：YeyuSu 没有 taoliupku/group 的权限
5. 返回 403 错误："Permission denied"
```

### 问题2：为什么 GitHub Desktop 也显示权限错误？

```
GitHub Desktop 读取：
1. 本地仓库的远程地址 → taoliugroup-pku.github.io（旧的）
2. 或者读取到 origin → taoliupku/group（新的）
3. 但登录的账号是 YeyuSu
4. 所以显示"没有权限"
```

---

## ✅ 解决方案的原理

### 方案1：清除旧凭据

```bash
# 清除Windows凭据管理器中的GitHub凭据
# 这样Git会要求你重新输入账号密码
```

**原理**：
- 删除旧的 `YeyuSu` 凭据
- 下次推送时，Git 会要求输入新账号
- 输入 `taoliupku` 的账号和 Token
- Windows 会保存新的凭据

### 方案2：使用 Token 直接推送

```bash
git push https://taoliupku:TOKEN@github.com/taoliupku/group.git main
```

**原理**：
- 直接在 URL 中包含用户名和 Token
- 绕过凭据管理器
- 一次性使用，不会保存

### 方案3：在 GitHub Desktop 中切换账号

**原理**：
- GitHub Desktop 有自己的账号管理
- 退出 `YeyuSu`，登录 `taoliupku`
- GitHub Desktop 会使用新账号的凭据

---

## 📊 完整流程图

```
┌─────────────────┐
│  你的本地仓库    │
│  (你的电脑)      │
│                 │
│  .git/          │
│  ├── config     │ ← 存储远程地址
│  └── ...        │
└────────┬────────┘
         │
         │ git push origin main
         │
         ▼
┌─────────────────┐
│  身份验证        │
│                 │
│  1. 读取远程地址  │
│  2. 查找凭据     │ ← Windows凭据管理器
│  3. 或要求输入   │
└────────┬────────┘
         │
         │ HTTPS请求
         │ (包含用户名+密码/Token)
         │
         ▼
┌─────────────────┐
│  GitHub服务器   │
│                 │
│  1. 验证身份     │
│  2. 检查权限     │ ← 这个账号能访问这个仓库吗？
│  3. 接收代码     │
│  4. 更新仓库     │
└─────────────────┘
```

---

## 🔍 关键点总结

1. **本地仓库 ≠ 远程仓库**
   - 本地：你电脑上的文件夹
   - 远程：GitHub 服务器上的文件夹

2. **远程地址（Remote）是"指针"**
   - 告诉 Git"推送到哪里"
   - 可以随时修改：`git remote set-url origin <新地址>`

3. **身份验证是独立的**
   - 远程地址改了，但凭据可能还是旧的
   - 需要清除旧凭据或使用新账号

4. **权限检查在服务器端**
   - GitHub 检查：这个账号能访问这个仓库吗？
   - 不能 → 403 错误

5. **推送是"上传"操作**
   - 把本地的提交（commit）上传到远程
   - 远程仓库会被更新

---

## 💡 类比理解

**Git 推送就像寄快递**：

1. **本地仓库** = 你的包裹（在你家里）
2. **远程地址** = 收件地址（写在快递单上）
3. **身份验证** = 你的身份证（证明你是谁）
4. **权限检查** = 快递员检查：这个地址是你家吗？
5. **推送** = 把包裹送到收件地址

**问题**：
- 你改了收件地址（远程地址）
- 但身份证还是旧的（凭据管理器）
- 快递员说："这个地址不是你的！"（权限错误）

**解决**：
- 换新的身份证（清除旧凭据，用新账号）
- 或者直接在快递单上写新地址+新身份证号（URL包含Token）

---

希望这个解释能帮助你理解 Git 推送的底层逻辑！如果还有疑问，随时问我。



