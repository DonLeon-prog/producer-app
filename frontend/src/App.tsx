import { useEffect } from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { useTelegramAuth } from './hooks/useTelegramAuth';
import { useStore } from './store/useStore';
import UserTypeSelect from './components/Onboarding/UserTypeSelect';
import OnboardingBlogger from './components/Onboarding/OnboardingBlogger';
import OnboardingMusician from './components/Onboarding/OnboardingMusician';

function AppRoutes() {
  const { loading, error } = useTelegramAuth();
  const { token, user } = useStore();

  useEffect(() => {
    window.Telegram?.WebApp?.ready();
    window.Telegram?.WebApp?.expand();
  }, []);

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-[#0F0F0F]">
        <div className="w-8 h-8 border-2 border-[#7F77DD] border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  if (error || !token) {
    return (
      <div className="flex flex-col items-center justify-center min-h-screen bg-[#0F0F0F] px-6 gap-3">
        <span className="text-4xl">🤖</span>
        <p className="text-white/60 text-center text-sm">
          {error ?? 'Открой приложение через Telegram'}
        </p>
      </div>
    );
  }

  return (
    <Routes>
      <Route
        path="/"
        element={
          user?.user_type
            ? <Navigate to="/app" replace />
            : <Navigate to="/onboarding" replace />
        }
      />
      <Route path="/onboarding" element={<UserTypeSelect />} />
      <Route path="/onboarding/blogger" element={<OnboardingBlogger />} />
      <Route path="/onboarding/musician" element={<OnboardingMusician />} />
      <Route
        path="/app/*"
        element={<div className="min-h-screen bg-[#0F0F0F] text-white p-6">Дашборд</div>}
      />
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <AppRoutes />
    </BrowserRouter>
  );
}
