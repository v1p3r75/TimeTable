const cache = 'timetable'
self.addEventListener('install', function(event) {
    event.waitUntil(
      caches.open(cache)
        .then(function(cache) {
          return cache.addAll([
            '/static/css/index.css',
            '/static/js/app.js',
            '/static/img/books.svg',
            '/static/img/dash-icon-01.svg',
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
            '/',
          ]);
        })
    );
  });
  self.addEventListener('activate', function(event) {
    event.waitUntil(
      caches.keys().then(function(cacheNames) {
        return Promise.all(
          cacheNames.filter(function(cacheName) {
            return cacheName.startsWith(CACHE_NAME) && cacheName !== CACHE_NAME;
          }).map(function(cacheName) {
            return caches.delete(cacheName);
          })
        );
      })
    );
  });
  
  self.addEventListener('fetch', function(event) {
    event.respondWith(
      caches.match(event.request)
        .then(function(response) {
          return response || fetch(event.request);
        })
        .catch(function() {
          return caches.match('/static/offline.html');
        })
    );
  });