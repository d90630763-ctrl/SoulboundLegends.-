from pathlib import Path
root=Path(__file__).resolve().parents[1]
assert (root/"Game/Packages/manifest.json").exists()
assert (root/"Game/ProjectSettings/ProjectVersion.txt").read_text().strip().startswith("m_EditorVersion: 6000.5.6f1")
cs=list((root/"Game/Assets").rglob("*.cs"))
assert len(cs)>300, len(cs)
for required in ["PlayerDatabaseBackend","AuthenticationIdentity","NetworkTransport","UniversalInstanceCoordinator","RiftSystem","SupremeRuinSystem","AudioMusicSystem"]:
    assert any(required.lower() in p.as_posix().lower() for p in (root/"Game/Assets").rglob("*")), required
print(f"Structural validation passed: {len(cs)} C# files")
