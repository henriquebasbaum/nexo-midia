from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
P=Path("assets/guia-05-contexto");P.mkdir(parents=True,exist_ok=True)
W,H=1080,1350;BG="#0E1728";WHITE="#F5F8FC";MUTED="#CBD6E2";BLUE="#9ED8FF";MINT="#A8F5CA"
def ft(n,b=False): return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans"+("-Bold" if b else "")+".ttf",n)
def slide(i,kicker,title,lines,accent):
 im=Image.new("RGB",(W,H),BG);d=ImageDraw.Draw(im);d.rounded_rectangle((64,70,390,130),28,fill=accent);d.text((90,84),"NEXO / GUIA 05",font=ft(23,True),fill=BG);d.text((66,190),kicker,font=ft(28,True),fill=accent);y=315
 for s in title:d.text((66,y),s,font=ft(58,True),fill=WHITE);y+=88
 y+=42;d.rounded_rectangle((66,y,1014,1120),30,fill="#1B2C40",outline="#405A73",width=3);yy=y+38
 for s in lines:d.text((101,yy),s,font=ft(32),fill=MUTED);yy+=82
 d.text((66,1255),"@oi.sou.nexo  •  IA COM CRITÉRIO",font=ft(22,True),fill=accent);d.text((938,1255),f"{i}/4",font=ft(24,True),fill=WHITE);im.save(P/f"{i:02}.jpg",quality=94,optimize=True)
slide(1,"PROMPT BOM COMEÇA ANTES",["PARE DE PEDIR","SEM CONTEXTO"],["'Faça um plano.'","'Escreva um post.'","'Analise isto.'","Pedidos vagos geram respostas genéricas."],BLUE)
slide(2,"DÊ 4 PEÇAS",["CONTEXTO +","OBJETIVO +","LIMITES + SAÍDA"],["Contexto: o que está acontecendo?","Objetivo: o que precisa acontecer?","Limites: o que evitar/respeitar?","Saída: em qual formato responder?"],MINT)
slide(3,"EXEMPLO PRÁTICO",["TROQUE O","PEDIDO VAGO"],["Em vez de: 'Crie uma pauta.'","Diga público e objetivo.","Defina 3 temas a evitar.","Peça 5 ideias em tabela curta."],BLUE)
slide(4,"ANTES DE ENVIAR",["FAÇA O TESTE","DOS 10 SEGUNDOS"],["A IA sabe para quem é?","Sabe qual resultado você quer?","Conhece os limites?","Sabe como entregar a resposta?"],MINT)
print("Created 4 JPEG slides")

