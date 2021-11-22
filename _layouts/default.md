<!DOCTYPE html>
<html lang="en">  
  {% include head.md %}
  

<main class="flex flex-col h-screen">
  <div class="flex flex-1 overflow-hidden">
    <div class="flex bg-gray-100 w-32 p-4">Sidebar</div>
    <div class="flex flex-1 flex-col">
      {% include header.md %}
      {{ content }}
    </div>
  </div>
</main>
</html>