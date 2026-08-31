/* Module progress bar.
   The denominator is DECLARED by the module page, never inferred from localStorage:

     <div data-module-progress data-total="18" data-pages="2"></div>

     data-total  every self-review item in this module, counted across all its pages
     data-pages  how many pages in this module carry a self-review list

   Counting only the keys that happen to exist in localStorage makes the denominator
   grow as the learner opens pages: a learner who opened one page and ticked
   everything on it would be told "100%", and this course has no teacher standing by
   to correct that. With a declared total the percentage means the same thing on the
   first visit and the last. Bilingual status (zh/en spans; site.css shows one). */
(function(){
  var bar=document.querySelector('[data-module-progress]');if(!bar)return;
  var PREFIX='dl:check:v2:';
  var folder=location.pathname.replace(/[^\/]*$/,'');
  var declared=parseInt(bar.getAttribute('data-total'),10);
  var pages=parseInt(bar.getAttribute('data-pages'),10);
  var done=0,opened=0;
  try{
    for(var i=0;i<localStorage.length;i++){
      var k=localStorage.key(i);
      if(k.indexOf(PREFIX+folder)!==0)continue;
      opened++;
      var st=JSON.parse(localStorage.getItem(k)||'{}');
      for(var id in st){if(st[id])done++}
    }
  }catch(e){}
  function bi(zh,en){return '<span class="zh">'+zh+'</span><span class="en">'+en+'</span>'}

  if(!(declared>0)){
    /* No declared total: report the count honestly rather than invent a percentage. */
    if(window.console&&console.warn)console.warn('progress.js: [data-module-progress] is missing a valid data-total, so no percentage is shown. Add data-total="N" (all self-review items in this module) and data-pages="N".');
    bar.innerHTML='<p class="checklist-status">'+bi('本单元自评清单已勾选 '+done+' 项 · 只保存在你自己的浏览器里',done+' self-review items checked in this module · saved only in this browser')+'</p>';
    return;
  }
  if(done>declared)done=declared;      /* stale ids from an older checklist must not overflow the bar */
  if(pages>0&&opened>pages)opened=pages;
  var pct=Math.round(done/declared*100);
  var zh='本单元共 '+declared+' 项自评，你已勾选 '+done+' 项（'+pct+'%）';
  var en=done+' of '+declared+' self-review items checked in this module ('+pct+'%)';
  if(pages>0){
    zh+=' · 含清单的页面已打开 '+opened+' / '+pages+' 页';
    en+=' · '+opened+' of '+pages+' checklist pages opened';
  }
  zh+=' · 只保存在你自己的浏览器里';
  en+=' · saved only in this browser';
  bar.innerHTML='<div class="progress"><div style="width:'+pct+'%"></div></div><p class="checklist-status">'+bi(zh,en)+'</p>';
})();
