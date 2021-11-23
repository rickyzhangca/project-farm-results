---
layout: default
---

<article class="bg-gray-100 w-full max-w-none py-8">
  <h2>
    {{ page.title | escape }}
  </h2>
  <div class="{{ page.markdown }} max-w-none text-justify leading-6 py-6">
    {{ content }}
  </div>
</article>
