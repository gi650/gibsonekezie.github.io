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
  - name: The Goal of Asyncio
  - name: Event Loop
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

It's going to be **legend .. a..**
<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/post/awaited/wait-for-it-barney-stinson.gif" class="img-fluid z-depth-1" zoomable=true %}
    </div>
</div>
**ryy!!**

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

When you call the function you just created, it executes the print function;

```python
ready_player_one()
This player exists in virtual world attacked by robots
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

Asyncio is a standard library framework for writing concurrent code in python. The main function of asyncio is to maximize usage of a single thread by handling I/O asynchronously and enabling concurrent code execution using coroutines. Another way to think of it is asyncio pads the gaps in a running thread with other concurrent tasks.

Now if you take a min to digest what you just read about a asyncio; you'll come up with similar questions like _How ? How does asyncio perform this ? what powers the asyncio framework ?_
This simple answer to both questions is **EVENT LOOP**

## Event Loop

The event loop is the engine inside asyncio that runs and schedules tasks. It contains a collection of jobs to be run. You can think of the collection of jobs as a queue where jobs are added by you and some by asyncio. Then the jobs are processed one at a time but not always in order(If have you expertise in AWS this should remind you of the Amazon SQS standard queue != FIFO).
The event loop takes a job from it's collection of jobs, invokes it then gives it control (similar to a calling a function). Then the job runs, once it pauses or stops it gives control back to the event loop. In football terms, the Event loop is the Messi in your team, he gives you the ball to do your tomfoolery then you return the ball to him to make the play.
This process continues indefinitely until there are no more jobs and the event loop is smart enough to rest and avoid wasting resources. The event loop will resume once there are more jobs to run.
_I know what you're thinking, all this attributes sounds a little bit too familiar what if your AI agent runtime is just one smartass event loop ? you're probably right_

**NOTE:**
Effective execution still relies on jobs sharing well and cooperating, a greedy job could easily hog control and leave other jobs to starve. Control doesn't always get ceded back to event loop but I'll touch more on that in the coming sections.

## Async Function

I want us to cover the basic tenants of the laws that govern an async function:

- It is defined using async def and can await expressions.
- It cannot be called directly from the async.run function. (async.run function is how you execute async code)
- Async function is a function that creates coroutines when called.

## Coroutines

- Object created by calling an async function.
- Can be called directly from the async.run function.
- Can be run only once.
- Is an awaitable object.

**Interesting Side Notes about Coroutine:**
The clear distinction between coroutine object (synonymous to coroutine) and coroutine function

| **Term**           | **What it is**                     | **How you get it**          | **How you inspect it**                    | **Lifecycle**                            |
| ------------------ | ---------------------------------- | --------------------------- | ----------------------------------------- | ---------------------------------------- |
| Coroutine function | An async def function definition   | Write async def work(): ... | inspect.iscoroutinefunction(work) -> True | Reusable callable; called many times     |
| ---                | ---                                | ---                         | ---                                       |                                          |
| Coroutine object   | A pauseable execution frame/object | Call coro = work()          | inspect.iscoroutine(coro) -> True.        | Single-use; must be awaited or scheduled |

Coroutines evolve from generators. Similar to coroutines functions, calling a generator function does not run it, it generates a generator object. Yield expressions and statements are only used when defining generator functions and are only in the body of a generator function. From this you can infer that the difference between a regular function and a generator function is the presence of yield expressions. If you yield directly within a coroutine function the coroutine function becomes an async generator function. "Yield from" is not allowed in coroutines, it creates a syntax error.

_For more information on the history of coroutines I suggest you check out Lukasz Langa's video from EdgeDB [Import Asyncio](https://www.youtube.com/watch?v=Xbl7XjFYsN4&list=PLhNSoGM2ik6SIkVGXWBwerucXjgP1rHmB&index=1)_

## Task

Task is a coroutine(not a coroutine function) tied to the event loop. A task also maintains a list of callbacks functions. Creating a task automatically schedules it for execution by adding a callback to run it, in the event loop's (*Collection of jobs).
This is the recommended way to create a task:

```python
asyncio.create_task()
```

A good way to think of a task is to identify it as a wrapper for coroutines. Remember a task itself is not added to the event loop only a callback to the task is added.

## Await

Can be used either as an awaited task or an awaited coroutine. For awaited task, the awaited task adds a callback of the original task or coroutine to the event loop.
For awaited coroutine, unlike the awaited task the behavior of the awaited coroutine is effectively the same as calling a regular synchronous python function (Remember when I told you that not all jobs cede control back to the event loop).

| **Field**               | **Awaited Coroutine**                           | **Awaited Task**                                                 |
| ----------------------- | ----------------------------------------------- | ---------------------------------------------------------------- |
| **Behavior**            | await coro() (Awaited Coroutine)                | t = asyncio.create_task(coro()) ... await t (Awaited Task)       |
| **When it starts**      | Immediately upon reaching await coro()          | Scheduled on the event loop as soon as create_task() is called   |
| **Overlap with caller** | None—caller waits until coro() finishes         | Can run concurrently while caller does other work before await t |
| **Can be cancelled ?**  | Only indirectly by cancelling the awaiting task | Yes—t.cancel() can cancel the task directly                      |
| **Best when..**         | You genuinely need the result before moving on. | You want work to start now and collect the result later          |
