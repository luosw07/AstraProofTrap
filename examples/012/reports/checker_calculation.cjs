'use strict';

// Independent finite check of the counterexample in tricker_report.md.
// All arithmetic used for join coordinates is integral, in units of 1/4.
// This is ordinary graph enumeration, not a formal proof assistant.
const assert = require('node:assert/strict');

const n = 13;
const edges = [
  [0,1], [0,5], [0,9], [0,12],
  [1,2], [1,8], [1,11],
  [2,3], [2,5], [2,9],
  [3,4], [3,10], [3,12],
  [4,5], [4,10], [4,11],
  [5,6], [6,7], [6,11], [6,12],
  [7,8], [7,9], [7,10], [8,9], [8,10], [11,12]
];
const key = (a,b) => a < b ? `${a}-${b}` : `${b}-${a}`;
assert.equal(new Set(edges.map(e => key(...e))).size, edges.length);
assert(edges.every(([a,b]) => 0 <= a && a < b && b < n));
const adj = Array.from({length:n}, () => []);
for (const [a,b] of edges) { adj[a].push(b); adj[b].push(a); }
for (const a of adj) { a.sort((x,y) => x-y); assert.equal(a.length,4); }

const connectivityCounts = [0,0,0,0];
function checkDeletion(deleted) {
  const forbidden = new Set(deleted);
  const start = adj.findIndex((_,v) => !forbidden.has(v));
  const reached = new Set([start]);
  const stack = [start];
  while (stack.length) {
    const v = stack.pop();
    for (const w of adj[v]) if (!forbidden.has(w) && !reached.has(w)) {
      reached.add(w); stack.push(w);
    }
  }
  assert.equal(reached.size, n-deleted.length,
    `Disconnected after deleting ${deleted.join(',')}`);
  connectivityCounts[deleted.length]++;
}
function chooseDeleted(size, chosen=[], next=0) {
  if (chosen.length === size) return checkDeletion(chosen);
  for (let v=next;v<n;v++) chooseDeleted(size,[...chosen,v],v+1);
}
for (let size=0;size<=3;size++) chooseDeleted(size);
assert.deepEqual(connectivityCounts,[1,13,78,286]);

const parent = Array(n).fill(-1), depth = Array(n).fill(-1);
const children = Array.from({length:n}, () => []), preorder = [];
function dfs(v) {
  depth[v] = parent[v] < 0 ? 0 : depth[parent[v]]+1;
  preorder.push(v);
  for (const w of adj[v]) if (depth[w] < 0) {
    parent[w]=v; children[v].push(w); dfs(w);
  }
}
dfs(0);
assert.deepEqual(preorder,Array.from({length:n},(_,i)=>i));
assert.deepEqual(parent,[-1,0,1,2,3,4,5,6,7,8,8,6,11]);
const isTree = (a,b) => parent[a] === b || parent[b] === a;
const incoming = Array.from({length:n},()=>[]);
const starMap = new Map();
for (let [a,b] of edges) {
  if (isTree(a,b)) continue;
  if (depth[a] > depth[b]) [a,b]=[b,a];
  incoming[a].push(b);
  let v=b;
  while (parent[v] !== a) {
    assert(parent[v]>=0, 'Non-tree edge does not join ancestor and descendant');
    v=parent[v];
  }
  const id=key(a,v);
  if (!starMap.has(id)) starMap.set(id,{center:a,child:v,edges:[[a,v]]});
  starMap.get(id).edges.push([a,b]);
}
const stars=[...starMap.values()].sort((a,b)=>a.center-b.center);
stars.forEach((s,i)=>{s.aux=n+i; s.edges=s.edges.map(e=>e.sort((a,b)=>a-b)).sort((a,b)=>a[0]-b[0]||a[1]-b[1]);});
const at = new Map(stars.map(s=>[s.center,s]));
const B2=preorder.filter(v=>v!==0&&children[v].length===2&&incoming[v].length===1);
const U=B2.filter(v=>!starMap.has(key(parent[v],v)));
const otherChild=v=>children[v].find(w=>!starMap.has(key(v,w)));
const D=B2.filter(v=>{
  const p=parent[v],w=otherChild(v),sp=starMap.get(key(p,v));
  return p!==0&&sp&&sp.edges.length===2&&sp.edges.some(e=>key(...e)===key(p,w))
    &&children[w].length===1&&incoming[w].length===1;
});
assert.deepEqual(B2,[6]); assert.deepEqual(U,[6]); assert.deepEqual(D,[]);
assert.equal(otherChild(6),7);
assert.equal(at.get(7).edges.length,3);
assert(!starMap.has(key(5,6)));
// Thus K has the sole node 6 and the unique maximum matching is empty.
const N=edges.filter(e=>!stars.some(s=>s.edges.some(f=>key(...e)===key(...f))));
assert.deepEqual(N,[[5,6],[6,7],[8,9],[8,10],[11,12]]);

