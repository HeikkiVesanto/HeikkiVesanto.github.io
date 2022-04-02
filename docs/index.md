---
layout: default
title: Home
---

Welcome to GISforThought.com.

### Featured posts:

<ul>
  {% for post in site.categories.featured %}
    {% if post.url %}
        <li>
      <a href="{{ post.url }}">{{ post.date | date: "%Y-%m-%d" }} - {{ post.title }}</a>
    </li>
    {% endif %}
  {% endfor %}
</ul>

### All posts:

<ul>
  {% for post in site.posts %}
      {% if post.url %}
    <li>
      <a href="{{ post.url }}">{{ post.date | date: "%Y-%m-%d" }} - {{ post.title }}</a>
    </li>
        {% endif %}
  {% endfor %}
</ul>

[RSS Feed](https://gisforthought.com/feed/)