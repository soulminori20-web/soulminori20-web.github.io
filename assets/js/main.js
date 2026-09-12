'use strict';
(() => {
 const root=document.documentElement;root.classList.add('motion-ready');
 const media=matchMedia('(prefers-reduced-motion: reduce)');
 const toggle=document.querySelector('.motion-toggle');
 let savedMotion=null;try{savedMotion=sessionStorage.getItem('diana-motion');}catch{}
 let paused=savedMotion===null?media.matches:savedMotion==='off';
 const applyMotion=()=>{
  root.classList.toggle('motion-off',paused);
  if(toggle){toggle.setAttribute('aria-pressed',String(paused));toggle.setAttribute('aria-label',paused?'Включить анимацию':'Отключить анимацию');toggle.title=toggle.getAttribute('aria-label');toggle.textContent=paused?'▷':'Ⅱ';}
  document.querySelectorAll('.mascot-body').forEach(el=>{if(paused){el.style.removeProperty('--mx');el.style.removeProperty('--my');el.style.removeProperty('--mr');}});
 };
 toggle?.addEventListener('click',()=>{paused=!paused;try{sessionStorage.setItem('diana-motion',paused?'off':'on');}catch{}applyMotion();});
 media.addEventListener('change',()=>{paused=media.matches;applyMotion();});applyMotion();
 let toastTimer;
 const announce=text=>{const t=document.querySelector('.toast');if(!t)return;clearTimeout(toastTimer);t.textContent=text;t.classList.add('visible');toastTimer=setTimeout(()=>t.classList.remove('visible'),3500);};
 async function copy(text){try{await navigator.clipboard.writeText(text);return true;}catch{const field=document.createElement('textarea');field.value=text;field.style.cssText='position:fixed;opacity:0';document.body.append(field);field.select();let ok=false;try{ok=document.execCommand('copy');}catch{}field.remove();return ok;}}
 document.querySelector('[data-copy-email]')?.addEventListener('click',async()=>announce(await copy('Soulminori2.0@gmail.com')?'Почта скопирована':'Адрес: Soulminori2.0@gmail.com'));
 document.querySelector('[data-copy-link]')?.addEventListener('click',async()=>{
  if(location.protocol==='file:'){announce('Откройте опубликованный сайт, чтобы поделиться ссылкой.');return;}
  const url=new URL(location.href);url.hash='';announce(await copy(url.href)?'Ссылка на кейс скопирована':'Скопируйте адрес из строки браузера.');
 });

 // Real pose assets share the same full-body canvas. Decode before switching.
 const mainImage=document.querySelector('.mascot-image');
 const assetBase=mainImage?new URL('.',mainImage.src).href:'';
 const cache=new Map();
 function preloadPose(pose){
  if(!cache.has(pose)){const im=new Image();im.src=assetBase+pose+'.webp?v=34';cache.set(pose,im.decode().then(()=>im.src).catch(()=>null));}
  return cache.get(pose);
 }
 async function setPose(scene,pose){
  if(!scene)return;
  scene.dataset.requestedPose=pose;
  const url=await preloadPose(pose);
  if(!url||scene.dataset.requestedPose!==pose)return;
  const image=scene.querySelector('.mascot-image');
  if(image&&image.src!==url){image.src=url;if(!paused){scene.classList.remove('is-greeting');requestAnimationFrame(()=>scene.classList.add('is-greeting'));}}
 }
 if(assetBase){const poses=new Set([...document.querySelectorAll('[data-default-pose],[data-pose]')].map(e=>e.dataset.pose||e.dataset.defaultPose));if(document.querySelector('.hero-character'))['urban-wave','urban-point','urban-neutral'].forEach(p=>poses.add(p));poses.forEach(preloadPose);}
 const heroScene=document.querySelector('.hero-character');
 let greetTimer;
 function greet(){if(!heroScene)return;clearTimeout(greetTimer);setPose(heroScene,'urban-wave');greetTimer=setTimeout(()=>setPose(heroScene,'urban-neutral'),2100);}
 document.querySelector('[data-greet]')?.addEventListener('click',greet);
 if(heroScene&&!paused){preloadPose('urban-wave').then(()=>{if(!paused)greet();});}
 const cta=document.querySelector('[data-hero-cta]');
 ['pointerenter','focus'].forEach(event=>cta?.addEventListener(event,()=>{if(!paused){clearTimeout(greetTimer);setPose(heroScene,'urban-point');}}));
 ['pointerleave','blur'].forEach(event=>cta?.addEventListener(event,()=>{if(heroScene)setPose(heroScene,'urban-neutral');}));
 document.querySelectorAll('[data-mascot]').forEach(scene=>{
  const zone=scene.closest('.hero-stage,.workshop-hero-art')||scene;
  const body=scene.querySelector('.mascot-body');let frame;
  zone.addEventListener('pointermove',event=>{
   if(paused||event.pointerType!=='mouse')return;cancelAnimationFrame(frame);
   frame=requestAnimationFrame(()=>{const b=zone.getBoundingClientRect();const x=(event.clientX-b.left)/b.width-.5,y=(event.clientY-b.top)/b.height-.5;body.style.setProperty('--mx',`${x*10}px`);body.style.setProperty('--my',`${y*6}px`);body.style.setProperty('--mr',`${x*1.5}deg`);});
  },{passive:true});
  zone.addEventListener('pointerleave',()=>{cancelAnimationFrame(frame);body.style.removeProperty('--mx');body.style.removeProperty('--my');body.style.removeProperty('--mr');});
 });

 const tabs=Array.from(document.querySelectorAll('[role=tab]'));
 function activateTab(tab,focus=false){
  tabs.forEach(t=>{const active=t===tab;t.setAttribute('aria-selected',String(active));t.tabIndex=active?0:-1;document.getElementById(t.getAttribute('aria-controls')).hidden=!active;});
  setPose(document.querySelector('.about-companion .mascot-scene'),tab.dataset.pose);
  const note=document.querySelector('.companion-note');if(note)note.textContent={profile:'Приятно познакомиться!',practice:'Идея → применение',skills:'Всё начинается с задачи',education:'Дизайн + технологии',process:'По шагам к результату',team:'Открыта к работе в команде'}[tab.id.replace('tab-','')];
  if(focus)tab.focus();
 }
 tabs.forEach((tab,i)=>{
  tab.addEventListener('click',()=>activateTab(tab));
  tab.addEventListener('keydown',event=>{let next=i;if(['ArrowRight','ArrowDown'].includes(event.key))next=(i+1)%tabs.length;else if(['ArrowLeft','ArrowUp'].includes(event.key))next=(i+tabs.length-1)%tabs.length;else if(event.key==='Home')next=0;else if(event.key==='End')next=tabs.length-1;else return;event.preventDefault();activateTab(tabs[next],true);});
 });

 const carousel=document.querySelector('.carousel');
 if(carousel){
  const slides=Array.from(carousel.children),dots=Array.from(document.querySelectorAll('[data-slide]'));
  const prev=document.querySelector('[data-carousel-prev]'),next=document.querySelector('[data-carousel-next]'),count=document.querySelector('[data-carousel-current]');
  let active=0,scrollFrame;
  function go(index){index=Math.max(0,Math.min(slides.length-1,index));carousel.scrollTo({left:slides[index].offsetLeft-slides[0].offsetLeft,behavior:paused?'auto':'smooth'});}
  function sync(){
   const pos=carousel.scrollLeft;
   let distance=Infinity;
   slides.forEach((slide,i)=>{const delta=Math.abs(slide.offsetLeft-slides[0].offsetLeft-pos);if(delta<distance){distance=delta;active=i;}});
   if(pos>=carousel.scrollWidth-carousel.clientWidth-3)active=slides.length-1;
   prev.disabled=active===0;next.disabled=active===slides.length-1;
   count.textContent=String(active+1).padStart(2,'0');dots.forEach((dot,i)=>dot.setAttribute('aria-current',String(i===active)));slides.forEach((slide,i)=>slide.setAttribute('aria-current',String(i===active)));
   setPose(document.querySelector('.carousel-character'),active===3?'workshop-vase':active===4?'workshop-sit':'workshop-wave');
  }
  prev.addEventListener('click',()=>go(active-1));next.addEventListener('click',()=>go(active+1));dots.forEach((dot,i)=>dot.addEventListener('click',()=>go(i)));
  carousel.addEventListener('scroll',()=>{cancelAnimationFrame(scrollFrame);scrollFrame=requestAnimationFrame(sync);},{passive:true});
  carousel.addEventListener('keydown',e=>{if(e.target!==carousel)return;if(['ArrowLeft','ArrowRight','Home','End'].includes(e.key)){e.preventDefault();go(e.key==='Home'?0:e.key==='End'?slides.length-1:active+(e.key==='ArrowLeft'?-1:1));}});
  window.addEventListener('resize',sync,{passive:true});sync();
 }

 const dialog=document.querySelector('.lightbox'),links=Array.from(document.querySelectorAll('[data-zoom]'));
 if(dialog&&typeof dialog.showModal==='function'){
  const image=dialog.querySelector('img'),caption=dialog.querySelector('#lightbox-caption'),counter=dialog.querySelector('[data-count]'),original=dialog.querySelector('[data-original]');
  let current=0,returnFocus,touch;
  function show(i){current=(i+links.length)%links.length;const a=links[current];image.src=a.href;image.alt=a.dataset.caption||'';caption.textContent=image.alt;counter.textContent=`${current+1} / ${links.length}`;original.href=a.href;}
  links.forEach((link,i)=>link.addEventListener('click',e=>{if(e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;e.preventDefault();returnFocus=link;show(i);document.body.classList.add('modal-open');dialog.showModal();dialog.querySelector('[data-close]').focus();}));
  dialog.querySelector('[data-close]').addEventListener('click',()=>dialog.close());
  dialog.querySelector('[data-prev]').addEventListener('click',()=>show(current-1));dialog.querySelector('[data-next]').addEventListener('click',()=>show(current+1));
  dialog.addEventListener('keydown',e=>{if(e.key==='ArrowLeft'||e.key==='ArrowRight'){e.preventDefault();show(current+(e.key==='ArrowLeft'?-1:1));}});
  dialog.addEventListener('close',()=>{document.body.classList.remove('modal-open');image.removeAttribute('src');returnFocus?.focus({preventScroll:true});});
  dialog.addEventListener('click',e=>{if(e.target===dialog)dialog.close();});
  const stage=dialog.querySelector('.lightbox-stage');stage.addEventListener('touchstart',e=>{touch=[e.touches[0].clientX,e.touches[0].clientY];},{passive:true});
  stage.addEventListener('touchend',e=>{if(!touch)return;const x=e.changedTouches[0].clientX-touch[0],y=e.changedTouches[0].clientY-touch[1];if(Math.abs(x)>65&&Math.abs(x)>Math.abs(y)*1.5)show(current+(x<0?1:-1));touch=null;},{passive:true});
  image.addEventListener('error',()=>caption.textContent='Изображение не загрузилось. Попробуйте открыть оригинал.');
 }
 if('IntersectionObserver' in window){
  const reveal=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){if(!paused)entry.target.classList.add('entering');reveal.unobserve(entry.target);}}),{threshold:.08});
  document.querySelectorAll('[data-reveal]').forEach(el=>reveal.observe(el));
  const navLinks=Array.from(document.querySelectorAll('.header-row nav a,.case-nav a')).filter(a=>a.getAttribute('href').startsWith('#'));
  const navObserver=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){navLinks.forEach(link=>{if(link.hash==='#'+entry.target.id)link.setAttribute('aria-current','location');else link.removeAttribute('aria-current');});}}),{rootMargin:'-20% 0px -55% 0px'});
  navLinks.forEach(link=>{const section=document.querySelector(link.hash);if(section)navObserver.observe(section);});
  const animated=new IntersectionObserver(entries=>entries.forEach(entry=>entry.target.style.animationPlayState=entry.isIntersecting?'running':'paused'));
 document.querySelectorAll('.ticker-track,.hero-asterisk').forEach(el=>animated.observe(el));
 }

 const header=document.querySelector('.site-header');
 const dividers=Array.from(document.querySelectorAll('.chapter-divider img'));
 let pageFrame;
 function updatePageMotion(){
  pageFrame=0;
  header?.classList.toggle('is-scrolled',scrollY>18);
  if(paused)return;
  const center=innerHeight/2;
  dividers.forEach(image=>{const box=image.getBoundingClientRect();const distance=(box.top+box.height/2-center)/innerHeight;image.style.translate=`${Math.max(-12,Math.min(12,distance*-10))}px 0`;});
 }
 addEventListener('scroll',()=>{if(!pageFrame)pageFrame=requestAnimationFrame(updatePageMotion);},{passive:true});
 updatePageMotion();
})();
