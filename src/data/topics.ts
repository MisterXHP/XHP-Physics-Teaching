// 中学物理主题分类（17 项）
// 以后若要增删主题，只需修改本数组；站点导航、分类页会自动跟随。

export interface Topic {
  slug: string;
  name: string;
  desc: string;
}

export const topics: Topic[] = [
  { slug: 'zhixian-yundong', name: '直线运动', desc: '位移、速度、加速度与匀变速直线运动' },
  { slug: 'xianghu-zuoyong', name: '相互作用', desc: '力、重力、弹力、摩擦力与受力分析' },
  { slug: 'niudun-dinglv', name: '牛顿运动定律', desc: '惯性、牛顿三定律与动力学应用' },
  { slug: 'quxian-yundong', name: '曲线运动', desc: '运动的合成与分解、抛体运动、圆周运动' },
  { slug: 'wanyou-yinli', name: '万有引力与宇宙航行', desc: '万有引力定律、天体运动与航天' },
  { slug: 'jixie-neng', name: '机械能守恒定律', desc: '功、功率、动能、势能与机械能守恒' },
  { slug: 'dongliang', name: '动量守恒定律', desc: '冲量、动量定理与动量守恒' },
  { slug: 'zhendong-bo', name: '机械振动与机械波', desc: '简谐运动、机械波与波的传播' },
  { slug: 'jingdianchang', name: '静电场', desc: '电荷、电场强度、电势与电容器' },
  { slug: 'zhiliu-dianlu', name: '直流电路', desc: '电流、欧姆定律、电功与电路分析' },
  { slug: 'cichang', name: '磁场', desc: '磁场、安培力与洛伦兹力' },
  { slug: 'dianci-ganying', name: '电磁感应', desc: '磁通量、感应电动势与楞次定律' },
  { slug: 'jiaobian-dianliu', name: '交变电流与电磁波', desc: '交变电流、变压器与电磁波' },
  { slug: 'guang', name: '光', desc: '几何光学、光的干涉衍射与折射' },
  { slug: 'rexue', name: '热学', desc: '分子动理论、内能、物态变化与气体定律' },
  { slug: 'jindai-wuli', name: '近代物理初步', desc: '光电效应、原子结构与核反应初步' },
  { slug: 'wuli-shiyan', name: '物理实验', desc: '力学、电学与光学实验探究' },
];

export function topicBySlug(slug: string): Topic | undefined {
  return topics.find((t) => t.slug === slug);
}

export function topicByName(name: string): Topic | undefined {
  return topics.find((t) => t.name === name);
}
