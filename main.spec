# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.pyw'],
             pathex=['C:\\Users\\shurk\\PycharmProjects\\PartyTraker'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=True,
             win_private_assemblies=True,
             cipher=block_cipher,
             noarchive=False)
a.datas += [("./ico.ico", "ico.ico", "DATA")]
a.datas += [("./changelog.txt", "changelog.txt", "DATA")]
a.datas += [("./VC_redist.x64.exe", "VC_redist.x64.exe", "DATA")]
a.datas += [("./VC_redist.arm64.exe", "VC_redist.arm64.exe", "DATA")]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='C:\\Users\\shurk\\PycharmProjects\\PartyTraker\\ico.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
