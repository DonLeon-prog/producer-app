import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import client from '../../api/client';
import { useStore } from '../../store/useStore';

const DEV_USER_PATCH = { id: 'dev-user-id', telegram_id: 'test_user_123', first_name: 'Тест', username: 'testuser', plan: 'free', requests_today: 0 };

const GENRES = [
  'Поп', 'Рэп / хип-хоп', 'R&B', 'Инди', 'Рок', 'Электронная',
  'Джаз', 'Классика', 'Фолк', 'Альтернатива', 'Lo-fi', 'Другой',
];
const PLATFORMS = ['Spotify', 'VK Музыка', 'YouTube', 'Instagram', 'TikTok', 'SoundCloud', 'Apple Music'];
const STATUSES = ['Только начинаю', 'Есть несколько треков', 'Регулярно выпускаю музыку', 'Готовлю альбом'];
const GOALS = [
  '1 000 слушателей в месяц', 'Попасть в плейлист',
  'Найти продюсера', 'Выступить на мероприятии', 'Подписать контракт',
];

interface FormData {
  name: string;
  genre: string[];
  platforms: string[];
  influences: string;
  release_status: string;
  goals: string;
}

const TOTAL = 6;

export default function OnboardingMusician() {
  const navigate = useNavigate();
  const { setUser } = useStore();
  const [step, setStep] = useState(1);
  const [animKey, setAnimKey] = useState(0);
  const [form, setForm] = useState<FormData>({
    name: '', genre: [], platforms: [], influences: '', release_status: '', goals: '',
  });
  const [submitting, setSubmitting] = useState(false);
  const [analysis, setAnalysis] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const canProceed = () => {
    if (step === 1) return form.name.trim().length > 0;
    if (step === 2) return form.genre.length > 0;
    if (step === 3) return form.platforms.length > 0;
    if (step === 4) return form.influences.trim().length > 0;
    if (step === 5) return form.release_status.length > 0;
    if (step === 6) return form.goals.length > 0;
    return false;
  };

  const toggleMulti = (field: 'genre' | 'platforms', value: string) =>
    setForm(p => ({
      ...p,
      [field]: p[field].includes(value) ? p[field].filter(v => v !== value) : [...p[field], value],
    }));

  const next = () => {
    if (!canProceed()) return;
    if (step < TOTAL) {
      setStep(s => s + 1);
      setAnimKey(k => k + 1);
    } else {
      submit();
    }
  };

  const back = () => {
    if (step > 1) { setStep(s => s - 1); setAnimKey(k => k + 1); }
  };

  const submit = async () => {
    setSubmitting(true);
    setError(null);
    try {
      const isDev = !window.Telegram?.WebApp?.initData;
      if (isDev) {
        await new Promise(r => setTimeout(r, 1200));
        setUser({ ...DEV_USER_PATCH, user_type: 'musician' } as any);
        setAnalysis('🎵 Dev-режим: AI-анализ заглушка.\n\nВ реальном приложении здесь будет персональный анализ жанра, приоритетные платформы и конкретный план продвижения.');
        return;
      }
      const res = await client.post('/api/profile', { user_type: 'musician', ...form });
      if (res.data.user) setUser(res.data.user);
      setAnalysis(res.data.analysis);
    } catch (e: any) {
      setError(e.response?.data?.detail ?? 'Ошибка. Попробуй ещё раз.');
      setSubmitting(false);
    }
  };

  if (submitting && !analysis) {
    return (
      <div className="min-h-screen bg-[#0F0F0F] flex flex-col items-center justify-center gap-6 px-6">
        <div className="w-12 h-12 border-2 border-[#7F77DD] border-t-transparent rounded-full animate-spin" />
        <p className="text-white/60 text-center text-lg" style={{ fontFamily: 'Onest, sans-serif' }}>
          Изучаем твой музыкальный профиль...
        </p>
      </div>
    );
  }

  if (analysis) {
    return (
      <div className="min-h-screen bg-[#0F0F0F] flex flex-col px-6 pt-12 pb-28">
        <h1 className="text-3xl font-bold text-white mb-6" style={{ fontFamily: 'Onest, sans-serif' }}>
          Твой AI-анализ 🎵
        </h1>
        <div className="bg-[#1A1A1A] rounded-2xl p-5">
          <p className="text-white/80 text-base leading-relaxed whitespace-pre-wrap">{analysis}</p>
        </div>
        <button
          onClick={() => navigate('/app')}
          className="fixed bottom-6 left-6 right-6 h-14 bg-[#7F77DD] rounded-2xl text-white font-semibold text-lg"
          style={{ fontFamily: 'Onest, sans-serif' }}
        >
          Перейти в приложение
        </button>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-[#0F0F0F] pt-12 pb-28" style={{ paddingLeft: 24, paddingRight: 24 }}>
      {/* Прогресс */}
      <div className="flex items-center gap-2 mt-4 mb-10">
        {Array.from({ length: TOTAL }).map((_, i) => (
          <div
            key={i}
            className="h-2.5 rounded-full transition-all duration-300"
            style={{
              width: i + 1 === step ? 28 : 10,
              backgroundColor: i + 1 < step ? '#4ade80' : i + 1 === step ? '#7F77DD' : 'rgba(255,255,255,0.15)',
            }}
          />
        ))}
        {step > 1 && (
          <button onClick={back} className="ml-auto text-white/40 text-sm">
            ← Назад
          </button>
        )}
      </div>

      {/* Контент шага */}
      <div key={animKey} className="animate-slide-in">
        {step === 1 && (
          <>
            <h2 className="text-3xl font-bold text-white mb-3" style={{ fontFamily: 'Onest, sans-serif' }}>
              Как тебя зовут?
            </h2>
            <p className="text-base text-white/50 mb-8">Твоё имя или псевдоним артиста</p>
            <input
              autoFocus
              type="text"
              value={form.name}
              onChange={e => setForm(p => ({ ...p, name: e.target.value }))}
              onKeyDown={e => e.key === 'Enter' && next()}
              placeholder="Имя артиста..."
              className="w-full h-14 bg-[#1A1A1A] rounded-2xl px-5 text-white text-lg placeholder-white/30 outline-none transition-all"
              style={{ border: '1.5px solid transparent' }}
              onFocus={e => (e.target.style.borderColor = '#7F77DD')}
              onBlur={e => (e.target.style.borderColor = 'transparent')}
            />
          </>
        )}

        {step === 2 && (
          <>
            <h2 className="text-3xl font-bold text-white mb-3" style={{ fontFamily: 'Onest, sans-serif' }}>
              Какая у тебя музыка?
            </h2>
            <p className="text-base text-white/50 mb-8">Выбери один или несколько жанров</p>
            <div className="flex flex-wrap gap-3">
              {GENRES.map(g => (
                <Chip key={g} label={g} selected={form.genre.includes(g)} onToggle={() => toggleMulti('genre', g)} />
              ))}
            </div>
          </>
        )}

        {step === 3 && (
          <>
            <h2 className="text-3xl font-bold text-white mb-3" style={{ fontFamily: 'Onest, sans-serif' }}>
              Где продвигаешься?
            </h2>
            <p className="text-base text-white/50 mb-8">Можно выбрать несколько</p>
            <div className="flex flex-wrap gap-3">
              {PLATFORMS.map(p => (
                <Chip key={p} label={p} selected={form.platforms.includes(p)} onToggle={() => toggleMulti('platforms', p)} />
              ))}
            </div>
          </>
        )}

        {step === 4 && (
          <>
            <h2 className="text-3xl font-bold text-white mb-3" style={{ fontFamily: 'Onest, sans-serif' }}>
              Кто тебя вдохновляет?
            </h2>
            <p className="text-base text-white/50 mb-8">Назови 1–3 артиста со схожим звуком или образом</p>
            <input
              autoFocus
              type="text"
              value={form.influences}
              onChange={e => setForm(p => ({ ...p, influences: e.target.value }))}
              onKeyDown={e => e.key === 'Enter' && next()}
              placeholder="Например: Грибы, IC3PEAK..."
              className="w-full h-14 bg-[#1A1A1A] rounded-2xl px-5 text-white text-lg placeholder-white/30 outline-none transition-all"
              style={{ border: '1.5px solid transparent' }}
              onFocus={e => (e.target.style.borderColor = '#7F77DD')}
              onBlur={e => (e.target.style.borderColor = 'transparent')}
            />
          </>
        )}

        {step === 5 && (
          <>
            <h2 className="text-3xl font-bold text-white mb-3" style={{ fontFamily: 'Onest, sans-serif' }}>
              На каком ты этапе?
            </h2>
            <p className="text-base text-white/50 mb-8">Выбери один вариант</p>
            <div className="flex flex-wrap gap-3">
              {STATUSES.map(s => (
                <Chip
                  key={s}
                  label={s}
                  selected={form.release_status === s}
                  onToggle={() => setForm(p => ({ ...p, release_status: s }))}
                />
              ))}
            </div>
          </>
        )}

        {step === 6 && (
          <>
            <h2 className="text-3xl font-bold text-white mb-3" style={{ fontFamily: 'Onest, sans-serif' }}>
              Цель на 3 месяца
            </h2>
            <p className="text-base text-white/50 mb-8">Выбери одну</p>
            <div className="flex flex-wrap gap-3">
              {GOALS.map(g => (
                <Chip
                  key={g}
                  label={g}
                  selected={form.goals === g}
                  onToggle={() => setForm(p => ({ ...p, goals: g }))}
                />
              ))}
            </div>
          </>
        )}
      </div>

      {error && <p className="text-red-400 text-base text-center mt-6">{error}</p>}

      {/* Фиксированная кнопка */}
      <button
        onClick={next}
        disabled={!canProceed()}
        className="fixed bottom-6 h-14 text-white font-semibold text-lg transition-opacity"
        style={{
          left: 16, right: 16, borderRadius: 16,
          fontFamily: 'Onest, sans-serif',
          backgroundColor: '#7F77DD',
          opacity: canProceed() ? 1 : 0.3,
        }}
      >
        {step === TOTAL ? 'Получить анализ' : 'Далее'}
      </button>
    </div>
  );
}

function Chip({ label, selected, onToggle }: { label: string; selected: boolean; onToggle: () => void }) {
  return (
    <button
      onClick={onToggle}
      className="text-base font-medium transition-all"
      style={{
        padding: '12px 20px',
        borderRadius: 24,
        backgroundColor: selected ? '#7F77DD' : '#1A1A1A',
        color: selected ? '#fff' : 'rgba(255,255,255,0.6)',
        border: selected ? '1.5px solid #7F77DD' : '1.5px solid rgba(255,255,255,0.1)',
      }}
    >
      {label}
    </button>
  );
}
