<script setup>
import { ref } from 'vue'

const form = ref({
  fullName: '',
  department: '',
  phone: '',
  note: '',
})

const loading = ref(false)
const successMessage = ref('')
const errorMessage = ref('')

const handleSubmit = async () => {
  successMessage.value = ''
  errorMessage.value = ''

  if (!form.value.fullName || !form.value.department) {
    errorMessage.value = 'Iltimos, F.I.Sh va bo‘limni kiriting.'
    return
  }

  loading.value = true
  try {
    // TODO: bu yerda backendga yuborish logikasini qo‘shasan
    // masalan:
    // await fetch('/api/register', {
    //   method: 'POST',
    //   headers: { 'Content-Type': 'application/json' },
    //   body: JSON.stringify(form.value),
    // })

    // Demo uchun faqat kichik delay
    await new Promise((resolve) => setTimeout(resolve, 400))

    successMessage.value = 'Ma’lumotlar muvaffaqiyatli yuborildi ✅'
  } catch (e) {
    errorMessage.value = 'Xatolik yuz berdi. Qayta urinib ko‘ring.'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="register-root">
    <!-- Title / intro -->
    <section class="section section-main">
      <h2 class="title">Ro‘yxatdan o‘tkazish</h2>
      <p class="subtitle">
        Quyidagi qisqa formani to‘ldiring. Ma’lumotlar tezkor ishlov berish
        uchun mini-app orqali yuboriladi.
      </p>

      <div class="badge-row">
        <span class="badge">HR</span>
        <span class="badge">Mini App</span>
        <span class="badge">Form</span>
      </div>
    </section>

    <!-- Status messages -->
    <section class="section section-narrow">
      <p v-if="successMessage" class="alert alert-success">
        {{ successMessage }}
      </p>
      <p v-if="errorMessage" class="alert alert-error">
        {{ errorMessage }}
      </p>

      <!-- FORM -->
      <form class="form" @submit.prevent="handleSubmit">
        <div class="field">
          <label class="field-label" for="fullName">F.I.Sh</label>
          <input
            id="fullName"
            v-model="form.fullName"
            class="field-input"
            type="text"
            placeholder="Familiya Ism Sharif"
            autocomplete="off"
          />
        </div>

        <div class="field">
          <label class="field-label" for="department">Bo‘lim</label>
          <input
            id="department"
            v-model="form.department"
            class="field-input"
            type="text"
            placeholder="Masalan: HRD, DTT, Zavod-1 va h.k."
            autocomplete="off"
          />
        </div>

        <div class="field">
          <label class="field-label" for="phone">Telefon raqam</label>
          <input
            id="phone"
            v-model="form.phone"
            class="field-input"
            type="tel"
            placeholder="+998 90 123 45 67"
            autocomplete="off"
          />
        </div>

        <div class="field">
          <label class="field-label" for="note">Izoh (ixtiyoriy)</label>
          <textarea
            id="note"
            v-model="form.note"
            class="field-input field-textarea"
            rows="3"
            placeholder="Qo‘shimcha ma’lumot yoki eslatma..."
          />
        </div>

        <button
          class="submit-btn"
          type="submit"
          :disabled="loading"
        >
          <span v-if="!loading">Yuborish</span>
          <span v-else>Yuborilmoqda...</span>
        </button>

        <p class="helper-text">
          Ma’lumotlar yuborilgandan so‘ng, kerak bo‘lsa, HR / DTT jamoasi
          tomonidan qo‘shimcha aloqa qilinadi.
        </p>
      </form>
    </section>
  </div>
</template>

<style scoped>
.register-root {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

/* Common section style */
.section {
  background: rgba(15, 23, 42, 0.98);
  border-radius: 18px;
  padding: 10px;
  border: 1px solid rgba(148, 163, 184, 0.18);
}

/* Title block */
.section-main {
  background: radial-gradient(circle at top left, rgba(56, 189, 248, 0.16), transparent 65%),
    rgba(15, 23, 42, 0.98);
}

.title {
  margin: 0 0 4px;
  font-size: 18px;
  font-weight: 600;
  color: #f9fafb;
}

.subtitle {
  margin: 0;
  font-size: 12px;
  color: #cbd5f5;
  opacity: 0.9;
}

/* badges */
.badge-row {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 10px;
}

.badge {
  font-size: 11px;
  padding: 3px 8px;
  border-radius: 999px;
  background: rgba(15, 23, 42, 0.9);
  border: 1px solid rgba(148, 163, 184, 0.4);
  color: #e5e7eb;
}

/* Narrow card for form */
.section-narrow {
  padding: 10px 10px 12px;
}

/* Alerts */
.alert {
  margin: 0 0 8px;
  font-size: 11px;
  padding: 6px 8px;
  border-radius: 10px;
}

.alert-success {
  background: rgba(22, 163, 74, 0.16);
  border: 1px solid rgba(34, 197, 94, 0.6);
  color: #bbf7d0;
}

.alert-error {
  background: rgba(220, 38, 38, 0.14);
  border: 1px solid rgba(248, 113, 113, 0.8);
  color: #fecaca;
}

/* Form */
.form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.field-label {
  font-size: 11px;
  color: #e5e7eb;
}

.field-input {
  border-radius: 12px;
  border: 1px solid rgba(55, 65, 81, 0.9);
  background: rgba(15, 23, 42, 0.96);
  padding: 8px 10px;
  font-size: 12px;
  color: #f9fafb;
  outline: none;
  transition: border-color 0.14s ease-out, box-shadow 0.14s ease-out, background-color 0.14s ease-out;
  font-family: inherit;
}

.field-input::placeholder {
  color: #6b7280;
}

.field-input:focus {
  border-color: rgba(96, 165, 250, 0.95);
  box-shadow: 0 0 0 1px rgba(37, 99, 235, 0.8);
  background: rgba(15, 23, 42, 0.98);
}

.field-textarea {
  resize: vertical;
  min-height: 70px;
}

/* Submit button */
.submit-btn {
  margin-top: 4px;
  width: 100%;
  border: none;
  border-radius: 999px;
  padding: 9px 12px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;

  background: linear-gradient(135deg, #38bdf8, #22c55e);
  color: #0f172a;
  box-shadow: 0 0 0 1px rgba(15, 23, 42, 0.6),
    0 12px 24px rgba(15, 23, 42, 0.95);
  transition: transform 0.16s ease-out, box-shadow 0.16s ease-out, opacity 0.16s ease-out,
    filter 0.16s ease-out;
}

.submit-btn:hover:not(:disabled) {
  transform: translateY(-1px);
  opacity: 0.96;
}

.submit-btn:active:not(:disabled) {
  transform: translateY(0);
  box-shadow: 0 7px 16px rgba(15, 23, 42, 0.9);
}

.submit-btn:disabled {
  opacity: 0.7;
  cursor: default;
  filter: grayscale(10%);
}

/* Helper text */
.helper-text {
  margin: 6px 0 0;
  font-size: 10px;
  color: #9ca3af;
}

/* Kattaroq ekranlar uchun */
@media (min-width: 768px) {
  .register-root {
    gap: 14px;
  }

  .title {
    font-size: 20px;
  }
}
</style>
