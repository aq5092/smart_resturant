<script setup>
// hozircha maxsus logika yo'q, faqat info sahifa
const technologies = [
  { id: 1, label: 'Frontend', value: 'Vue 3 + Vite' },
  { id: 2, label: 'UI', value: 'Custom mini-app layout (Telegram)' },
  { id: 3, label: 'Routing', value: 'vue-router' },
  { id: 4, label: 'Integratsiya', value: 'Telegram WebApp / Mini App' },
]
</script>

<template>
  <div class="about-root">
    <!-- Title block -->
    <section class="section section-main">
      <h2 class="title">Loyiha haqida</h2>
      <p class="subtitle">
        Ushbu mini-app UzAuto tizimidagi HR jarayonlarini
        <span class="highlight">Telegram orqali tezkor boshqarish</span>
        va ko‘rish uchun mo‘ljallangan.
      </p>

      <div class="pill-row">
        <span class="pill">Mini App</span>
        <span class="pill">HR Tools</span>
        <span class="pill">Real-time</span>
      </div>
    </section>

    <!-- Goals -->
    <section class="section">
      <h3 class="section-title">Asosiy maqsadlar</h3>
      <ul class="list">
        <li class="list-item">
          <span class="bullet">•</span>
          <div>
            <p class="list-title">Tezkor kirish</p>
            <p class="list-text">
              Xodimlar haqidagi qisqa ma’lumotlar va asosiy funksiyalarga
              Telegram ichidan chiqmasdan kirish imkoniyati.
            </p>
          </div>
        </li>

        <li class="list-item">
          <span class="bullet">•</span>
          <div>
            <p class="list-title">Yig‘ilgan interfeys</p>
            <p class="list-text">
              Kichik ekranlarda ham qulay ishlashi uchun maxsus mini-app
              layout qo‘llangan.
            </p>
          </div>
        </li>

        <li class="list-item">
          <span class="bullet">•</span>
          <div>
            <p class="list-title">HR jarayonlarni yengillashtirish</p>
            <p class="list-text">
              Ro‘yxatdan o‘tkazish, statistikani ko‘rish va qisqa amallarni
              bir joydan boshqarish.
            </p>
          </div>
        </li>
      </ul>
    </section>

    <!-- Tech stack -->
    <section class="section">
      <h3 class="section-title">Texnik ma’lumot</h3>
      <div class="tech-grid">
        <div
          v-for="t in technologies"
          :key="t.id"
          class="tech-card"
        >
          <p class="tech-label">{{ t.label }}</p>
          <p class="tech-value">{{ t.value }}</p>
        </div>
      </div>
    </section>

    <!-- Contact / future -->
    <section class="section">
      <h3 class="section-title">Keyingi rejalashtirilgan imkoniyatlar</h3>
      <ul class="list">
        <li class="list-item-simple">• KPI va statistikani grafik ko‘rinishda chiqarish</li>
        <li class="list-item-simple">• Xodimlar bo‘yicha qisqa profil oynasi</li>
        <li class="list-item-simple">• Telegram’dan kelgan parametrlar asosida personalizatsiya</li>
      </ul>

      <div class="note">
        <p class="note-title">Taklif va fikrlar</p>
        <p class="note-text">
          Agar yangi funksiya yoki o‘zgartirish bo‘yicha g‘oyangiz bo‘lsa,
          uni HR / DTT jamoasiga yetkazish mumkin.
        </p>
      </div>
    </section>
  </div>
</template>

<style scoped>
.about-root {
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

/* Main header section */
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

.highlight {
  color: #7dd3fc;
}

/* pilllar */
.pill-row {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 10px;
}

.pill {
  font-size: 11px;
  padding: 3px 8px;
  border-radius: 999px;
  background: rgba(15, 23, 42, 0.9);
  border: 1px solid rgba(148, 163, 184, 0.4);
  color: #e5e7eb;
}

/* Section titles */
.section-title {
  margin: 0 0 8px;
  font-size: 13px;
  font-weight: 600;
  color: #e5e7eb;
}

/* List */
.list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.list-item {
  display: flex;
  gap: 6px;
}

.bullet {
  font-size: 14px;
  line-height: 1.5;
  color: #64748b;
}

.list-title {
  margin: 0;
  font-size: 12px;
  font-weight: 500;
  color: #e5e7eb;
}

.list-text {
  margin: 2px 0 0;
  font-size: 11px;
  color: #9ca3af;
}

.list-item-simple {
  font-size: 11px;
  color: #d1d5db;
}

/* Tech grid */
.tech-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 8px;
}

.tech-card {
  border-radius: 14px;
  padding: 8px;
  background: rgba(15, 23, 42, 0.96);
  border: 1px solid rgba(55, 65, 81, 0.7);
}

.tech-label {
  margin: 0;
  font-size: 10px;
  color: #9ca3af;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.tech-value {
  margin: 4px 0 0;
  font-size: 12px;
  font-weight: 500;
  color: #e5e7eb;
}

/* Note block */
.note {
  margin-top: 8px;
  padding: 8px;
  border-radius: 14px;
  background: rgba(15, 23, 42, 0.96);
  border: 1px dashed rgba(148, 163, 184, 0.6);
}

.note-title {
  margin: 0 0 4px;
  font-size: 12px;
  font-weight: 500;
  color: #e5e7eb;
}

.note-text {
  margin: 0;
  font-size: 11px;
  color: #9ca3af;
}

/* Kattaroq ekranlar uchun */
@media (min-width: 768px) {
  .about-root {
    gap: 14px;
  }

  .title {
    font-size: 20px;
  }
}
</style>
