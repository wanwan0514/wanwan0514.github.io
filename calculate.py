"""
---
layout: post
title: "导随记录1153"
date: 2024-04-06 00:00:00 +0800
categories: [导随, 学者]
tags: [导随]
author: wanwan
toc: true
comments: true
pin: true
---

---
layout: post
title: 导随记录990
date: 2024-03-16 09:16:12
categories:
  - 导随
  - 学者
tags:
  - 导随
pin: true
toc: true
comments: true
---
"""



import os

jobs = []
dates = []

for file_name in os.listdir("_posts"):
    file_path = os.path.join("_posts", file_name)
    if os.path.isfile(file_path) and (file_name.endswith(".md") or file_name.endswith("markdown")):
        with open(file_path, 'r') as f:
            raw = f.readlines()
            categ = raw[4]
            categ = categ.rstrip(']\n').lstrip('categories: [')
            try:
                _, role = categ.split(', ')
            except:
                role = raw[6].lstrip('  - ').rstrip('\n')
            jobs.append(role)

            date = raw[3]
            date = date.lstrip('date: ').split(' ')[0]
            yyyy, mm, dd = date.split('-')
            if len(mm) < 2:
                mm = "0" + mm
            dates.append(yyyy + '-' + mm)
            

from collections import Counter

job_counts = Counter(jobs)
date_counts = Counter(dates)

'''
```mermaid
pie
    title 导随职业分布
    "白魔": 37
    "贤者": 486
    "学者": 64
```

```mermaid
xychart-beta
    title "导随统计情况"
    x-axis [2023-11, 2023-12, 2024-1]
    y-axis "导随次数" 0 --> 500
    bar [205, 345, 37]
```
'''

for job in job_counts:
    print(f'"{job}": {job_counts[job]}')
    
    
xychart_x = "x-axis ["
xychart_y = "bar ["

for date, count in sorted(date_counts.items()):
    xychart_x += date + ', '
    xychart_y += str(count) + ', '
xychart_x = xychart_x.rstrip(", ") + "]"
xychart_y = xychart_y.rstrip(", ") + "]"

print(xychart_x)
print(xychart_y)