const H=[];
for (const [a,b] of edges) {
  const s=stars.find(s=>s.edges.some(e=>key(...e)===key(a,b)));
  const ends=s?[s.aux,a===s.center?b:a]:[a,b];
  const value=isTree(a,b)?1:(s.center===0||s.edges.length===3?3:2);
  H.push({a:ends[0],b:ends[1],label:`rep(${a},${b})`,value});
}
for (const s of stars) H.push({a:s.center,b:s.aux,label:`c_${s.center}`,value:s.center===0?4:1});
const original=H.map(e=>({...e})),modified=H.map(e=>({...e}));
// There are no free parent-edge changes: the only B2 vertex has parent edge in N.
original.find(e=>e.label==='c_6').value=2;
modified.find(e=>e.label==='rep(6,7)').value=2;
const demandBoundary=modified.filter(e=>(e.a===6)!==(e.b===6));
assert.equal(demandBoundary.reduce((s,e)=>s+e.value,0),4);
const violatingCut=modified.filter(e=>(e.a===7)!==(e.b===7));
assert.deepEqual(violatingCut.map(e=>e.label),['rep(6,7)','c_7']);
const violationQuarter=violatingCut.find(e=>e.label==='c_7').value
  +4-violatingCut.find(e=>e.label==='rep(6,7)').value;
assert.equal(violationQuarter,3);

function objectiveQuarter(vector) {
  let total=4*(n-1);
  for (const e of N) total+=vector.find(a=>a.label===`rep(${e[0]},${e[1]})`).value;
  for (const s of stars) {
    const reprSum=s.edges.reduce((sum,e)=>sum+vector.find(a=>a.label===`rep(${e[0]},${e[1]})`).value,0);
    total+=Math.max(vector.find(e=>e.label===`c_${s.center}`).value,4*(s.edges.length-1)-reprSum);
  }
  return total;
}
assert.equal(objectiveQuarter(H),63);
assert.equal(objectiveQuarter(original),64);
assert.equal(objectiveQuarter(modified),64);

function checkAllBlossoms(vector) {
  const size=n+stars.length;
  let minQuarter=Infinity,violatedCuts=0,witness=null;
  // Fix the last auxiliary vertex outside the shore, so each nontrivial cut
  // appears exactly once. For each cut, minimize over choices with an odd
  // number of positive-side terms, i.e. |C minus F| odd.
  for (let mask=1;mask<(1<<(size-1));mask++) {
    let sum=0,positiveParity=0,parityFlip=Infinity,crossing=0;
    for (const e of vector) if (((mask>>>e.a)&1)!==((mask>>>e.b)&1)) {
      crossing++;
      sum+=Math.min(e.value,4-e.value);
      if (e.value<=2) positiveParity^=1;
      parityFlip=Math.min(parityFlip,Math.abs(4-2*e.value));
    }
    if (!crossing) continue;
    if (!positiveParity) sum+=parityFlip;
    if (sum<4) violatedCuts++;
    if (sum<minQuarter) {
      minQuarter=sum;
      witness=Array.from({length:size},(_,v)=>v).filter(v=>(mask>>>v)&1);
    }
  }
  return {cutCount:(1<<(size-1))-1,minQuarter,violatedCuts,witness};
}
const originalBlossoms=checkAllBlossoms(original);
const modifiedBlossoms=checkAllBlossoms(modified);
assert.equal(originalBlossoms.minQuarter,4);
assert.equal(originalBlossoms.violatedCuts,0);
assert.equal(modifiedBlossoms.minQuarter,3);
assert.equal(modifiedBlossoms.violatedCuts,4);

const result={
  run_id:'tricker_3301',
  graph:{n,m:edges.length,edges,adjacency:adj,connectivityCounts,
    allVertexDeletionsOfSizeAtMostThreeConnected:true},
  dfs:{root:0,neighborOrder:'increasing numerical order',preorder,parent,children,incoming},
  stars,nonremovableEdges:N,
  demands:{B2,U,D,correctionGraphVertices:[6],correctionGraphEdges:[],maximumMatching:[]},
  changes:{original:['c_6: 1/4 -> 1/2'],modified:['rep(6,7): 1/4 -> 1/2'],paidIncreaseCount:1},
  witness:{shore:[7],cut:violatingCut,F:['rep(6,7)'],positiveSide:['c_7'],
    leftHandSideQuarter:violationQuarter,requiredQuarter:4},
  objectiveQuarter:{initial:objectiveQuarter(H),original:objectiveQuarter(original),modified:objectiveQuarter(modified)},
  blossomEnumeration:{original:originalBlossoms,modified:modifiedBlossoms}
};
console.log(JSON.stringify({
  graphVertices:n,graphEdges:edges.length,vertexDeletionChecks:connectivityCounts,
  fourVertexConnected:true,demands:result.demands,
  witnessLeftHandSide:'3/4',required:'1',objective:'16',
  originalBlossoms,modifiedBlossoms
},null,2));
