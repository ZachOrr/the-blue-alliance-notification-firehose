import React, { createContext, useContext, useState, useEffect, useCallback, useMemo } from 'react';
import type { Notification, NotificationType, FilterState } from '../types/notification';
import { fetchNotifications } from '../api/client';

interface NotificationContextType {
  notifications: Notification[];
  filters: FilterState;
  loading: boolean;
  error: string | null;
  toggleFilter: (type: NotificationType) => void;
  selectAllFilters: () => void;
  clearAllFilters: () => void;
  refetch: () => void;
}

const NotificationContext = createContext<NotificationContextType | undefined>(undefined);

const ALL_NOTIFICATION_TYPES: NotificationType[] = [
  'upcoming_match',
  'match_score',
  'schedule_updated',
  'starting_comp_level',
  'alliance_selection',
  'awards_posted',
  'match_video',
  'ping',
  'broadcast',
];

const DEFAULT_FILTERS = ALL_NOTIFICATION_TYPES.reduce((acc, type) => ({ ...acc, [type]: true }), {}) as FilterState;

const ALL_FILTERS_ON = ALL_NOTIFICATION_TYPES.reduce((acc, type) => ({ ...acc, [type]: true }), {}) as FilterState;

const ALL_FILTERS_OFF = ALL_NOTIFICATION_TYPES.reduce((acc, type) => ({ ...acc, [type]: false }), {}) as FilterState;

export const NotificationProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [allNotifications, setAllNotifications] = useState<Notification[]>([]);
  const [filters, setFilters] = useState<FilterState>(DEFAULT_FILTERS);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [fetchKey, setFetchKey] = useState(0);

  const selectedTypes = useMemo(
    () => (Object.keys(filters) as NotificationType[]).filter((type) => filters[type]),
    [filters]
  );

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    setError(null);
    fetchNotifications()
      .then((data) => {
        if (!cancelled) setAllNotifications(data.notifications);
      })
      .catch((err) => {
        if (!cancelled) setError(err instanceof Error ? err.message : 'An error occurred');
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });
    return () => {
      cancelled = true;
    };
  }, [fetchKey]);

  const notifications = useMemo(
    () => allNotifications.filter((notification) => selectedTypes.includes(notification.type)),
    [allNotifications, selectedTypes]
  );

  const refetch = useCallback(() => {
    setFetchKey((k) => k + 1);
  }, []);

  const toggleFilter = (type: NotificationType) => {
    setFilters((prev) => ({
      ...prev,
      [type]: !prev[type],
    }));
  };

  const selectAllFilters = () => {
    setFilters(ALL_FILTERS_ON);
  };

  const clearAllFilters = () => {
    setFilters(ALL_FILTERS_OFF);
  };

  const value: NotificationContextType = {
    notifications,
    filters,
    loading,
    error,
    toggleFilter,
    selectAllFilters,
    clearAllFilters,
    refetch,
  };

  return (
    <NotificationContext.Provider value={value}>{children}</NotificationContext.Provider>
  );
};

export const useNotifications = () => {
  const context = useContext(NotificationContext);
  if (!context) {
    throw new Error('useNotifications must be used within NotificationProvider');
  }
  return context;
};
