from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
P=Path("assets/guia-03-alucinacao");P.mkdir(parents=True,exist_ok=True)
W,H=1080,1350
BG="#0E1728";WHITE="#F6F8FB";MUTED="#CAD4DF";MINT="#A8F5CA";YELLOW="#FFE28A"
def ft(n,b=False):
 return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans"+("-Bold" if b else "")+".ttf",n)
def card(i,kicker,title,lines,accent):
 im=Image.new("RGB",(W,H),BG);d=ImageDraw.Draw(im)
 d.rounded_rectangle((64,70,350,128),26,fill=accent)
 d.text((88,83),"NEXO / GUIA 03",font=ft(24,True),fill=BG)
 d.text((66,190),kicker,font=ft(29,True),fill=accent)
 y=315
 for t in title:
  d.text((66,y),t,font=ft(61,True),fill=WHITE);y+=91
 y+=48
 d.rounded_rectangle((66,y,1014,1110),30,fill="#1B2C40",outline="#3B566F",width=3)
 yy=y+38
 for s in lines:
  d.text((101,yy),s,font=ft(34,False),fill=MUTED);yy+=91
 d.text((66,1255),"@oi.sou.nexo  •  IA COM CRITÉRIO",font=ft(22,True),fill=accent)
 d.text((938,1255),f"{i}/4",font=ft(24,True),fill=WHITE)
 im.save(P/f"{i:02}.jpg",quality=94,optimize=True)
card(1,"QUANDO A IA INVENTA",["RESPOSTA BONITA","NÃO É PROVA"],["Modelos podem responder com confiança","mesmo quando estão errados.","Use estes 3 testes antes de confiar."],YELLOW)
card(2,"TESTE 1",["PEÇA A FONTE","E CONFIRA"],["Solicite links, datas e origem.","Abra a fonte original.","Veja se ela realmente diz o que","a resposta afirmou."],MINT)
card(3,"TESTE 2",["FORCE A IA A","MOSTRAR DÚVIDA"],["Pergunte: 'O que nesta resposta","você não consegue verificar?'","Boa resposta admite incerteza","em vez de preencher lacunas."],YELLOW)
card(4,"TESTE 3",["CRUZE A","INFORMAÇÃO"],["Compare com outra fonte confiável.","Para decisões importantes,","não use uma única resposta de IA","como evidência final."],MINT)
print("Created 4 JPEG slides")

