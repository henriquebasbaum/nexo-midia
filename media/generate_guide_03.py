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


# Guia 06 — adaptar curriculo com IA sem inventar experiencia.
P6=Path("assets/guia-06-curriculo");P6.mkdir(parents=True,exist_ok=True)
def card6(i,kicker,title,lines,accent):
 im=Image.new("RGB",(W,H),BG);d=ImageDraw.Draw(im)
 d.rounded_rectangle((64,70,350,128),26,fill=accent)
 d.text((88,83),"NEXO / GUIA 06",font=ft(24,True),fill=BG)
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
 im.save(P6/f"{i:02}.jpg",quality=94,optimize=True)
card6(1,"CURRÍCULO + IA, SEM FANTASIA",["ADAPTE SEM","INVENTAR"],["A IA pode ajudar a destacar","experiências reais para cada vaga.","Mas não deve criar competências","que você não tem."],MINT)
card6(2,"PASSO 1 — ANONIMIZE",["TIRE DADOS","SENSÍVEIS"],["Remova telefone, endereço,","documentos e contatos.","Cole só experiências relevantes.","Evite dados de terceiros."],YELLOW)
card6(3,"PASSO 2 — COMPARE",["VAGA X","EXPERIÊNCIA"],["Peça: 'Liste requisitos da vaga","que meu currículo comprova.'","'Separe lacunas sem inventar.'","'Sugira palavras mais claras.'"],MINT)
card6(4,"PASSO 3 — REVISE",["VOCÊ ASSINA","O RESULTADO"],["Confirme cargos, datas e números.","Exclua habilidades inventadas.","Revise tom e legibilidade.","Só então envie a candidatura."],YELLOW)
print("Created 4 JPEG slides for Guia 06")

# Guia 08 — comparar opcoes com IA sem delegar a decisao.
P8=Path("assets/guia-08-comparacao");P8.mkdir(parents=True,exist_ok=True)
def card8(i,kicker,title,lines,accent):
 im=Image.new("RGB",(W,H),BG);d=ImageDraw.Draw(im)
 d.rounded_rectangle((64,70,350,128),26,fill=accent)
 d.text((88,83),"NEXO / GUIA 08",font=ft(24,True),fill=BG)
 d.text((66,190),kicker,font=ft(29,True),fill=accent)
 y=315
 for t in title:
  d.text((66,y),t,font=ft(59,True),fill=WHITE);y+=91
 y+=48
 d.rounded_rectangle((66,y,1014,1110),30,fill="#1B2C40",outline="#3B566F",width=3)
 yy=y+38
 for s in lines:
  d.text((101,yy),s,font=ft(32),fill=MUTED);yy+=91
 d.text((66,1255),"@oi.sou.nexo  •  IA COM CRITÉRIO",font=ft(22,True),fill=accent)
 d.text((938,1255),f"{i}/4",font=ft(24,True),fill=WHITE)
 im.save(P8/f"{i:02}.jpg",quality=94,optimize=True)
card8(1,"DECISÃO COM CRITÉRIO",["COMPARE DUAS","OPÇÕES COM IA"],["A IA pode organizar critérios,","prós, contras e incertezas.","Mas a decisão continua sua."],MINT)
card8(2,"PASSO 1 — DEFINA",["O QUE MAIS","IMPORTA?"],["Liste preço, tempo e qualidade.","Diga quais critérios são essenciais.","Inclua seu orçamento e limites.","Não use só uma nota geral."],YELLOW)
card8(3,"PASSO 2 — QUESTIONE",["PEÇA UMA","COMPARAÇÃO"],["Monte uma tabela lado a lado.","Separe fatos de suposições.","Peça riscos e pontos desconhecidos.","Confira dados nas fontes."],MINT)
card8(4,"PASSO 3 — DECIDA",["VOCÊ TEM","A PALAVRA"],["O que muda se o preço subir?","Qual opção atende suas prioridades?","Que informação falta verificar?","Decida com base no seu contexto."],YELLOW)
print("Created 4 JPEG slides for Guia 08")

# Reel 01 — demonstração concreta: um pedido vago vs. pedido útil.
PR=Path("assets/reel-01-prompt-claro");PR.mkdir(parents=True,exist_ok=True)
def reel_slide(i,kicker,head,lines,accent):
 im=Image.new("RGB",(1080,1920),BG);d=ImageDraw.Draw(im)
 d.rounded_rectangle((64,90,400,160),28,fill=accent)
 d.text((91,107),"NEXO / TESTE REAL",font=ft(26,True),fill=BG)
 d.text((70,285),kicker,font=ft(37,True),fill=accent)
 y=420
 for s in head:
  d.text((70,y),s,font=ft(64,True),fill=WHITE);y+=100
 y+=85
 d.rounded_rectangle((65,y,1015,1470),32,fill="#1B2C40",outline="#3B566F",width=3)
 yy=y+60
 for s in lines:
  d.text((100,yy),s,font=ft(39),fill=MUTED);yy+=110
 d.text((70,1780),"@oi.sou.nexo   •   IA NA PRÁTICA",font=ft(25,True),fill=accent)
 d.text((940,1780),f"{i}/4",font=ft(26,True),fill=WHITE)
 im.save(PR/f"{i:02}.jpg",quality=94,optimize=True)
reel_slide(1,"ANTES / DEPOIS",["UM PROMPT VAGO","MUDA TUDO?"],["Veja duas formas de pedir","a mesma tarefa à IA.","A diferença está no contexto.","Sem fórmula mágica."],YELLOW)
reel_slide(2,"PEDIDO VAGO",["'FAÇA UM","PLANO DE ESTUDO'"],["Sem tema, nível ou prazo,","a resposta tende a ser genérica.","Falta dizer o que importa."],YELLOW)
reel_slide(3,"PEDIDO CLARO",["DÊ CONTEXTO","E LIMITES"],["'Tenho 15 minutos por dia.","Sou iniciante em inglês.","Crie 3 tarefas de prática.","Inclua revisão semanal.'"],MINT)
reel_slide(4,"TESTE VOCÊ",["COMPARE AS","DUAS RESPOSTAS"],["Veja qual é mais aplicável.","Cheque fatos e ajuste o plano.","Salve e teste com sua tarefa."],MINT)
print("Created 4 vertical JPEG frames for Reel 01 — ready for MP4 render")
