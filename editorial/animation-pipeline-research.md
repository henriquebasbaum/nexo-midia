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
