/* Deterministic gameplay rules; no renderer, storage or network dependencies. */
(function(root){
'use strict';
const VERSION=1, SAVE_KEY='emberbrook.save.v1';
function initial(){return {version:VERSION,wood:0,ore:0,gold:120,health:100,xp:0,level:1,sword:false,relic:false,claimed:false,chestOpened:false,gatheredWood:0,gatheredOre:0,kills:0,scene:'village',x:785,y:760,language:'en',sound:false};}
function normalize(raw){const s=initial();if(!raw||typeof raw!=='object'||raw.version!==VERSION)return s;for(const k of ['wood','ore','gold','health','xp','level','gatheredWood','gatheredOre','kills'])if(Number.isFinite(raw[k]))s[k]=Math.max(0,Math.min(k==='health'?100:999999,Math.floor(raw[k])));for(const k of ['sword','relic','claimed','sound','chestOpened'])s[k]=raw[k]===true;s.language=raw.language==='zh'?'zh':'en';s.scene=raw.scene==='dungeon'&&s.sword?'dungeon':'village';if(Number.isFinite(raw.x)&&Number.isFinite(raw.y)){s.x=Math.max(95,Math.min(1435,raw.x));s.y=Math.max(150,Math.min(900,raw.y));}return s;}
function stage(s){return s.claimed?4:s.relic?3:s.sword?2:s.gatheredWood>=3&&s.gatheredOre>=2?1:0;}
function gather(s,type){if(!['wood','ore'].includes(type))return {ok:false,reason:'invalid'};s[type]++;s[type==='wood'?'gatheredWood':'gatheredOre']++;s.xp+=5;return {ok:true,type};}
function craft(s){if(s.sword)return {ok:false,reason:'owned'};if(s.wood<3||s.ore<2||s.gold<30)return {ok:false,reason:'materials'};s.wood-=3;s.ore-=2;s.gold-=30;s.sword=true;s.xp+=25;return {ok:true};}
function claim(s){if(!s.relic)return {ok:false,reason:'relic'};if(s.claimed)return {ok:false,reason:'claimed'};s.claimed=true;s.gold+=250;s.xp+=100;s.level=2;return {ok:true};}
function takeRelic(s){if(s.kills<3)return {ok:false,reason:'enemies'};if(s.relic)return {ok:false,reason:'owned'};s.relic=true;s.xp+=50;return {ok:true};}
function insideRect(x,y,r){return x>=r[0]&&y>=r[1]&&x<=r[2]&&y<=r[3];}
const villageBlocks=[[120,225,570,470],[865,270,1300,500],[590,480,735,605],[105,630,450,840],[890,840,1290,1024],[0,0,640,155]];
const dungeonBlocks=[[655,225,905,385],[285,245,380,380],[1140,245,1220,400]];
function walkable(x,y,scene){if(scene==='dungeon')return x>=245&&x<=1290&&y>=395&&y<=820&&!dungeonBlocks.some(r=>insideRect(x,y,r));return x>=100&&x<=1425&&y>=165&&y<=930&&!(x>1300&&(y<535||y>670))&&!villageBlocks.some(r=>insideRect(x,y,r));}
// A* on a 24px grid, 4-way movement keeps routes outside solid props.
function route(from,to,scene){const step=24;const cell=p=>({x:Math.round(p.x/step),y:Math.round(p.y/step)});const start=cell(from);let goal=cell(to);const valid=p=>walkable(p.x*step,p.y*step,scene);if(!valid(goal)){let best=null;for(let d=1;d<7&&!best;d++)for(let a=-d;a<=d;a++)for(let b=-d;b<=d;b++){const c={x:goal.x+a,y:goal.y+b};if(valid(c)&&(!best||Math.hypot(a,b)<best.dist))best={...c,dist:Math.hypot(a,b)};}if(!best)return [];goal=best;}
const key=p=>p.x+','+p.y, open=[{...start,g:0,f:0}], seen=new Map(),closed=new Set();seen.set(key(start),open[0]);let end=null;
for(let count=0;open.length&&count<4500;count++){open.sort((a,b)=>a.f-b.f);const cur=open.shift(),ck=key(cur);if(closed.has(ck))continue;closed.add(ck);if(cur.x===goal.x&&cur.y===goal.y){end=cur;break;}for(const [dx,dy] of [[1,0],[-1,0],[0,1],[0,-1]]){const n={x:cur.x+dx,y:cur.y+dy};if(!valid(n)||closed.has(key(n)))continue;const g=cur.g+1,old=seen.get(key(n));if(!old||g<old.g){const next={...n,g,f:g+Math.abs(n.x-goal.x)+Math.abs(n.y-goal.y),parent:cur};seen.set(key(n),next);open.push(next);}}}
const result=[];for(let c=end;c&&c.parent;c=c.parent)result.unshift({x:c.x*step,y:c.y*step});return result;}
const api={VERSION,SAVE_KEY,initial,normalize,stage,gather,craft,claim,takeRelic,walkable,route};root.EmberCore=api;if(typeof module!=='undefined')module.exports=api;
})(typeof globalThis!=='undefined'?globalThis:this);
