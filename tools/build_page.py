"""Builds a project page from a dict. Usage: imported by tools/projects.py"""
import os, html
from PIL import Image
SRC='/mnt/project-files/portfolio-website/'
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E=html.escape
def img(slug, src):
    name=os.path.basename(src).split('-',2)[-1] if src.split('/')[-1][:2].isdigit() else os.path.basename(src)
    name=os.path.splitext(name)[0]+'.jpg'
    d=f'{ROOT}/bilder/{slug}'; os.makedirs(d,exist_ok=True)
    out=f'{d}/{name}'
    if not os.path.exists(out):
        im=Image.open(SRC+src)
        if im.mode in ('RGBA','LA','P'):
            im=im.convert('RGBA'); bg=Image.new('RGB',im.size,(0,0,0)); bg.paste(im,mask=im.split()[-1]); im=bg
        im=im.convert('RGB'); im.thumbnail((1800,1800)); im.save(out,quality=82,optimize=True,progressive=True)
    return f'../../bilder/{slug}/{name}'
def next_img(nx):
    slug=nx[2].strip('./').split('/')[-1]
    if slug=='scorpion': return '../../bilder/scorpion/historic-tram.jpg'
    return f'../../bilder/projekte/{nx[0]}-{slug}-cover.jpg?v=3'
def fig(slug,src,cap,alt):
    return f'<figure><img src="{img(slug,src)}" alt="{E(alt)}" loading="lazy"><figcaption>{E(cap)}</figcaption></figure>' if cap else f'<figure><img src="{img(slug,src)}" alt="{E(alt)}" loading="lazy"></figure>'
def justified(slug,images):
    n=len(images); nrows=max(1,round(n/3.4)); base,extra=divmod(n,nrows)
    sizes=[base+(1 if r>=nrows-extra else 0) for r in range(nrows)]
    out='<div class="gallery sketches">'; k=0
    for sz in sizes:
        out+='<div class="sk-row">'
        for src,cap,alt in images[k:k+sz]:
            url=img(slug,src); w,h=Image.open(os.path.join(ROOT,'bilder',slug,os.path.basename(url))).size; ar=w/h
            out+=f'<figure style="flex:{ar:.3f} 1 0"><img src="{url}" alt="{E(alt)}" loading="lazy" width="{w}" height="{h}"><figcaption>{E(cap)}</figcaption></figure>'
        out+='</div>'; k+=sz
    return out+'</div>'
def build(p):
    s=p['slug']
    meta=''.join(f'<div><dt>{E(k)}</dt><dd>{E(v)}</dd></div>' for k,v in p['meta'])
    secs=''
    where=' '.join(v for k,v in p['meta'] if k=='Where')
    uni='<div class="meta-uni"><img src="../../bilder/about/logo-htw-black.png?v=1" alt="" loading="lazy"><span>Hochschule für Technik<br>und Wirtschaft Berlin</span></div>' if 'HTW' in where else ('<div class="meta-uni sfsu"><img src="../../bilder/about/logo-sfsu-full.jpg?v=1" alt="San Francisco State University" loading="lazy"></div>' if 'San Francisco' in where else '')
    def ncols(sec):
        im=sec.get('images') or []
        if sec.get('layout')=='sketches': return 9
        if len(im) in (2,4): return 2
        if len(im)>=3: return 3
        return 0
    cols=[ncols(x) for x in p['sections']]
    for idx,sec in enumerate(p['sections']):
        c=cols[idx] or next((x for x in cols[idx+1:] if x), 3)
        tcls='text stack' if idx==0 else 'text t2' if c==2 else ('text stack' if c==9 else 'text')
        txt=''.join(f'<p>{E(t)}</p>' for t in sec.get('text',[]))
        gal=''
        if sec.get('images'):
            cls='gallery sketches' if sec.get('layout')=='sketches' else ('gallery two' if len(sec['images'])==4 else ('gallery one' if len(sec['images'])==1 else 'gallery'))
            if sec.get('layout')=='sketches':
                gal=justified(s,sec['images'])
            else:
                gal=f'<div class="{cls}">'+''.join(fig(s,*i) for i in sec['images'])+'</div>'
        head=f'<h2>{E(sec["title"])}</h2>'
        secs+=f'<section class="block"><div class="{tcls}">{head}<div>{txt}</div></div>{gal}</section>\n'
    nx=p['next']
    page=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(p["title"])} · {E(p["sub"])} · Leonard Philp</title>
<meta name="description" content="{E(p["desc"])}">
<link rel="stylesheet" href="../../style.css?v=32">
</head>
<body>
  <nav class="label"><a href="../../">Leonard Philp</a><ul><li><a href="../../#work">Work</a></li><li><a href="../../#about">About</a></li><li><a href="../../#newsletter">Newsletter</a></li><li><a href="../../#contact">Contact</a></li></ul></nav>
  <header class="p-hero">
    <p class="label accent">{E(p["label"])}</p>
    <h1>{E(p["title"])}</h1>
    <p class="tagline">{E(p["tagline"])}</p>
  </header>
  <img class="full" src="{img(s,p["cover"][0])}" alt="{E(p["cover"][1])}">
  <main class="p-body">
    <dl class="meta">{meta}{uni}</dl>
{secs}  </main>
  <footer class="next">
    <a class="next-link" href="{nx[2]}"><div class="next-img"><img src="{next_img(nx)}" alt="" loading="lazy"></div><div class="next-meta"><span class="label accent">Next project</span><span class="label">{nx[0]}</span><h2>{E(nx[1])}</h2><span class="label go">View project →</span></div></a>
  </footer>
  <script src="../../lightbox.js?v=5" defer></script>
</body>
</html>
'''
    os.makedirs(f'{ROOT}/work/{s}',exist_ok=True)
    open(f'{ROOT}/work/{s}/index.html','w').write(page)
