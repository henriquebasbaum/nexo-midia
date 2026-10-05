from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
P=Path("assets/guia-03-verificacao");P.mkdir(parents=True,exist_ok=True)
W,H=1080,1350;BG="#101A2D";WHT="#F3F7FC";TXT="#C5D3E0";GRN="#A8F5CA";YEL="#FFE58A"
def F(n,b=False):return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans"+("-Bold" if b else "")+".ttf",n)
slides=[
("GUIA PRÁTICO 03",["A IA RESPONDEU.","E AGORA?"],["Resposta convincente","não é o mesmo que","resposta correta."],YEL),
("SINAL DE ALERTA",["PARE QUANDO","HOUVER..."],["• números ou estatísticas","• datas e acontecimentos","• leis e regras","• citações e fontes"],GRN),
("PEÇA E CONFIRA",["USE A IA COMO","PONTO DE PARTIDA"],["Peça fontes verificáveis.","Abra a fonte original.","Confira data e contexto.","Compare quando for importante."],YEL),
("REGRA DO NEXO",["QUANTO MAIOR","O IMPACTO..."],["...maior deve ser a checagem.","Saúde, dinheiro e decisões","importantes merecem fontes","confiáveis — não só confiança."],GRN)]
for idx,(tag,head,body,accent) in enumerate(slides,1):
 im=Image.new("RGB",(W,H),BG);d=ImageDraw.Draw(im)
 d.rounded_rectangle((65,75,390,133),28,fill=accent);d.text((91,86),"NEXO / LAB",font=F(25,True),fill=BG)
 d.text((68,190),tag,font=F(28,True),fill=accent)
 d.ellipse((785,90,990,295),outline=accent,width=6);d.line((925,245,1020,340),fill=accent,width=12)
 y=350
 for s in head:d.text((66,y),s,font=F(59,True),fill=WHT);y+=92
 y+=55;d.rounded_rectangle((65,y,1015,y+390),30,fill="#1C3043",outline="#3E6370",width=3)
 for k,s in enumerate(body):d.text((101,y+35+k*78),s,font=F(32),fill=TXT)
 d.line((65,1220,1010,1220),fill="#456173",width=2);d.text((69,1262),"@oi.sou.nexo  •  IA COM CRITÉRIO",font=F(22,True),fill=accent);d.text((933,1262),f"{idx}/4",font=F(24,True),fill=WHT)
 im.save(P/(str(idx).zfill(2)+".jpg"),quality=94,optimize=True)
