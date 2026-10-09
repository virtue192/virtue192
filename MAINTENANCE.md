# 主页维护

默认主页为 `README.md`，另有英文与三种配色组合，共六个版本。顶部语言和配色按钮会跳转至对应 README；语言切换保留配色，配色切换保留语言。

内容来源：[慢慢的个人说明书](https://moonspaceai.feishu.cn/wiki/QnwSwDygIiG7PUkklyicAjcQncg)，整理日期为 2026-10-09。这里只维护公开介绍的摘要，尚未配置自动同步飞书。不要将私人笔记或加密备份仓库加入展示。

修改 `scripts/build_profile.py` 中的 `ZH` / `EN` 文案或 `THEMES` 配色，再从仓库根目录执行：

```sh
python scripts/build_profile.py
```

六份 README 和所有 SVG 会一起更新。更新时间目前是文案中的日期，更新内容时需一起修改。

打字机标题使用仓库内 SVG / SMIL 动画，没有外部动画服务、脚本或字体请求。标题每 15 秒循环三句；不支持动画的阅读器仍显示第一句及正文介绍。GitHub README 不执行 JavaScript，配色与语言选择通过链接实现。

`assets/wechat-qr.jpg` 是用户提供的个人微信二维码原图，保留原始像素和文件内容。需要更换二维码时，用新原图覆盖该文件即可。README 中显示缩略图，点击查看完整原图。
