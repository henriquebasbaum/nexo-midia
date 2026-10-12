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

# Experimento 09 — antes/depois: organizar 90 minutos com limites reais.
from PIL import Image as Im09, ImageDraw as Dr09, ImageFont as Fo09
from pathlib import Path as Pa09
P09=Pa09("assets/experimento-09-agenda-90min");P09.mkdir(parents=True,exist_ok=True)
B09="#101B30";I09="#F8FAFF";S09="#C7D8E5";C09="#68E5DF";O09="#FFAD6A";N09="#20344B";D09="#12263D"
def f09(sz,b=False):return Fo09.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans"+("-Bold" if b else "")+".ttf",sz)
def t09(d,x,y,s,sz=36,col=I09,b=False):d.text((x,y),s,font=f09(sz,b),fill=col)
def r09(d,xy,col=N09,rad=30,stroke=None):d.rounded_rectangle(xy,radius=rad,fill=col,outline=stroke,width=3 if stroke else 1)
def bg09(n,tag):
 im=Im09.new("RGB",(1080,1350),B09);d=Dr09.Draw(im)
 d.ellipse((735,-200,1320,395),outline="#28465A",width=4)
 d.ellipse((860,-70,1200,270),outline="#275166",width=3)
 d.polygon([(910,145),(928,179),(966,198),(928,216),(910,250),(892,216),(854,198),(892,179)],fill=O09)
 r09(d,(62,65,366,126),C09,20);t09(d,88,79,"NEXO  /  LAB",26,B09,True)
 t09(d,64,174,tag,27,C09,True)
 d.line((62,1232,1015,1232),fill="#456073",width=2)
 t09(d,65,1254,"@oi.sou.nexo  •  IA NA PRÁTICA",21,S09,True)
 t09(d,948,1254,f"{n}/4",23,C09,True)
 return im,d
def h09(d,lines,y=265,sz=66):
 for line in lines:t09(d,64,y,line,sz,I09,True);y+=int(sz*1.34)
def s09(im,n):im.save(P09/f"{n:02}.jpg",quality=93,optimize=True)
im,d=bg09(1,"EXPERIMENTO 09  /  ANTES E DEPOIS")
h09(d,["90 MINUTOS LIVRES.","3 TAREFAS.","POR ONDE COMEÇAR?"],285,56)
r09(d,(64,680,1016,1067),D09,35,"#39617B")
for yy,dur,task in [(728,"5 min","Pagar conta"),(829,"35 min","Enviar proposta"),(930,"40 min","Revisar contrato")]:
 t09(d,105,yy,dur,51,C09,True);t09(d,340,yy+8,task,36)
t09(d,75,1122,"A IA ajuda a organizar. Você ajusta.",29,O09,True);s09(im,1)
im,d=bg09(2,"ANTES  /  PEDIDO VAGO")
h09(d,['"ORGANIZE','MEU DIA."'],315,75)
r09(d,(65,605,1014,1020),N09,35,"#456276")
t09(d,104,655,"Faltam informações:",38,C09,True)
for i,line in enumerate(["• Quanto tempo existe?","• Quais são as tarefas?","• O que é mais urgente?"]):t09(d,104,752+i*77,line,33,S09)
t09(d,75,1095,"Sem contexto, o plano pode ser genérico.",28,O09,True);s09(im,2)
im,d=bg09(3,"DEPOIS  /  PEDIDO COM CONTEXTO")
h09(d,["UM PROMPT","QUE CABE NA ROTINA"],294,58)
r09(d,(65,550,1014,1080),N09,35,"#3C6672")
for i,line in enumerate(['"Tenho 90 minutos livres.','Preciso pagar uma conta (5 min),','enviar proposta (35 min) e','revisar contrato (40 min).','Organize em blocos de tempo,','incluindo margem para imprevistos.','Não invente outras tarefas."']):t09(d,98,601+i*63,line,31,I09)
t09(d,74,1124,"Objetivo + tarefas + tempo + limite.",28,C09,True);s09(im,3)
im,d=bg09(4,"EXEMPLO ILUSTRATIVO  /  PLANO")
h09(d,["80 MIN DE TAREFAS.","10 MIN DE MARGEM."],274,56)
for i,(tm,label,col) in enumerate([("00–05","Pagar conta",C09),("05–40","Enviar proposta","#7FC9FF"),("40–80","Revisar contrato","#C6B4FF"),("80–90","Margem / imprevistos",O09)]):
 y=520+i*140;r09(d,(64,y,1016,y+119),N09,24);r09(d,(82,y+17,268,y+102),col,17)
 t09(d,101,y+38,tm,28,B09,True);t09(d,296,y+39,label,31,I09,True)
t09(d,72,1132,"Salve e adapte à sua prioridade real.",28,O09,True);s09(im,4)
print("Generated Experimento 09 — 4 original JPEG images")
