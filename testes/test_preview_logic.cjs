/* Teste de lógica em DOM simulado. Não certifica renderização em navegador.
   Uso: node testes/test_preview_logic.cjs caminho/preview.html */
const fs=require('node:fs');
const vm=require('node:vm');
const assert=require('node:assert/strict');
const html=fs.readFileSync(process.argv[2],'utf8');
const match=html.match(/<script>([\s\S]*?)<\/script>/);
assert.ok(match,'Script não encontrado');
const els=Object.fromEntries(['slider','frame','label','play','prev','next','bg','stage','meta'].map(id=>[id,{style:{},value:'0',textContent:''}]));
const timers=new Map();let tid=0;
const context=vm.createContext({document:{getElementById:id=>els[id]},matchMedia:()=>({matches:false}),
    setTimeout:(fn,ms)=>{const id=++tid;timers.set(id,{fn,ms});return id;},clearTimeout:id=>timers.delete(id)});
vm.runInContext(match[1],context);
assert.ok(els.frame.src.startsWith('data:image/png;base64,'));
const count=Number(els.slider.max)+1;assert.ok(count>=2);
assert.equal(els.play.textContent,'Pausar');
els.play.onclick();assert.equal(els.play.textContent,'Reproduzir');assert.equal(timers.size,0);
els.next.onclick();assert.equal(Number(els.slider.value),1);
els.prev.onclick();assert.equal(Number(els.slider.value),0);
els.slider.value=String(count-1);els.slider.oninput();assert.ok(els.label.textContent.includes(`${count}/${count}`));
els.bg.value='#111827';els.bg.onchange();assert.equal(els.stage.style.background,'#111827');
els.play.onclick();assert.equal(timers.size,1);
const scheduled=[...timers.values()][0];assert.ok(scheduled.ms>0);timers.clear();scheduled.fn();
assert.ok(Number(els.slider.value)>=0&&Number(els.slider.value)<count);
console.log('PASS controles do preview em DOM simulado; renderização não avaliada');
