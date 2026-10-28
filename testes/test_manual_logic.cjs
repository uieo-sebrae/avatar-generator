/* Lógica do manual em ambiente simulado; não certifica layout no navegador. */
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const html=fs.readFileSync(process.argv[2],'utf8');
const script=html.match(/<script>([\s\S]*?)<\/script>/)[1];
const events={},downloads=[];let copied=null,revoked=false,selected=false;
const kickoff='Use esta distro e me conduza.';
const elements={kickoff:{value:kickoff,focus(){},select(){selected=true;}},copyStatus:{textContent:''},
 starterText:{textContent:'protocolo de teste'},
 copyPrompt:{addEventListener:(name,fn)=>events.copy=fn},
 downloadStart:{addEventListener:(name,fn)=>events.download=fn}};
const navigator={clipboard:{writeText:async t=>{copied=t;}}};
const context=vm.createContext({document:{getElementById:id=>elements[id],createElement:()=>({click(){downloads.push({href:this.href,download:this.download});}})},
 navigator,Blob:class{constructor(parts){assert.equal(parts[0],elements.starterText.textContent);}},
 URL:{createObjectURL:()=> 'blob:teste',revokeObjectURL:()=>{revoked=true;}},setTimeout:fn=>fn()});
vm.runInContext(script,context);
(async()=>{
 await events.copy();assert.equal(copied,kickoff);assert.ok(elements.copyStatus.textContent.includes('copiada'));
 navigator.clipboard=null;await events.copy();assert.ok(selected);assert.ok(elements.copyStatus.textContent.includes('selecionado'));
 events.download();assert.equal(downloads[0].download,'INICIAR_AVATAR.md');assert.ok(revoked);
 console.log('PASS copiar, seleção alternativa e download do protocolo; layout não avaliado');
})().catch(e=>{console.error(e);process.exit(1);});
