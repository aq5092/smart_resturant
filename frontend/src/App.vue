<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="app-root">
    <!-- TOP BAR -->
    <header class="app-header">
      <div class="brand">
        <img
          alt="App logo"
          class="logo"
          src="@/assets/logo.svg"
          width="40"
          height="40"
        />
        <div class="brand-text">
          <h1 class="brand-title">Register Mini App</h1>
          <p class="brand-subtitle">Restaurant panel</p>
        </div>
      </div>

      <!-- TOP NAV (icon + text) -->
      <nav class="top-nav">
        <RouterLink to="/" class="nav-item">
          <span class="nav-icon">🏠</span>
          <span class="nav-label">Home</span>
        </RouterLink>
        <RouterLink to="/about" class="nav-item">
          <span class="nav-icon">ℹ️</span>
          <span class="nav-label">About</span>
        </RouterLink>
        <RouterLink to="/register" class="nav-item">
          <span class="nav-icon">📝</span>
          <span class="nav-label">Register</span>
        </RouterLink>
      </nav>
    </header>

    <!-- PAGE CONTENT -->
    <main class="app-main">
      <section class="page-card">
        <RouterView />
      </section>
    </main>
  </div>
</template>

<style scoped>
.app-root {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  padding: 12px;
  box-sizing: border-box;

  /* Telegram mini-app’ga mos: yumshoq gradient fon */
  background: radial-gradient(circle at top left, #1e88e5 0, #0f172a 45%, #020617 100%);
  color: #f9fafb;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

/* HEADER */
.app-header {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 12px;
}

/* Brand qismi */
.brand {
  display: flex;
  align-items: center;
  gap: 10px;
}

.logo {
  border-radius: 14px;
  padding: 4px;
  background: rgba(15, 23, 42, 0.7);
  box-shadow: 0 8px 20px rgba(15, 23, 42, 0.6);
}

.brand-text {
  display: flex;
  flex-direction: column;
}

.brand-title {
  margin: 0;
  font-size: 18px;
  font-weight: 600;
}

.brand-subtitle {
  margin: 0;
  font-size: 12px;
  opacity: 0.8;
}

/* TOP NAV – pill buttonlar */
.top-nav {
  display: flex;
  gap: 8px;
  background: rgba(15, 23, 42, 0.7);
  padding: 6px;
  border-radius: 999px;
  backdrop-filter: blur(18px);
  box-shadow: 0 8px 22px rgba(15, 23, 42, 0.9);
}

.nav-item {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4px;

  text-decoration: none;
  color: #e5e7eb;
  font-size: 12px;
  padding: 6px 8px;
  border-radius: 999px;
  transition: all 0.18s ease-out;
  opacity: 0.8;
}

/* Active route */
.nav-item.router-link-exact-active {
  background: linear-gradient(135deg, #38bdf8, #22c55e);
  color: #0f172a;
  font-weight: 600;
  opacity: 1;
  box-shadow: 0 0 0 1px rgba(15, 23, 42, 0.6),
    0 10px 26px rgba(15, 23, 42, 0.95);
}

.nav-item:hover {
  opacity: 1;
  transform: translateY(-1px);
}

.nav-icon {
  font-size: 14px;
}

.nav-label {
  white-space: nowrap;
}

/* MAIN CONTENT */
.app-main {
  flex: 1;
  display: flex;
  margin-top: 4px;
}

/* Ichki karta – RouterView shu yerda */
.page-card {
  width: 100%;
  background: rgba(15, 23, 42, 0.92);
  border-radius: 18px;
  padding: 12px;
  box-shadow: 0 14px 30px rgba(15, 23, 42, 0.95);
  border: 1px solid rgba(148, 163, 184, 0.18);
  box-sizing: border-box;
  overflow: auto;
}

/* Kattaroq ekranlar uchun ozgina responsivlik */
@media (min-width: 768px) {
  .app-root {
    padding: 16px 20px;
  }

  .app-header {
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
  }

  .brand-title {
    font-size: 20px;
  }

  .page-card {
    max-width: 900px;
    margin: 0 auto;
  }
}
</style>
