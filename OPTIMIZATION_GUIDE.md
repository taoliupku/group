# 网站优化建议

本文档列出了当前网站项目的优化建议，以提升可维护性和管理效率。

## 🔍 当前问题分析

### 1. **代码重复问题**
- ❌ Header导航栏在所有16个HTML文件中重复
- ❌ Footer信息在所有HTML文件中重复  
- ❌ "返回顶部"脚本在16个文件中重复
- ❌ 修改导航链接需要改16个文件

### 2. **图片管理混乱**
- ❌ 图片分散在3个文件夹：`images/`、`all pictures/`、`new pics/`
- ❌ 同样功能的图片存在多个位置

### 3. **链接不一致**
- ❌ 有些导航链接指向 `LiuLab.html`，有些指向 `index.html`
- ❌ 首页链接应该统一使用 `index.html`

### 4. **配置信息硬编码**
- ❌ 联系方式、地址等信息硬编码在多个文件
- ❌ 修改信息需要改多个文件

---

## 💡 优化方案

### 优先级1：立即实施（简单、高效）

#### 方案1.1：统一首页链接
**问题**：导航栏中Home链接不一致
**解决**：将所有 `href="LiuLab.html"` 改为 `href="index.html"`

**操作步骤**：
```bash
# 使用查找替换功能，在所有HTML文件中：
# 查找：href="LiuLab.html"
# 替换：href="index.html"

# Logo链接也需要修改：
# 查找：<a href="LiuLab.html">
# 替换：<a href="index.html">
```

**预期效果**：统一入口，避免混淆

---

#### 方案1.2：创建配置文件
**问题**：联系信息、链接等硬编码在多个文件
**解决**：创建JavaScript配置文件

**创建文件** `js/config.js`：
```javascript
// 网站配置文件
const SiteConfig = {
    // 联系信息
    contact: {
        email: "taoliupku@pku.edu.cn",
        tel: "010-82805519",
        address: {
            line1: "Peking University Health Science Center,",
            line2: "38 Xueyuan Rd, Haidian Distrcit, Beijing, 100191, China"
        }
    },
    // 外部链接
    links: {
        pku: "http://www.pku.edu.cn/",
        hsc: "http://www.bjmu.edu.cn/",
        sps: "http://sps.bjmu.edu.cn/",
        sklnbd: "http://sklnbd.bjmu.edu.cn/"
    },
    // 当前年份（自动更新版权）
    currentYear: new Date().getFullYear()
};
```

**使用方式**：在HTML中引入并在Footer中使用：
```html
<script src="js/config.js"></script>
<script>
    document.getElementById('email').textContent = SiteConfig.contact.email;
    document.getElementById('tel').textContent = SiteConfig.contact.tel;
    document.getElementById('year').textContent = SiteConfig.currentYear;
</script>
```

**预期效果**：修改联系信息只需改一个配置文件

---

#### 方案1.3：提取公共脚本
**问题**："返回顶部"脚本在16个文件中重复
**解决**：提取到独立的JS文件

**创建文件** `js/common.js`：
```javascript
// 返回顶部功能
window.onscroll = function () {
    scrollFunction()
};

function scrollFunction() {
    const btn = document.getElementById("myBtn");
    if (!btn) return;
    
    if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
        btn.style.display = "block";
    } else {
        btn.style.display = "none";
    }
}

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
```

**在HTML中使用**：
- 删除内联的 `<script>` 标签
- 在 `</body>` 前添加：`<script src="js/common.js"></script>`

**预期效果**：公共功能统一管理，易于维护

---

### 优先级2：中期优化（需要一些重构）

#### 方案2.1：使用JavaScript动态加载Header和Footer
**问题**：Header和Footer在16个文件中重复
**解决**：使用JavaScript动态插入

**创建文件** `js/components.js`：
```javascript
// 动态加载公共组件
function loadHeader() {
    fetch('components/header.html')
        .then(response => response.text())
        .then(html => {
            document.getElementById('header-container').innerHTML = html;
            // 设置当前页面的激活状态
            setActiveNavItem();
        });
}

function loadFooter() {
    fetch('components/footer.html')
        .then(response => response.text())
        .then(html => {
            document.getElementById('footer-container').innerHTML = html;
        });
}

function setActiveNavItem() {
    const currentPage = window.location.pathname.split('/').pop();
    const navLinks = document.querySelectorAll('#nav a');
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPage || 
            (currentPage === '' && link.getAttribute('href') === 'index.html')) {
            link.innerHTML = '<big style="color: #0080af">' + link.textContent + '</big>';
        }
    });
}

// 页面加载时执行
document.addEventListener('DOMContentLoaded', function() {
    loadHeader();
    loadFooter();
});
```

**创建目录** `components/`：
- `header.html` - 包含Header HTML代码
- `footer.html` - 包含Footer HTML代码

**在HTML中使用**：
```html
<!-- Header容器 -->
<div id="header-container"></div>

<!-- 页面内容 -->
...

<!-- Footer容器 -->
<div id="footer-container"></div>

<script src="js/components.js"></script>
```

**注意**：GitHub Pages是静态托管，需要确保支持fetch API。如果不支持，考虑使用JQuery的`load()`或使用构建工具。

