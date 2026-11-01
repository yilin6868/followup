#!/usr/bin/env python3
"""Build the reference-aligned app as one offline, double-clickable HTML file.

The reference's public browser bundles and CSS are kept beside this script.
No remote scripts, module loader, package installation or server is required.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent / "genjin-mvp.html"


def read(name):
    return (ROOT / name).read_text(encoding="utf-8")


def scope(source, imports, exports):
    source = re.sub(r'^import[^;]+;', '', source)
    source = re.sub(r'^import[^;]+;', '', source)
    match = re.search(r'export\{[^}]+\};?\s*$', source)
    if not match:
        raise ValueError("Unexpected public bundle export layout")
    return "(()=>{\n" + imports + "\n" + source[:match.start()] + "\nreturn " + exports + ";\n})()"


runtime = scope(read("module-runtime.js"), "", "{r:l,t:o}")
framework = scope(read("react-runtime.js"), "const e=ModuleRuntime.t;", "{react:i,jsx:n,dom:u}")
dashboard = scope(read("dashboard.js"),
                  "const e=ModuleRuntime.r,t=ReactRuntime.jsx,n=ReactRuntime.react;",
                  "T")
# Keep reference/demo storage separate from the existing v0.2 customer data.
dashboard = dashboard.replace('genjinbao-interview-demo-v1', 'genjinbao-local-v3')
# The public reference's reset handler switches to unrelated B2B samples.
# Reset to the same insurance demo dataset shown on first launch instead.
old_reset = 'function ke(){t&&(D(te()),'
if old_reset not in dashboard:
    raise ValueError("Reference reset handler changed; review before rebuilding")
dashboard = dashboard.replace(old_reset, 'function ke(){t&&(D(re()),', 1)
# Orange palette follows the supplied product screenshot, including alpha variants.
palette = {
    '#557bc3':'#c3480b', '#4569af':'#a93c08', '#4c6fb3':'#b6410a',
    '#6387ca':'#d86425', '#8ea8d8':'#eaa269', '#91aad8':'#eca168',
    '#edf1fa':'#fff1e5', '#edf1f9':'#fff1e5', '#e9edf7':'#fce8d7',
    '#c7d3ec':'#f2bb94', '#d2dbed':'#f2bb94', '#d5def0':'#f5c8aa',
    '#d6dff0':'#f5c8aa', '#dae2f3':'#f5d4bc', '#dce3f1':'#f5d4bc',
    '#eff1f7':'#fff4e8', '#f1f2f5':'#fcf1e6',
}
css = read("styles.css")
css = re.sub(r'#[0-9a-fA-F]{6}(?:[0-9a-fA-F]{2})?\b',
             lambda m: palette.get(m.group()[:7].lower(), m.group()[:7]) + m.group()[7:], css)
css = re.sub(r'^@import\s+"[^"]*"\s*;', '', css)
# Offline system-font fallback; the source uses Google-hosted DM Sans/Noto Sans SC.
css += '\nbody{font-family:"DM Sans","Noto Sans SC",-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;line-height:1.4}\n'
css += '\n.statusIndicators{display:flex;align-items:center;gap:6px;font-size:12px;line-height:1}.statusIndicators svg{display:block}.statusNetwork{font-weight:600}.statusBattery{position:relative;width:27px;height:14px;border-radius:4px;background:#d8cec2;color:#302d27;text-align:center;font-size:10px;font-weight:800;line-height:14px;isolation:isolate}.statusBattery:before{content:"";position:absolute;inset:0 auto 0 0;width:64%;background:#302d27;border-radius:4px 0 0 4px;z-index:-1}.statusBattery:after{content:"";position:absolute;right:-3px;top:4px;width:2px;height:6px;background:#968d82;border-radius:0 2px 2px 0}.statusBattery span{position:absolute;inset:0;display:block;color:#fff;text-shadow:1px 0 #302d27,-1px 0 #302d27,0 1px #302d27,0 -1px #302d27;line-height:14px;font-size:10px;letter-spacing:0}\n'
css += '\nhtml.appViewport,html.appViewport body{min-height:100%;background:#f6f3ed}html.appViewport .shell{min-height:100dvh}html.appViewport .content{padding-bottom:calc(110px + env(safe-area-inset-bottom,0px))}@media(max-width:600px){html.appViewport .shell{width:100%;max-width:none;box-shadow:none}html.appViewport .mobileNav{width:100%;max-width:none}html.appViewport .content{padding-top:max(22px,env(safe-area-inset-top,0px));padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}\n'
entry = r'''
const isApp = new URL(location.href).searchParams.get('view') === 'app' || matchMedia('(max-width: 600px)').matches;
if (isApp) {
  document.documentElement.classList.add('appViewport');
  ReactRuntime.dom().createRoot(document.getElementById('app')).render(
    ReactRuntime.react().createElement(Dashboard,{demo:true,user:{name:'本地演示',email:'demo@example.invalid'}})
  );
} else {
  document.getElementById('app').innerHTML = `<main class="phoneStage">
    <div class="phoneCaption"><strong>跟进宝</strong><span>小程序界面 · 交互预览</span></div>
    <div class="phoneDevice">
      <div class="phoneStatus"><span>9:41</span><span class="statusIndicators" role="img" aria-label="信号满格，5G，电量64%"><svg width="18" height="14" viewBox="0 0 18 14" aria-hidden="true"><rect x="0" y="10" width="3" height="4" rx="1" fill="currentColor"/><rect x="5" y="7" width="3" height="7" rx="1" fill="currentColor"/><rect x="10" y="3" width="3" height="11" rx="1" fill="currentColor"/><rect x="15" width="3" height="14" rx="1" fill="currentColor"/></svg><span class="statusNetwork">5G</span><span class="statusBattery"><span>64</span></span></span></div>
      <div class="miniAppBar"><span>跟进宝</span><div aria-hidden="true"><span>•••</span><i></i><span>⊙</span></div></div>
      <iframe title="跟进宝手机交互预览"></iframe>
      <div class="phoneHome"><i></i></div>
    </div>
    <p class="phoneFootnote">可点击体验 · 示例数据仅保存在当前浏览器<br>当前为界面预览，微信小程序版本待开发</p>
  </main>`;
  const appUrl = new URL(location.href);
  appUrl.searchParams.set('view','app');
  document.querySelector('iframe').src = appUrl.href;
}
'''
script = f"const ModuleRuntime={runtime};\nconst ReactRuntime={framework};\nconst Dashboard={dashboard};\n{entry}"
script = "/*\n" + read("THIRD_PARTY_NOTICES.md") + "\n*/\n" + script
if re.search(r'</script', script, re.I):
    raise ValueError("Bundle contains an unsafe inline script terminator")
html = f'''<!doctype html>
<!-- Generated by tools/genjin/build.py. Source reference: https://genjinbao-followup.chinajuan520.chatgpt.site/ -->
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#f6f3ed">
<meta name="description" content="跟进宝：客户跟进、提醒、记录与复盘。本地交互演示。">
<title>跟进宝｜客户跟进工作台</title>
<style>{css}</style></head><body><div id="app"></div>
<noscript>请启用 JavaScript 使用客户跟进工作台。</noscript>
<script>{script}</script></body></html>
'''
OUT.write_text(html, encoding="utf-8")
print(f"Built {OUT} ({len(html.encode('utf-8')):,} bytes)")
