const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const assert = require('node:assert/strict');
const root = path.resolve(__dirname, '..');
const html = fs.readFileSync(path.join(root, 'START_HERE.html'), 'utf8');
const script = html.match(/<script>([\s\S]*)<\/script>/)[1];
class Element {
  constructor(tag) {
    this.tagName=tag;this.children=[];this.textContent='';this.className='';
    this.dataset={};this.style={};this.value='';this.listeners={};this.classes=new Set();
    this.classList={toggle:(name,on)=>on?this.classes.add(name):this.classes.delete(name)};
  }
  append(...items){this.children.push(...items);}
  replaceChildren(...items){this.children=items;}
  addEventListener(name,fn){this.listeners[name]=fn;}
}
const elements=Object.fromEntries(['nav','profile','query','sources'].map(id=>[id,new Element('div')]));
const document={
  createElement:tag=>new Element(tag),
  createTextNode:text=>Object.assign(new Element('#text'),{textContent:text}),
  getElementById:id=>elements[id],
  querySelectorAll:selector=>{assert.equal(selector,'#nav button');return elements.nav.children;},
};
const context=vm.createContext({document});
vm.runInContext(script,context);
const textOf=node=>node.textContent+' '+node.children.map(textOf).join(' ');
assert.equal(elements.nav.children.length,8);
assert.equal(elements.sources.children.length,99);
assert.match(textOf(elements.profile),/60s 间谍片头/);
elements.nav.children.find(n=>n.dataset.id==='silhouette-rhythm').listeners.click();
assert.match(textOf(elements.profile),/剪影律动/);
assert.equal(elements.nav.children.filter(n=>n.classes.has('active')).length,1);
elements.query.value='paper-popup';elements.query.listeners.input();
assert.equal(elements.sources.children.length,1);
assert.match(textOf(elements.sources),/纸片立体书/);
elements.query.value='no_such_style_123';elements.query.listeners.input();
assert.equal(elements.sources.children.length,0);
const report={status:'passed',profiles:8,reference_entries:99,
  checks:['initial profile','profile switching','single active selector','slug search','empty search results'],
  scope:'Offline reader JavaScript behavior in a minimal DOM; not a browser screenshot or visual-quality test.'};
fs.writeFileSync(path.join(root,'validation/reader_report.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report));
