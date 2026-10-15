"""Nexo Experimento 10: reunião em tarefas sem inventar responsáveis.
Gera 4 JPGs 1080x1350. Exemplo totalmente fictício.
Executar: python media/generate_experimento_10.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT=Path("assets/experimento-10-ata-sem-inventar")
OUT.mkdir(parents=True,exist_ok=True)
W,H=1080,1350
NAVY="#101B30";PANEL="#1E344C";CYAN="#6FE9E0";ORANGE="#FFB36F"
WHITE="#F7FAFF";MUTED="#C6D7E6";RED="#FFACAC"
FONT="/usr/share/fonts/truetype/dejavu/DejaVuSans"
def font(size,bold=False):
    return ImageFont.truetype(FONT+("-Bold" if bold else "")+".ttf",size)
def txt(d,x,y,s,size=36,color=WHITE,bold=False):
    d.text((x,y),s,font=font(size,bold),fill=color)
def rect(d,xy,color=PANEL,radius=30):
    d.rounded_rectangle(xy,radius=radius,fill=color,outline="#375B72",width=3)
def base(num,tag):
    im=Image.new("RGB",(W,H),NAVY);d=ImageDraw.Draw(im)
    d.ellipse((800,-170,1300,310),outline="#32566B",width=4)
    d.polygon([(902,130),(922,169),(965,190),(922,210),(902,252),(882,210),(840,190),(882,169)],fill=ORANGE)
    d.rounded_rectangle((65,64,364,128),radius=22,fill=CYAN)
    txt(d,93,80,"NEXO  /  LAB",26,NAVY,True)
    txt(d,66,174,tag,28,CYAN,True)
    d.line((66,1234,1016,1234),fill="#45657C",width=2)
    txt(d,67,1262,"@oi.sou.nexo  •  IA COM CRITÉRIO",21,MUTED,True)
    txt(d,948,1262,f"{num}/4",23,CYAN,True)
    return im,d
def headline(d,lines,y=285,size=62):
    for line in lines:
        txt(d,66,y,line,size,WHITE,True);y+=int(size*1.40)
def save(im,n):
    im.save(OUT/f"{n:02}.jpg",quality=94,optimize=True)

im,d=base(1,"EXPERIMENTO 10  /  REUNIÕES")
headline(d,["A IA INVENTOU","O RESPONSÁVEL?"])
rect(d,(65,570,1015,1010))
txt(d,105,635,"De notas soltas para tarefas:",35,CYAN,True)
txt(d,105,744,"organize o que foi dito,",39,WHITE)
txt(d,105,810,"sem atribuir decisões",39,WHITE)
txt(d,105,876,"a quem não participou.",39,WHITE)
txt(d,74,1118,"Exemplo fictício. Veja o antes/depois.",28,ORANGE,True)
save(im,1)

im,d=base(2,"ANTES  /  NOTAS INCOMPLETAS")
headline(d,["ANOTAÇÕES","DA REUNIÃO"])
rect(d,(65,535,1015,1040))
for y,s in [(590,"• Revisar proposta até sexta."),(687,"• Conferir custos."),(784,"• Responder ao cliente.")]:
    txt(d,102,y,s,35,WHITE)
txt(d,105,915,"Quem fará cada tarefa?",35,ORANGE,True)
txt(d,74,1118,"Não está escrito. Não podemos supor.",28,RED,True)
save(im,2)

im,d=base(3,"DEPOIS  /  PROMPT MAIS SEGURO")
headline(d,["PEÇA UMA TABELA","SEM INVENÇÕES"],size=57)
rect(d,(65,545,1015,1095))
for i,s in enumerate([
    '"Transforme estas notas em',
    'uma tabela com: ação,',
    'responsável, prazo e dúvidas.',
    '',
    'Não invente nomes, datas',
    'ou decisões. Se faltar dado,',
    'escreva NÃO INFORMADO."'
]):
    txt(d,97,598+i*66,s,32,WHITE if i<4 else CYAN,i==6)
txt(d,74,1143,"Copie a estrutura. Revise a saída.",27,ORANGE,True)
save(im,3)

im,d=base(4,"EXEMPLO  /  RESULTADO ESPERADO")
headline(d,["CLAREZA >","ADIVINHAÇÃO"],size=67)
rect(d,(65,550,1015,1090))
txt(d,100,601,"AÇÃO",27,CYAN,True)
txt(d,100,651,"Revisar proposta",39,WHITE,True)
txt(d,100,744,"RESPONSÁVEL",27,CYAN,True)
txt(d,100,791,"Não informado",38,ORANGE,True)
txt(d,100,879,"PRAZO",27,CYAN,True)
txt(d,100,928,"Sexta (confirmar data)",35,WHITE)
txt(d,73,1145,"Salve para a próxima reunião.",28,ORANGE,True)
save(im,4)
print("Criados 4 JPGs originais em",OUT)
