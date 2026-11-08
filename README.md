<a id="top"></a>

<div align="center">

# 跟进宝 · Followup

### 客户再多，关键跟进不漏。

面向保险顾问的客户跟进工作台，让每次沟通都有记录，让下一步行动有着落。

**[立即体验 ↗](https://sgogl91sm8dfmb051cntr.apigateway-cn-beijing.volceapi.com/?v=c6b547b)** · **[观看介绍](#product-video)** · **[快速上手](#quick-start)**

`今日行动`　`客户时间轴`　`跟进建议`　`移动端适配`

</div>

<p align="center">
  <img src="https://github.com/user-attachments/assets/87ead5be-6bee-4cd5-955a-d5e769065cef" alt="跟进宝宣传海报：客户再多，关键跟进不漏。今日行动、客户时间轴与跟进建议，让每一次跟进都有下一步。" width="100%" />
</p>

<p align="center"><strong>让每一次跟进，都有下一步。</strong></p>

<a id="product-video"></a>

## 20 秒，认识跟进宝

https://github.com/user-attachments/assets/0e32f097-5ea3-4729-9cdc-3a408cf9fe24

<p align="center">
  <a href="https://sgogl91sm8dfmb051cntr.apigateway-cn-beijing.volceapi.com/?v=c6b547b"><strong>打开在线演示，亲自体验 →</strong></a>
</p>

> 视频与海报展示产品方向；当前仓库为可交互原型。页面中的跟进建议由内置规则生成，尚未接入真实 AI 模型。

## 把分散的跟进，放回一条清晰的行动线

客户多了以后，难记住的往往不只是名字：**今天该联系谁、上次聊到哪里、下一次准备做什么**，都需要随时找得到。

跟进宝围绕这三个问题，把客户信息、沟通记录和提醒连接起来。

<table>
  <tr>
    <td width="33%" valign="top">
      <h3>01 · 今日行动</h3>
      <p><strong>今天先跟谁，一眼看清。</strong></p>
      <p>集中查看逾期、今日和待安排事项，结合优先级决定先联系哪位客户。</p>
    </td>
    <td width="33%" valign="top">
      <h3>02 · 客户时间轴</h3>
      <p><strong>每次沟通，随时回顾。</strong></p>
      <p>把客户摘要、沟通记录、阶段变化与下一次动作放在同一个客户档案里。</p>
    </td>
    <td width="33%" valign="top">
      <h3>03 · 跟进建议</h3>
      <p><strong>下一步怎么跟，心中有数。</strong></p>
      <p>查看建议动作与异议场景话术，按实际情况编辑，再由顾问确认并安排时间。</p>
    </td>
  </tr>
</table>

## 从一次沟通，到下一次行动

| ① 建立客户 | ② 记录沟通 | ③ 确认下一步 | ④ 回看与复盘 |
| :--- | :--- | :--- | :--- |
| 填写客户摘要、阶段和优先级 | 留下沟通方式、结果与关键内容 | 确认动作和时间，形成下一次提醒 | 从今日行动进入任务，回看时间轴与跟进趋势 |

**建议体验路径：** 打开示例客户 → 查看历史记录 → 记录一次跟进 → 安排下一次动作 → 返回首页查看提醒。

## 你可以在演示里体验什么？

| 功能 | 具体体验 |
| :--- | :--- |
| **今日跟进** | 逾期 / 今日 / 待安排入口、优先联系清单、优先级筛选 |
| **客户管理** | 新增、搜索、阶段与优先级、客户摘要、详情时间轴 |
| **沟通记录** | 电话 / 微信 / 会议 / 邮件，记录结果，编辑历史记录 |
| **提醒与日历** | 安排下一次时间和动作，按日期查看跟进事项 |
| **建议与话术** | 规则演示、异议场景、自定义异议、可编辑建议与话术 |
| **跟进复盘** | 客户阶段分布、去重跟进统计、近 7 天 / 近 6 个月趋势 |
| **手机与电脑** | 手机直接全屏显示，电脑保留模拟手机交互预览 |

<a id="quick-start"></a>

## 立即开始

**只想体验产品？** [点击打开在线演示](https://sgogl91sm8dfmb051cntr.apigateway-cn-beijing.volceapi.com/?v=c6b547b)，手机和电脑都可以访问。

**想在本地运行？** 下载仓库后，直接打开 `index.html`。无需安装前端依赖，也无需配置 API Key。

<details>
<summary><strong>开发者入口：本地服务、构建与目录说明</strong></summary>

### 启动本地服务

```sh
git clone https://github.com/yilin6868/followup.git
cd followup
python3 -m http.server 8000
```

浏览器打开 [http://localhost:8000](http://localhost:8000)。

### 修改与构建

```sh
python3 tools/genjin/build.py
cp tools/genjin-mvp.html index.html
```

构建器把脚本、样式与运行时内联为单个 HTML。橙色主题、状态栏及手机全屏入口在 `tools/genjin/build.py` 中调整。

```text
followup/
├── index.html                  # 可直接打开、可部署的单文件页面
├── README.md                   # 产品介绍与使用说明
└── tools/genjin/
    ├── build.py                # 主题、适配与打包逻辑
    ├── dashboard.js            # 交互脚本
    ├── styles.css              # 基础样式
    ├── *runtime.js             # 浏览器运行时
    └── THIRD_PARTY_NOTICES.md   # 来源与第三方声明
```

构建产物可部署至静态托管服务；当前在线演示部署在火山引擎。

</details>

## 关于当前版本

- **可交互演示：** 内置虚拟客户，用于体验跟进流程；尚未生成微信小程序。
- **浏览器本地存储：** 记录保存在当前浏览器的 `localStorage`，不同浏览器或域名之间不自动同步，没有云端客户账户或 CRM 同步。
- **顾问确认行动：** 跟进建议与话术为内置规则演示，未接入真实模型，也不学习语言偏好；实际沟通内容与后续安排由使用者确认。
- **语音按需使用：** 语音输入依赖浏览器支持与用户授权，不支持时可直接输入文字。

<details>
<summary><strong>来源与第三方声明</strong></summary>

相关素材与代码的原有权利和条款继续适用；React 运行时保留 MIT 许可。

详见 [THIRD_PARTY_NOTICES.md](tools/genjin/THIRD_PARTY_NOTICES.md)。宣传海报和介绍视频由项目维护者提供。

</details>

---

<p align="center">
  <strong>记住关键节点，把下一步留在计划里。</strong><br />
  <a href="https://sgogl91sm8dfmb051cntr.apigateway-cn-beijing.volceapi.com/?v=c6b547b">体验跟进宝</a> · <a href="#product-video">再看一遍介绍</a> · <a href="#top">回到顶部 ↑</a>
</p>
