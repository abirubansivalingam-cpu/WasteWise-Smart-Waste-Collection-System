document.querySelectorAll('input,select,textarea').forEach(el=>el.classList.add('control'));
document.querySelectorAll('.notice').forEach(n=>{setTimeout(()=>{n.style.opacity='0';},4500);});
