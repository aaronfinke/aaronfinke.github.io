---
layout: page
title: Publications
permalink: /publications/
lead: Peer-reviewed articles, book chapters and preprints. Also on <a href="https://orcid.org/0000-0002-6842-1122">ORCID</a>.
---

<div class="pub-tools">
  <input id="pub-filter" type="search" placeholder="Filter by title, author, journal or year…" aria-label="Filter publications">
  <span id="pub-count" class="pub-count">{{ site.data.publications.size }} items</span>
</div>

{% assign by_year = site.data.publications | group_by: "year" | sort: "name" | reverse %}
{% for g in by_year %}
<section class="pub-year-group">
  <h2 class="year-heading">{{ g.name }}</h2>
  <ul class="pub-list">
    {% for p in g.items %}{% include publication.html pub=p %}{% endfor %}
  </ul>
</section>
{% endfor %}

<script>
(function () {
  var input = document.getElementById('pub-filter');
  var count = document.getElementById('pub-count');
  var items = document.querySelectorAll('li.pub');
  var groups = document.querySelectorAll('.pub-year-group');
  input.addEventListener('input', function () {
    var q = input.value.trim().toLowerCase(), n = 0;
    items.forEach(function (li) {
      var year = li.closest('.pub-year-group').querySelector('.year-heading').textContent;
      var hit = !q || (li.textContent + ' ' + year).toLowerCase().indexOf(q) !== -1;
      li.hidden = !hit; if (hit) n++;
    });
    groups.forEach(function (g) { g.hidden = !g.querySelector('li.pub:not([hidden])'); });
    count.textContent = n + (n === 1 ? ' item' : ' items');
  });
})();
</script>
