import os
import yaml
from pathlib import Path
from datetime import datetime
import re

def update_mkdocs_config():
    config = {
        'site_name': '📚 Chuks Docs/Notes',
        'site_url': 'https://docs.hackerman-1337.xyz',
        'theme': {
            'name': 'material',
            'logo': 'https://hackerman-1337.xyz/favicon.ico',
            'favicon': 'https://hackerman-1337.xyz/favicon.ico',
            'palette': {
                'scheme': 'slate',
                'primary': 'black',
                'accent': 'indigo',
                'background': 'slate grey'
            },
            'font': False,
            'palette_primary': 'black',
            'css_minify': True,
            'extra_css': [
                'https://gistcdn.githack.com/chrisrhymes/20050e61501c94766f56d5b1d4c527c6/raw/cd358b7ad37391ff24c40f230f42cd907c33f657/custom.css',
            ],
            'extra': {
                'css': """
                :root {
                    --md-default-bg-color: #1a1a1a;
                    --md-default-fg-color: #ffffff;
                    --md-default-fg-color--light: #f5f5f5;
                    --md-default-fg-color--lighter: #eeeeee;
                    --md-default-fg-color--lightest: #e0e0e0;
                    --md-code-bg-color: #2d2d2d;
                    --md-code-fg-color: #fafafa;
                    --md-typeset-a-color: #8aa1ff;
                    --md-accent-fg-color: #8aa1ff;
                    --md-primary-fg-color: #2d2d2d;
                    --md-primary-fg-color--light: #2d2d2d;
                    --md-primary-fg-color--dark: #2d2d2d;
                }
                """
            },
            'features': [
                'navigation.instant',
                'navigation.tracking',
                'navigation.tabs',
                'navigation.sections',
                'navigation.expand',
                'navigation.indexes',
                'navigation.path',
                'toc.follow',
                'search.suggest',
                'search.highlight',
                'content.code.copy',
                'content.code.annotate',
                'content.tabs.link',
                'toc.follow',
                'navigation.top',
                'navigation.footer'
            ],
            'icon': {
                'repo': 'fontawesome/brands/git-alt'
            }
        },
        'markdown_extensions': [
            'pymdownx.highlight',
            'pymdownx.superfences',
            'pymdownx.tabbed',
            'pymdownx.tasklist',
            'pymdownx.details',
            'admonition',
            'toc',
            {'toc': {'permalink': True}}
        ],
        'repo_url': 'https://git.chuk.dev/chuk/docs/',
        'repo_name': '🔧 Docs on Gitea',
        'plugins': [
            'search',
            'tags',
            'minify',
            {'git-revision-date-localized': {'type': 'datetime'}}
        ],
        'nav': [
            {'🏠 Home': 'index.md'},
            {'📦 Installation': [
                {'🌐 Web Services': [
                    {'🌟 Apache': 'Installation/apache.md'},
                    {'🌊 Seafile': 'Installation/seafile.md'},
                    {'🛍️ Shopware': 'Installation/Shopware.md'},
                    {'🐙 Gitea': 'Installation/gitea.md'}
                ]},
                {'💻 Development': [
                    {'📝 Git': 'Installation/git.md'},
                    {'🔤 Languages': 'Installation/languages.md'}
                ]},
                {'🔒 Security': [
                    {'🔑 SSH': 'Installation/SSH.md'},
                    {'📜 Certificates': 'Installation/certs.md'}
                ]},
                {'⚙️ System': [
                    {'💾 QEMU': 'Installation/qemu.md'},
                    {'🎮 AMD GPU': 'Installation/amdgpu/amdgpuinstall.md'},
                    {'🎯 NVIDIA Docker': 'Installation/nvidiagpu/nvida-docker.md'}
                ]},
                {'🔄 Remote Tools': [
                    {'🖥️ RustDesk': 'Installation/rustdesk.md'}
                ]},
                {'🐍 Python': [
                    {'🔊 PyAudio': 'Installation/python/pyaudio.md'}
                ]}
            ]}
        ]
    }

    with open('mkdocs.yml', 'w') as f:
        yaml.dump(config, f, allow_unicode=True, sort_keys=False)

