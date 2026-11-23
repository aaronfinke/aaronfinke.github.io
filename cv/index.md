---
layout: page
title: Curriculum Vitae
permalink: /cv/
lead: Aaron D. Finke, Ph.D. · Data Management and Scientific Computing, European Spallation Source
---

<p class="cv-contact">
  {% include email.html reveal=true label="show email address" %} ·
  <a href="https://orcid.org/{{ site.author.orcid }}">ORCID {{ site.author.orcid }}</a> ·
  <a href="https://github.com/{{ site.author.github }}">GitHub</a>
</p>

<section class="cv-section">
<h2>Professional experience</h2>
{% for e in site.data.cv.experience %}
<div class="cv-row">
  <div class="cv-date">{{ e.dates }}</div>
  <div class="cv-body">
    <div class="cv-title">{{ e.role }}</div>
    <div class="cv-place">{{ e.place }}</div>
    {% if e.detail %}<div class="cv-detail">{{ e.detail }}</div>{% endif %}
  </div>
</div>
{% endfor %}
</section>

<section class="cv-section">
<h2>Education</h2>
{% for e in site.data.cv.education %}
<div class="cv-row">
  <div class="cv-date">{{ e.dates }}</div>
  <div class="cv-body">
    <div class="cv-title">{{ e.degree }}</div>
    <div class="cv-place">{{ e.place }}</div>
    {% if e.detail %}<div class="cv-detail">{{ e.detail }}</div>{% endif %}
  </div>
</div>
{% endfor %}
</section>

<section class="cv-section">
<h2>Awards</h2>
{% for e in site.data.cv.awards %}
<div class="cv-row">
  <div class="cv-date">{{ e.dates }}</div>
  <div class="cv-body">{{ e.text }}</div>
</div>
{% endfor %}
</section>

<section class="cv-section">
<h2>Professional societies</h2>
{% for e in site.data.cv.societies %}
<div class="cv-row">
  <div class="cv-date">{{ e.dates }}</div>
  <div class="cv-body">{{ e.role }}</div>
</div>
{% endfor %}
</section>

<section class="cv-section">
<h2>Teaching</h2>
{% for e in site.data.cv.teaching %}
<div class="cv-row">
  <div class="cv-date">{{ e.dates }}</div>
  <div class="cv-body">
    <div class="cv-title">{{ e.role }}</div>
    <div class="cv-place">{{ e.place }}</div>
  </div>
</div>
{% endfor %}
</section>

<section class="cv-section">
<h2>Presentations</h2>
<ul class="cv-list">
{% for e in site.data.cv.presentations %}
  <li><span class="badge badge-{{ e.kind | downcase }}">{{ e.kind }}</span> {{ e.text }}</li>
{% endfor %}
</ul>
</section>

<section class="cv-section">
<h2>Patents</h2>
<ul class="cv-list">
{% for e in site.data.cv.patents %}<li>{{ e.text }}</li>{% endfor %}
</ul>
</section>

<section class="cv-section">
<h2>Publications</h2>
<p>{{ site.data.publications.size }} publications, listed on the <a href="{{ '/publications/' | relative_url }}">publications page</a>.</p>
</section>

<section class="cv-section">
<h2>Languages</h2>
<p>{{ site.data.cv.languages | join: " · " }}</p>
</section>
