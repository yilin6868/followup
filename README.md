# 跟进宝 Followup

面向寿险顾问的客户跟进交互原型：把客户、沟通记录、下一次动作和提醒放在一个工作台里。

[在线体验](https://sgogl91sm8dfmb051cntr.apigateway-cn-beijing.volceapi.com/?v=mobile2)

## 功能

- 今日行动：逾期、今日、待安排清单和优先级筛选。
- 客户管理：新增、搜索、客户阶段、优先级与详情时间轴。
- 跟进记录：沟通方式、结果、摘要、下一次动作和提醒时间。
- 日历与复盘：日期安排、客户阶段分布、去重跟进趋势。
- 话术建议：规则演示、异议场景和可编辑建议。
- 手机全屏适配；电脑保留模拟手机预览。

## 本地运行

直接打开 `index.html`，无需安装依赖或配置密钥。也可运行：

```sh
python3 -m http.server 8000
```

打开 http://localhost:8000 。

## 修改与构建

```sh
python3 tools/genjin/build.py
cp tools/genjin-mvp.html index.html
```

`tools/genjin` 保存公开参考页的浏览器脚本、样式、运行时和本地构建器。橙色主题、状态栏和手机全屏入口在 `build.py` 中调整。构建产物为单个 HTML，可部署到静态托管或火山引擎函数服务。

## 当前边界

当前是交互演示，内置虚拟客户；数据保存在当前浏览器的 localStorage，不同域名或浏览器不会同步。话术由内置规则生成，未接入真实模型，也不学习语言偏好。语音输入依赖浏览器能力和用户授权。手机外观不代表微信小程序版本已开发。

## 来源与第三方声明

页面与交互依据用户提供的参考站 https://genjinbao-followup.chinajuan520.chatgpt.site/ 还原，另做橙色主题、手机适配和重置数据修正。相关素材与代码的原有权利和条款继续适用；React 运行时保留 MIT 许可。详见 [第三方声明](tools/genjin/THIRD_PARTY_NOTICES.md)。
