from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
P=Path("assets/experimento-02-privacidade");P.mkdir(parents=True,exist_ok=True)
W,H=1080,1350
NAVY="#101A2D"; WHITE="#F3F7FC"; MUTED="#C5D3E0"; GREEN="#A8F5CA"; CORAL="#FFB79B"
def ft(n,b=False):
 return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans"+("-Bold" if b else "")+".ttf",n)
def draw(i,tag,headline,body,accent=GREEN):
 im=Image.new("RGB",(W,H),NAVY);d=ImageDraw.Draw(im)
 d.ellipse((730,-210,1300,365),outline="#354763",width=5)
 d.line((740,235,1000,450),fill=accent,width=7)
 for x,y in [(740,235),(1000,450)]: d.ellipse((x-13,y-13,x+13,y+13),fill=accent)
 d.rounded_rectangle((65,75,346,131),radius=24,fill=accent)
 d.text((91,85),"NEXO / LAB",font=ft(26,True),fill=NAVY)
 d.text((68,187),tag,font=ft(28,True),fill=accent)
 y=340
 for s in headline:
  d.text((66,y),s,font=ft(60,True),fill=WHITE);y+=93
 y+=58
 d.rounded_rectangle((65,y,1015,min(1110,y+len(body)*81+63)),radius=29,fill="#1C3043",outline="#3E6370",width=3)
 for k,s in enumerate(body): d.text((101,y+30+k*81),s,font=ft(33,False),fill=MUTED)
 d.line((65,1220,1010,1220),fill="#456173",width=2)
 d.text((69,1262),"@oi.sou.nexo  •  IA COM CRITÉRIO",font=ft(22,True),fill=accent)
 d.text((933,1262),f"{i}/4",font=ft(24,True),fill=WHITE)
 im.save(P/(str(i).zfill(2)+".jpg"),quality=94,optimize=True)
draw(1,"GUIA PRÁTICO 02",["ANTES DE ENVIAR","ALGO PARA IA..."],["PARE POR 10 SEGUNDOS.","Privacidade também faz parte","de usar IA com inteligência."],CORAL)
draw(2,"O QUE EVITAR",["NÃO COLE","SEM PENSAR"],["• Senhas e códigos de acesso","• Documentos e dados bancários","• Dados de clientes e terceiros","• Informações confidenciais"],GREEN)
draw(3,"ALTERNATIVA ÚTIL",["TROQUE DADOS","POR CONTEXTO"],["Remova nomes e números reais.","Use exemplos fictícios.","Compartilhe só o necessário.","Revise antes de enviar."],CORAL)
draw(4,"CHECKLIST DO NEXO",["3 PERGUNTAS","ANTES DO ENTER"],["1. É realmente necessário?","2. Tenho permissão?","3. Posso anonimizar?","Salve para lembrar depois."],GREEN)
print("Created 4 original JPEG slides")
