import { useNavigate } from 'react-router-dom';

export default function UserTypeSelect() {
  const navigate = useNavigate();

  const pick = (type: 'blogger' | 'musician') => {
    window.Telegram?.WebApp?.HapticFeedback?.impactOccurred('medium');
    navigate(`/onboarding/${type}`);
  };

  return (
    <div className="min-h-screen bg-[#0F0F0F] flex flex-col px-6 pt-16 pb-10">
      <div className="mb-12 animate-slide-in">
        <h1
          className="text-3xl font-bold text-white mb-3"
          style={{ fontFamily: 'Onest, sans-serif' }}
        >
          Кто ты?
        </h1>
        <p className="text-white/50 text-base">Выбери — и я подстрою всё под тебя</p>
      </div>

      <div className="flex flex-col gap-4 flex-1 justify-center">
        {/* Карточка блогера */}
        <button
          onClick={() => pick('blogger')}
          className="w-full bg-[#1A1A1A] rounded-3xl p-6 text-left active:scale-95 transition-transform"
          style={{ animationDelay: '0.05s' }}
        >
          <div
            className="w-14 h-14 rounded-2xl flex items-center justify-center mb-4"
            style={{ backgroundColor: 'rgba(127,119,221,0.15)' }}
          >
            <CameraIcon />
          </div>
          <h2
            className="text-xl font-bold text-white mb-1"
            style={{ fontFamily: 'Onest, sans-serif' }}
          >
            Я блогер
          </h2>
          <p className="text-white/50 text-sm">Снимаю видео, хочу вырасти в соцсетях</p>
          <div className="mt-4 flex items-center gap-1 text-[#7F77DD] text-sm font-medium">
            Начать <ArrowIcon />
          </div>
        </button>

        {/* Карточка музыканта */}
        <button
          onClick={() => pick('musician')}
          className="w-full bg-[#1A1A1A] rounded-3xl p-6 text-left active:scale-95 transition-transform"
          style={{ animationDelay: '0.1s' }}
        >
          <div
            className="w-14 h-14 rounded-2xl flex items-center justify-center mb-4"
            style={{ backgroundColor: 'rgba(127,119,221,0.15)' }}
          >
            <MicIcon />
          </div>
          <h2
            className="text-xl font-bold text-white mb-1"
            style={{ fontFamily: 'Onest, sans-serif' }}
          >
            Я музыкант
          </h2>
          <p className="text-white/50 text-sm">Записываю треки, хочу набрать аудиторию</p>
          <div className="mt-4 flex items-center gap-1 text-[#7F77DD] text-sm font-medium">
            Начать <ArrowIcon />
          </div>
        </button>
      </div>
    </div>
  );
}

function CameraIcon() {
  return (
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none">
      <path
        d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"
        stroke="#7F77DD" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"
      />
      <circle cx="12" cy="13" r="4" stroke="#7F77DD" strokeWidth="1.8" />
    </svg>
  );
}

function MicIcon() {
  return (
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none">
      <rect x="9" y="2" width="6" height="11" rx="3" stroke="#7F77DD" strokeWidth="1.8" />
      <path
        d="M5 10a7 7 0 0 0 14 0"
        stroke="#7F77DD" strokeWidth="1.8" strokeLinecap="round"
      />
      <line x1="12" y1="17" x2="12" y2="21" stroke="#7F77DD" strokeWidth="1.8" strokeLinecap="round" />
      <line x1="9" y1="21" x2="15" y2="21" stroke="#7F77DD" strokeWidth="1.8" strokeLinecap="round" />
    </svg>
  );
}

function ArrowIcon() {
  return (
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
      <path d="M5 12h14M13 6l6 6-6 6" stroke="#7F77DD" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  );
}
