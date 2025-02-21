title: How to prevent OpenAi and similar from scraping your blog
slug: how-to-prevent-openai-and-similar-from-scraping-your-blog
pub: 2024-11-05 21:27:00
authors: arj
tags: 
category: web


If you want to disable OpenAi or similar crawlers from harvesting your data, create a file called robots.txt at the root of your domain.

If your domain is `health.com`, make sure the file can be accessed at `health.com/robots.txt`

Here is the snippet i use (you can check [the site's robot.txt](/robots.txt) file here):

```txt
# Disallow OpenAI and related bots
User-agent: OpenAI
Disallow: /

User-agent: GPTBot
Disallow: /

# Disallow Google AI crawlers
User-agent: Bard
Disallow: /

# Disallow Anthropic AI
User-agent: Claude
Disallow: /

# Disallow Microsoft AI crawlers
User-agent: BingAI
Disallow: /

# Disallow CommonCrawl (often used by AI models for datasets)
User-agent: CCBot
Disallow: /

# Disallow Neeva AI (deprecated but still included for completeness)
User-agent: NeevaBot
Disallow: /

# Disallow Baidu AI
User-agent: Baiduspider
Disallow: /

# Disallow Yandex AI
User-agent: YandexBot
Disallow: /

# Disallow other common web crawlers used for AI data collection
User-agent: DuckDuckGo-Bot
Disallow: /

User-agent: AhrefsBot
Disallow: /

User-agent: MJ12bot
Disallow: /

User-agent: SemrushBot
Disallow: /

User-agent: DotBot
Disallow: /

User-agent: BLEXBot
Disallow: /

User-agent: PetalBot
Disallow: /
```
