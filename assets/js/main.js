'use strict';
(() => {
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const toast = document.querySelector('.toast');
  let toastTimer;
  function announce(message) {
    if (!toast) return;
    window.clearTimeout(toastTimer);
    toast.textContent = message;
    toast.classList.add('is-visible');
    toastTimer = window.setTimeout(() => toast.classList.remove('is-visible'), 4200);
  }
  async function copyText(value) {
    if (navigator.clipboard && window.isSecureContext) {
      try { await navigator.clipboard.writeText(value); return true; } catch (_) { /* file:// or permission fallback */ }
    }
    const previous = document.activeElement;
    const field = document.createElement('textarea');
    field.value = value;
    field.setAttribute('readonly', '');
    field.setAttribute('aria-label', 'Текст для копирования');
    field.style.cssText = 'position:fixed;left:0;top:0;width:1px;height:1px;opacity:0';
    document.body.append(field);
    field.select();
    let success = false;
    try { success = document.execCommand('copy'); } catch (_) { /* expose the visible address on failure */ }
    field.remove();
    if (previous instanceof HTMLElement) previous.focus({preventScroll:true});
    return success;
  }
  document.querySelectorAll('[data-copy-email]').forEach(button => button.addEventListener('click', async () => {
    const ok = await copyText('Soulminori2.0@gmail.com');
    announce(ok ? 'Почта скопирована' : 'Не удалось скопировать. Адрес: Soulminori2.0@gmail.com');
  }));
  document.querySelectorAll('[data-copy-link]').forEach(button => button.addEventListener('click', async () => {
    if (location.protocol === 'file:') {
      announce('Для отправки ссылки откройте опубликованную версию сайта.');
      return;
    }
    const address = new URL(location.href);
    address.hash = '';
    announce(await copyText(address.href) ? 'Ссылка на проект скопирована' : 'Скопируйте ссылку из адресной строки браузера.');
  }));

  const lightbox = document.querySelector('.lightbox');
  const links = Array.from(document.querySelectorAll('[data-zoom]'));
  if (lightbox && typeof lightbox.showModal === 'function') {
    const image = lightbox.querySelector('.lightbox-stage img');
    const stage = lightbox.querySelector('.lightbox-stage');
    const caption = lightbox.querySelector('#lightbox-caption');
    const counter = lightbox.querySelector('[data-image-count]');
    const original = lightbox.querySelector('[data-image-open]');
    const sizeButton = lightbox.querySelector('[data-image-size]');
    const previous = lightbox.querySelector('[data-image-prev]');
    const next = lightbox.querySelector('[data-image-next]');
    let activeIndex = 0;
    let returnFocus = null;
    let touchStart = null;
    function render(index) {
      activeIndex = (index + links.length) % links.length;
      const selected = links[activeIndex];
      const text = selected.dataset.caption || selected.querySelector('img')?.alt || 'Изображение проекта';
      image.alt = text;
      image.src = selected.href;
      caption.textContent = text;
      counter.textContent = `${activeIndex + 1} / ${links.length}`;
      original.href = selected.href;
      lightbox.classList.remove('is-actual');
      sizeButton.setAttribute('aria-pressed', 'false');
      sizeButton.textContent = 'Исходный размер';
      stage.scrollTop = 0;
      stage.scrollLeft = 0;
      previous.disabled = next.disabled = links.length < 2;
    }
    links.forEach((link,index) => link.addEventListener('click', event => {
      if (event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      returnFocus = link;
      render(index);
      document.body.classList.add('modal-open');
      lightbox.showModal();
      lightbox.querySelector('[data-image-close]').focus({preventScroll:true});
    }));
    lightbox.querySelector('[data-image-close]').addEventListener('click', () => lightbox.close());
    lightbox.addEventListener('close', () => {
      document.body.classList.remove('modal-open');
      image.removeAttribute('src');
      if (returnFocus?.isConnected) returnFocus.focus({preventScroll:true});
    });
    previous.addEventListener('click', () => render(activeIndex - 1));
    next.addEventListener('click', () => render(activeIndex + 1));
    sizeButton.addEventListener('click', () => {
      const actual = lightbox.classList.toggle('is-actual');
      sizeButton.setAttribute('aria-pressed', String(actual));
      sizeButton.textContent = actual ? 'Вписать в экран' : 'Исходный размер';
      stage.scrollTop = stage.scrollLeft = 0;
    });
    lightbox.addEventListener('keydown', event => {
      // In actual-size mode arrows remain available for scrolling large artwork.
      if (lightbox.classList.contains('is-actual')) return;
      if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') {
        event.preventDefault();
        render(activeIndex + (event.key === 'ArrowRight' ? 1 : -1));
      }
    });
    stage.addEventListener('click', event => { if (event.target === stage) lightbox.close(); });
    stage.addEventListener('touchstart', event => {
      const touch = event.touches[0];
      touchStart = touch ? [touch.clientX,touch.clientY] : null;
    }, {passive:true});
    stage.addEventListener('touchend', event => {
      if (!touchStart || lightbox.classList.contains('is-actual')) return;
      const touch = event.changedTouches[0];
      if (!touch) return;
      const dx = touch.clientX - touchStart[0],dy = touch.clientY - touchStart[1];
      if (Math.abs(dx) > 70 && Math.abs(dx) > Math.abs(dy)*1.5) render(activeIndex + (dx < 0 ? 1 : -1));
      touchStart = null;
    }, {passive:true});
    image.addEventListener('error', () => { caption.textContent = 'Изображение не загрузилось. Попробуйте открыть его отдельно.'; });
  }

  const carousel = document.querySelector('.carousel');
  if (carousel) {
    const move = direction => {
      const first = carousel.querySelector('figure');
      carousel.scrollBy({left:direction*((first?.getBoundingClientRect().width || carousel.clientWidth)+22),behavior:reducedMotion.matches ? 'auto' : 'smooth'});
    };
    document.querySelector('[data-carousel-prev]')?.addEventListener('click', () => move(-1));
    document.querySelector('[data-carousel-next]')?.addEventListener('click', () => move(1));
    carousel.addEventListener('keydown', event => {
      if (event.target !== carousel) return;
      if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {event.preventDefault();move(event.key === 'ArrowLeft' ? -1 : 1);}
    });
    const syncButtons = () => {
      const left = carousel.scrollLeft, end = carousel.scrollWidth-carousel.clientWidth;
      const prev = document.querySelector('[data-carousel-prev]'),next = document.querySelector('[data-carousel-next]');
      if (prev) prev.disabled = left <= 2;
      if (next) next.disabled = left >= end-2;
    };
    carousel.addEventListener('scroll',syncButtons,{passive:true});
    window.addEventListener('resize',syncButtons,{passive:true});
    syncButtons();
  }

  // Subtle pointer response; no perpetual animation or work while the hero is off screen.
  const artwork = document.querySelector('.hero-art');
  if (artwork) {
    artwork.addEventListener('pointermove', event => {
      if (reducedMotion.matches || event.pointerType !== 'mouse') return;
      const box = artwork.getBoundingClientRect();
      artwork.style.setProperty('--portrait-x', `${((event.clientX-box.left)/box.width-.5)*6}px`);
      artwork.style.setProperty('--portrait-y', `${((event.clientY-box.top)/box.height-.5)*4}px`);
    },{passive:true});
    const reset=()=>{artwork.style.removeProperty('--portrait-x');artwork.style.removeProperty('--portrait-y');};
    artwork.addEventListener('pointerleave',reset,{passive:true});
    reducedMotion.addEventListener?.('change',reset);
  }
  const navLinks=Array.from(document.querySelectorAll('.site-header nav a'));
  const sections=navLinks.map(a=>a.getAttribute('href')).filter(href=>href?.startsWith('#')).map(href=>document.getElementById(href.slice(1))).filter(Boolean);
  if (sections.length && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry=>{
        if (!entry.isIntersecting) return;
        navLinks.forEach(link=>{
          if(link.getAttribute('href') === `#${entry.target.id}`) link.setAttribute('aria-current','location');
          else link.removeAttribute('aria-current');
        });
      });
    },{rootMargin:'-15% 0px -55% 0px',threshold:0});
    sections.forEach(section=>observer.observe(section));
  }
})();
