<!DOCTYPE html>
<html lang="en">  
  {% include head.md %}

<main class="flex flex-col h-screen">
  <div class="flex flex-1 overflow-hidden">
    <div class="flex flex-shrink-0 w-96">
      {% include header.md %}
    </div>
    <div class="flex flex-1 flex-col">
      <!-- <div class="flex bg-gray-300 h-16">Header</div> -->
      <div class="flex flex-1 overflow-y-auto paragraph">
        {{ content }}
      </div>
    </div>
  </div>
</main>
</html>