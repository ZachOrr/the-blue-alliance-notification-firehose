import './App.css';
import { useEffect, useState } from 'react';
import { FilterBar } from './components/FilterBar';
import { NotificationList } from './components/NotificationList';
import { useNotifications } from './contexts/NotificationContext';

type ThemeMode = 'system' | 'light' | 'dark';

function App() {
  const { refetch } = useNotifications();
  const [timestampMode, setTimestampMode] = useState<'browser' | 'utc'>('browser');
  const [themeMode, setThemeMode] = useState<ThemeMode>(() => {
    const stored = window.localStorage.getItem('themeMode');
    if (stored === 'system' || stored === 'light' || stored === 'dark') {
      return stored;
    }
    return 'system';
  });

  useEffect(() => {
    const root = document.documentElement;
    const media = window.matchMedia('(prefers-color-scheme: dark)');

    const applyTheme = () => {
      const useDark = themeMode === 'dark' || (themeMode === 'system' && media.matches);
      root.classList.toggle('dark', useDark);
    };

    applyTheme();
    window.localStorage.setItem('themeMode', themeMode);

    if (themeMode !== 'system') {
      return;
    }

    const onSystemThemeChange = () => applyTheme();
    media.addEventListener('change', onSystemThemeChange);
    return () => media.removeEventListener('change', onSystemThemeChange);
  }, [themeMode]);

  return (
    <div className="min-h-screen bg-white dark:bg-gray-950">
      <header className="bg-blue-600 dark:bg-blue-800 text-white sticky top-0 z-10 shadow-lg">
        <div className="max-w-6xl mx-auto px-4 py-4 sm:px-6 lg:px-8">
          <div className="flex flex-col gap-3 sm:flex-row sm:justify-between sm:items-center">
            <h1 className="text-2xl sm:text-3xl font-bold">TBA Notifications Dashboard</h1>
            <div className="flex flex-wrap items-center gap-2">
              <div className="flex rounded-lg overflow-hidden border border-blue-200 bg-blue-700/35">
                <button
                  onClick={() => setThemeMode('system')}
                  className={`px-3 py-2 text-sm font-medium transition ${
                    themeMode === 'system'
                      ? 'bg-white text-blue-800'
                      : 'text-white hover:bg-white/20'
                  }`}
                >
                  System
                </button>
                <button
                  onClick={() => setThemeMode('light')}
                  className={`px-3 py-2 text-sm font-medium transition ${
                    themeMode === 'light'
                      ? 'bg-white text-blue-800'
                      : 'text-white hover:bg-white/20'
                  }`}
                >
                  Light
                </button>
                <button
                  onClick={() => setThemeMode('dark')}
                  className={`px-3 py-2 text-sm font-medium transition ${
                    themeMode === 'dark'
                      ? 'bg-white text-blue-800'
                      : 'text-white hover:bg-white/20'
                  }`}
                >
                  Dark
                </button>
              </div>
              <div className="flex rounded-lg overflow-hidden border border-blue-200 bg-blue-700/35">
                <button
                  onClick={() => setTimestampMode('browser')}
                  className={`px-3 py-2 text-sm font-medium transition ${
                    timestampMode === 'browser'
                      ? 'bg-white text-blue-800'
                      : 'text-white hover:bg-white/20'
                  }`}
                >
                  Browser Time
                </button>
                <button
                  onClick={() => setTimestampMode('utc')}
                  className={`px-3 py-2 text-sm font-medium transition ${
                    timestampMode === 'utc'
                      ? 'bg-white text-blue-800'
                      : 'text-white hover:bg-white/20'
                  }`}
                >
                  UTC
                </button>
              </div>
              <button
                onClick={refetch}
                className="px-4 py-2 bg-white text-blue-800 hover:bg-blue-50 rounded-lg font-semibold transition border border-blue-200"
              >
                Refresh
              </button>
            </div>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-[300px_minmax(0,1fr)] gap-6 items-start">
          <aside className="lg:sticky lg:top-24">
            <FilterBar />
          </aside>
          <section>
            <NotificationList timestampMode={timestampMode} />
          </section>
        </div>
      </main>
    </div>
  );
}

export default App;
