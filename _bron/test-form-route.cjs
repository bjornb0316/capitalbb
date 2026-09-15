const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const source = fs.readFileSync('js/site.js','utf8');
const code = source.slice(source.indexOf('  function verstuur('),source.indexOf('  var scanform ='));
async function run(response) {
 const nodes = {url:{value:'voorbeeld.nl'},naam:{value:'Test'},contact:{value:'test@example.com'},doel:{value:''},'scan-vervolg':{hidden:true,focus(){this.focused=true;}}};
 const events=[]; let calls=0, fallback=0, payload;
 const button={textContent:'Verstuur'}, ready={hidden:true}, error={};
 const form={id:'scanform',dataset:{},querySelector(s){return s.includes('botcheck')?{value:''}:button;},reset(){this.resetDone=true;}};
 const context={document:{getElementById(id){return nodes[id];}},FORM:{sleutel:'test-only'},CONTACT:{},location:{href:'https://example.com/scan/',pathname:'/scan/'},bericht(){return 'test';},doel(name){events.push(name);},zelfVersturen(){fallback++;},setTimeout(){},fetch:async(url,options)=>{calls++;payload=JSON.parse(options.body);return response;}};
 vm.createContext(context);vm.runInContext(code,context);
 context.verstuur(form,{website:'url',naam:'naam',bereikbaar:'contact',doel:'doel'},error,'Test scan',ready);
 context.verstuur(form,{website:'url',naam:'naam',bereikbaar:'contact',doel:'doel'},error,'Test scan',ready);
 await new Promise(resolve=>setImmediate(resolve));
 return {calls,fallback,events,ready,form,button,nodes,payload};
}
(async()=>{
 const success=await run({ok:true,json:async()=>({success:true})});
 assert.equal(success.calls,1);assert.equal(success.fallback,0);assert.equal(success.ready.hidden,false);assert.equal(success.nodes['scan-vervolg'].hidden,false);assert.equal(success.form.resetDone,true);assert.equal(success.events.filter(x=>x==='generate_lead').length,1);assert.equal(success.payload.doel,'');
 for(const response of [{ok:true,json:async()=>{throw Error('bad JSON');}},{ok:false,json:async()=>({success:true})},{ok:true,json:async()=>({success:false})},{ok:true,json:async()=>({success:'true'})}]){
  const result=await run(response);assert.equal(result.fallback,1);assert.equal(result.events.length,0);assert.equal(result.nodes['scan-vervolg'].hidden,true);assert.equal(result.button.disabled,false);
 }
 console.log('PASS: confirmed success, optional goal, duplicate guard, invalid JSON, HTTP error, rejection and non-boolean response. No network calls made.');
})().catch(error=>{console.error(error);process.exitCode=1;});
