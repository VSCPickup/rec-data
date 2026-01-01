# VSCPickup Recommendation Datas

**简体中文** / [English](./README-en.md)

## 这是什么？

这里存储了VSCPickup往期节目推荐的所有歌曲的JSON数据，配合`https://raw.githubusercontent.com/`，实现数据的获取

## 许可证

<div style="margin: 20px 0; padding: 15px; background: #f9f9f9; border-radius: 8px;">
  <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/" 
     style="display: inline-block; text-decoration: none;">
    <img alt="Creative Commons License" 
         style="border-width:0; margin-right: 10px; vertical-align: middle;" 
         src="https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-nc-sa.svg"
         width="88" height="31">
  </a>
  <div style="display: inline-block; vertical-align: middle; max-width: 600px;">
    <strong>VSCPickup 歌曲数据</strong> 采用
    <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
      知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议
    </a>
    进行许可。这意味着您可以：
    <ul style="margin: 8px 0; padding-left: 20px;">
      <li><strong>共享</strong> — 在任何媒介以任何形式复制、发行本作品</li>
      <li><strong>署名</strong> — 必须给出署名，提供指向许可协议的链接</li>
      <li><strong>非商业性使用</strong> — 不得将本作品用于商业目的</li>
      <li><strong>相同方式共享</strong> — 如果您修改本作品，必须使用相同的协议分发</li>
    </ul>
  </div>
</div>

[Full LICENSE](./LICENSE)

# 使用

## 查询Metadata

这里存放与VSCPickup节目相关的元信息

URL:`https://raw.githubusercontent.com/VSCPickup/rec-data/refs/heads/main/datas/v1/metadata.json`

示例响应：

```json5
{
  "last_update": 1767246457.7084787, // 上次更新时间戳
  "latest_episode": 1, // 最新期数
  "total": 1 // 总计期数
}
```

## 查看期数索引

期数索引存储了我们节目所有期数的基本数据

URL:`https://raw.githubusercontent.com/VSCPickup/rec-data/refs/heads/main/datas/v1/episode/index.json`

示例响应：

```json5
[
  {
    "episode": 9, // 期号
    "timestamp": 1767280091.6040616, // 本期数据生成时间
    "video_count": 12 // 推荐视频总数
  }, // ......后续都是相同的对象
]
```

## 查看往期推荐

这里可以查询往期推荐的歌曲数据

使用方法：将`{期号}`换成对应一期的期号

URL:`https://raw.githubusercontent.com/VSCPickup/rec-data/refs/heads/main/datas/v1/episode/{期号}.json`

示例响应：

请求：`https://raw.githubusercontent.com/VSCPickup/rec-data/refs/heads/main/datas/v1/episode/9.json`

```json5
{
  "metadata": { // 元数据对象
    "episode": "009", // 本期期号
    "timestamp": 1767280091.6040616 // 本期数据生成时间
  },
  "videos": [ // 被推荐的视频信息的数组
    {
      "type_": "电子", // 曲风类型
      "bvid": "BV1PeyYBLE44", // 视频BV号
      "title": "关于它的恐惧", // 视频标题
      "author": "衝泡飲品", // 作者B站昵称/圈名
      "drop_time": "105.0", // 我们选择的精彩片段开始时间（单位秒）
      "default_cut_time": "20", // 我们截入视频的市场（单位秒）
                                // 从drop_time一直切到drop_time+default_cut_time，持续default_cut_time秒
      "comments": [ // 推荐理由数组
        {
          "author": "鱼回烂片事务所", // 推荐词作者
          "content": "这个在术力口太屈才了，应该在bof的", // 推荐词内容
          "level": 1 // 作为第几条评价
        },// .....后续都是相同的对象，comments数组结束
      ],
      "publish_time": "2025-10-30T19:42:01", // 从B站获取的视频发布时间
      "singer": "诗岸SV", // 歌姬信息
      "video_type": "组员作品", // 稿件类别
      "cid": 33530971733 // 我们截取用的稿件cid
      
    }, //.....后续皆为此对象，videos数组结束
  ]
}

```


## 查看最新推荐

获取最新一期视频的推荐信息

URL:`https://raw.githubusercontent.com/VSCPickup/rec-data/refs/heads/main/datas/v1/latest.json`

响应与[查看往期推荐](#查看往期推荐)一致