**预期效果**：修改导航栏只需改1个文件

---

#### 方案2.2：统一图片管理
**问题**：图片分散在多个文件夹
**解决**：制定图片组织规范

**推荐结构**：
```
images/
├── logo/              # Logo图片
│   └── LiuLogo.jpg
├── publications/       # 论文相关图片
│   ├── 2024_jacs.jpeg
│   ├── 2024_ncb.jpeg
│   └── ...
├── members/           # 成员照片
│   ├── LIU_tao.jpg
│   ├── wangyong.jpg
│   └── ...
├── homepage/          # 首页轮播图
│   ├── 2024_summer_cover.jpg
│   └── ...
└── photos/            # 照片页面
    ├── 2017_spring_travel/
    ├── 2018_spring_travel/
    └── ...
```

**迁移步骤**：
1. 创建新的文件夹结构
2. 移动图片到对应分类文件夹
3. 更新HTML中的图片路径
4. 删除旧的图片文件夹（保留备份）

---

### 优先级3：长期优化（可选）

#### 方案3.1：使用静态网站生成器
**推荐工具**：
- **Jekyll**（GitHub原生支持）
- **Hugo**（快速）
- **11ty/Eleventy**（灵活）

**优势**：
- 模板系统，避免代码重复
- 数据文件管理（YAML/JSON）
- 自动构建和部署
- Markdown支持

**实施难度**：中等（需要学习新工具）

---

#### 方案3.2：添加构建脚本
**创建文件** `build.js`（使用Node.js）：
```javascript
// 简单的构建脚本
// 可以：
// 1. 压缩HTML/CSS/JS
// 2. 优化图片
// 3. 检查链接
// 4. 生成sitemap
```

**或使用工具**：
- `gulp` 或 `webpack` 自动化构建
- `imagemin` 自动压缩图片

---

#### 方案3.3：添加网站搜索功能
**方案**：使用静态搜索工具
- **Algolia**（免费方案）
- **SimpleJekyllSearch**（Jekyll插件）
- **Fuse.js**（客户端搜索）

---

## 📋 优化实施计划

### 阶段1：快速优化（1-2小时）
1. ✅ 统一所有 `LiuLab.html` 链接为 `index.html`
2. ✅ 创建 `js/common.js` 提取公共脚本
3. ✅ 创建 `js/config.js` 统一配置
4. ✅ 更新所有HTML文件使用新的JS文件

### 阶段2：中期优化（半天）
1. ✅ 创建 `components/header.html` 和 `components/footer.html`
2. ✅ 创建 `js/components.js` 动态加载
3. ✅ 重构所有HTML文件使用组件系统

### 阶段3：整理资源（1天）
1. ✅ 重新组织图片文件夹结构
2. ✅ 更新所有图片路径
3. ✅ 清理重复图片

---

## 🛠️ 实用工具推荐

### 代码工具
- **VS Code扩展**：
  - `Find and Replace` - 批量查找替换
  - `Path Intellisense` - 路径自动补全
  - `HTMLHint` - HTML检查

### 图片优化
- **TinyPNG** - 在线压缩图片
- **ImageOptim** - 本地压缩工具
- **squoosh.app** - Google图片优化工具

### 链接检查
- **W3C Link Checker** - 在线检查链接
- **Broken Link Checker** - Chrome扩展

---

## 📝 代码规范建议

### 1. 文件命名
- ✅ 使用小写字母和连字符：`about-liu.html`
- ❌ 避免空格：`About Liu.html` → `about-liu.html`
- ✅ 图片命名：使用下划线或连字符，避免空格

### 2. 路径规范
- ✅ 始终使用相对路径
- ✅ 统一使用 `images/` 而不是多个图片文件夹
- ✅ 文件名中的空格使用URL编码或避免使用

### 3. HTML结构
- ✅ 添加语义化标签（`<header>`, `<nav>`, `<main>`, `<footer>`）
- ✅ 添加适当的`alt`属性
- ✅ 使用`<meta>`标签优化SEO

---

## 🎯 快速实施清单

**今天可以做的**（30分钟）：
- [ ] 查找替换所有 `LiuLab.html` → `index.html`
- [ ] 创建 `js/common.js` 文件
- [ ] 在至少一个HTML文件中测试 `common.js`
- [ ] 创建 `js/config.js` 配置文件

**本周可以做的**（2-3小时）：
- [ ] 将所有HTML的Header提取到 `components/header.html`
- [ ] 创建 `js/components.js` 动态加载组件
- [ ] 更新所有HTML文件使用组件系统
- [ ] 测试所有页面确保正常工作

**本月可以做的**（1-2天）：
- [ ] 重新组织图片文件夹
- [ ] 更新所有图片路径
- [ ] 优化图片大小
- [ ] 清理重复文件

---

## 💬 总结

**最重要的3项优化**：
1. **统一首页链接** - 5分钟，立即提升一致性
2. **提取公共脚本** - 30分钟，减少代码重复
3. **创建配置文件** - 30分钟，便于管理信息

这些优化将显著提升网站的可维护性，特别是当您需要更新导航栏、联系信息或添加新页面时。

---

**最后更新**：2025年1月


