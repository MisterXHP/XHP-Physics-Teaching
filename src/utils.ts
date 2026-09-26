export function sortByDateDesc<T extends { data: { date?: Date } }>(items: T[]): T[] {
  return [...items].sort(
    (a, b) => (b.data.date?.getTime() ?? 0) - (a.data.date?.getTime() ?? 0)
  );
}

export function formatDate(d?: Date): string {
  if (!d) return '';
  const y = d.getFullYear();
  const m = String(d.getMonth() + 1).padStart(2, '0');
  const day = String(d.getDate()).padStart(2, '0');
  return `${y}-${m}-${day}`;
}

/** 把内容里的 embed / video / file 字段解析为可用的 URL（相对路径自动加 base） */
export function resolveAssetUrl(value: string, base: string): string {
  if (/^https?:\/\//i.test(value) || value.startsWith('data:')) return value;
  return base.replace(/\/$/, '') + '/' + value.replace(/^\//, '');
}
