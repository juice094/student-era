const PREFIX = 'edu_admin_'

export function persist<T>(key: string, data: T): void {
  try {
    localStorage.setItem(PREFIX + key, JSON.stringify(data))
  } catch {
    // localStorage 满或禁用，静默失败
  }
}

export function restore<T>(key: string, defaultValue: T): T {
  try {
    const raw = localStorage.getItem(PREFIX + key)
    return raw ? (JSON.parse(raw) as T) : defaultValue
  } catch {
    return defaultValue
  }
}

export function removePersist(key: string): void {
  localStorage.removeItem(PREFIX + key)
}
