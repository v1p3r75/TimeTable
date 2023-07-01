self.addEventListener('install', function(event) {
    event.waitUntil(
      caches.open('nom_cache')
        .then(function(cache) {
          return cache.addAll([
            '/static/css/font.css',
            '/static/css/index.css',
            '/static/js/app.js',
          ]);
        })
    );
  });