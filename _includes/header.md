
<header class="flex flex-1 flex-col p-10 bg-white">
  <div class="flex flex-1">
    <nav class="" role="navigation">
      <a href="{{ site.github.url }}/" title="{{site.description}}">
        <img src="{{ site.github.url }}/assets/icon/logo.svg" class="w-40 mb-8">      
      </a>
      <h1 class="mb-1 text-gray-900 text-2xl font-semibold">{{site.title}}</h1>
      <p class="mb-16 text-gray-400 text-base font-semibold">Non-official</p>
      <p class="text-gray-900 text-base font-regular">
        A quick way to search through the products <a class="text-red-600 hover:text-red-700 hover:no-underline" href="https://www.youtube.com/c/projectfarm" target="_blank" >Project Farm</a> tested and the results, in case if you are already inside Home Depot.<br>Saw something off? <a class="text-red-600 hover:text-red-700 hover:no-underline" href="https://github.com/rickyzhangca/project-farm-results/issues" target="_blank">Create an issue</a> so I'll fix it.
      </p>
      <!--
      <ul class="flex mt-8 sm:mt-0 space-x-4 items-center self-center">
        {% for item in site.data.navigation %}
        <li>
          <a
            href="{{ site.github.url }}{{item.url}}"
            title="{{item.title}}"
            class="capitalize py-1 text-blue-500 hover:text-blue-700 no-underline hover:underline"
            >{{item.name}}</a
          >
        </li>
        {% endfor %}
      </ul>
      -->      
    </nav>
  </div>
  <div class="space-y-1">
    <button class="flex justify-center items-center space-x-4 bg-red-600 hover:bg-red-700 text-white font-medium py-3.5 px-4 rounded" 
    onclick=" window.open('https://www.youtube.com/c/projectfarm','_blank')">
      <img class="mr-3" src="/assets/images/youtube.svg">
      Project Farm YouTube
    </button>
    <button class="flex justify-center items-center space-x-4 bg-white hover:bg-gray-100 text-gray-900 border border-gray-200 font-medium py-3 px-4 rounded" 
    onclick=" window.open('https://www.patreon.com/projectfarm','_blank')">
      <img class="mr-3" src="/assets/images/patreon.svg">
      Project Farm Patreon
    </button>
    <button class="flex justify-center items-center space-x-4 bg-white hover:bg-gray-100 text-gray-900 border border-gray-200 font-medium py-3 px-4 rounded" 
    onclick=" window.open('https://project-farm.com/','_blank')">
      <img class="mr-3" src="/assets/images/merch.svg">
      Project Farm Merch
    </button>
  </div>
</header>
