# 多多速记 · AI 录音转写

免费、零配置的录音转写与 AI 撰写工具。单文件 HTML 应用，支持 PWA 离线安装。

## 功能

- 🎙️ **一键录音**：实时频谱、暂停/继续、时长统计
- 📝 **实时转写**：浏览器内置语音识别（Web Speech API），中文免费转文字，带时间戳分段
- ✨ **AI 撰写**：润色全文 / 生成会议纪要 / 提取待办（接入 Kimi / Moonshot 等 OpenAI 兼容 API，Kimi 有免费额度）
- 🗂️ **记录库**：搜索、回放音频、编辑转写、导出 TXT / Markdown、复制全文
- 🔒 **本地存储**：数据全部存在浏览器 IndexedDB，不上传服务器
- 📴 **PWA**：可添加到手机主屏，离线可用

## 使用

### 本地运行

```bash
cd voice-scribe
python3 -m http.server 8080
# 浏览器打开 http://localhost:8080
```

### 部署（GitHub Pages）

```bash
git init && git add -A && git commit -m "init"
git remote add origin git@github.com:<user>/voice-scribe.git
git push -u origin main
# 仓库 Settings → Pages → 选择 main 分支
```

## 配置 AI（可选）

设置 → 启用 AI 功能 → 选择 Kimi Code（`sk-kimi-` 开头的 Key）或 Kimi 开放平台 → 填入 API Key。

- **Kimi Code**：直接使用 Kimi 编程版订阅的 Key（`sk-kimi-` 开头），无需另行购买
- **Kimi 开放平台**：访问 https://platform.moonshot.cn/ → 注册/登录 →「API Keys」→ 创建（有免费额度）

## 浏览器兼容性

| 功能 | Chrome/Edge | Safari | 说明 |
|---|---|---|---|
| 录音 | ✅ | ✅ | 需授权麦克风 |
| 语音转写 | ✅ | ⚠️ 部分 | 依赖 Web Speech API，需联网 |

Android WebView（Capacitor 打包）不支持 Web Speech API，后续需接原生语音识别插件或云端 ASR。

## 文件结构

```
voice-scribe/
├── index.html      # 应用本体（Vue 3 + Tailwind，单文件）
├── manifest.json   # PWA 配置
├── sw.js           # Service Worker 离线缓存
├── icon-192.png    # 图标
├── icon-512.png
└── make_icons.py   # 图标生成脚本
```

## 技术栈

Vue 3 · Tailwind CSS · dayjs · idb-keyval (IndexedDB) · Web Speech API · MediaRecorder · OpenAI 兼容 API
