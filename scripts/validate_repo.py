from pathlib import Path
import json, re, sys
root=Path(__file__).resolve().parents[1]
errors=[]
expected={'architect','arena','blast-radius','bro','how','in-your-own-words','ketchup','principle-attack-the-premise','principle-build-the-lever','principle-exhaust-the-design-space','principle-explain-the-number','principle-fix-root-causes','principle-foundational-thinking','principle-laziness-protocol','principle-minimize-reader-load','principle-model-the-domain','principle-prove-it-works','principle-sequence-verifiable-units','principle-subtract-before-you-add','principle-test-behavior-not-implementation','teach','technical-writing','unslop','why'}
skills={p.parent.name for p in (root/'skills').glob('*/SKILL.md')}
if skills != expected:
 errors.append(f'Skill set differs: missing={sorted(expected-skills)}, unexpected={sorted(skills-expected)}')
for name in sorted(skills):
 p=root/'skills'/name/'SKILL.md'
 text=p.read_text(encoding='utf-8')
 if not text.startswith('---\n'):
  errors.append(f'{p.relative_to(root)}: frontmatter missing')
  continue
 parts=text.split('---',2)
 if len(parts)<3:
  errors.append(f'{p.relative_to(root)}: frontmatter not closed')
  continue
 front=parts[1]
 match=re.search(r'^name:\s*["\']?([^\s"\']+)',front,re.M)
 if not match or match.group(1)!=name:
  errors.append(f'{p.relative_to(root)}: name does not match directory')
 if not re.search(r'^description:\s*\S+',front,re.M):
  errors.append(f'{p.relative_to(root)}: description missing')
 if re.search(r'\{\{|TBD',text,re.I):
  errors.append(f'{p.relative_to(root)}: unfinished placeholder')
for rel in ['plugin.json','.claude-plugin/plugin.json','.codex-plugin/plugin.json','.claude-plugin/marketplace.json','.agents/plugins/marketplace.json']:
 p=root/rel
 try: json.loads(p.read_text(encoding='utf-8'))
 except (OSError,json.JSONDecodeError) as e: errors.append(f'{rel}: {e}')
link_re=re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
for p in [root/'README.md',root/'CONTRIBUTING.md',*root.glob('docs/**/*.md'),*root.glob('skills/**/*.md')]:
 text=p.read_text(encoding='utf-8')
 for target in link_re.findall(text):
  target=target.strip().split()[0].strip('<>')
  if target.startswith(('http://','https://','#','mailto:')): continue
  clean=target.split('#',1)[0]
  if not clean or (clean == 'url' and p.name == 'synthesizer-prompt.md'): continue
  if not (p.parent/clean).resolve().exists():
   errors.append(f'{p.relative_to(root)}: broken link {target}')
if errors:
 print('Validation failed:',file=sys.stderr)
 for error in errors: print(f'- {error}',file=sys.stderr)
 sys.exit(1)
print(f'Validation passed: {len(skills)} skills, manifests valid, local links resolve.')
