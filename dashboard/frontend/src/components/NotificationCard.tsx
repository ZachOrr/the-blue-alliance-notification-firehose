import type { Notification, NotificationType } from '../types/notification';

interface NotificationCardProps {
  notification: Notification;
  timestampMode: 'browser' | 'utc';
}

const getTypeColor = (type: NotificationType): string => {
  const colorMap: Record<NotificationType, string> = {
    upcoming_match: 'bg-red-300 border-red-700 text-red-950',
    match_score: 'bg-orange-300 border-orange-700 text-orange-950',
    schedule_updated: 'bg-yellow-300 border-yellow-700 text-yellow-950',
    starting_comp_level: 'bg-emerald-300 border-emerald-700 text-emerald-950',
    alliance_selection: 'bg-cyan-300 border-cyan-700 text-cyan-950',
    awards_posted: 'bg-blue-300 border-blue-700 text-blue-950',
    match_video: 'bg-violet-300 border-violet-700 text-violet-950',
    ping: 'bg-fuchsia-300 border-fuchsia-700 text-fuchsia-950',
    broadcast: 'bg-zinc-300 border-zinc-700 text-zinc-950',
  };
  return colorMap[type];
};

const getTypeDarkColor = (type: NotificationType): string => {
  const colorMap: Record<NotificationType, string> = {
    upcoming_match: 'dark:bg-red-700 dark:border-red-400 dark:text-red-50',
    match_score: 'dark:bg-orange-700 dark:border-orange-400 dark:text-orange-50',
    schedule_updated: 'dark:bg-yellow-700 dark:border-yellow-400 dark:text-yellow-50',
    starting_comp_level: 'dark:bg-emerald-700 dark:border-emerald-400 dark:text-emerald-50',
    alliance_selection: 'dark:bg-cyan-700 dark:border-cyan-400 dark:text-cyan-50',
    awards_posted: 'dark:bg-blue-700 dark:border-blue-400 dark:text-blue-50',
    match_video: 'dark:bg-violet-700 dark:border-violet-400 dark:text-violet-50',
    ping: 'dark:bg-fuchsia-700 dark:border-fuchsia-400 dark:text-fuchsia-50',
    broadcast: 'dark:bg-zinc-700 dark:border-zinc-400 dark:text-zinc-50',
  };
  return colorMap[type];
};

const formatDate = (timestamp: string, mode: 'browser' | 'utc'): string => {
  try {
    const date = new Date(timestamp);
    const options: Intl.DateTimeFormatOptions = {
      year: 'numeric',
      month: 'numeric',
      day: 'numeric',
      hour: 'numeric',
      minute: '2-digit',
      second: '2-digit',
      timeZoneName: 'short',
    };

    if (mode === 'utc') {
      options.timeZone = 'UTC';
    }

    return date.toLocaleString(undefined, {
      ...options,
    });
  } catch {
    return timestamp;
  }
};

const formatNotificationType = (type: NotificationType): string => {
  return type.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
};

export const NotificationCard: React.FC<NotificationCardProps> = ({ notification, timestampMode }) => {
  const baseClasses = 'border-2 rounded-lg p-4 mb-4 transition-shadow hover:shadow-md';
  const colorClasses = getTypeColor(notification.type);
  const darkColorClasses = getTypeDarkColor(notification.type);

  return (
    <div className={`${baseClasses} ${colorClasses} ${darkColorClasses}`}>
      <div className="flex justify-between items-start gap-4">
        <div className="flex-1 text-left">
          <div className="flex items-center gap-2 mb-2">
            <span className="inline-block px-3 py-1 bg-white/90 text-gray-900 dark:bg-black/70 dark:text-gray-100 rounded-full text-sm font-semibold">
              {formatNotificationType(notification.type)}
            </span>
            <span className="text-xs opacity-75">
              {formatDate(notification.timestamp, timestampMode)}
            </span>
          </div>
          <pre className="bg-white/95 dark:bg-black/55 text-gray-900 dark:text-gray-100 rounded p-3 overflow-auto max-h-64 text-xs font-mono whitespace-pre-wrap break-words">
            {JSON.stringify(notification.payload, null, 2)}
          </pre>
        </div>
      </div>
    </div>
  );
};
