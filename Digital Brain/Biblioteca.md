---
cssclass: cards
---

```dataview
table without id
("![cover|90](" + cover +")") as cover,
 ("![progress + " + (round((pageread/total)*100)) + " %](https://progress-bar.dev/" + (round((pageread/total)*100)) +"/)") as progress,
file.link as title,
author,
category,
status,
rating
FROM "Books"
```






