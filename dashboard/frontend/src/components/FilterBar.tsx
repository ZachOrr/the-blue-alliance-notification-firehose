import type { NotificationType } from '../types/notification';
import { useNotifications } from '../contexts/NotificationContext';

const NOTIFICATION_TYPES: NotificationType[] = [
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

const formatTypeName = (type: NotificationType): string => {
  return type.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
};

const getTypeColorClasses = (type: NotificationType): string => {
  const colorMap: Record<NotificationType, string> = {
    upcoming_match: 'bg-red-300 border-red-700 text-red-950 dark:bg-red-700 dark:border-red-400 dark:text-red-50',
    match_score: 'bg-orange-300 border-orange-700 text-orange-950 dark:bg-orange-700 dark:border-orange-400 dark:text-orange-50',
    schedule_updated: 'bg-yellow-300 border-yellow-700 text-yellow-950 dark:bg-yellow-700 dark:border-yellow-400 dark:text-yellow-50',
    starting_comp_level: 'bg-emerald-300 border-emerald-700 text-emerald-950 dark:bg-emerald-700 dark:border-emerald-400 dark:text-emerald-50',
    alliance_selection: 'bg-cyan-300 border-cyan-700 text-cyan-950 dark:bg-cyan-700 dark:border-cyan-400 dark:text-cyan-50',
    awards_posted: 'bg-blue-300 border-blue-700 text-blue-950 dark:bg-blue-700 dark:border-blue-400 dark:text-blue-50',
    match_video: 'bg-violet-300 border-violet-700 text-violet-950 dark:bg-violet-700 dark:border-violet-400 dark:text-violet-50',
    ping: 'bg-fuchsia-300 border-fuchsia-700 text-fuchsia-950 dark:bg-fuchsia-700 dark:border-fuchsia-400 dark:text-fuchsia-50',
    broadcast: 'bg-zinc-300 border-zinc-700 text-zinc-950 dark:bg-zinc-700 dark:border-zinc-400 dark:text-zinc-50',
  };

  return colorMap[type];
};

export const FilterBar: React.FC = () => {
  const { filters, toggleFilter, selectAllFilters, clearAllFilters } = useNotifications();

  const allSelected = Object.values(filters).every(v => v);
  const someSelected = Object.values(filters).some(v => v);

  return (
    <div className="bg-gray-50 dark:bg-gray-800 rounded-lg p-4 border border-gray-200 dark:border-gray-700">
      <div className="mb-4">
        <h2 className="text-lg font-semibold text-gray-900 dark:text-gray-100">
          Notification Filters
        </h2>
        <div className="grid grid-cols-2 gap-2 mt-3">
          <button
            onClick={selectAllFilters}
            className={`px-3 py-2 rounded text-sm font-medium transition ${
              allSelected
                ? 'bg-blue-500 text-white'
                : 'bg-gray-200 dark:bg-gray-700 text-gray-900 dark:text-gray-100 hover:bg-gray-300 dark:hover:bg-gray-600'
            }`}
          >
            Select All
          </button>
          <button
            onClick={clearAllFilters}
            className={`px-3 py-2 rounded text-sm font-medium transition ${
              !someSelected
                ? 'bg-gray-400 text-white'
                : 'bg-gray-200 dark:bg-gray-700 text-gray-900 dark:text-gray-100 hover:bg-gray-300 dark:hover:bg-gray-600'
            }`}
          >
            Clear All
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 gap-2">
        {NOTIFICATION_TYPES.map((type) => (
          <label
            key={type}
            className={`flex items-center gap-3 p-2.5 rounded border cursor-pointer transition ${
              filters[type]
                ? `${getTypeColorClasses(type)} ring-1 ring-white/20 dark:ring-white/20`
                : `${getTypeColorClasses(type)} opacity-35 hover:opacity-75`
            }`}
          >
            <input
              type="checkbox"
              checked={filters[type] || false}
              onChange={() => toggleFilter(type)}
              className="w-4 h-4 rounded cursor-pointer"
            />
            <span className="text-sm font-medium">
              {formatTypeName(type)}
            </span>
          </label>
        ))}
      </div>
    </div>
  );
};