def clean_markdown_files():
    docs_path = Path('docs')

    for markdown_file in docs_path.rglob('*.md'):
        if markdown_file.name in ['README.md', 'index.md']:
            continue

        with open(markdown_file, 'r', encoding='utf-8') as f:
            content = f.read()

        content = re.sub(r'^---\n.*?---\n', '', content, flags=re.DOTALL)

        with open(markdown_file, 'w', encoding='utf-8') as f:
            f.write(content.strip() + '\n')

def get_display_name_and_icon(filename):
    display_names = {
        'apache': ('Apache Server', '🌐'),
        'seafile': ('Seafile Cloud', '☁️'),
        'shopware': ('Shopware E-Commerce', '🛍️'),
        'gitea': ('Gitea Git Server', '🐙'),
        'git': ('Git Version Control', '📝'),
        'languages': ('Programming Languages', '👨‍💻'),
        'ssh': ('SSH Configuration', '🔑'),
        'certs': ('SSL Certificates', '🔒'),
        'qemu': ('QEMU Virtualization', '💻'),
        'amdgpuinstall': ('AMD GPU Drivers', '🎮'),
        'nvida-docker': ('NVIDIA Docker Setup', '🐳'),
        'rustdesk': ('RustDesk Remote Desktop', '🖥️'),
        'pyaudio': ('PyAudio Setup', '🎵')
    }

    filename_lower = filename.lower()
    for key, (name, icon) in display_names.items():
        if key in filename_lower:
            return name, icon

    # Convert filename to title case and add generic icon
    return filename.replace('-', ' ').title(), '📄'

def categorize_file(filename):
    categories = {
        'Web Services 🌐': ['apache', 'seafile', 'shopware', 'gitea'],
        'Development 💻': ['git', 'python', 'languages'],
        'Security 🔒': ['certs', 'ssh'],
        'System ⚙️': ['qemu', 'amdgpu', 'nvidia-docker'],
        'Remote Tools 🔄': ['rustdesk']
    }

    filename_lower = filename.lower()
    for category, files in categories.items():
        if any(tech in filename_lower for tech in files):
            return category
    return 'Other 📋'

def generate_index():
    docs_path = Path('docs')
    categories = {}

    for markdown_file in docs_path.rglob('*.md'):
        if markdown_file.name in ['README.md', 'index.md']:
            continue

        category = categorize_file(markdown_file.stem)
        rel_path = markdown_file.relative_to(docs_path)
        display_name, icon = get_display_name_and_icon(markdown_file.stem)

        if category not in categories:
            categories[category] = []
        categories[category].append((display_name, icon, str(rel_path)))

    index_content = [
        "# 📚 Welcome to Chuk Docs",
        "",
        "🚀 Documentation for various installation and configuration procedures.",
        "",
        "## 📑 Categories",
        ""
    ]

    for category, files in sorted(categories.items()):
        index_content.extend([
            f"### {category}",
            ""
        ])

        # Sort by display name
        files.sort(key=lambda x: x[0])

        for display_name, icon, path in files:
            index_content.append(f"- {icon} [{display_name}]({path})")

        index_content.append("")

    index_content.extend([
        "## 🔍 Quick Links",
        "",
        "- 📞 [Contact Support](contact.md)",
        "- ❓ [Frequently Asked Questions](faq.md)",
        "",
        "---",
        "",
        "*🔄 Last updated: " + datetime.now().strftime('%Y-%m-%d %H:%M') + "*"
    ])

    with open(docs_path / 'index.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(index_content))

def main():
    clean_markdown_files()
    update_mkdocs_config()
    generate_index()

if __name__ == "__main__":
    main()
