# VSCPickup Recommendation Datas

[简体中文](./README.md) / **English**

## What is this?

This repository stores JSON data of all songs recommended in past episodes of VSCPickup programs. Combined with `https://raw.githubusercontent.com/`, it enables data retrieval.

## License

<div style="margin: 20px 0; padding: 15px; background: #f9f9f9; border-radius: 8px;">
  <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/" 
     style="display: inline-block; text-decoration: none;">
    <img alt="Creative Commons License" 
         style="border-width:0; margin-right: 10px; vertical-align: middle;" 
         src="https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-nc-sa.svg"
         width="88" height="31">
  </a>
  <div style="display: inline-block; vertical-align: middle; max-width: 600px;">
    <strong>VSCPickup Song Data</strong> is licensed under a
    <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
      Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License
    </a>.
    This means you are free to:
    <ul style="margin: 8px 0; padding-left: 20px;">
      <li><strong>Share</strong> — Copy and redistribute the material in any medium or format</li>
      <li><strong>Attribution</strong> — You must give appropriate credit and provide a link to the license</li>
      <li><strong>NonCommercial</strong> — You may not use the material for commercial purposes</li>
      <li><strong>ShareAlike</strong> — If you remix, transform, or build upon the material, you must distribute your contributions under the same license</li>
    </ul>
  </div>
</div>

[Full LICENSE](./LICENSE)

# Usage

## Query Metadata

This section contains metadata related to the VSCPickup program.

URL: `https://raw.githubusercontent.com/VSCPickup/rec-data/refs/heads/main/datas/v1/metadata.json`

Example response:

```json5
{
  "last_update": 1767246457.7084787, // Last update timestamp
  "latest_episode": 1, // Latest episode number
  "total": 1 // Total number of episodes
}
```

## View Episode Index

The episode index stores basic data for all episodes of our program.

URL: `https://raw.githubusercontent.com/VSCPickup/rec-data/refs/heads/main/datas/v1/episode/index.json`

Example response:

```json5
[
  {
    "episode": 9, // Episode number
    "timestamp": 1767280091.6040616, // Timestamp when this episode's data was generated
    "video_count": 12 // Total number of recommended videos
  }, // ... subsequent objects are the same
]
```

## View Past Recommendations

Here you can query song data from past recommendations.

Usage: Replace `{episode_number}` with the corresponding episode number.

URL: `https://raw.githubusercontent.com/VSCPickup/rec-data/refs/heads/main/datas/v1/episode/{episode_number}.json`

Example response:

Request: `https://raw.githubusercontent.com/VSCPickup/rec-data/refs/heads/main/datas/v1/episode/9.json`

```json5
{
  "metadata": { // Metadata object
    "episode": "009", // Episode number
    "timestamp": 1767280091.6040616 // Timestamp when this episode's data was generated
  },
  "videos": [ // Array of recommended video information
    {
      "type_": "Electronic", // Music genre
      "bvid": "BV1PeyYBLE44", // Video BV ID
      "title": "关于它的恐惧", // Video title
      "author": "衝泡飲品", // Author's Bilibili nickname/group name
      "drop_time": "105.0", // Start time of the highlighted clip we selected (in seconds)
      "default_cut_time": "20", // Duration we cut into the video (in seconds)
                                // From drop_time to drop_time+default_cut_time, lasting default_cut_time seconds
      "comments": [ // Array of recommendation reasons
        {
          "author": "鱼回烂片事务所", // Comment author
          "content": "这个在术力口太屈才了，应该在bof的", // Comment content
          "level": 1 // Which comment this is
        }, // ... subsequent objects are the same, comments array ends
      ],
      "publish_time": "2025-10-30T19:42:01", // Video publish time obtained from Bilibili
      "singer": "诗岸SV", // Singer information
      "video_type": "组员作品", // Video category
      "cid": 33530971733 // CID of the video we used for clipping

    }, // ... subsequent objects are the same, videos array ends
  ]
}

```

## View Latest Recommendations

Get recommendation information for the latest episode.

URL: `https://raw.githubusercontent.com/VSCPickup/rec-data/refs/heads/main/datas/v1/latest.json`

Response is consistent with [View Past Recommendations](#view-past-recommendations)
