import { useState, useEffect } from 'react';
import client from '../api/client';
import { useStore } from '../store/useStore';
import type { User } from '../store/useStore';

const DEV_USER: User = {
  id: 'dev-user-id',
  telegram_id: 'test_user_123',
  first_name: 'Тест',
  username: 'testuser',
  user_type: null,
  profile: null,
  plan: 'free',
  requests_today: 0,
};

// Фейковый JWT (header.payload.signature) — только для dev-режима
const DEV_TOKEN = [
  btoa(JSON.stringify({ alg: 'HS256', typ: 'JWT' })),
  btoa(JSON.stringify({ sub: 'test_user_123', exp: 9999999999 })),
  'dev_signature',
].join('.');

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
      // Dev-режим: браузер без Telegram — используем тестовые данные
      setToken(DEV_TOKEN);
      setUser(DEV_USER);
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
