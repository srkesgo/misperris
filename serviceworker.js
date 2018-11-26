var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/core/css/estilos.css',
    '/static/core/img/adoptados/Tom.jpg.',
    '/static/core/img/adoptados/Apolo.jpg',
    '/static/core/img/adoptados/Duque.jpg',
    '/static/core/img/logo.png',
    '/static/core/img/social-inst.png',
    '/static/core/img/social-twitter.png',
    '/static/core/img/socialfacebook.png',
    '/static/core/img/socialplus.png',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.css',
    'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js',
    '/static/core/js/inicializacion.js'
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event){
    event.respondWith(
        caches.match(event.request).then(function(response) {
            if(response) {
                return response;
            }

            return fetch(event.request);
        })
    );
});


importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var config = {
    apiKey: "AIzaSyDEaPMZ38uq2DwIhEpsOXDSRZ737XvsN1Q",
    authDomain: "MisPerris-43afc.firebaseapp.com",
    databaseURL: "https://MisPerris-43afc.firebaseio.com",
    projectId: "MisPerris-43afc",
    storageBucket: "MisPerris-43afc.appspot.com",
    messagingSenderId: "393993915876"
};
firebase.initializeApp(config);

const messaging = firebase.messaging();

//programamos una funcion que estara escuchando cuando llegue una
//notificacion desde firebase

messaging.setBackgroundMessageHandler(function(payload) {

    //el payload contendrá el mensaje destinado al usuario
    var title = "notificacion"
    var options = {
        body:"este es el cuerpo del mensaje"
    }

    //mostramos la notificacion al usuario
    return self.registration.showNotification(title, options);

})
