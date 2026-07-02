(function () {
  const SELECTOR = '#quarto-content img:not(.navbar-logo):not(.aoa-hero-logo):not(.no-lightbox)';
  const MIN_ZOOM = 0.5;
  const MAX_ZOOM = 4;
  const STEP = 0.25;

  let overlay;
  let image;
  let caption;
  let zoom = 1;
  let offsetX = 0;
  let offsetY = 0;
  let dragging = false;
  let dragStartX = 0;
  let dragStartY = 0;
  let dragOriginX = 0;
  let dragOriginY = 0;

  function buildOverlay() {
    overlay = document.createElement('div');
    overlay.className = 'image-viewer';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.setAttribute('aria-label', 'Image viewer');
    overlay.hidden = true;

    overlay.innerHTML = `
      <div class="image-viewer__bar">
        <div class="image-viewer__caption"></div>
        <div class="image-viewer__controls">
          <button type="button" data-action="out" aria-label="Zoom out">-</button>
          <button type="button" data-action="reset" aria-label="Reset zoom">Reset</button>
          <button type="button" data-action="in" aria-label="Zoom in">+</button>
          <button type="button" data-action="close" aria-label="Close image viewer">Close</button>
        </div>
      </div>
      <div class="image-viewer__stage">
        <img alt="">
      </div>
    `;

    image = overlay.querySelector('img');
    caption = overlay.querySelector('.image-viewer__caption');
    document.body.appendChild(overlay);

    overlay.addEventListener('click', (event) => {
      if (event.target === overlay || event.target.classList.contains('image-viewer__stage')) {
        close();
      }
    });

    overlay.querySelector('[data-action="close"]').addEventListener('click', close);
    overlay.querySelector('[data-action="in"]').addEventListener('click', () => setZoom(zoom + STEP));
    overlay.querySelector('[data-action="out"]').addEventListener('click', () => setZoom(zoom - STEP));
    overlay.querySelector('[data-action="reset"]').addEventListener('click', resetZoom);

    overlay.querySelector('.image-viewer__stage').addEventListener('wheel', (event) => {
      event.preventDefault();
      setZoom(zoom + (event.deltaY < 0 ? STEP : -STEP));
    }, { passive: false });

    image.addEventListener('pointerdown', startDrag);
    window.addEventListener('pointermove', drag);
    window.addEventListener('pointerup', stopDrag);
    window.addEventListener('keydown', handleKey);
  }

  function open(source) {
    if (!overlay) buildOverlay();

    const fullSrc = source.currentSrc || source.src;
    image.src = fullSrc;
    image.alt = source.alt || '';
    caption.textContent = source.alt || source.getAttribute('title') || 'Image';
    resetZoom();

    overlay.hidden = false;
    document.body.classList.add('image-viewer-open');
    overlay.querySelector('[data-action="close"]').focus();
  }

  function close() {
    if (!overlay || overlay.hidden) return;
    overlay.hidden = true;
    image.src = '';
    document.body.classList.remove('image-viewer-open');
  }

  function setZoom(nextZoom) {
    zoom = Math.min(MAX_ZOOM, Math.max(MIN_ZOOM, nextZoom));
    if (zoom === 1) {
      offsetX = 0;
      offsetY = 0;
    }
    updateTransform();
  }

  function resetZoom() {
    zoom = 1;
    offsetX = 0;
    offsetY = 0;
    updateTransform();
  }

  function updateTransform() {
    image.style.transform = `translate(${offsetX}px, ${offsetY}px) scale(${zoom})`;
    image.classList.toggle('is-zoomed', zoom > 1);
  }

  function startDrag(event) {
    if (zoom <= 1) return;
    dragging = true;
    dragStartX = event.clientX;
    dragStartY = event.clientY;
    dragOriginX = offsetX;
    dragOriginY = offsetY;
    image.setPointerCapture(event.pointerId);
  }

  function drag(event) {
    if (!dragging) return;
    offsetX = dragOriginX + event.clientX - dragStartX;
    offsetY = dragOriginY + event.clientY - dragStartY;
    updateTransform();
  }

  function stopDrag() {
    dragging = false;
  }

  function handleKey(event) {
    if (!overlay || overlay.hidden) return;
    if (event.key === 'Escape') close();
    if (event.key === '+' || event.key === '=') setZoom(zoom + STEP);
    if (event.key === '-' || event.key === '_') setZoom(zoom - STEP);
    if (event.key === '0') resetZoom();
  }

  function prepareImages() {
    document.querySelectorAll(SELECTOR).forEach((img) => {
      if (img.dataset.imageViewerReady === 'true') return;
      img.dataset.imageViewerReady = 'true';
      img.classList.add('image-viewer-target');
      img.setAttribute('tabindex', '0');
      img.setAttribute('role', 'button');
      img.setAttribute('title', img.getAttribute('title') || 'View larger image');
      img.addEventListener('click', () => open(img));
      img.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          open(img);
        }
      });
    });
  }

  function setPathImageExpanded(img, expanded) {
    img.classList.toggle('is-expanded', expanded);
    img.setAttribute('aria-expanded', String(expanded));
    img.setAttribute('title', expanded ? 'Shrink image' : 'Enlarge image');
  }

  function preparePathImages() {
    document.querySelectorAll('.path-image').forEach((img) => {
      if (img.dataset.pathImageReady === 'true') return;
      img.dataset.pathImageReady = 'true';
      img.setAttribute('tabindex', '0');
      img.setAttribute('role', 'button');
      img.setAttribute('aria-expanded', 'false');
      img.setAttribute('title', img.getAttribute('title') || 'Enlarge image');
      img.addEventListener('click', () => setPathImageExpanded(img, !img.classList.contains('is-expanded')));
      img.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          setPathImageExpanded(img, !img.classList.contains('is-expanded'));
        }
        if (event.key === 'Escape') {
          setPathImageExpanded(img, false);
        }
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      preparePathImages();
      prepareImages();
    });
  } else {
    preparePathImages();
    prepareImages();
  }
})();
