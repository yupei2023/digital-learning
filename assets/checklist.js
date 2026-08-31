/* Checkable self-review lists, saved in this browser only (localStorage).

   State is keyed by each checkbox's OWN id, never by its position in the list.
   A positional key ("c0, c1, c2 …") silently shifts every saved tick by one place
   the moment an item is inserted anywhere but the end: the learner comes back to a
   self-review that appears filled in, wrongly, with no error to warn them. So a
   checkbox with no id simply does not save, and says so in the console — a release
   check (tools/check-checklist-ids.py) fails the build before that ever ships.

   The key namespace is versioned. Bump VERSION whenever a checklist's items change
   meaning, so old state expires instead of restoring ticks that belonged to
   different wording. Status line is bilingual (zh/en spans; site.css shows one). */
(function(){
  var VERSION='v2';
  function key(list){return 'dl:check:'+VERSION+':'+location.pathname+'#'+(list.id||'list')}
  function load(list){try{return JSON.parse(localStorage.getItem(key(list))||'{}')}catch(e){return {}}}
  function save(list,state){try{localStorage.setItem(key(list),JSON.stringify(state))}catch(e){}}
  function bi(zh,en){return '<span class="zh">'+zh+'</span><span class="en">'+en+'</span>'}
  function warn(msg){if(window.console&&console.warn)console.warn('checklist.js: '+msg)}
  function status(list,unsaved){
    var boxes=list.querySelectorAll('input[type=checkbox]'),done=0;
    boxes.forEach(function(b){if(b.checked)done++});
    var s=list.nextElementSibling;
    if(!s||!s.classList.contains('checklist-status')){s=document.createElement('p');s.className='checklist-status';list.after(s)}
    var zh='已完成 '+done+' / '+boxes.length+'（只保存在你自己的浏览器里）';
    var en='Done '+done+' of '+boxes.length+' (saved only in this browser)';
    if(unsaved){
      zh='已完成 '+done+' / '+boxes.length+'（其中 '+unsaved+' 项本次不会被保存）';
      en='Done '+done+' of '+boxes.length+' ('+unsaved+' of them will not be saved)';
    }
    s.innerHTML=bi(zh,en);
    document.dispatchEvent(new CustomEvent('dl:checklist',{detail:{id:list.id,done:done,total:boxes.length,unsaved:unsaved}}));
  }
  document.querySelectorAll('ul.checklist').forEach(function(list){
    if(!list.id)warn('a <ul class="checklist"> has no id, so its state shares one key with every other unnamed list on this page. Give the list a stable id.');
    var state=load(list),unsaved=0;
    list.querySelectorAll('input[type=checkbox]').forEach(function(b){
      var id=b.id;
      if(!id)unsaved++;
      else if(state[id])b.checked=true;
      b.addEventListener('change',function(){
        if(id){state[id]=b.checked;save(list,state)}
        status(list,unsaved);
      });
    });
    if(unsaved)warn(unsaved+' checkbox(es) in list "'+(list.id||'(unnamed)')+'" have no id, so their ticks are NOT saved. Add a stable id to every checklist checkbox.');
    status(list,unsaved);
  });
})();
