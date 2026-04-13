export type NotificationType =
  | 'upcoming_match'
  | 'match_score'
  | 'schedule_updated'
  | 'starting_comp_level'
  | 'alliance_selection'
  | 'awards_posted'
  | 'match_video'
  | 'ping'
  | 'broadcast';

export interface Notification {
  id: string;
  timestamp: string; // ISO 8601 format
  type: NotificationType;
  payload: Record<string, unknown>;
}

export interface ApiResponse {
  notifications: Notification[];
}

export type FilterState = {
  [T in NotificationType]?: boolean;
}
