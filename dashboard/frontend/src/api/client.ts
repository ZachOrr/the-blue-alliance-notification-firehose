import type { ApiResponse, NotificationType } from '../types/notification';

const API_BASE_URL = '/api';

export async function fetchNotifications(selectedTypes: NotificationType[] = []): Promise<ApiResponse> {
  const params = new URLSearchParams();

  if (selectedTypes.length > 0) {
    params.append('types', selectedTypes.join(','));
  }

  const queryString = params.toString();
  const url = queryString ? `${API_BASE_URL}/notifications?${queryString}` : `${API_BASE_URL}/notifications`;

  const response = await fetch(url);

  if (!response.ok) {
    throw new Error(`Failed to fetch notifications: ${response.statusText}`);
  }

  return response.json();
}
