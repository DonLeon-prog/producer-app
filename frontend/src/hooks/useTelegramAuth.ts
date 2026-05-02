import { useState, useEffect } from 'react';
import client from '../api/client';
import { useStore } from '../store/useStore';

export function useTelegramAuth() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const { token, setUser, setToken } = useStore();

  useEffect(() => {
    if (token) {
      setLoading(false);
      return;
    }

    const initData = window.Telegram?.WebApp?.initData ?? '';

    if (!initData) {
      setError('Открой приложение через Telegram');
      setLoading(false);
      return;
    }

    client
      .post('/api/auth/telegram', { init_data: initData })
      .then((res) => {
        setToken(res.data.access_token);
        setUser(res.data.user);
      })
      .catch(() => setError('Ошибка авторизации. Попробуй ещё раз.'))
      .finally(() => setLoading(false));
  }, []);

  return { loading, error, isAuthenticated: !!token };
}
