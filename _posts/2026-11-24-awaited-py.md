---
layout: distill
title: The Awaited Art of Async Programming in Python
description: Import asyncio
tags: Python code formatting jupyter
giscus_comments: false
date: 2026-11-24
featured: false
mermaid:
  enabled: true
  zoomable: true
code_diff: true
map: false

author:
  - name: Ekezie Gibson
    url: "https://www.gibsonekezie.com"

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

**Async Programming in Python 101**

The goal of this article is to help you build a strong mental model of asyncio.

It's going to be legend .. a..
<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/post/awaited/wait-for-it-barney-stinson.gif" class="img-fluid z-depth-1" zoomable=true %}
    </div>
</div>
ryy!!

Let’s start by differentiating synchronous code execution from asynchronous code execution

## Difference between Synchronous Code Execution and Asynchronous Code Execution

I want you to think of the difference this way, synchronous code execution is the basic python code execution we are familiar with. This means code executes in a strict sequence and the running code blocks everything else until completion (blocking behavior);

**Example of Basic Python Function (Synchronous Code)**

{::nomarkdown}
{% assign jupyter_path = 'assets/jupyter/posts/awaited/sync.ipynb' | relative_url %}
{% capture notebook_exists %}{% file_exists assets/jupyter/posts/awaited/sync.ipynb %}{% endcapture %}
{% if notebook_exists == 'true' %}
{% jupyter_notebook jupyter_path %}
{% else %}
  <p>Sorry, the notebook you are looking for does not exist.</p>
{% endif %}
{:/nomarkdown}

When you call the function you just created it performs the print function;

```python
ready_player_one()
This player exists in virtual world that is under attack by robots
```

While for asynchronous code execution .. ?
You guessed correctly! Asynchronous code execution does the opposite. It initiates tasks and continues without waiting for completion.

**Example of Asynchronous code**

{::nomarkdown}
{% assign jupyter_path = 'assets/jupyter/posts/awaited/async.ipynb' | relative_url %}
{% capture notebook_exists %}{% file_exists assets/jupyter/posts/awaited/async.ipynb %}{% endcapture %}
{% if notebook_exists == 'true' %}
{% jupyter_notebook jupyter_path %}
{% else %}
  <p>Sorry, the notebook you are looking for does not exist.</p>
{% endif %}
{:/nomarkdown}

in this case when you try to run the async function you get this instead; you realise that calling the async function does not execute the print function but it does something else. It creates a coroutine object.

```python
ready_player_two()
<coroutine object ready_player_two at 0x105e16680>
```

## The Goal of Asyncio
