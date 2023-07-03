const CACHE_NAME = 'timetable'
const OFFLINE_URL = '/static/offline.html'


self.addEventListener('install', function(event) {
    event.waitUntil(
      caches.open(CACHE_NAME)
        .then(function(cache) {
          return cache.addAll([
            '/static/css/index.css',
            '/static/js/app.js',
            '/static/img/books.svg',
            // '/static/img/dash-icon-01.svg',
            '/static/img/dash-icon-03.svg',
            '/static/img/loader.svg',
            '/static/img/login.png',
            '/static/img/logo.png',
            '/static/img/social-icon-01.svg',
            '/static/img/social-icon-02.svg',
            '/static/img/social-icon-03.svg',
            '/static/img/social-icon-04.svg',
            '/static/img/teacher.svg',
            '/static/vendor/bootstrap/bootstrap.min.css',
            '/static/vendor/animate/animate.css',
            '/static/vendor/chartjs/chartjs.min.js',
            '/static/vendor/bootstrap/bootstrap.min.js',
            '/static/vendor/sweetalert/sweetalert2.min.css',
            '/static/vendor/sweetalert/sweetalert2.all.min.js',
            '/static/vendor/jquery/jquery.js',
            '/static/offline.html',
            new Request(OFFLINE_URL, { cache: "reload"}),
          ]);
        })
    );
    self.skipWaiting()
  });
 
self.addEventListener("activate", (event) => {
  event.waitUntil(
    (async () => {
      // Enable navigation preload if it's supported.
      // See https://developers.google.com/web/updates/2017/02/navigation-preload
      if ("navigationPreload" in self.registration) {
        await self.registration.navigationPreload.enable();
      }
    })()
  );

  // Tell the active service worker to take control of the page immediately.
  self.clients.claim();
});

self.addEventListener("fetch", (event) => {
  // Only call event.respondWith() if this is a navigation request
  // for an HTML page.
  if (event.request.mode === "navigate") {
    event.respondWith(
      (async () => {
        try {
          // First, try to use the navigation preload response if it's
          // supported.
          const preloadResponse = await event.preloadResponse;
          if (preloadResponse) {
            return preloadResponse;
          }

          // Always try the network first.
          const networkResponse = await fetch(event.request);
          return networkResponse;
        } catch (error) {
          // catch is only triggered if an exception is thrown, which is
          // likely due to a network error.
          // If fetch() returns a valid HTTP response with a response code in
          // the 4xx or 5xx range, the catch() will NOT be called.
          console.log("Fetch failed; returning offline page instead.", error);

          const cache = await caches.open(CACHE_NAME);
          const cachedResponse = await cache.match(OFFLINE_URL);
          return cachedResponse;
        }
      })()
    );
  }

  // If our if() condition is false, then this fetch handler won't
  // intercept the request. If there are any other fetch handlers
  // registered, they will get a chance to call event.respondWith().
  // If no fetch handlers call event.respondWith(), the request
  // will be handled by the browser as if there were no service
  // worker involvement.
});