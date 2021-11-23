<!DOCTYPE html>
<html lang="en">  
  {% include head.md %}
  <main class="flex flex-col h-screen">
    <div class="overflow-visible flex flex-col lg:flex-row lg:flex-1 lg:overflow-hidden">
      <div class="block flex flex-shrink-0 lg:w-96">
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