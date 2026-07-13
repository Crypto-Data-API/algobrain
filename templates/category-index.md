---
title: "{{category_name}}"
type: index
created: {{date}}
updated: {{date}}
status: stub
tags: [{{tags}}, index, meta]
---

# {{category_name}}

{{Description of this category}}

## Subcategories

{{List of subcategories with links}}

## All Pages

```dataview
TABLE status, updated, tags
FROM "wiki/{{category_path}}"
WHERE type != "index"
SORT updated DESC
```
