"""Adds icons, canonical URL and social-sharing (Open Graph) tags to every page. Run after projects.py."""
import os, re, glob, html, json
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE='https://leonardphilp.com'
def block(path, title, desc, url, img, pre, extra=''):
    dims='<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n' if path=='index.html' else ''
    return f'''<!--seo-->
<link rel="canonical" href="{url}">
<link rel="icon" href="{pre}favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{pre}favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="{pre}favicon-192.png">
<link rel="apple-touch-icon" href="{pre}apple-touch-icon.png">
<meta name="theme-color" content="#111111">
<meta name="author" content="Leonard Philp">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Leonard Philp · Industrial Design">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img}">
{dims}<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{img}">
{extra}<!--/seo-->'''
pages=['index.html']+sorted(glob.glob('work/*/index.html',root_dir=ROOT))
urls=[]
for rel in pages:
    p=os.path.join(ROOT,rel); s=open(p).read()
    s=re.sub(r'\n?<!--seo-->.*?<!--/seo-->','',s,flags=re.S)
    title=html.unescape(re.search(r'<title>(.*?)</title>',s).group(1))
    desc=html.unescape(re.search(r'<meta name="description" content="(.*?)">',s).group(1))
    if rel=='index.html':
        url=SITE+'/'; pre=''; img=SITE+'/og-image.jpg'
        ld={"@context":"https://schema.org","@type":"Person","name":"Leonard Philp","jobTitle":"Industrial Design Student","url":url,
            "affiliation":{"@type":"CollegeOrUniversity","name":"HTW Berlin – Hochschule für Technik und Wirtschaft Berlin"},
            "address":{"@type":"PostalAddress","addressLocality":"Berlin","addressCountry":"DE"},
            "knowsAbout":["Industrial design","Transportation design","Automotive design","Product design","Tape rendering","Car sketching"],
            "sameAs":re.findall(r'href="(https://(?:www\.)?(?:instagram|linkedin|behance)\.[^"]+)"',s)}
        extra='<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False)+'</script>\n'
    else:
        slug=rel.split('/')[1]; url=f'{SITE}/work/{slug}/'; pre='../../'
        m=re.search(r'<img class="full" src="\.\./\.\./([^"?]+)',s)
        img=SITE+'/'+m.group(1) if m else SITE+'/og-image.jpg'; extra=''
    E=lambda t: html.escape(t,quote=True)
    b=block(rel,E(title),E(desc),url,img,pre,extra)
    s=s.replace('<link rel="stylesheet"',b+'\n<link rel="stylesheet"',1)
    open(p,'w').write(s); urls.append(url)
open(os.path.join(ROOT,'sitemap.xml'),'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{u}</loc></url>\n' for u in urls)+'</urlset>\n')
open(os.path.join(ROOT,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
print(len(urls),'pages')
