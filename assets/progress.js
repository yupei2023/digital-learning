/* Module progress bar: reads every saved checklist in this module folder from localStorage. */
(function(){
  var bar=document.querySelector('[data-module-progress]');if(!bar)return;
  var folder=location.pathname.replace(/[^\/]*$/,'');var done=0,total=0;
  try{for(var i=0;i<localStorage.length;i++){var k=localStorage.key(i);if(k.indexOf('dl:check:'+folder)!==0)continue;var st=JSON.parse(localStorage.getItem(k)||'{}');for(var id in st){total++;if(st[id])done++}}}catch(e){}
  var pct=total?Math.round(done/total*100):0;
  bar.innerHTML='<div class="progress"><div style="width:'+pct+'%"></div></div><p class="checklist-status">本单元自评清单已勾选 '+done+' 项（'+pct+'%）· '+done+' self-review items checked in this module · 本地保存 saved locally</p>';
})();
