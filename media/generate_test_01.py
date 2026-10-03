#!/usr/bin/env python3
"""NEXO / Experimento 01: carrossel autoral para Instagram (1080x1350)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1350
OUT = Path(__file__).resolve().parents[1] / "assets" / "teste-01-ideia-para-plano"
OUT.mkdir(parents=True, exist_ok=True)
BG = "#0D1427"
WHITE = "#F3F5F2"
MUTED = "#B6C1CD"
MINT = "#B3F4CF"
LIME = "#D4FC77"
PURPLE = "#B8B4FF"
PANEL = "#1A2639"

def f(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/" + name, size)

def base(page, kicker, accent=MINT):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    # Formas geométricas: conexões entre ideias, sem imagens genéricas.
    d.ellipse((688,-225,1315,402), outline="#2A4C56", width=3)
    d.ellipse((762,-146,1220,312), outline="#314764", width=2)
    d.line([(696,186),(911,370),(1128,246)], fill="#3C5771", width=4, joint="curve")
    for x,y in ((696,186),(911,370),(1128,246)):
        d.ellipse((x-8,y-8,x+8,y+8),fill=accent)
    d.rounded_rectangle((68,72,290,126),radius=18,fill=accent)
    d.text((87,81),"NEXO  /  LAB",font=f(25,True),fill="#0D1427")
    d.text((69,160),kicker,font=f(26,True),fill=accent,stroke_width=0)
    d.line((68,1220,1012,1220),fill="#445064",width=2)
    d.text((69,1251),"@oi.sou.nexo    •    IA SEM PROMESSA MÁGICA",font=f(21,True),fill=MUTED)
    d.text((947,1251),f"{page}/5",font=f(23,True),fill=accent)
    return im,d

def title(d, lines, y, size=68, color=WHITE, leading=1.18):
    for line in lines:
        d.text((67,y),line,font=f(size,True),fill=color)
        y+=int(size*leading)
    return y

def box(d,coords,fill=PANEL,outline="#455B6B",radius=34):
    d.rounded_rectangle(coords,radius=radius,fill=fill,outline=outline,width=2)

# 1 — promessa editorial específica, sem alegação de resultados fictícios.
im,d=base(1,"EXPERIMENTO 01",LIME)
title(d,["UMA IDEIA SOLTA.","UM PLANO CLARO."],480,64)
d.text((70,682),"Um prompt prático para sair do",font=f(37),fill=MUTED)
d.text((70,735),"rascunho e decidir o próximo passo.",font=f(37),fill=MUTED)
box(d,(68,897,1012,1069),fill="#243B35",outline="#477B64")
d.text((108,933),"5 SLIDES  •  1 PROMPT  •  VOCÊ NO CONTROLE",font=f(27,True),fill=LIME)
im.save(OUT/"01-capa.jpg",quality=92,optimize=True)

# 2 — contexto.
im,d=base(2,"O PROBLEMA",MINT)
title(d,["IDEIAS NÃO FALTAM.","FALTA COMEÇAR."],430,61)
d.text((70,636),"Notas espalhadas. Muitas opções.",font=f(38),fill=MUTED)
d.text((70,689),"Nenhuma ação definida.",font=f(38),fill=MUTED)
box(d,(68,851,1012,1040),fill="#202F43")
d.text((108,896),"A IA ORGANIZA.",font=f(45,True),fill=MINT)
d.text((108,964),"VOCÊ DECIDE.",font=f(34,True),fill=WHITE)
im.save(OUT/"02-desafio.jpg",quality=92,optimize=True)

# 3 — texto curto e copiável no card; versão completa na legenda.
im,d=base(3,"COPIE A ESTRUTURA",PURPLE)
title(d,["UM PROMPT.","QUATRO SAÍDAS."],332,63)
box(d,(68,530,1012,1048),fill="#202A46",outline="#5B5B8F")
rows=[
 "01   Objetivo em uma frase",
 "02   Três ações, em ordem",
 "03   Primeiro passo de 10 min",
 "04   Duas dúvidas a confirmar",
]
for i,row in enumerate(rows):
    yy=590+i*105
    d.text((112,yy),row,font=f(34,True),fill=WHITE)
    if i<3:d.line((110,yy+76,964,yy+76),fill="#4A5371",width=2)
d.text((73,1104),"O TEXTO COMPLETO ESTÁ NA LEGENDA ↓",font=f(26,True),fill=PURPLE)
im.save(OUT/"03-prompt.jpg",quality=92,optimize=True)

# 4 — integridade / qualidade.
im,d=base(4,"O FILTRO HUMANO",MINT)
title(d,["ANTES DE USAR,","CONFIRA."],315,72)
for i,(h,sub) in enumerate([
 ("PRAZO","É realista para sua rotina?"),
 ("DADOS","Faltou informação importante?"),
 ("DECISÃO","O que só você pode decidir?")
]):
    yy=525+i*198
    box(d,(69,yy,1010,yy+163))
    d.text((107,yy+23),h,font=f(29,True),fill=MINT)
    d.text((107,yy+78),sub,font=f(33),fill=WHITE)
im.save(OUT/"04-filtro.jpg",quality=92,optimize=True)

# 5 — engajamento orientado a uso real.
im,d=base(5,"SUA VEZ",LIME)
title(d,["TESTE.","COMPARE.","DECIDA."],299,84)
box(d,(68,688,1012,1040),fill="#243B35",outline="#477B64")
d.text((110,730),"1  Escolha um rascunho real.",font=f(32,True),fill=WHITE)
d.text((110,819),"2  Rode o prompt da legenda.",font=f(32,True),fill=WHITE)
d.text((110,908),"3  Revise antes de agir.",font=f(32,True),fill=WHITE)
d.text((75,1114),"SALVE PARA TESTAR QUANDO PRECISAR.",font=f(26,True),fill=LIME)
im.save(OUT/"05-convite.jpg",quality=92,optimize=True)
print("Generated",len(list(OUT.glob("*.jpg"))),"JPEG images in",OUT)
