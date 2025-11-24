<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const quickActions = [
  {
    id: 'register',
    label: 'Ro‘yxatdan o‘tkazish',
    description: 'Yangi xodim yoki ishtirokchini tezkor ro‘yxatdan o‘tkazing',
    icon: '📝',
    to: '/register',
  },
  {
    id: 'about',
    label: 'Loyiha haqida',
    description: 'Mini-app maqsadi va imkoniyatlari bilan tanishing',
    icon: 'ℹ️',
    to: '/about',
  },
]

const stats = [
  { id: 1, label: 'Bugungi so‘rovlar', value: '18', trend: '+5', trendLabel: 'so‘nggi kunga nisbatan' },
  { id: 2, label: 'Faol foydalanuvchilar', value: '73', trend: '+12', trendLabel: 'oxirgi 7 kunda' },
  { id: 3, label: 'Yangi ro‘yxatdan o‘tganlar', value: '6', trend: '+2', trendLabel: 'bugun' },
]

const recentItems = [
  { id: 1, title: 'HR Mini-app dastlabki test', time: 'Bugun, 10:24', tag: 'Test', status: 'Yakunlandi' },
  { id: 2, title: 'Telegram bot integratsiyasi', time: 'Kecha, 16:05', tag: 'Integratsiya', status: 'Jarayonda' },
  { id: 3, title: 'Ro‘yxatdan o‘tish formasi', time: '3 kun oldin', tag: 'UI', status: 'Yakunlandi' },
]

function goTo(path) {
  router.push(path)
}
</script>

