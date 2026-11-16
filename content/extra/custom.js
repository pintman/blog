// Externe Links in neuem Fenster/Tab öffnen
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('a[href^="http"]').forEach(function (a) {
    if (a.hostname !== location.hostname && a.hostname !== 'blog.bakera.de') {
      a.target = '_blank';
      a.rel = (a.rel ? a.rel + ' ' : '') + 'noopener noreferrer';
    }
  });
});
