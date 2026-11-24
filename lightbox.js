(function(){
  var imgs=[].slice.call(document.querySelectorAll('.p-body figure img, .dark-block figure img'));
  if(!imgs.length) return;
  var lb=document.createElement('div'); lb.className='lb'; lb.setAttribute('role','dialog'); lb.setAttribute('aria-modal','true');
  lb.innerHTML='<span class="lb-count"></span><button class="lb-close" aria-label="Close">✕</button><button class="lb-prev" aria-label="Previous image">←</button><img alt=""><p class="lb-cap"></p><button class="lb-next" aria-label="Next image">→</button>';
  document.body.appendChild(lb);
  var big=lb.querySelector('img'), cap=lb.querySelector('.lb-cap'), cnt=lb.querySelector('.lb-count'), i=0;
  function show(n){ i=(n+imgs.length)%imgs.length; var im=imgs[i]; big.src=im.currentSrc||im.src; big.alt=im.alt;
    var fc=im.closest('figure'); fc=fc&&fc.querySelector('figcaption'); cap.textContent=fc?fc.textContent:'';
    cnt.textContent=(i+1)+' / '+imgs.length; }
  function open(n){ show(n); lb.classList.add('open'); document.body.style.overflow='hidden'; }
  function close(){ lb.classList.remove('open'); document.body.style.overflow=''; }
  imgs.forEach(function(im,n){ im.addEventListener('click',function(){ open(n); }); });
  lb.querySelector('.lb-close').onclick=close;
  lb.querySelector('.lb-prev').onclick=function(e){ e.stopPropagation(); show(i-1); };
  lb.querySelector('.lb-next').onclick=function(e){ e.stopPropagation(); show(i+1); };
  lb.addEventListener('click',function(e){ if(e.target===lb) close(); });
  document.addEventListener('keydown',function(e){ if(!lb.classList.contains('open')) return;
    if(e.key==='Escape') close(); else if(e.key==='ArrowRight') show(i+1); else if(e.key==='ArrowLeft') show(i-1); });
  var x0=null; lb.addEventListener('touchstart',function(e){ x0=e.touches[0].clientX; },{passive:true});
  lb.addEventListener('touchend',function(e){ if(x0===null) return; var dx=e.changedTouches[0].clientX-x0; if(Math.abs(dx)>50) show(i+(dx<0?1:-1)); x0=null; });
})();
(function(){
  var reduce=window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var main=document.querySelector('figure.vid-main video');
  if(main && 'IntersectionObserver' in window){
    new IntersectionObserver(function(es){ es.forEach(function(e){
      if(e.isIntersecting){ if(!reduce && !main.dataset.user){ var p=main.play(); if(p&&p.catch) p.catch(function(){}); } } else main.pause(); }); },{threshold:.35}).observe(main);
    main.addEventListener('pause',function(e){ if(e.isTrusted && document.visibilityState==='visible' && main.getBoundingClientRect().top<innerHeight && main.getBoundingClientRect().bottom>0) main.dataset.user='1'; });
  }
  var tiles=[].slice.call(document.querySelectorAll('figure.vid.tile'));
  tiles.forEach(function(f){
    var v=f.querySelector('video'); v.removeAttribute('loop');
    var b=document.createElement('button'); b.className='vplay'; b.setAttribute('aria-label','Play video'); b.innerHTML='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l11-6.5z"/></svg>';
    f.appendChild(b);
    function toggle(){ if(v.paused){ tiles.forEach(function(o){ var ov=o.querySelector('video'); if(ov!==v){ ov.pause(); } }); if(main) main.pause(); v.play(); } else v.pause(); }
    b.addEventListener('click',toggle); v.addEventListener('click',toggle);
    v.addEventListener('play',function(){ f.classList.add('playing'); b.setAttribute('aria-label','Pause video'); });
    v.addEventListener('pause',function(){ f.classList.remove('playing'); b.setAttribute('aria-label','Play video'); });
    v.addEventListener('ended',function(){ f.classList.remove('playing'); v.currentTime=0; });
  });
})();
