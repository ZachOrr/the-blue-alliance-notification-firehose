import { NotificationCard } from './NotificationCard';
import { useNotifications } from '../contexts/NotificationContext';

interface NotificationListProps {
  timestampMode: 'browser' | 'utc';
}

export const NotificationList: React.FC<NotificationListProps> = ({ timestampMode }) => {
  const { notifications, loading, error } = useNotifications();

  if (loading) {
    return (
      <div className="flex justify-center items-center py-12">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-red-50 dark:bg-red-900 border-2 border-red-300 dark:border-red-700 rounded-lg p-4 mb-4">
        <h3 className="text-lg font-semibold text-red-900 dark:text-red-100 mb-2">
          Error Loading Notifications
        </h3>
        <p className="text-red-800 dark:text-red-200">{error}</p>
      </div>
    );
  }

  if (notifications.length === 0) {
    return (
      <div className="bg-gray-50 dark:bg-gray-800 rounded-lg p-8 text-center">
        <p className="text-gray-600 dark:text-gray-400 text-lg">
          No notifications found. Try adjusting your filters.
        </p>
      </div>
    );
  }

  return (
    <div>
      <h2 className="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-4">
        Notifications ({notifications.length})
      </h2>
      {notifications.map((notification) => (
        <NotificationCard
          key={notification.id}
          notification={notification}
          timestampMode={timestampMode}
        />
      ))}
    </div>
  );
};
