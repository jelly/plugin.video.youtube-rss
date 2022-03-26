# plugin.video.youtube-rss

Youtube RSS plugin for Kodi.

This addon expects a `subscriptions.json` file in the root directory of the
addon. The file contains the youtube RSS urls and their title as a json object
formatted as:

```
{
  "CGP Grey": "https://www.youtube.com/feeds/videos.xml?channel_id=UC2C_jShtL725hvbm1arSV9w"
}
```

Where the channel id can be obtained by clicking on the channel icon from a
youtube video, it should go to this
[url](https://www.youtube.com/channel/UC2C_jShtL725hvbm1arSV9w). Of which the
last part is the channel id.

The Youtube RSS feed is limited to 15 items, so the addon only shows the last 15 videos.
