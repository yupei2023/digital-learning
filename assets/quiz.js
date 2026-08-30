/* Ungraded self-quiz with instant feedback. Data: window.DL_QUIZ = [{q,options:[..],a:index,why}] ; optional data-range="0-3" on .quiz */
(function(){
  var host=document.querySelector('.quiz');if(!host||!window.DL_QUIZ)return;
  var items=window.DL_QUIZ,range=host.getAttribute('data-range');
  if(range){var r=range.split('-');items=items.slice(+r[0],+r[1]+1)}
  var answered=0,correct=0;
  items.forEach(function(it,n){
    var q=document.createElement('div');q.className='q';
    var stem=document.createElement('p');stem.className='stem';stem.textContent=(n+1)+'. '+it.q;q.appendChild(stem);
    var fb=document.createElement('div');fb.className='fb';
    it.options.forEach(function(o,i){
      var l=document.createElement('label');l.className='opt';
      var inp=document.createElement('input');inp.type='radio';inp.name='q'+n;inp.value=i;
      l.appendChild(inp);l.appendChild(document.createTextNode(o));
      inp.addEventListener('change',function(){
        var ok=i===it.a;
        q.querySelectorAll('input').forEach(function(x){x.disabled=true});
        fb.className='fb '+(ok?'ok':'no');
        fb.textContent=(ok?'✅ 对了 Correct. ':'❌ 再想想 Not quite. ')+it.why;
        answered++;if(ok)correct++;
        if(answered===items.length){var s=document.createElement('p');s.className='summary';s.textContent='本次 '+correct+' / '+items.length+' · '+correct+' of '+items.length+' this time. 不计分，可重做 Ungraded — retake as often as you like.';host.appendChild(s)}
      });
      q.appendChild(l);
    });
    q.appendChild(fb);host.appendChild(q);
  });
  var btn=document.createElement('button');btn.className='ghost';btn.textContent='重做 Retake';btn.addEventListener('click',function(){host.innerHTML='';answered=0;correct=0;location.reload()});host.appendChild(btn);
})();
