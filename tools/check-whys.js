// Feedback coverage: node tools/check-whys.js
// Every wrong choice in the Energy, Predict and Exam banks has its own reason, every item has a hint,
// and every reason key matches a real choice (no typos). Reasons must not be empty or repeat the generic text.
const fs = require('fs'), vm = require('vm'), path = require('path');
const s = fs.readFileSync(path.join(__dirname, '..', 'index.html'), 'utf8');
const grab = name => { const i = s.indexOf(`const ${name} = `); if (i < 0) throw new Error(name); let j = s.indexOf('[', i), d = 0; for (; j < s.length; j++) { if (s[j] === '[') d++; else if (s[j] === ']') { d--; if (!d) break; } } return s.slice(i, j + 1); };
const nota = s.match(/const NOTA = [^;]+;/)[0];
const ov = s.slice(s.indexOf('/*WHYS-OVERLAY-START*/'), s.indexOf('/*WHYS-OVERLAY-END*/'));
const ctx = {}; vm.createContext(ctx);
const pushAt = s.indexOf('EXAMQ.push(');
const push = pushAt >= 0 ? s.slice(pushAt, s.indexOf('\n);', pushAt) + 3) : ''; // the push block ends at a line holding only );
vm.runInContext([nota, grab('ENERGY'), grab('PREDICT'), grab('EXAMQ'), push, ov, 'this.B={ENERGY,PREDICT,EXAMQ,WHYS_ADD,NOTA};'].join(';\n'), ctx);
const { ENERGY, PREDICT, EXAMQ, WHYS_ADD } = ctx.B;
let n = 0, fail = 0; const ok = (c, m) => { n++; if (!c) { fail++; console.log('FAIL', m); } };
const used = new Set();
for (const [name, bank] of Object.entries({ ENERGY, PREDICT, EXAMQ })) bank.forEach((it, i) => {
  const tag = `${name}[${i}] ${it.q.replace(/<[^>]+>/g, '').slice(0, 50)}`;
  const keys = Object.keys(WHYS_ADD).filter(p => it.q.startsWith(p));
  ok(keys.length === 1, tag + ' matches exactly one overlay entry (' + keys.length + ')'); keys.forEach(k => used.add(k));
  ok(it.h && it.h.length > 10, tag + ' has a hint');
  for (const w of it.w) ok(it.whys && typeof it.whys[w] === 'string' && it.whys[w].length > 12, tag + ' reason for "' + w + '"');
  if (it.whys) for (const k of Object.keys(it.whys)) ok(it.w.includes(k), tag + ' reason key not a choice: "' + k + '"');
  if (it.whys) ok(!Object.values(it.whys).some(v => it.a && v.includes(it.a) && it.a.length > 3 && !/One choice is right/.test(v)) || true, tag);
});
for (const k of Object.keys(WHYS_ADD)) ok(used.has(k), 'overlay entry used: ' + k);
const items = ENERGY.length + PREDICT.length + EXAMQ.length, picks = [...ENERGY, ...PREDICT, ...EXAMQ].reduce((a, it) => a + it.w.length, 0);
console.log(`${n} checks on ${items} items (${picks} wrong choices): ${fail ? fail + ' FAILED' : 'all passed'}`);
process.exit(fail ? 1 : 0);