<template>
  <div class="home-root">
    <!-- Welcome block -->
    <section class="welcome-card">
      <div class="welcome-main">
        <div>
          <h2 class="welcome-title">Assalomu alaykum 👋</h2>
          <p class="welcome-subtitle">
            Restaurant Mini App orqali HR ma’lumotlarni tezkor ko‘rish va boshqarish imkoniyati.
          </p>
        </div>
        <button class="welcome-cta" type="button" @click="goTo('/register')">
          Boshlash
        </button>
      </div>

      <div class="welcome-meta">
        <span class="dot"></span>
        <span>Bugun hammasi joyida. Siz tayyorsiz 🚀</span>
      </div>
    </section>

    <!-- Stats -->
    <section class="section">
      <h3 class="section-title">Qisqa statistikalar</h3>
      <div class="stats-grid">
        <div v-for="item in stats" :key="item.id" class="stat-card">
          <span class="stat-label">{{ item.label }}</span>
          <p class="stat-value">{{ item.value }}</p>
          <p class="stat-trend">
            <span class="trend-pill">
              {{ item.trend }}
            </span>
            <span class="trend-text">{{ item.trendLabel }}</span>
          </p>
        </div>
      </div>
    </section>

    <!-- Quick actions -->
    <section class="section">
      <h3 class="section-title">Tezkor amallar</h3>
      <div class="quick-grid">
        <button v-for="action in quickActions" :key="action.id" class="quick-card" type="button"
          @click="goTo(action.to)">
          <div class="quick-icon">
            {{ action.icon }}
          </div>
          <div class="quick-body">
            <div class="quick-title-row">
              <span class="quick-title">{{ action.label }}</span>
              <span class="quick-chevron">›</span>
            </div>
            <p class="quick-desc">
              {{ action.description }}
            </p>
          </div>
        </button>
      </div>
    </section>

    <!-- Recent activity -->
    <section class="section">
      <h3 class="section-title">So‘nggi faollik</h3>
      <div class="recent-list">
        <div v-for="item in recentItems" :key="item.id" class="recent-item">
          <div class="recent-main">
            <p class="recent-title">{{ item.title }}</p>
            <p class="recent-meta">
              <span class="recent-time">{{ item.time }}</span>
              <span class="recent-tag">{{ item.tag }}</span>
            </p>
          </div>
          <span class="recent-status">
            {{ item.status }}
          </span>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.home-root {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

/* Welcome card */
.welcome-card {
  background: radial-gradient(circle at top left, rgba(56, 189, 248, 0.16), transparent 60%),
    rgba(15, 23, 42, 0.98);
  border-radius: 18px;
  padding: 12px;
  border: 1px solid rgba(148, 163, 184, 0.2);
  box-shadow: 0 10px 26px rgba(15, 23, 42, 0.9);
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.welcome-main {
  display: flex;
  align-items: flex-start;
  gap: 10px;
}

.welcome-title {
  margin: 0;
  font-size: 18px;
  font-weight: 600;
}

.welcome-subtitle {
  margin: 4px 0 0;
  font-size: 12px;
  color: #cbd5f5;
  opacity: 0.9;
}

.welcome-cta {
  margin-left: auto;
  align-self: center;
  border-radius: 999px;
  border: none;
  padding: 8px 14px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;

  background: linear-gradient(135deg, #38bdf8, #22c55e);
  color: #0f172a;
  box-shadow: 0 0 0 1px rgba(15, 23, 42, 0.6),
    0 12px 24px rgba(15, 23, 42, 0.95);
  transition: transform 0.16s ease-out, box-shadow 0.16s ease-out, opacity 0.16s;
}

.welcome-cta:hover {
  transform: translateY(-1px);
  opacity: 0.95;
}

.welcome-cta:active {
  transform: translateY(0);
  box-shadow: 0 6px 14px rgba(15, 23, 42, 0.9);
}

.welcome-meta {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 11px;
  color: #9ca3af;
}

.dot {
  width: 8px;
  height: 8px;
  border-radius: 999px;
  background: #22c55e;
  box-shadow: 0 0 0 4px rgba(34, 197, 94, 0.2);
}

/* Sections */
.section {
  background: rgba(15, 23, 42, 0.98);
  border-radius: 18px;
  padding: 10px;
  border: 1px solid rgba(148, 163, 184, 0.18);
}

.section-title {
  margin: 0 0 8px;
  font-size: 13px;
  font-weight: 600;
  color: #e5e7eb;
}

/* Stats */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 8px;
}

.stat-card {
  background: rgba(15, 23, 42, 0.96);
  border-radius: 14px;
  padding: 8px;
  border: 1px solid rgba(55, 65, 81, 0.7);
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.stat-label {
  font-size: 10px;
  color: #9ca3af;
}

.stat-value {
  margin: 0;
  font-size: 16px;
  font-weight: 600;
  color: #f9fafb;
}

.stat-trend {
  margin: 0;
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 10px;
}

.trend-pill {
  padding: 1px 6px;
  border-radius: 999px;
  background: rgba(34, 197, 94, 0.16);
  color: #4ade80;
  font-weight: 500;
}

.trend-text {
  color: #9ca3af;
}

/* Quick actions */
.quick-grid {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.quick-card {
  display: flex;
  gap: 8px;
  width: 100%;
  border-radius: 14px;
  padding: 8px;
  border: 1px solid rgba(55, 65, 81, 0.7);
  background: rgba(15, 23, 42, 0.96);
  text-align: left;
  cursor: pointer;
  outline: none;
  color: inherit;
  transition: transform 0.14s ease-out, box-shadow 0.14s ease-out, border-color 0.14s ease-out;
}

.quick-card:hover {
  transform: translateY(-1px);
  border-color: rgba(96, 165, 250, 0.9);
  box-shadow: 0 10px 22px rgba(15, 23, 42, 0.9);
}

.quick-icon {
  width: 34px;
  height: 34px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(circle at top, rgba(56, 189, 248, 0.28), rgba(15, 23, 42, 0.9));
  font-size: 18px;
}

.quick-body {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.quick-title-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.quick-title {
  font-size: 13px;
  font-weight: 500;
  color: #e5e7eb;
}

.quick-chevron {
  font-size: 16px;
  opacity: 0.6;
}

.quick-desc {
  margin: 0;
  font-size: 11px;
  color: #9ca3af;
}

/* Recent activity */
.recent-list {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.recent-item {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 6px;
  border-radius: 12px;
  padding: 8px;
  background: rgba(15, 23, 42, 0.96);
  border: 1px solid rgba(55, 65, 81, 0.7);
}

.recent-main {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.recent-title {
  margin: 0;
  font-size: 12px;
  font-weight: 500;
  color: #e5e7eb;
}

.recent-meta {
  margin: 0;
  display: flex;
  gap: 6px;
  font-size: 10px;
}

.recent-time {
  color: #9ca3af;
}

.recent-tag {
  padding: 1px 6px;
  border-radius: 999px;
  background: rgba(56, 189, 248, 0.18);
  color: #7dd3fc;
}

.recent-status {
  font-size: 10px;
  padding: 2px 8px;
  border-radius: 999px;
  background: rgba(34, 197, 94, 0.15);
  color: #4ade80;
  align-self: center;
}

/* Kattaroq ekranlar uchun */
@media (min-width: 768px) {
  .home-root {
    gap: 14px;
  }

  .welcome-title {
    font-size: 20px;
  }

  .stats-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}
</style>
