<script>
import Test from "@/components/Test.vue";

export default {
  name: "TestView",
  components: { Test },
  data() {
    return {
      testStarted: false,
      testCompleted: false,
      progress: 0,
      test: null,
    };
  },
  methods: {
    startTest() {
      this.testStarted = true;
      this.testCompleted = false;
      this.progress = 0;
      this.simulateTestExecution();
    },
    simulateTestExecution() {
      this.test = {
        id: 1,
        date: new Date().toISOString().split("T")[0],
        llmUsed: "GPT-4",
        score: 85,
        questionSet: "Vue Basics",
        questions: [
          {
            text: "Quanto fa 2 + 2?",
            expectedAnswer: "Il risultato di 2 + 2 è 4.",
            llmResponse: "4",
            score: 10
          },
          {
            text: "Qual è la capitale d'Italia?",
            expectedAnswer: "La capitale d'Italia è Roma.",
            llmResponse: "Roma",
            score: 10
          }
        ],
      };

      let interval = setInterval(() => {
        if (this.progress < 100) {
          this.progress += 10;
        } else {
          clearInterval(interval);
          this.testCompleted = true;
        }
      }, 300);
    },
  },
};
</script>

<template>
  <main class="container">
    <h1 class="page-title">Esegui un Test</h1>

    <div class="spacer"></div>

    <button v-if="!testStarted" class="start-btn" @click="startTest">
      Inizia Test
    </button>

    <div v-if="testStarted && !testCompleted" class="progress-container">
      <p>Test in esecuzione...</p>
      <div class="progress-bar">
        <div class="progress-fill" :style="{ width: progress + '%' }"></div>
      </div>
    </div>

    <div v-if="testCompleted" class="test-results">
      <h2 class="results-title">Test Completato</h2>
      <Test :test="test" />
    </div>
  </main>
</template>

<style scoped>
.container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
  text-align: center;
}

.page-title {
  font-size: 2.5rem;
  font-weight: bold;
  color: white;
}

.spacer {
  height: 40px;
}

.start-btn {
  background-color: white;
  color: black;
  font-size: 1.2rem;
  padding: 12px 20px;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  transition: 0.3s;
}

.start-btn:hover {
  background-color: #ddd;
}

.progress-container {
  margin-top: 30px;
}

.progress-container p {
  font-size: 1.1rem;
  font-weight: bold;
  color: white;
}

.progress-bar {
  width: 100%;
  height: 20px;
  background: #4c4c4c;
  border-radius: 10px;
  overflow: hidden;
  margin-top: 10px;
}

.progress-fill {
  height: 100%;
  background: #ffffff;
  transition: width 0.3s ease-in-out;
}

.test-results {
  margin-top: 50px;
  padding: 20px;
  background-color: #222;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.results-title {
  font-size: 1.8rem;
  font-weight: bold;
  color: white;
  margin-bottom: 20px;
}
</style>
