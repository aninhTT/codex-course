---
module: 8
lesson: 3
title: "Access, Secrets, And Storage"
difficulty: intermediate
prerequisites: "8.02"
---

# Lesson 8.03: Access, Secrets, And Storage

## Learn

A hosted site raises a few questions that a local prototype can ignore for a while:

- **Access:** who should be able to open the site?
- **Secrets:** what values should never be committed into source files?
- **Environment values:** what configuration does the hosted site need at runtime?
- **Storage:** does the site need to remember real data, uploaded files, or user progress?

Do not add storage just because it sounds powerful. Use it only when the product needs to remember information between visits. Do not put secrets in the repo. Ask Codex to help identify what should be configured through the hosting layer instead.

## Practice

Try this in Codex:

```text
Help me review this prototype for hosted-site concerns. Identify the intended audience, any secrets or environment values, whether it needs durable storage, and what access setting would be safest for a first review.
```

**Success criteria:** The learner can name the safest first audience, identify whether storage is needed, and avoid putting secret values in source files.
