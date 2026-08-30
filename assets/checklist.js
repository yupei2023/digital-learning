/* Checkable self-review lists, saved in this browser only (localStorage). Status line is bilingual (zh/en spans; site.css shows the active language). */
(function(){
  function key(list){return 'dl:check:'+location.pathname+'#'+(list.id||'list')}
  function load(list){try{return JSON.parse(localStorage.getItem(key(list))||'{}')}catch(e){return {}}}
  function save(list,state){try{localStorage.setItem(key(list),JSON.stringify(state))}catch(e){}}
  function bi(zh,en){return '<span class="zh">'+zh+'</span><span class="en">'+en+'</span>'}
  function status(list){
    var boxes=list.querySelectorAll('input[type=checkbox]'),done=0;
    boxes.forEach(function(b){if(b.checked)done++});
    var s=list.nextElementSibling;
    if(!s||!s.classList.contains('checklist-status')){s=document.createElement('p');s.className='checklist-status';list.after(s)}
    s.innerHTML=bi('已完成 '+done+' / '+boxes.length+'（只保存在你自己的浏览器里）','Done '+done+' of '+boxes.length+' (saved only in this browser)');
    document.dispatchEvent(new CustomEvent('dl:checklist',{detail:{id:list.id,done:done,total:boxes.length}}));
  }
  document.querySelectorAll('ul.checklist').forEach(function(list){
    var state=load(list);
    list.querySelectorAll('input[type=checkbox]').forEach(function(b,i){
      var id=b.id||('c'+i);
      if(state[id])b.checked=true;
      b.addEventListener('change',function(){state[id]=b.checked;save(list,state);status(list)});
    });
    status(list);
  });
})();
