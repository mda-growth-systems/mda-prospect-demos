
const menu=document.querySelector('.menu'),nav=document.querySelector('.nav-links');
if(menu){menu.addEventListener('click',()=>{const open=nav.classList.toggle('open');menu.setAttribute('aria-expanded',String(open));});}
const form=document.querySelector('[data-brief-form]');
if(form){
 const inputs=[...form.querySelectorAll('input,select,textarea')];
 const list=document.querySelector('.brief-list'),bar=document.querySelector('.progress span');
 const labelFor=i=>{const l=form.querySelector(`label[for="${i.id}"]`);return l?l.textContent:i.name;};
 const update=()=>{
   const completed=inputs.filter(i=>String(i.value).trim()).length;
   bar.style.width=`${Math.round(completed/inputs.length*100)}%`;
   const visible=inputs.filter(i=>String(i.value).trim()).slice(0,6);
   list.innerHTML=visible.length?visible.map(i=>`<div class="brief-item"><strong>${labelFor(i)}</strong><br>${String(i.value).replace(/[<>]/g,'')}</div>`).join(''):'<div class="brief-item">Complete the form to build a summary.</div>';
 };
 inputs.forEach(i=>i.addEventListener('input',update)); update();
}
