<script>
export default {
  name: "AggiungiDomanda",
  data() {
    return {
      question: "",
      expectedAnswer: ""
    };
  },
  methods: {
    submitForm() {
      console.log("Form inviato con:", this.question, this.expectedAnswer);
      this.$router.push("/questions");
      // API in futuro
    }
  }
};
</script>

<template>
  <main class="container">
    <h1 class="page-title">Aggiungi una Domanda</h1>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="question">Domanda</label>
        <input
            type="text"
            id="question"
            v-model="question"
            placeholder="Inserisci la domanda"
            required
        />
      </div>

      <div class="form-group">
        <label for="answer">Risposta</label>
        <textarea
            id="answer"
            v-model="expectedAnswer"
            placeholder="Inserisci la risposta"
            required
        ></textarea>
      </div>

      <div class="button-container">
        <button type="submit" class="submit-btn">Invia</button>
      </div>
    </form>
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

input, textarea {
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
</style>
