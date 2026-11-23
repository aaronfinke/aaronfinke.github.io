---
layout: page
title: Blog
permalink: /blog/
lead: Short technical notes, statistics and slides. Newest first.
---

<ul class="post-list">
  {% for post in site.posts %}
  <li>
    <span class="post-meta">{{ post.date | date: "%-d %B %Y" }}</span>
    <h3><a href="{{ post.link | default: post.url | relative_url }}">{{ post.title | escape }}</a></h3>
    {% if post.excerpt %}<p>{{ post.excerpt | strip_html | truncatewords: 35 }}</p>{% endif %}
  </li>
  {% endfor %}
</ul>

<p class="subscribe"><a href="{{ '/feed.xml' | relative_url }}">Subscribe via RSS</a></p>
