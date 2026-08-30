/* Ungraded self-quiz with instant feedback.
   Data: window.DL_QUIZ = [{q:[zh,en], options:[[zh,en],...], a:index, why:[zh,en]}]; optional data-range="0-3" on .quiz.
   Both languages are rendered; site.css shows the active one. */
(function(){
  var host=document.querySelector('.quiz');if(!host||!window.DL_QUIZ)return;
  var items=window.DL_QUIZ,range=host.getAttribute('data-range');
  if(range){var r=range.split('-');items=items.slice(+r[0],+r[1]+1)}
  function bi(t){var f=document.createDocumentFragment();var z=document.createElement('span');z.className='zh';z.textContent=t[0];var e=document.createElement('span');e.className='en';e.textContent=t[1];f.appendChild(z);f.appendChild(e);return f}
  var answered=0,correct=0;
  items.forEach(function(it,n){
    var q=document.createElement('div');q.className='q';
    var stem=document.createElement('p');stem.className='stem';stem.appendChild(document.createTextNode((n+1)+'. '));stem.appendChild(bi(it.q));q.appendChild(stem);
    var fb=document.createElement('div');fb.className='fb';
    it.options.forEach(function(o,i){
      var l=document.createElement('label');l.className='opt';
      var inp=document.createElement('input');inp.type='radio';inp.name='q'+n;inp.value=i;
      l.appendChild(inp);l.appendChild(bi(o));
      inp.addEventListener('change',function(){
        var ok=i===it.a;
        q.querySelectorAll('input').forEach(function(x){x.disabled=true});
        fb.className='fb '+(ok?'ok':'no');
        fb.textContent='';fb.appendChild(bi(ok?['✅ 对了。'+it.why[0],'✅ Correct. '+it.why[1]]:['❌ 再想想。'+it.why[0],'❌ Not quite. '+it.why[1]]));
        answered++;if(ok)correct++;
        if(answered===items.length){var s=document.createElement('p');s.className='summary';s.appendChild(bi(['本次 '+correct+' / '+items.length+'。不计分，可重做。',correct+' of '+items.length+' this time. Ungraded — retake as often as you like.']));host.appendChild(s)}
      });
      q.appendChild(l);
    });
    q.appendChild(fb);host.appendChild(q);
  });
  var btn=document.createElement('button');btn.className='ghost';btn.appendChild(bi(['重做','Retake']));btn.addEventListener('click',function(){location.reload()});host.appendChild(btn);
})();
