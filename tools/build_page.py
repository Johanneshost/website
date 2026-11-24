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
        im=Image.open(SRC+src).convert('RGB'); im.thumbnail((1800,1800)); im.save(out,quality=82,optimize=True,progressive=True)
    return f'../../bilder/{slug}/{name}'
def fig(slug,src,cap,alt):
    return f'<figure><img src="{img(slug,src)}" alt="{E(alt)}" loading="lazy"><figcaption>{E(cap)}</figcaption></figure>' if cap else f'<figure><img src="{img(slug,src)}" alt="{E(alt)}" loading="lazy"></figure>'
def build(p):
    s=p['slug']
    meta=''.join(f'<div><dt>{E(k)}</dt><dd>{E(v)}</dd></div>' for k,v in p['meta'])
    secs=''
    for sec in p['sections']:
        txt=''.join(f'<p>{E(t)}</p>' for t in sec.get('text',[]))
        gal=''
        if sec.get('images'):
            cls='gallery two' if len(sec['images'])==4 else ('gallery one' if len(sec['images'])==1 else 'gallery')
            gal=f'<div class="{cls}">'+''.join(fig(s,*i) for i in sec['images'])+'</div>'
        secs+=f'<section class="block"><div class="text"><h2>{E(sec["title"])}</h2><div>{txt}</div></div>{gal}</section>\n'
    nx=p['next']
    page=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(p["title"])} · {E(p["sub"])} · Leonard Philp</title>
<meta name="description" content="{E(p["desc"])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@600;700&family=Inter:wght@400;500&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../style.css">
</head>
<body>
  <nav class="label"><a href="../../">Leonard Philp</a><ul><li><a href="../../#work">Work</a></li></ul></nav>
  <header class="p-hero">
    <p class="label accent">{E(p["label"])}</p>
    <h1>{E(p["title"])}</h1>
    <p class="tagline">{E(p["tagline"])}</p>
  </header>
  <img class="full" src="{img(s,p["cover"][0])}" alt="{E(p["cover"][1])}">
  <main class="p-body">
    <dl class="meta">{meta}</dl>
{secs}  </main>
  <footer class="next">
    <span class="label accent">Next project</span>
    <a href="{nx[2]}"><span class="label">{nx[0]}</span><h2>{E(nx[1])}</h2></a>
  </footer>
</body>
</html>
'''
    os.makedirs(f'{ROOT}/work/{s}',exist_ok=True)
    open(f'{ROOT}/work/{s}/index.html','w').write(page)
