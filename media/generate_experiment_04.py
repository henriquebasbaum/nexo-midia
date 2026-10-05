from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
P=Path("assets/experimento-04-email");P.mkdir(parents=True,exist_ok=True)
W,H=1080,1350; BG="#0E1728"; WHITE="#F5F8FC"; MUTED="#CBD6E2"; BLUE="#9ED8FF"; MINT="#A8F5CA"
def ft(n,b=False): return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans"+("-Bold" if b else "")+".ttf",n)
def slide(i,kicker,title,lines,accent):
 im=Image.new("RGB",(W,H),BG);d=ImageDraw.Draw(im)
 d.rounded_rectangle((64,70,390,130),28,fill=accent);d.text((90,84),"NEXO / EXPERIMENTO 04",font=ft(21,True),fill=BG)
 d.text((66,190),kicker,font=ft(28,True),fill=accent); y=315
 for s in title:d.text((66,y),s,font=ft(58,True),fill=WHITE);y+=88
 y+=42;d.rounded_rectangle((66,y,1014,1120),30,fill="#1B2C40",outline="#405A73",width=3);yy=y+38
 for s in lines:d.text((101,yy),s,font=ft(32),fill=MUTED);yy+=82
 d.text((66,1255),"@oi.sou.nexo  •  IA COM CRITÉRIO",font=ft(22,True),fill=accent);d.text((938,1255),f"{i}/4",font=ft(24,True),fill=WHITE)
 im.save(P/f"{i:02}.jpg",quality=94,optimize=True)
slide(1,"MENOS TEXTO. MAIS CLAREZA.",["USE IA PARA","ENCURTAR E-MAILS"],["Não peça só: 'melhore este texto'.","Dê objetivo, público e limite.","O resultado tende a ficar mais útil."],BLUE)
slide(2,"PROMPT REPRODUZÍVEL",["DIGA O QUE","DEVE SOBRAR"],["'Reescreva em até 120 palavras.'","'Mantenha decisão, prazo e ação.'","'Remova repetição e linguagem vaga.'","'Não invente fatos.'"],MINT)
slide(3,"ANTES DE ENVIAR",["FAÇA UMA","REVISÃO HUMANA"],["O tom combina com você?","Datas e nomes estão corretos?","A ação esperada está explícita?","Algum dado sensível ficou no texto?"],BLUE)
slide(4,"TESTE EM 2 MINUTOS",["PEGUE UM E-MAIL","LONGO DE HOJE"],["Anonimize o conteúdo.","Use o prompt do slide 2.","Compare antes e depois.","Ficou mais claro? Só então envie."],MINT)
print("Created 4 JPEG slides")