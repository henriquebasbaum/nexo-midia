# Nexo — estudo de animação de personagem (12/10/2026)

## Requisito criativo obrigatório
Nexo **não pode flutuar como sticker**. Precisa ter atuação: sincronia de boca com áudio em português brasileiro, piscadas, sobrancelhas/expressões, braços que gesticulam e apontam, reações à informação e mudanças de enquadramento. Mascote azul-turquesa com estrela laranja, visual 3D acolhedor. **Não publicar** testes que não cumpram esses requisitos.

## Pipeline gratuito candidato (ainda não validado)
1. **Rig original:** modelar Nexo com peças/shape keys independentes para olhos, boca, braços e corpo; usar Blender, não apenas recorte PNG. A fidelidade ao mascote canônico precisa ser revisada visualmente.
2. **Narração:** sintetizar áudio pt-BR localmente via Piper TTS e uma voz licenciada para uso comercial; confirmar licença do modelo escolhido e qualidade da pronúncia antes de usar.
3. **Lip sync:** addon Blender Lip Sync (Charley3D) para converter áudio em visemas e keyframes de shape keys; alternativa Rhubarb Lip Sync (exporta JSON/TSV de boca) e Babylon Lipsync para Blender. Conferir precisão em pt-BR e ajustar manualmente se necessário.
4. **Atuação:** animação procedural com keyframes independentes para piscadas, expressões e braços (ex.: apontar para o prompt vago, desaprovar, apontar para prompt contextualizado, comemorar). Reações sincronizadas aos pontos do roteiro; câmera em pelo menos três planos.
5. **Render:** vertical 1080x1920, 24/30 fps, MP4 H.264/AAC, 15–30s; legendas em pt-BR revisadas. Só publicar após verificação visual de boca/olhos/gestos, legibilidade, áudio e conformidade com a identidade.

## Fontes oficiais
- Blender Lip Sync addon: https://extensions.blender.org/add-ons/iocgpoly-lip-sync/
- Fonte do addon: https://github.com/Charley3d/lip-sync (GPL-3.0-or-later)
- Rhubarb Lip Sync: https://github.com/DanielSWolf/rhubarb-lip-sync
- Babylon Lipsync: https://github.com/danemadsen/Babylon-Lipsync
- Piper TTS com vozes pt-BR: https://github.com/networkedaudio/piperTTS (verificar licença de cada modelo)

## Diagnóstico de 12/10
No ambiente de execução atual há ffmpeg e espeak, mas não há Blender nem Piper instalados; por isso o pipeline **não foi validado** e nenhum novo Reel foi autorizado. Próximo teste: criar rig de Nexo em Blender, gerar um trecho falado de 5–8s e inspecionar frames e sincronização. Não chamar carrossel ou vídeo com recorte estático de 'animação 3D'.

## Atualização de engenharia — 13/10/2026
- Teste local de 8 segundos realizado com **Pillow + FFmpeg + espeak pt-BR** (540×960, 18 fps, H.264/AAC). Modelo 2D desenhado por partes: olhos com piscadas, boca abrindo/fechando em função do envelope RMS do áudio, braços articulados com gestos, mudança de expressão/caixa de prompt e legendas. MP4 foi gerado e inspecionado localmente.
- **Resultado:** demonstra que é tecnicamente possível fazer Nexo atuar e falar sem simplesmente mover um PNG, mas o visual ainda é 2D simplificado, não corresponde com fidelidade à referência canônica e não possui visemas fonéticos precisos. **NÃO APROVADO PARA PUBLICAÇÃO** e não confundir com o pipeline Blender 3D.
- O script Blender 3D com rig procedural e envelope de voz foi escrito e passou por verificação de sintaxe, porém não foi executado: Blender continua indisponível neste ambiente. Próxima validação deve ocorrer em runner com Blender instalado, gerando 5–8 s e inspecionando resultado visual antes de qualquer publicação.
- Publicação do carrossel pronto foi tentada uma vez em 13/10 08h BRT pelo Windsor e novamente bloqueada pelas verificações de segurança do conector antes da execução. Não foi publicado; não insistir na mesma rodada. As leituras do Instagram e Metricool não mostraram novo post em 12/10 ou 13/10 até a coleta, mas os dados Windsor podem estar em cache.
