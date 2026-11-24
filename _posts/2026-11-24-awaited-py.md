---
layout: distill
title: The Awaited Art of Async Programming in Python
description: blog post to help understand asyncio
tags: distill formatting
giscus_comments: false
date: 2021-05-22
featured: true
mermaid:
  enabled: true
  zoomable: true
code_diff: true
map: true
chart:
  chartjs: true
  echarts: true
  vega_lite: true
tikzjax: true
typograms: true

author:
  - name: Ekezie Gibson
    url: "https://en.wikipedia.org/wiki/Albert_Einstein"
    affiliations:
      name: IAS, Princeton

# bibliography: 2018-12-22-distill.bib

# Optionally, you can add a table of contents to your post.
# NOTES:
#   - make sure that TOC names match the actual section names
#     for hyperlinks within the post to work correctly.
#   - we may want to automate TOC generation in the future using
#     jekyll-toc plugin (https://github.com/toshimaru/jekyll-toc).
toc:
  - name: Difference between Synchronous Code Execution and Asynchronous Code Execution
    # if a section has subsections, you can add them as follows:
    # subsections:
    #   - name: Example Child Subsection 1
    #   - name: Example Child Subsection 2
  - name: Goal of Asyncio
  - name: Async Function
  - name: Coroutines
  - name: Task
  - name: Await
  - name: Futures
  - name: Async Code Support
    subsections:
      - name: Async with
      - name: Async for
      - name: Asynchronous Generators
  - name: Reference
---

**The Awaited Art of Async Programming in Python**

The goal of this post is to get a strong mental model of asyncio.
This post is going to be legend .. a..
![wait for it](assets/img/post/awaited/wait-for-it-barney-stinson.gif)
ryy!!

Let’s start by differentiating between synchronous code execution from asynchronous code execution

## Difference between Synchronous Code Execution and Asynchronous Code Execution

Synchronous code execution is the basic python code execution we are familiar with. It means code execute in a strict sequence and the running code blocks everything else until completion (blocking behavior);
Example of Basic Python Function (Synchronous Code)

While for asynchronous code execution .. ?
You guessed correctly! Asynchronous code execution does the opposite. It initiates tasks and continues without waiting for completion.
Example of Asynchronous code

The Goal of Asyncio
