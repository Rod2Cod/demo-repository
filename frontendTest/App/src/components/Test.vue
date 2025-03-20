<script>
export default {
  name: "Test",
  props: {
    test: Object,
  },
};
</script>

<template>
  <div class="test-card">
    <h2 class="test-title">Test del {{ test.date }}</h2>
    <p class="test-info"><strong>Modello LLM:</strong> {{ test.llmUsed }}</p>
    <p class="test-info"><strong>Punteggio:</strong> {{ test.score }}</p>
    <p class="test-info"><strong>Set di Domande:</strong> {{ test.questionSet }}</p>

    <h3 class="section-title">Risultati del Test</h3>
    <div class="question-list">
      <div v-for="(question, index) in test.questions" :key="index" class="question-item">
        <p class="question-text"><strong>Domanda:</strong> {{ question.text }}</p>
        <p class="expected-answer"><strong>Risposta Attesa:</strong> {{ question.expectedAnswer }}</p>
        <p class="llm-response"><strong>Risposta del LLM:</strong> {{ question.llmResponse }}</p>
        <p class="score"><strong>Punteggio:</strong> {{ question.score }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.test-card {
  background-color: #222;
  padding: 20px;
  border-radius: 10px;
}

.test-title {
  font-size: 1.5rem;
  font-weight: bold;
  color: white;
  margin-bottom: 10px;
}

.section-title {
  font-size: 1.3rem;
  font-weight: bold;
  margin-top: 20px;
  color: white;
}

.test-info {
  font-size: 1rem;
  color: #ccc;
  margin-bottom: 5px;
}

.question-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.question-item {
  padding: 15px;
  border-radius: 8px;
  background: #333;
}

.question-text, .expected-answer, .llm-response, .score {
  color: #ddd;
  font-size: 1rem;
  margin-bottom: 5px;
}
</style>
