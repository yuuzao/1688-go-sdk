#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
根据 tools/aop 中的 Python SDK（biz 目录）生成 Go 静态注册表 api/biz/registry_static.go。
使用方式：
  python3 tools/generate.py

可通过环境变量覆盖：
  INPUT_DIR=tools/aop/api/biz OUTPUT=api/biz/registry_static.go python3 tools/generate.py
"""
import os
import re
from collections import defaultdict

INPUT_DIR = os.environ.get('INPUT_DIR', 'tools/aop/api/biz')
OUTPUT = os.environ.get('OUTPUT', 'api/biz/registry_static.go')

re_class = re.compile(r'class\s+(\w+)\(BaseApi\):')
re_uri = re.compile(r'def\s+get_api_uri\(self\):\s*\n\s*return\s+[\'\"]([^\'\"]+)[\'\"]')
def re_bool(name):
    return re.compile(r'def\s+'+name+r'\(self\):\s*\n\s*return\s+(True|False)')
re_required = re.compile(r'def\s+get_required_params\(self\):\s*\n\s*return\s*\[(?s:(.*?))\]')
re_multipart = re.compile(r'def\s+get_multipart_params\(self\):\s*\n\s*return\s*\[(?s:(.*?))\]')

def parse_list(s: str):
    s = (s or '').strip()
    if not s:
        return []
    out = []
    for part in s.split(','):
        part = part.strip()
        if not part:
            continue
        if part[0] in ('"', "'") and part[-1] == part[0]:
            part = part[1:-1]
        out.append(part)
    return out

def category_from_uri(uri: str) -> str:
    try:
        ns = uri.split('/')[1]
    except Exception:
        return 'other'
    cat = ns.split('.')[-1] if '.' in ns else ns
    alias = {
        'open': 'open',
        'logistics': 'logistics',
        'trade': 'trade',
        'product': 'product',
        'account': 'account',
        'category': 'category',
    }
    return alias.get(cat, cat or 'other')

def scan_entries(root: str):
    bools = {
        'sign': re_bool('need_sign'),
        'ts': re_bool('need_timestamp'),
        'auth': re_bool('need_auth'),
        'https': re_bool('need_https'),
        'inner': re_bool('is_inner_api'),
    }
    entries = []
    for dirpath, _, files in os.walk(root):
        for fn in sorted(f for f in files if f.endswith('.py')):
            p = os.path.join(dirpath, fn)
            txt = open(p, 'r', encoding='utf-8').read()
            mc = re_class.search(txt)
            mu = re_uri.search(txt)
            if not (mc and mu):
                continue
            cls = mc.group(1)
            uri = mu.group(1)
            def b(rx):
                m = rx.search(txt)
                return bool(m and m.group(1) == 'True')
            req = re_required.search(txt)
            mp = re_multipart.search(txt)
            name = cls[:-5] if cls.endswith('Param') else cls
            entries.append({
                'Name': name,
                'APIURI': uri,
                'NeedSign': b(bools['sign']),
                'NeedTimestamp': b(bools['ts']),
                'NeedAuth': b(bools['auth']),
                'NeedHTTPS': b(bools['https']),
                'IsInnerAPI': b(bools['inner']),
                'Required': parse_list(req.group(1) if req else ''),
                'Multipart': parse_list(mp.group(1) if mp else ''),
                'Cat': category_from_uri(uri),
            })
    entries.sort(key=lambda x: (x['Cat'], x['Name']))
    return entries

def q(s: str) -> str:
    return '"' + s.replace('\\', r'\\').replace('"', r'\"') + '"'

def qa(arr):
    return '[]string{' + ', '.join(q(x) for x in arr) + '}'

def emit(entries):
    bycat = defaultdict(list)
    for e in entries:
        bycat[e['Cat']].append(e)
    cats = sorted(bycat.keys())
    lines = []
    lines.append('package biz')
    lines.append('')
    lines.append('// Code generated from Python SDK; DO NOT EDIT.')
    lines.append('')
    lines.append('var StaticApis = []Descriptor{')
    for cat in cats:
        lines.append(f'  // ===== {cat} =====')
        for e in bycat[cat]:
            lines.append('  {Name:%s, APIURI:%s, NeedSign:%s, NeedTimestamp:%s, NeedAuth:%s, NeedHTTPS:%s, IsInnerAPI:%s, Required:%s, Multipart:%s},' % (
                q(e['Name']), q(e['APIURI']), str(e['NeedSign']).lower(), str(e['NeedTimestamp']).lower(), str(e['NeedAuth']).lower(), str(e['NeedHTTPS']).lower(), str(e['IsInnerAPI']).lower(), qa(e['Required']), qa(e['Multipart'])
            ))
    lines.append('}')
    lines.append('')
    lines.append('func init(){ for _, d := range StaticApis { Register(d) } }')
    return '\n'.join(lines) + '\n'

def main():
    entries = scan_entries(INPUT_DIR)
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    code = emit(entries)
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f'Generated {OUTPUT} from {INPUT_DIR}, {len(entries)} entries.')

if __name__ == '__main__':
    main()
