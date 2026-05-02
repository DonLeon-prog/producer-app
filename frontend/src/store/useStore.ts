import { create } from 'zustand';

export interface User {
  id: string;
  telegram_id: string;
  username?: string | null;
  first_name?: string | null;
  user_type?: 'blogger' | 'musician' | null;
  profile?: Record<string, unknown> | null;
  plan: string;
  requests_today: number;
}

interface AppState {
  user: User | null;
  token: string | null;
  profile: Record<string, unknown> | null;
  userType: 'blogger' | 'musician' | null;
  isAuthenticated: boolean;
  setUser: (user: User) => void;
  setToken: (token: string) => void;
  setProfile: (profile: Record<string, unknown>) => void;
  setUserType: (userType: 'blogger' | 'musician') => void;
}

const initialToken = localStorage.getItem('token');

export const useStore = create<AppState>()((set) => ({
  user: null,
  token: initialToken,
  isAuthenticated: !!initialToken,
  profile: null,
  userType: null,
  setUser: (user) =>
    set({
      user,
      userType: (user.user_type ?? null) as 'blogger' | 'musician' | null,
    }),
  setToken: (token) => {
    localStorage.setItem('token', token);
    set({ token, isAuthenticated: true });
  },
  setProfile: (profile) => set({ profile }),
  setUserType: (userType) => set({ userType }),
}));
