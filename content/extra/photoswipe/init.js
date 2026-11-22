// Lightbox (PhotoSwipe) für Bilder, die auf sich selbst verlinken: [![alt](bild)](bild)
import PhotoSwipeLightbox from './photoswipe-lightbox.esm.min.js';

const IMAGE_EXT = /\.(jpe?g|png|gif|webp|svg)$/i;

document.querySelectorAll('.entry-content a').forEach((a) => {
  const img = a.children.length === 1 ? a.querySelector(':scope > img') : null;
  if (img && IMAGE_EXT.test(a.pathname) && a.href === img.src) {
    a.classList.add('pswp-link');
  }
});

const lightbox = new PhotoSwipeLightbox({
  gallery: '.entry-content',
  children: 'a.pswp-link',
  pswpModule: () => import('./photoswipe.esm.min.js'),
  wheelToZoom: true,
  secondaryZoomLevel: 1,
  maxZoomLevel: 4,
});

lightbox.addFilter('domItemData', (itemData, element, linkEl) => {
  const img = linkEl.querySelector('img');
  itemData.w = img.naturalWidth || img.width;
  itemData.h = img.naturalHeight || img.height;
  itemData.alt = img.alt;
  return itemData;
});

lightbox.init();
