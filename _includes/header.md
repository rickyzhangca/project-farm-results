
<header class="flex flex-1 flex-col p-10 bg-white">
  <div class="flex flex-1">
    <nav class="flex flex-col" role="navigation">
      <div class="flex flex-col items-start">
        <a href="{{ site.url }}/" title="{{site.description}}"  class="mr-6 lg:mr-0 mb-4">
          <img src="{{ site.url }}/assets/icon/logo.svg" class="w-40">      
        </a>
        <div class="flex flex-col">
          <h1 class="lg:mb-1 text-gray-900 text-2xl font-semibold">{{site.title}}</h1>
          <p class="mb-6 lg:mb-16 text-gray-400 text-base font-semibold">Non-official</p>
        </div>
      </div>
      <p class="mb-6 lg:mb-0 text-gray-900 text-base font-regular">
        A quick way to search through the products <a class="text-red-600 hover:text-red-700 hover:no-underline" href="https://www.youtube.com/c/projectfarm" target="_blank" >Project Farm</a> tested and the results, in case if you are already inside Home Depot.<br>Saw something off? <a class="text-red-600 hover:text-red-700 hover:no-underline" href="https://github.com/rickyzhangca/project-farm-results/issues" target="_blank">Create an issue</a> so I'll fix it.
      </p>   
    </nav>
  </div>
  <div class="flex flex-row space-x-1 lg:block lg:flex-col lg:space-x-0 lg:space-y-1">
    <button class="flex justify-center items-center space-x-4 bg-red-600 hover:bg-red-700 text-white font-medium py-3 lg:py-3.5 px-4 rounded" 
    onclick=" window.open('https://www.youtube.com/c/projectfarm','_blank')">
      <img src="{{ site.url }}/assets/images/youtube.svg">
      <span class="hidden lg:block lg:ml-3">Project Farm YouTube</span>
    </button>
    <button class="flex justify-center items-center space-x-4 bg-white hover:bg-gray-100 text-gray-900 border border-gray-200 font-medium py-3 px-4 rounded" 
    onclick=" window.open('https://www.patreon.com/projectfarm','_blank')">
      <img src="{{ site.url }}/assets/images/patreon.svg">
      <span class="hidden lg:block lg:ml-3">Project Farm Patreon</span>
    </button>
    <button class="flex justify-center items-center space-x-4 bg-white hover:bg-gray-100 text-gray-900 border border-gray-200 font-medium py-3 px-4 rounded" 
    onclick=" window.open('https://project-farm.com/','_blank')">
      <img src="{{ site.url }}/assets/images/merch.svg">
      <span class="hidden lg:block lg:ml-3">Project Farm Merch</span>
    </button>
    
  </div>
</header>
