export interface PersistAPI {
  persist<T>(key: string, data: T): void
  restore<T>(key: string, defaultValue: T): T
  remove(key: string): void
}

export function createPersist(namespace: string): PersistAPI {
  const prefix = namespace.endsWith('_') ? namespace : namespace + '_'

  return {
    persist<T>(key: string, data: T): void {
      try {
        localStorage.setItem(prefix + key, JSON.stringify(data))
      } catch {
        // localStorage full or disabled — silent failure
      }
    },

    restore<T>(key: string, defaultValue: T): T {
      try {
        const raw = localStorage.getItem(prefix + key)
        return raw ? (JSON.parse(raw) as T) : defaultValue
      } catch {
        return defaultValue
      }
    },

    remove(key: string): void {
      localStorage.removeItem(prefix + key)
    }
  }
}

// Default instance for backward compatibility
const defaultPersist = createPersist('student_era')

export const persist = defaultPersist.persist
export const restore = defaultPersist.restore
export const removePersist = defaultPersist.remove
