/* Quest layer: tier progress, badges, and soft locks.
   Reads the SAME localStorage the self-review lists already write (checklist.js,
   key 'dl:check:v2:' + page path + '#' + list id), so nothing new is stored.

   A module declares its tiers once per page:
     <script type="application/json" id="quest-def">
       {"tiers":[
         {"id":"base","page":"base-camp.html","list":"bc-list","total":7,"pts":3}, ...]}
     </script>
   Totals are declared, never inferred (same reason as progress.js), and
   tools/check-release.py verifies them against the real checklists.

   What it draws:
     [data-quest-status]   one progress bar per tier + badges (module home)
     .q-tier[data-tier]    adds is-locked / is-done to tier cards
     .q-gate[data-gate]    shows "finish the earlier tier first" on a later tier's page
     .q-cheer[data-cheer]  shows "this tier's checklist is done" on that tier's page

   Locks are SOFT: a locked tier stays readable and clickable. Ticks live in one
   browser only, so a hard lock would shut out a student who switched devices.

   When storage is unavailable (private window, blocked site data), progress from
   OTHER pages cannot be known. Then nothing is shown as locked, gates stay hidden,
   and the status box says plainly that progress cannot be saved here; the current
   page still reacts to its own ticks through the dl:checklist event. */
(function(){
  var defEl=document.getElementById('quest-def');if(!defEl)return;
  var def;try{def=JSON.parse(defEl.textContent)}catch(e){return}
  var PREFIX='dl:check:v2:';
  var folder=location.pathname.replace(/[^\/]*$/,'');
  var here=location.pathname.slice(folder.length)||'index.html';

  var storageOK=(function(){
    try{var k='dl:quest:probe';localStorage.setItem(k,'1');localStorage.removeItem(k);return true}catch(e){return false}
  })();
  var live={};   /* list id -> done count reported by checklist.js on THIS page */

  function lang(){return document.documentElement.getAttribute('data-lang')==='zh'?'zh':'en'}
  function bi(zh,en){return '<span class="zh">'+zh+'</span><span class="en">'+en+'</span>'}
  function countDone(t){
    if(t.page===here&&live.hasOwnProperty(t.list))return Math.min(live[t.list],t.total);
    if(!storageOK)return null;                  /* unknown, not zero */
    var n=0;
    try{
      var st=JSON.parse(localStorage.getItem(PREFIX+folder+t.page+'#'+t.list)||'{}');
      for(var k in st){if(st[k])n++}
    }catch(e){return null}
    return Math.min(n,t.total);
  }
  var NAMES={base:['起点营地','Base Camp'],ridge:['山脊','Ridge Trail'],summit:['登顶','Summit']};
  var BADGE={base:'badge-base-camp.svg',ridge:'badge-ridge.svg',summit:'badge-summit.svg'};
  var cssLink=document.querySelector('link[href$="quest.css"]');
  var img=cssLink?cssLink.getAttribute('href').replace('quest.css','img/quest/'):'';

  function render(){
    var state=def.tiers.map(function(t){var d=countDone(t);return {t:t,done:d,known:d!==null,full:d!==null&&d>=t.total}});
    var maxPts=def.tiers.reduce(function(a,t){return a+t.pts},0);
    var L=lang();

    var box=document.querySelector('[data-quest-status]');
    if(box){
      var segs='',labels='',badges='',ticked=0,all=0,unknown=false;
      state.forEach(function(s){
        var w=(s.t.pts/maxPts*100).toFixed(2);
        var d=s.known?s.done:0;
        var pct=Math.round(d/s.t.total*100);
        if(!s.known)unknown=true;
        ticked+=d;all+=s.t.total;
        var nm=NAMES[s.t.id]||[s.t.id,s.t.id];
        var aria=L==='zh'?nm[0]+'清单进度':nm[1]+' checklist progress';
        var txt=!s.known?(L==='zh'?'无法显示':'unavailable'):(L==='zh'?'已勾选 '+d+' / '+s.t.total:d+' of '+s.t.total+' ticked');
        /* unknown progress gets no aria-valuenow (an indeterminate bar), never a false zero */
        var now=s.known?' aria-valuenow="'+d+'"':'';
        segs+='<div class="q-seg '+s.t.id+(s.known?'':' unknown')+'" style="flex:0 0 calc('+w+'% - 3px)" role="progressbar" aria-label="'+aria+'" aria-valuemin="0" aria-valuemax="'+s.t.total+'"'+now+' aria-valuetext="'+txt+'"><i style="width:'+pct+'%"></i></div>';
        labels+='<span style="flex:0 0 calc('+w+'% - 3px)" aria-hidden="true">'+(s.known?bi(nm[0]+' '+d+'/'+s.t.total,nm[1]+' '+d+'/'+s.t.total):bi(nm[0]+' ?',nm[1]+' ?'))+'</span>';
        badges+='<div class="q-badge'+(s.full?' earned':'')+'"><img src="'+img+(s.full?BADGE[s.t.id]:'badge-locked.svg')+'" alt="">'+
                (s.known?bi(nm[0]+(s.full?' · 徽章已点亮':' · 未点亮'),nm[1]+(s.full?' · badge lit':' · not yet')):bi(nm[0]+' · 无法显示',nm[1]+' · unavailable'))+'</div>';
      });
      box.querySelector('.q-bar').innerHTML=segs;
      box.querySelector('.q-seg-labels').innerHTML=labels;
      box.querySelector('.q-badges').innerHTML=badges;
      var c=box.querySelector('.q-status-pts');
      if(c)c.innerHTML=unknown?
        bi('这个浏览器无法保存勾选，这里看不到进度——分数以导师评分为准。','This browser cannot save ticks, so progress cannot be shown here — your mentor\'s score is what counts.'):
        bi('已勾选 '+ticked+' / '+all+' 项',ticked+' of '+all+' steps ticked');
    }

    /* a tier is locked only when an earlier tier is KNOWN to be incomplete */
    var blocked=false;
    state.forEach(function(s){
      var card=document.querySelector('.q-tier[data-tier="'+s.t.id+'"]');
      if(card){card.classList.toggle('is-locked',blocked);card.classList.toggle('is-done',s.full)}
      var gate=document.querySelector('.q-gate[data-gate="'+s.t.id+'"]');
      if(gate)gate.classList.toggle('show',blocked);
      var cheer=document.querySelector('.q-cheer[data-cheer="'+s.t.id+'"]');
      if(cheer)cheer.classList.toggle('show',s.full);
      if(s.known&&!s.full)blocked=true;
    });
  }
  render();
  document.addEventListener('dl:checklist',function(e){
    if(e.detail&&e.detail.id){live[e.detail.id]=e.detail.done}
    render();
  });
  document.addEventListener('dl:lang',render);
  window.addEventListener('storage',render);
})();
