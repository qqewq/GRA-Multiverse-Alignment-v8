import os
import zipfile

def build():
    repo_name = "GRA-Multiverse-Alignment-v8"
    zip_name = f"{repo_name}.zip"

    files = [
        "core/embeddings.py",
        "core/foam.py",
        "core/dynamics.py",
        "llm/llm_interface.py",
        "llm/prompts.py",
        "llm/reflection.py",
        "agents/agent.py",
        "agents/agent_system.py",
        "experiments/run_v8.py",
        "demo/visualize_alignment.py",
        "README.md",
        "requirements.txt",
        "build_zip.py",
    ]

    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            zf.write(f, os.path.join(repo_name, f))

    print(f"Created {zip_name}")

if __name__ == "__main__":
    build()
