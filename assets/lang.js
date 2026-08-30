/* Language switch: 中文 / English. Every bilingual unit is <span class="zh"> + <span class="en">;
   site.css shows one of them according to html[data-lang].
   Default: the learner's own choice if they have pressed the button before (localStorage "dl:lang");
   otherwise the browser language — Chinese for zh-* browsers, English for everything else.
   The tiny inline script in each page's <head> applies the same rule before first paint. */
(function(){
  var root=document.documentElement;
  function stored(){try{return localStorage.getItem('dl:lang')}catch(e){return null}}
  function browser(){var n=(navigator.language||'').toLowerCase();return n.indexOf('zh')===0?'zh':'en'}
  function current(){var l=root.getAttribute('data-lang');return l==='zh'?'zh':'en'}
  function apply(lang,save){
    root.setAttribute('data-lang',lang);
    root.setAttribute('lang',lang==='zh'?'zh-CN':'en');
    var t=document.querySelector('title');
    if(t){var d=t.getAttribute('data-'+lang);if(d)document.title=d}
    document.querySelectorAll('[data-lang-toggle]').forEach(function(b){
      b.querySelectorAll('[data-l]').forEach(function(s){s.classList.toggle('on',s.getAttribute('data-l')===lang)});
      b.setAttribute('aria-label',lang==='zh'?'当前中文，点击切换为英文 · Switch to English':'Now in English — switch to Chinese · 切换为中文');
    });
    if(save){try{localStorage.setItem('dl:lang',lang)}catch(e){}}
    document.dispatchEvent(new CustomEvent('dl:lang',{detail:{lang:lang}}));
  }
  function toggle(){apply(current()==='zh'?'en':'zh',true)}
  document.querySelectorAll('[data-lang-toggle]').forEach(function(b){b.addEventListener('click',toggle)});
  var s=stored();
  apply(s==='zh'||s==='en'?s:browser(),false);
})();
