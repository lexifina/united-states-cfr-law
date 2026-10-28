"""Per-window diagnosis: how many changed sections have versioner dates in the window."""
import sys, collections, difflib
import parse as P
P.below_normal()
n=int(sys.argv[1]); show=int(sys.argv[2]) if len(sys.argv)>2 else 0
t=[t for t in P.E.titles() if t['number']==n][0]
dates=collections.defaultdict(list)
for v in P.E.versions(n): dates[v['identifier']].append(v['amendment_date'])
prev=None
for day,label,secs,url in P.snapshots(t):
    if prev:
        d0,s0=prev; c=collections.Counter(); ex=[]
        for sid in set(s0)|set(secs):
            a,b=s0.get(sid),secs.get(sid)
            if a and b and P.same(P.text_of(a),P.text_of(b)): continue
            inside=[d for d in dates.get(sid,[]) if d0<d<=day]
            kind=('dated' if inside else 'undated')+('-add' if not a else '-rm' if not b else '')
            c[kind]+=1
            if not inside and a and b and len(ex)<show: ex.append((sid,a,b))
        print(day,label,len(secs),dict(c))
        for sid,a,b in ex:
            print('  ##',sid)
            for l in difflib.unified_diff(P.text_of(a).split('\n'),P.text_of(b).split('\n'),lineterm='',n=0): print('   ',l[:160])
    prev=(day,secs)
print(P.SKIPPED)
