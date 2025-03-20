<script>
export default {
  name: "ModificaDomanda",
  data() {
    return {
      question: "",
      expectedAnswer: "",
      isLoaded: false, // Per simulare il caricamento dei dati
    };
  },
  mounted() {
    this.loadQuestion();
  },
  methods: {
    loadQuestion() {

      setTimeout(() => {
        this.question = "Cos'è Vue.js?";
        this.expectedAnswer =
            "Vue.js è un framework JavaScript progressivo per la creazione di interfacce utente.";
        this.isLoaded = true;
      }, 500);
    },
    submitForm() {
      console.log("Domanda modificata:", this.question, this.expectedAnswer);
      // API per aggiornare la domanda
    },
    cancel() {
      this.$router.push("/questions")
    },
  },
};
</script>

<template>
  <main class="container">
    <h1 class="page-title">Modifica la Domanda</h1>

    <form v-if="isLoaded" @submit.prevent="submitForm">
      <div class="form-group">
        <label for="question">Domanda</label>
        <input
            type="text"
            id="question"
            v-model="question"
            placeholder="Modifica la domanda"
            required
        />
      </div>

      <div class="form-group">
        <label for="answer">Risposta</label>
        <textarea
            id="answer"
            v-model="expectedAnswer"
            placeholder="Modifica la risposta"
            required
        ></textarea>
      </div>

      <div class="button-container">
        <button type="submit" class="submit-btn">Salva Modifica</button>
        <button type="button" class="cancel-btn" @click="cancel">Annulla</button>
      </div>
    </form>

    <p v-else class="loading-text">Caricamento domanda...</p>
  </main>
</template>

<style scoped>
.container {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  background-color: #222;
  border-radius: 10px;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
  color: white;
}

.loading-text {
  text-align: center;
  color: white;
  font-size: 18px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
  color: white;
}

input,
textarea {
  width: 100%;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #444;
  background-color: #333;
  color: white;
}

textarea {
  resize: none;
  height: 100px;
}

.button-container {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}

.submit-btn {
  background-color: white;
  color: black;
  padding: 12px 20px;
  font-size: 16px;
  border-radius: 5px;
  border: 1px solid black;
  cursor: pointer;
  transition: 0.3s;
}

.submit-btn:hover {
  background-color: #ddd;
}

.cancel-btn {
  background-color: #e74c3c;
  color: white;
  padding: 12px 20px;
  font-size: 16px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  transition: 0.3s;
}

.cancel-btn:hover {
  background-color: #c0392b;
}
</style>
