/* Deterministic gameplay rules; no renderer, storage or network dependencies. */
(function(root){
'use strict';
const VERSION=1, SAVE_KEY='emberbrook.save.v1';
function initial(){return {version:VERSION,wood:0,ore:0,gold:120,health:100,xp:0,level:1,sword:false,relic:false,claimed:false,chestOpened:false,fish:0,herbs:0,potions:0,orders:0,shrineBlessed:false,gatheredWood:0,gatheredOre:0,kills:0,scene:'village',x:785,y:720,language:'en',sound:false};}
function normalize(raw){const s=initial();if(!raw||typeof raw!=='object'||raw.version!==VERSION)return s;for(const k of ['wood','ore','gold','health','xp','level','gatheredWood','gatheredOre','kills','fish','herbs','potions','orders'])if(Number.isFinite(raw[k]))s[k]=Math.max(0,Math.min(k==='health'?100:999999,Math.floor(raw[k])));for(const k of ['sword','relic','claimed','sound','chestOpened','shrineBlessed'])s[k]=raw[k]===true;s.language=raw.language==='zh'?'zh':'en';s.scene=raw.scene==='forest'?'forest':raw.scene==='dungeon'&&s.sword?'dungeon':'village';if(Number.isFinite(raw.x)&&Number.isFinite(raw.y)){s.x=Math.max(95,Math.min(1435,raw.x));s.y=Math.max(150,Math.min(900,raw.y));}return s;}
function stage(s){return s.claimed?4:s.relic?3:s.sword?2:s.gatheredWood>=3&&s.gatheredOre>=2?1:0;}
function gather(s,type){if(!['wood','ore'].includes(type))return {ok:false,reason:'invalid'};s[type]++;s[type==='wood'?'gatheredWood':'gatheredOre']++;s.xp+=5;return {ok:true,type};}
function craft(s){if(s.sword)return {ok:false,reason:'owned'};if(s.wood<3||s.ore<2||s.gold<30)return {ok:false,reason:'materials'};s.wood-=3;s.ore-=2;s.gold-=30;s.sword=true;s.xp+=25;return {ok:true};}
function claim(s){if(!s.relic)return {ok:false,reason:'relic'};if(s.claimed)return {ok:false,reason:'claimed'};s.claimed=true;s.gold+=250;s.xp+=100;s.level=Math.max(s.level,2);return {ok:true};}
function takeRelic(s){if(s.kills<3)return {ok:false,reason:'enemies'};if(s.relic)return {ok:false,reason:'owned'};s.relic=true;s.xp+=50;return {ok:true};}
function insideRect(x,y,r){return x>=r[0]&&y>=r[1]&&x<=r[2]&&y<=r[3];}
const villageBlocks=[[120,225,570,470],[865,270,1300,500],[590,480,735,605],[105,630,450,840],[890,840,1290,1024],[0,0,640,155]];
const dungeonBlocks=[[655,225,905,385],[285,245,380,380],[1140,245,1220,400]];
// Collision uses a foot radius, not the sprite's bounding box. The river is
// only crossable on the bridge deck; crops and the entrance sign are solid.
function insidePolygon(x,y,points){let inside=false;for(let i=0,j=points.length-1;i<points.length;j=i++){const a=points[i],b=points[j];if((a[1]>y)!==(b[1]>y)&&x<(b[0]-a[0])*(y-a[1])/(b[1]-a[1])+a[0])inside=!inside;}return inside;}
const roofBlocks=[[[120,260],[380,135],[500,155],[590,310]],[[835,305],[930,175],[1115,175],[1190,270],[1300,340]]];
// Walkable surfaces are explicitly traced from the illustration. Empty space
// between old rectangular blockers is not automatically traversable scenery.
const villageGround=[[[495,480],[590,480],[590,625],[495,625]],
[[145,500],[340,480],[480,470],[580,470],[590,610],[735,625],[755,550],[860,500],[1180,520],[1230,550],[1220,610],[1150,640],[1090,670],[980,740],[850,760],[840,850],[800,930],[650,930],[640,850],[620,800],[540,760],[480,690],[440,625],[230,620],[145,570]],
[[535,480],[600,360],[660,290],[720,235],[780,200],[850,165],[900,150],[900,185],[850,215],[780,250],[730,310],[700,350],[650,430],[620,510]],
[[810,160],[910,125],[1040,140],[1170,145],[1270,130],[1300,180],[1290,245],[1230,250],[1180,230],[1080,220],[1000,200],[900,205],[840,220]],
[[1190,578],[1290,578],[1450,574],[1490,580],[1490,630],[1410,638],[1260,638],[1190,620]]];
const sceneryBlocks=[[[744,282],[846,260],[873,360],[830,394],[754,375]],[[780,379],[874,375],[886,453],[820,468]],[[610,838],[650,838],[655,906],[615,906]],[[795,837],[832,837],[831,905],[795,905]]];
const forestGround=[[[180,430],[350,350],[550,330],[620,300],[680,230],[720,130],[800,130],[800,210],[760,300],[850,290],[1050,280],[1190,290],[1210,340],[1130,390],[1080,450],[1050,500],[1100,515],[1280,515],[1280,570],[1090,580],[1050,640],[970,690],[850,750],[820,850],[810,1024],[650,1024],[680,850],[640,760],[480,730],[330,690],[260,610],[190,550]]];
function rawWalkable(x,y,scene){if(scene==='dungeon')return x>=245&&x<=1290&&y>=395&&y<=820&&!dungeonBlocks.some(r=>insideRect(x,y,r));if(scene==='forest')return forestGround.some(p=>insidePolygon(x,y,p))&&![[610,430,865,574],[270,390,440,520],[850,300,1025,405]].some(r=>insideRect(x,y,r));return villageGround.some(p=>insidePolygon(x,y,p))&&!villageBlocks.some(r=>insideRect(x,y,r))&&!roofBlocks.some(p=>insidePolygon(x,y,p))&&!sceneryBlocks.some(p=>insidePolygon(x,y,p));}
function safePosition(p,scene){if(walkable(p.x,p.y,scene))return {x:p.x,y:p.y};let best=null;for(let y=144;y<=928;y+=16)for(let x=112;x<=1472;x+=16){const d=Math.hypot(x-p.x,y-p.y);if((!best||d<best.d)&&walkable(x,y,scene))best={x,y,d};}return best?{x:best.x,y:best.y}:{x:785,y:720};}
function catchFish(s,phase){if(!Number.isFinite(phase)||phase<.38||phase>.62)return {ok:false};s.fish++;s.xp+=8;return {ok:true};}
function gatherHerb(s){s.herbs++;s.xp+=5;return {ok:true};}
function fulfillOrder(s){if(s.fish<2||s.herbs<3)return {ok:false};s.fish-=2;s.herbs-=3;s.orders++;s.gold+=65;s.xp+=35;s.potions++;s.level=Math.max(s.level,1+Math.floor(s.xp/180));return {ok:true};}
function drinkPotion(s){if(s.potions<1||s.health>=100)return {ok:false};s.potions--;s.health=Math.min(100,s.health+50);return {ok:true};}
function blessShrine(s){if(s.shrineBlessed||s.orders<1)return {ok:false};s.shrineBlessed=true;s.gold+=100;s.xp+=60;return {ok:true};}
function walkable(x,y,scene){return [[0,0],[8,0],[-8,0],[0,8],[0,-8],[6,6],[-6,6],[6,-6],[-6,-6]].every(([a,b])=>rawWalkable(x+a,y+b,scene));}
function segmentWalkable(a,b,scene){const n=Math.max(1,Math.ceil(Math.hypot(b.x-a.x,b.y-a.y)/4));for(let i=0;i<=n;i++)if(!walkable(a.x+(b.x-a.x)*i/n,a.y+(b.y-a.y)*i/n,scene))return false;return true;}
function move(from,dx,dy,scene){let p={x:from.x,y:from.y};const n=Math.max(1,Math.ceil(Math.hypot(dx,dy)/4));for(let i=0;i<n;i++){if(walkable(p.x+dx/n,p.y,scene))p.x+=dx/n;if(walkable(p.x,p.y+dy/n,scene))p.y+=dy/n;}return p;}
function joystickVector(x,y,radius=42){const d=Math.hypot(x,y),m=Math.min(1,d/radius);if(m<.16)return {x:0,y:0};const v=(m-.16)/.84;return {x:x/d*v,y:y/d*v};}
function route(from,to,scene){if(!walkable(from.x,from.y,scene)||!walkable(to.x,to.y,scene))return [];if(segmentWalkable(from,to,scene))return [{x:to.x,y:to.y}];const step=16,key=p=>p.x+','+p.y;
const cell=p=>{let best=null;for(let a=-2;a<=2;a++)for(let b=-2;b<=2;b++){const c={x:Math.round(p.x/step)+a,y:Math.round(p.y/step)+b},w={x:c.x*step,y:c.y*step},d=Math.hypot(w.x-p.x,w.y-p.y);if((!best||d<best.d)&&segmentWalkable(p,w,scene))best={...c,d};}return best;};const start=cell(from),goal=cell(to);if(!start||!goal)return [];
const open=[{...start,g:0,f:0}],seen=new Map(),closed=new Set();seen.set(key(start),open[0]);let end=null;
for(let count=0;open.length&&count<10000;count++){open.sort((a,b)=>a.f-b.f);const cur=open.shift(),ck=key(cur);if(closed.has(ck))continue;closed.add(ck);if(cur.x===goal.x&&cur.y===goal.y){end=cur;break;}for(const [dx,dy] of [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]){const n={x:cur.x+dx,y:cur.y+dy};if(closed.has(key(n))||!segmentWalkable({x:cur.x*step,y:cur.y*step},{x:n.x*step,y:n.y*step},scene))continue;const g=cur.g+Math.hypot(dx,dy),old=seen.get(key(n));if(!old||g<old.g){const next={...n,g,f:g+Math.hypot(n.x-goal.x,n.y-goal.y),parent:cur};seen.set(key(n),next);open.push(next);}}}
if(!end)return [];const points=[{x:to.x,y:to.y}];for(let c=end;c;c=c.parent)points.unshift({x:c.x*step,y:c.y*step});const result=[];let anchor=from,i=0;while(i<points.length){let j=points.length-1;while(j>i&&!segmentWalkable(anchor,points[j],scene))j--;result.push(points[j]);anchor=points[j];i=j+1;}return result;}
const api={VERSION,SAVE_KEY,initial,normalize,stage,gather,craft,claim,takeRelic,walkable,segmentWalkable,move,joystickVector,route,safePosition,catchFish,gatherHerb,fulfillOrder,drinkPotion,blessShrine};root.EmberCore=api;if(typeof module!=='undefined')module.exports=api;
})(typeof globalThis!=='undefined'?globalThis:this);
