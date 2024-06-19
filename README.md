# Meu caro paçoca

Identificação de faces em um vídeo a cerimônia da Bola de Ouro

# Funcionamento

O código faz a detecção de faces usando HAAR Cascade, e uma validação usando detecção de olhos dentro das ROIs criadas com as faces.

Para a detecção de faces, foi usado o [haarcascade_frontalface](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml), e para detecção de olhos foi usado o [haarcascade_eye](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml)

Etapas de funcionamento:

- O vídeo é carregado e lido frame por frame com o [OpenCV](https://opencv.org/)
- Detecta as possíveis faces presentes na imagem
- Desenha uma ROI pra cada face, e então detecta se há olhos nessa região
- Caso existam, valida a face e anota, colocando bounding boxes ao redor
- Mostra e salva o frame anotado com o OpenCV.

# Perguntas técnicas

### 2.1. Funcionamento do Método de Detecção Escolhido

O HAAR Cascade funciona através de uma cascata de classificadores treinados com características positivas e negativas de imagens. Ele usa uma série de estágios, cada um com múltiplos classificadores, para detectar características faciais em várias escalas. Cada estágio filtra as áreas menos prováveis de conter uma face.

### 2.2. Classificação dos Métodos para Detecção de Faces

**Classificação:**

1. CNN (Convolutional Neural Network)
2. HAAR Cascade
3. NN Linear
4. Filtros de correlação cruzada

**Justificativa:**

- **CNN**: Muito precisa e versátil para detecção de faces, porém requer mais recursos computacionais e tempo de treinamento.
- **HAAR Cascade**: Fácil de implementar, rápido e eficaz para detecção de faces, mas pode gerar mais falsos positivos em comparação com CNN.
- **NN Linear**: Menos preciso que CNN, mais simples, mas não muito eficaz para detecção de faces complexas.
- **Filtros de correlação cruzada**: São menos comuns e mais difíceis de implementar para detecção de faces em comparação com os métodos acima.

No geral, apesar da CNN ser mais difícil de implementar, costuma ter resultados melhores que o HAAR Cascade, que apresenta uma dificuldade clara de detectar rostos que não estão de frente. Ponto pra CNN por versatilidade! Os filtros de correlação cruzada, apesar de sua facilidade de implementação, têm dificuldade em detectar faces em cenários diferentes. Um filtro para detectar a face do ronaldinho em uma foto específica funciona bem, mas ao mudar um pouco a face do jogador, a probabilidade de detecção cai muito, por conta da diferença da imagem para o kernel.

Se o objetivo é apenas detectar faces, o HAAR Cascade é uma opção ótima. Se for necessário mais precisão, CNN é o cara. No caso dessa implementação, o HAAR Cascade foi escolhido pela facilidade e por conta do seu resultado ser satisfatório o suficiente, não tendo que detectar rostos em situações complexas.

### 2.3. Classificação para Detecção de Emoções

**Classificação:**

1. CNN
2. NN Linear
3. HAAR Cascade
4. Filtros de correlação cruzada

**Justificativa:**

- **CNN**: Excelente para detecção de emoções devido à sua capacidade de capturar características complexas e sutis das faces.
- **NN Linear**: Pode ser usado para emoções, mas com menor precisão que CNN.
- **HAAR Cascade**: Bom para detecção de faces, mas não específico para emoções.
- **Filtros de correlação cruzada**: Menos eficaz para capturar nuances emocionais em comparação com CNN e NN Linear.

### 2.4. Consideração de Variações entre Frames

Nenhuma das soluções consegue, por si só, considerar variações de um frame pra outro. É possível implementar uma abordagem de análise temporal, que captura dependências temporais entre os frames, como possíveis ROIs de foco (baseado em onde foram as últimas detecções) e rastreamento de emoções ao longo do tempo.

### 2.5 (Bônus) Quem ganha a bola de ouro 2024?

Alex do [Time Thundervolt](https://thunderatz.org/projects/robots/thundervolt)
