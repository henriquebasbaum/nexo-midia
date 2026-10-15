"""Nexo / Experimento 10: notas de reunião fictícias -> ações verificáveis."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path("assets/experimento-10-reuniao-acoes")
OUT.mkdir(parents=True, exist_ok=True)
W,H=1080,1350
NAVY="#0F1B30"; CARD="#1A3047"; TEXT="#F5FAFF"; MUTED="#D0E0EC"
CYAN="#6BE8E0"; ORANGE="#FFAE72"; BLUE="#91C8FA"
REG="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def font(sz,b=False):
    return ImageFont.truetype(BOLD if b else REG, sz)
def txt(d,x,y,s,sz=32,color=TEXT,b=False):
    d.text((x,y),s,font=font(sz,b),fill=color)
def base(n,label):
    im=Image.new("RGB",(W,H),NAVY); d=ImageDraw.Draw(im)
    d.ellipse((715,-205,1280,345),outline="#294A60",width=5)
    d.ellipse((845,-90,1210,265),outline="#25485B",width=3)
    # Four-point orange brand star (not a replacement mascot)
    d.polygon([(922,126),(941,166),(985,186),(941,205),(922,245),(903,205),(860,186),(903,166)],fill=ORANGE)
    d.rounded_rectangle((62,65,361,125),radius=22,fill=CYAN)
    txt(d,89,80,"NEXO  /  LAB",26,NAVY,True)
    txt(d,64,171,label,27,CYAN,True)
    d.line((64,1228,1015,1228),fill="#456073",width=2)
    txt(d,65,1252,"@oi.sou.nexo  •  IA COM CRITÉRIO",22,MUTED,True)
    txt(d,948,1252,f"{n}/4",24,CYAN,True)
    return im,d
def head(d,lines,top=270,size=62):
    for i,s in enumerate(lines):
        txt(d,64,top+i*(size+20),s,size,TEXT,True)
def box(d,y1,y2):
    d.rounded_rectangle((64,y1,1016,y2),radius=32,fill=CARD,outline="#40627A",width=3)
def save(im,n):
    im.save(OUT/f"{n:02d}.jpg",quality=93,optimize=True)

im,d=base(1,"EXPERIMENTO 10  /  REUNIÕES")
head(d,["A IA INVENTOU","QUEM FARIA","A TAREFA?"],277,64)
box(d,663,1091)
txt(d,103,714,"Uma ata não deve criar decisões.",38,CYAN,True)
for i,line in enumerate(["Notas incompletas + pedido vago","podem virar uma lista convincente,","mas com responsáveis inventados."]):
    txt(d,103,803+i*75,line,32,MUTED)
txt(d,75,1133,"Veja como pedir sem inventar dados →",29,ORANGE,True)
save(im,1)

im,d=base(2,"ANTES  /  EXEMPLO FICTÍCIO")
head(d,["NOTAS SOLTAS","DE UMA REUNIÃO"],282,61)
box(d,559,1079)
for i,line in enumerate(["• Revisar a página inicial.","• Validar os preços até sexta.","• Dúvida: qual versão aprovar?","• Ninguém assumiu a revisão."]):
    txt(d,99,620+i*88,line,34,MUTED)
txt(d,95,1007,"Pedido vago: “Faça a ata.”",30,ORANGE,True)
txt(d,74,1125,"Exemplo ilustrativo; não é reunião real.",26,CYAN,True)
save(im,2)

im,d=base(3,"DEPOIS  /  PROMPT MAIS SEGURO")
head(d,["TRANSFORME EM","AÇÕES, SEM INVENTAR"],278,57)
box(d,535,1115)
for i,line in enumerate([
    "“Use apenas as notas abaixo.",
    "Separe em: decisões confirmadas,",
    "ações, prazos e dúvidas abertas.",
    "Se faltar responsável, escreva",
    "‘não definido’. Não invente",
    "datas, acordos ou participantes.",
    "Liste o que precisa ser confirmado.”"
]):
    txt(d,93,593+i*69,line,31,TEXT)
txt(d,76,1141,"O que falta vira pergunta, não fato.",27,ORANGE,True)
save(im,3)

im,d=base(4,"RESULTADO  /  EXEMPLO ILUSTRATIVO")
head(d,["AÇÕES CLARAS.","LACUNAS VISÍVEIS."],274,59)
box(d,537,1112)
txt(d,95,584,"AÇÕES",36,CYAN,True)
txt(d,95,652,"• Revisar página inicial",31,TEXT)
txt(d,95,715,"  Responsável: não definido",29,MUTED)
txt(d,95,786,"• Validar preços — até sexta*",31,TEXT)
txt(d,95,848,"  Responsável: não definido",29,MUTED)
txt(d,95,935,"DÚVIDA: qual versão aprovar?",31,ORANGE,True)
txt(d,95,1034,"*Confirmar a data exata.",27,MUTED)
txt(d,75,1146,"Salve para sua próxima reunião.",29,CYAN,True)
save(im,4)
print("Created",len(list(OUT.glob("*.jpg"))),"original images")
